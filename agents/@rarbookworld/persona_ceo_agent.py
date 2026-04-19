"""
persona_ceo_agent.py — CEO persona, composite of two specialist agents.

Delegates to ceo_risk + ceo_decision specialists. Same agent.py-all-the-way-down
pattern as the Editor persona.
"""
try:
    from agents.basic_agent import BasicAgent  # RAPP layout
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent      # flat / @publisher layout
    except ModuleNotFoundError:
        class BasicAgent:                       # last-resort standalone
            def __init__(self, name, metadata): self.name, self.metadata = name, metadata
# ── dir-agnostic sibling loader (works in RAPP agents/, RAR agents/@rarbookworld/, anywhere) ──
import importlib.util as _ilu, os as _os, sys as _sys
def _load_sibling(filename, class_name):
    here = _os.path.dirname(_os.path.abspath(__file__))
    path = _os.path.join(here, filename)
    if not _os.path.exists(path):
        # fall back to RAPP agents/ layout for development
        from importlib import import_module as _im
        return getattr(_im(f"agents.{filename[:-3]}"), class_name)
    spec = _ilu.spec_from_file_location(filename[:-3], path)
    mod = _ilu.module_from_spec(spec)
    _sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return getattr(mod, class_name)

CEORiskAgent = _load_sibling("ceo_risk_agent.py", "CEORiskAgent")
CEODecisionAgent = _load_sibling("ceo_decision_agent.py", "CEODecisionAgent")
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/persona_ceo",
    "version": "0.2.0",
    "display_name": "CEO Persona (composite)",
    "description": "CEO persona. Composite of 2 specialists: decision + partner-risk. Returns a strategic-message-discipline review.",
    "author": "rarbookworld",
    "tags": [
        "persona",
        "creative-pipeline",
        "composite"
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT"
    ],
    "dependencies": [
        "@rapp/basic_agent",
        "@rarbookworld/ceo_risk",
        "@rarbookworld/ceo_decision"
    ],
    "delegates_to": [
        "@rarbookworld/ceo_risk",
        "@rarbookworld/ceo_decision"
    ],
    "example_call": {
        "args": {
            "input": "edited chapter"
        }
    }
}


class PersonaCEOAgent(BasicAgent):
    def __init__(self):
        self.name = "CEO"
        self.metadata = {
            "name": self.name,
            "description": "The CEO persona. Delegates to risk + decision specialists "
                           "and composes a strategic-message-discipline review.",
            "parameters": {
                "type": "object",
                "properties": {"input": {"type": "string", "description": "Content under review"}},
                "required": ["input"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, input="", **kwargs):
        risks    = CEORiskAgent().perform(input=input)
        decision = CEODecisionAgent().perform(input=input)
        return f"**Decision**\n{decision}\n\n**Partner-conversation risks**\n{risks}\n"