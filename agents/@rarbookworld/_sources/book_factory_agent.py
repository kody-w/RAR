"""
book_factory_agent.py — top-level composite for the digital twin book factory.

Direct-imports each persona agent.py and runs them in order. No pipeline DSL,
no orchestrator endpoint, no special step kinds. Just one agent.py whose
perform() does Python function calls on other agent.py files.

Run via the sacred OG path:
    POST /api/swarm/{guid}/agent  {"name":"BookFactory","args":{...}}

Returns the final chapter as a string. Also writes intermediate artifacts
to a workspace dir so .egg snapshots can capture the in-flight state.

Inputs:
    source       — raw source material (a string)
    chapter_title — working title for the chapter
    workspace    — optional dir to drop artifacts in (default: $TWIN_WORKSPACE/book or /tmp/book-factory)

Returns:
    The final chapter markdown.
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

PersonaWriterAgent = _load_sibling("persona_writer_agent.py", "PersonaWriterAgent")
PersonaEditorAgent = _load_sibling("persona_editor_agent.py", "PersonaEditorAgent")
PersonaCEOAgent = _load_sibling("persona_ceo_agent.py", "PersonaCEOAgent")
PersonaPublisherAgent = _load_sibling("persona_publisher_agent.py", "PersonaPublisherAgent")
PersonaReviewerAgent = _load_sibling("persona_reviewer_agent.py", "PersonaReviewerAgent")
import os


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/book_factory",
    "version": "0.1.0",
    "display_name": "BookFactory (multi-file source)",
    "description": "Five-persona content pipeline (Writer \u2192 Editor \u2192 CEO \u2192 Publisher \u2192 Reviewer) as a composite of 13 sibling agent.py files.",
    "author": "rarbookworld",
    "tags": [
        "composite",
        "creative-pipeline",
        "twin-stack"
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
        "@rarbookworld/persona_writer",
        "@rarbookworld/persona_editor",
        "@rarbookworld/persona_ceo",
        "@rarbookworld/persona_publisher",
        "@rarbookworld/persona_reviewer"
    ],
    "delegates_to": [
        "@rarbookworld/persona_writer",
        "@rarbookworld/persona_editor",
        "@rarbookworld/persona_ceo",
        "@rarbookworld/persona_publisher",
        "@rarbookworld/persona_reviewer"
    ],
    "example_call": {
        "args": {
            "source": "raw notes...",
            "chapter_title": "Chapter 1"
        }
    }
}


class BookFactoryAgent(BasicAgent):
    def __init__(self):
        self.name = "BookFactory"
        self.metadata = {
            "name": self.name,
            "description": "Five-persona content pipeline. Source → Writer → Editor → "
                           "CEO → Publisher → Reviewer. Returns the final chapter.",
            "parameters": {
                "type": "object",
                "properties": {
                    "source":        {"type": "string", "description": "Raw source material"},
                    "chapter_title": {"type": "string", "description": "Working title"},
                    "author":        {"type": "string", "description": "Author byline"},
                    "workspace":     {"type": "string", "description": "Dir for intermediate artifacts"},
                },
                "required": ["source"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, source="", chapter_title="Untitled chapter",
                author="@rapp", workspace=None, **kwargs):
        ws = workspace or os.environ.get("TWIN_WORKSPACE") or "/tmp/book-factory"
        os.makedirs(ws, exist_ok=True)

        def save(name, content):
            path = os.path.join(ws, name)
            with open(path, "w") as f:
                f.write(content if isinstance(content, str) else str(content))
            return path

        save("00-source.md", source)

        # 1. Writer
        draft = PersonaWriterAgent().perform(input=source, chapter_title=chapter_title)
        save("01-draft.md", draft)

        # 2. Editor (composite — calls cutweak + factcheck + voicecheck)
        edited = PersonaEditorAgent().perform(input=draft)
        save("02-edited.md", edited)

        # 3. CEO (composite — calls risk + decision)
        ceo_note = PersonaCEOAgent().perform(input=edited)
        save("03-ceo-note.md", ceo_note)

        # 4. Publisher
        final = PersonaPublisherAgent().perform(input=edited, ceo_note=ceo_note,
                                                  title=chapter_title, author=author)
        save("04-final-chapter.md", final)

        # 5. Reviewer (read it cold)
        review = PersonaReviewerAgent().perform(input=final)
        save("05-review.md", review)

        # Summary header + the final chapter (the artifact the caller wants)
        return (
            f"Book factory complete. Workspace: {ws}\n"
            f"---\n"
            f"FINAL CHAPTER:\n\n{final}\n"
            f"---\n"
            f"REVIEWER:\n\n{review}\n"
        )