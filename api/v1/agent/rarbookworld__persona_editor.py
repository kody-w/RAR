"""
persona_editor_agent.py — Editor persona, composite of FIVE specialist agents.

v0.3.0: added strip_scaffolding (catches `## Outline` artifacts the Writer
left in) and restructure (consolidates repetitive middle sections). Composite
runs in order: strip → cut → restructure, then runs factcheck and voicecheck
in parallel-style for the editor's note. cutweak now preserves fenced code.

Each specialist is its own portable agent.py with its own inlined LLM call.
Editor's perform() direct-imports them and runs each in sequence, then
composes the final output.

Sacred all the way down: this file is a single agent.py, but its perform()
delegates to other agent.py files. Cat any one of them to read the unit.
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

EditorStripScaffoldingAgent = _load_sibling("editor_strip_scaffolding_agent.py", "EditorStripScaffoldingAgent")
EditorCutweakAgent = _load_sibling("editor_cutweak_agent.py", "EditorCutweakAgent")
EditorRestructureAgent = _load_sibling("editor_restructure_agent.py", "EditorRestructureAgent")
EditorFactcheckAgent = _load_sibling("editor_factcheck_agent.py", "EditorFactcheckAgent")
EditorVoicecheckAgent = _load_sibling("editor_voicecheck_agent.py", "EditorVoicecheckAgent")
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/persona_editor",
    "version": "0.3.0",
    "display_name": "Editor Persona (composite)",
    "description": "Editor persona. Composite of 5 specialists: strip \u2192 cut \u2192 restructure, plus factcheck + voicecheck for the editor's note.",
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
        "@rarbookworld/editor_strip_scaffolding",
        "@rarbookworld/editor_cutweak",
        "@rarbookworld/editor_restructure",
        "@rarbookworld/editor_factcheck",
        "@rarbookworld/editor_voicecheck"
    ],
    "delegates_to": [
        "@rarbookworld/editor_strip_scaffolding",
        "@rarbookworld/editor_cutweak",
        "@rarbookworld/editor_restructure",
        "@rarbookworld/editor_factcheck",
        "@rarbookworld/editor_voicecheck"
    ],
    "example_call": {
        "args": {
            "input": "draft text"
        }
    }
}


class PersonaEditorAgent(BasicAgent):
    def __init__(self):
        self.name = "Editor"
        self.metadata = {
            "name": self.name,
            "description": "The Editor persona. Strips scaffolding → cuts weak prose "
                           "(preserving code) → restructures repetitive middles, then "
                           "runs factcheck + voicecheck for the editor's note.",
            "parameters": {
                "type": "object",
                "properties": {"input": {"type": "string", "description": "Writer's draft"}},
                "required": ["input"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, input="", **kwargs):
        # Sequential transformations on the prose itself
        stripped     = EditorStripScaffoldingAgent().perform(input=input)
        cut          = EditorCutweakAgent().perform(input=stripped)
        restructured = EditorRestructureAgent().perform(input=cut)

        # Parallel-in-spirit checks against the original draft (so the
        # checks see what was claimed before any cutting happened)
        facts = EditorFactcheckAgent().perform(input=input)
        voice = EditorVoicecheckAgent().perform(input=input)

        return (
            f"{restructured}\n"
            f"---\n"
            f"**Editor's note**\n\n"
            f"_Sourcing flags:_\n{facts}\n\n"
            f"_Voice drift:_\n{voice}\n"
        )