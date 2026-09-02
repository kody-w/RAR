---
name: "rar-kody-w-manage-memory"
description: "Manages memories in the conversation system. This agent allows me to save important information to our memory system for future reference."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/manage_memory_agent", "rar_sha256": "a3866eaef31b35e1a7b9bb17755d42950e3b62ab4c04b051f3f0e27808acb435", "source_kind": "rar-agent", "source_commit": "fd516f31dfe3dc22441098daa43af4b5af84e047", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "manage_memory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/manage-memory:96e311205d0b86dee407a4630d425816b70c161170a4d63b95fbbfff0e5702ce", "kind": "skill"}, "author": "Kody Wildfeuer", "tags": ["core", "memory", "storage", "persistence"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/manage_memory_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `manage_memory_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/81ZWbeiyJb+K6xzH7KqyUxB5uzVa7WgDMqgoIJW1spkCAZlkkGE6vrvHajn5Km6ee9TP7QP5wARe4hv7/3tCPjjxW2buKhevrysiqBH7CQNQtCC6uXjSwBqv0rKJilyOKy5uRuBGslAVlQJvEhypIkB4hf5FVS1O05D6r5uQPYZ2cZJjcDpeYO4aVp0oxjSFEjtXgGSZGVRNS4cS/KwqLKHKBwt2uqhvn8qQuAwErZNWwGkAiGoQO6Dz9A1cHOzMgX1y5fffv/4AhWmL1/+ePFTt67fXNXummajE1AidfMIDpU9XG0O70tQjbbhowCEyPPulxqk4UfkP/7j3LlVVP/65WuOPH8Pv741fQmQ/0Ie458j0Pzy4d3Ih4/Ih9D1mw+//hCE+DQjDn8Vej4dBd5PfoXG/7uRHwNQhHgn0bhR/be54yM467ff301ra1B9i9ok+Nvct+fvvXjnT4jkRfO6hndwjL8KwMDkyNeXRVUV1RdEL94WW1bFNQlAcA/ga0ibooJh+fz15WeW/oEsbmWa+EmTwqmgeZW6a7w1Y3qM2Tb6+6FGpJ0yH517tfNezz33QF7DpKlH8Tqp7z497SNp4T8yrkuaGBEe+t8lyw9dYzZ8fop9y+5JVX2Gvn17hvzp2y9vIP7685VZUAW4u/8Q/DH2hPDNEHiq/uVdUn18RfXju/T4eA/8ry9/wuzP66Zq/XFJY/L/4x+IlvhVURdhg1h+0TZI1eZNkoGv+df8Ds62cCEkAfLdWimq+jkLviPw6egfrAW3TRtEqtwkHdE9gbtipAiR7/99hgzxqZs8kHgF4V7l38eShwYgM0RJ7qaIOVuvnwQAVfsx8M91m326jtqh5Sd3mIKC+G5Ztyn4T+T7T/R+LvvRt685BMpNcigJWQFi4FYJTBMXcgzi9Q34BPnAh+ss0tRz/TMy/mnLz+OC7RjkTxh8N0fADfht80iCFAkTyCEfYRTqIr2OEYK+1uckTZEgqeDKxwR082AE8Muo7Pv3755bx1/zB40QyIMg6wmc8OYw8ulTCckqTaIY5hLw4wL58MefH5D/Qf6d1F35aGMNOewOTgWgh0vL0BFYrm0Gp42cCwPnBvdw/PHnA/XRuxxUCGThJByJuRkj8S624woeoXiNA1xzeefTp6W/4oZ0McQFSRqIFqyd+uPXfFRRwKlVl9TgFcSH8AP618A+7IwxqZ8YwjiFVZHd597TagymX1TBZ0QJkTek4HLH3B4jGhd1AzOxBHkA+b6Hkm7zI4QjH43dpg77jyMdfM1Hzd89qHoEJ/vmw+nfEU1YQ84o0pE4IECPVuXmRZ6MgX9mZv6OU77m/KuKz4gOIJpI6VZuGVdu/SjekdnHjICU9ioPlbtIDrqxMlMwxuhOLffM+3/VMCGzQkoEL1/yNk0/vuRuBv7WKMeeCNebgQY6N3ZTWP2wLTYJuN89OWi8/Ou+YPtY0p1iR4fvXAeX+vDrubI6Lto0QDwA4YKT/TGLaojVHbJHgCEPNHfKHjH66YrHdYyECI1CxktgP//z3vuflPjPrik/umkFNeTRIxPxT9RHmOMQHIQa2Skb8+3N4mglc29J1sLNAQWvk/xxjb9Zh3EHsBWM5t/x9E+gGTcLsFSfIXpF5zMiQCaCWDz2CnALUL7FaryDSThWBLyEwYTdvD5/uO958tGL315GoTFYbzIv9x4wiowAwekvv/8EqLFf/LOLxv0CVkQKK3309b6fgJ7CHgkimLfDkxaf4RxtwajdNf2ziccDt6rcfrx/64v/xm6bJ5cWBhyWejPSV3V34lmVPxLqCSHMK/c+8qkugQ/n+2/t/CfZAV2owKWFNBSMwL2P1ce3hP6BVeGN3W50vEzd5rE7/ANKNW7gNu54/eDHB2dDgZ83rFH3K9F8eyTv6NPYVu6b6nuH/ebCyrpH8sdQNLLjtwc5vnyBPR2MmQjLMXFTGIdxs/vyMP37GP7X3gw1wH74qR4JcoJ/xqAmSFvl6O85yYN3BsbHYzCeF1/+2tA/PdbxhaMBgeNTjAowj6UDAEiMcUmawAJySrE47TGYj9M4zmAuGdCEx1Gh54VhiAGKwab3dKxho8ncp6EJPkIKXXzD7d9sJF4eM+vYnVL0mEsES9PABSGBewQFcJfxOM/DGYaioDschQHCo6euR/oY6WEUHhLQjynDYqzreyRBjfqe3e1h4NvrTuIV4RqSqA/gXi7LktG5MKBwGpqDxyAi8KdTksQxjg1clyTckPQoN2RJgJHMy5voE+UxCI81jIkHyxOm6RXcc/+5cJhANAlnymStzB4/YYLiR3rKeH0soxXtH7T57Jz7lSY4FWuSgkr2nsHbWFvzmC8qZFytsvS2jJzjEWAVXwhDssbMSS2E3oa17CBLUcsq4i3TCjB1FsomYdqhZoyBILphM0yFAAP5kQ067qoc8orifMJjqWgA6yJYlJKSLclU0yrbJXUf425+BeSU9Zsbw2vcPj3P0LTnd3KxS3pN9upsFjpXTbkaHsUrYZwILie3FTVR0EnoXSfYmt4WRHgljUhEwYBjx8YZSG49oPOhIlD5eMvO9oZcnQiyCZ3kSpmbdj+J2ISwjAEeUYo8uqThRG+ns75z2vXmkg/9ZmOQ3kFG1yKmLcGS1bxo5YkHZq4d5NPkFk5M6Xgi94m7PeY02tN2OUG9aG7QTtHsN3SfriwzsvEky84iIx62u3LPp6TkUraGK9JKrOABmCpzKyui1ihMdbnRyuOyVNaL2Mp3WMYZnbUCG4GYporPRZvjtcrnfOWtdRV3VYWizknlTASFnV3Bchqrq82FIrQbNsQME9lkOYQCqwp24aw387m1v6YeDVENpkub7w1bM0WJsO1BWt92yemq7pcKe2aoVjyY5kJJmDwNbztTTtBk119dANQ+OqvZjrolWOQmBJ0ZRMqunM3OFsGJXl88c6pcrdg99pdFUWTn61Km3SIJh9VSjI5smWtsI8NyOsW42p6G7UKWdudk6FeNjV69ndopW3roTsZxyxblbLre0519w/jSt9QVvXFxyjA8L/OLzbLUitOWZ/m0kgpzms8HguYlVLswdHXh2J1lb1pWShKhmvQ78ngs7dMul2gx5lJBojcnez4rMmM1V1e7SBQ2Mij23dbpyAyDfMnz0K9Atc8Hs2D3OG1zvHwm5lthn618Kou9FX/kd/z2rB8oxbZ22v4k2da+2LQxti78027GZFMf67yjq82Cc3rj0rMa2FKHXTr8pG43ce1ms2M/ULbtBZvD0JzZJAkCuycGX89bXuhrecO3h7roDyBXir0qOISwz9nF5HjxaC2zFgQlHif2Ml9XaJXiqZ1sfNq1DNc9WibG2bKDpU5AiSV9xLnuqFhWfiODsD9rC0+bMqVcr+Ljnp3DSl0nebyax9pZXpgwVhtJv/kOuh/OCyUSD7tiiObXmJavhJG7pcJEJz1R2I6+rXjCp9BLc+Fxvjhsi/myZHO080+2xtzQdjZj1/yyvK5pc97czoJwXc56ccm055sy3RtV4pjTXmpJ7RqLy6TxrxthhRqBZ/M1QzMox/T6TZyfZtk+KoZa6YZjyFecGGZLTNQyNq+DpuGtre0ebI+0mOQKNw9bei/wZ80WT4fDtMwLVFCEg0qXQjdXVqbixJnTc+dorfA3MesWHMoZt56qBDsbBKVVSeoyy06WecEJwr8ZVdArllucDh0tce4SIsyhqbkrfZOwV5thFcjhwZKZuVPu1/4WFw033C7Coeu4vXVZptPFpRmU+VberpsCd+fXgZ/ftJhwytJZ4OLtZGI5OLsEVSR7sEWFFcH5qrSi9J1ZCkVoqPalEg67FpPyQLtI2LI1s1tckB5HH85stlkRlWhlZjXP6I5eup7mkts4FXUs87Z6s80Pl4pkIal45qHbuyZ9yoVOPV7WbdxkbCyLYUdeiYqiTQfsslN8ycAyvZQZ5zumFwUtuyJVQWNPZ1YHl0DJ6nwi91gldUMl2fM+D+dVqt8wVsiyqc2lLbg4fjU9AmHmiibto5vZoTYJZiNM6+AScQVJ09UVW+troPDc4cbojLzmbsnhtNjPrJ20l4EBrKUo6lv6tl/hAWbE4qKeTsWTxeIG01c7bQK3zsR2Q/uNI+kyVD/b70mh5068UjpWfJDkytPbhdcYYEo4zinhzquT5J3TxmoPW4KfXwWfDTg73/l2drKjdaHkE4Zxt/N6reHbtTRNW+t43sWEmm1i+6BcdDUCYM80gbf0Gq9ecORxu6XtG7MnDwa76IFsx86AlxfHzt1laUWLuZ2SXdlU4bkmUbtU5eVeP+I4WetofnOZVsJwCY0qUYgZbT7R0/rU00aykSPY/9MJ3GKo3NU9E96qNc4NpjokQzjFhNhWeGx2ZV+1tRPbO8lRquhy7k9AZ4KjKp2XG289NDgetfKiPi9M3oiXtUHVDkGIzsHfgMKcD+2FcJgBNLvQZKXdrudj9eB2XL3b2JnKNE1KezWmXnE9Ooq5WNv8VPQoQrUpMLtm+PEaM3MendiHbMt13lIxbZucea6BU55e61PXWS2FUqhUd2LiewncuiE4rsq6DjIFxyWsECebg8ku/EtykROWlWITH27n+X4/T7dzqbrkYrO0pNhb4wuiN0JTbfBdcLKXVCTBhihZ8U0t0i65tSmhkaVDdJebUlLecJH9/qgLQReg5UmXvUJgDwupubDNdO9A0lITDSePrblXWx/vdzFzCC3IY7YPRMyXenyYOOhBTzD5zDok2JdDxs6dExBcc3veEGSOT8GKPmqXgoKbkOOw71BDP5SeY++ofLFv/HpbtNPiiOYC5plufDpjsTPDTG9lK0f5ZPcWa2s8daGmawxWvKXy3lTTiCNGEPywCVshMOVc3QOHuZADJpD7U1lZmT5nJkY96bHZpMJvdH3weOmIY47GHkt8WsccaSfzIEKXfRzcrmqgzzDXS1rWT+eyqu9m+sQ6hVFY91FQi2uH7NCSZ9j5fIIeDnbDxhN92qnorXfiQZxOBl28HiuBEfq0aKyS4DuK60y9J5UuJI7b7kJ4CV4TvUzxPeV1oWW7OopO6UMypdswzYesP9XGrsBpqV5YXb5VDSLX5DDc7t2r7ZkeI/kFceBOqHgqrqq5ImU9TVhPpCrfX52jaavOdihXnltNZHKzp6SwaAx0wpvEUdz1e2pr2KlORW2F7XYJ1uaePTP2l/o6xVat7FjWal5dNd5bUvvtbDAjSSc93t01c1Iwug2+Me0zcw2vIFmKjs1eeU10lvNilqLAXCumR5VcsQTMXhsWg3JAF7sgj3NVig56HK8cmcrcQ5YRKe9ywdxgVmsd3CSSC04k2vLJduWgxrmIGE+GDUQyZ2rQ8Ud7qKspSy7iwfeoXpHnOc9p8Z7eJIC01yK6w50rhl7r9c1AMX17lmhlLmEinU/FXNa9LM9lZr12WbizInJO1q8SPJLcshotaU++KLSjtvnMIDUXa25owZLz42DH+c3bLiZNnQ6JhTl2cbl1s14T93s8W5StWm3VPDVxY7NVGCV1PO60zhzec2OLXi3Sfko2jsXum/nFE9LswtRzcdVq7pEM3QWVXjgdlrq2TjZJPsy9cFJeNd0kziSN2eilR9FjAttHnKNZyXE9PDDpckmJRgX/0XhORuV2o1RxS29b0RXXKgOU4iS69VJOU8xczGdMqMn5IRkYn5IL+8rFkPaF8FhldTMYpc7rqwO3NpxW42OdWC2NUMJ9IitMfBM0IXM7qtfA0R0TLHKOxQQi7I3YFjzCmCxom+TR7YQnmu2ttSYaOZt0JKuRnFpHw2SCFjm2kPaXU3q1VCMFw0RaX8yWoCeEirrUdiBR9KJJqIz6zHydDBYLTweas0w6D54VLqhXrZj4eC5Iv7zSnTs9HU6En8UTlPc31qrbVatuNoPHt/tbypcvOA7PjR9fxnfBz9di//JcHw1J+e0pNqU4Ch4B/88Oqo9DY3GFTtxfZv32UgE3+HK3/uVfePQ7PN36CbT+OPbXaRs9D6KPE/anv5zsxxn94xXp48PF69vAx6uh3178ohpP7z9mPz59PL6WPT6jQM+g0fH95ePNAzQMTf/5v6T10G9HHAAA -->
