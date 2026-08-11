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
