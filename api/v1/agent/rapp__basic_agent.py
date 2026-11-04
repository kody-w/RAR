# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/basic_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/basic_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/basic_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
BasicAgent — Base class for all RAPP agents.
Every agent in the RAPP ecosystem inherits from this.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/basic_agent",
    "version": "1.0.1",
    "display_name": "BasicAgent",
    "description": "Provides the base class every RAPP agent inherits from; stores the agent's name and metadata, with no behavior of its own.",
    "author": "RAPP Core",
    "tags": ["devtools", "base-class", "required"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": [],
}
# ═══════════════════════════════════════════════════════════════


class BasicAgent:
    def __init__(self, name, metadata):
        self.name = name
        self.metadata = metadata
