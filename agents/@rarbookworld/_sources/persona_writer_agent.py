"""
persona_writer_agent.py — the Writer persona, as a single sacred agent.py.

Drop this one file into any RAPP brainstem's agents/ directory and it works.
No sibling imports. The LLM call helper is inlined so this file is the
complete unit of share, version, audit, and trust.

Reads AZURE_OPENAI_* (or OPENAI_API_KEY) from the process environment.
"""
try:
    from agents.basic_agent import BasicAgent  # RAPP layout
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent      # flat / @publisher layout
    except ModuleNotFoundError:
        class BasicAgent:                       # last-resort standalone
            def __init__(self, name, metadata): self.name, self.metadata = name, metadata
import json
import os
import urllib.request
import urllib.error


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/persona_writer",
    "version": "0.1.0",
    "display_name": "Writer Persona",
    "description": "Senior nonfiction writer. Takes raw source material and returns chapter-style prose with code preserved verbatim.",
    "author": "rarbookworld",
    "tags": [
        "persona",
        "creative-pipeline",
        "writer"
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT"
    ],
    "dependencies": [
        "@rapp/basic_agent"
    ],
    "example_call": {
        "args": {
            "input": "raw notes",
            "chapter_title": "Chapter 1"
        }
    }
}


SOUL = """You are a senior nonfiction writer. You take raw source material and turn it
into prose that respects the reader's time. You favor concrete examples over
abstractions. You write in scenes, not summaries. You never pad. If the source
has gaps, you say so rather than fabricate.

CRITICAL for technical writing: when the source material contains code blocks
(text inside ```...``` fences) or specific filenames, function names, or API
shapes, INCLUDE THEM VERBATIM in your draft. Code is evidence. A claim about
how a system works lands twice as hard when the reader can see the actual
function being discussed. Use 1-3 fenced code blocks per draft when source
material supports it. Quote real filenames (`agents/foo_agent.py`) and real
identifiers (`run_pipeline`) instead of paraphrasing them.

You also output clean publishable prose — no '## Outline' scaffolding at the
top, no 'TODO' placeholders, no draft-state labels. Write as if your draft
will be published as-is."""


class PersonaWriterAgent(BasicAgent):
    def __init__(self):
        self.name = "Writer"
        self.metadata = {
            "name": self.name,
            "description": "The Writer persona. Takes source material, returns chapter-style prose.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input": {"type": "string", "description": "Raw source material"},
                    "chapter_title": {"type": "string", "description": "Working title"},
                    "max_words": {"type": "integer", "description": "Word cap (default 800)"},
                },
                "required": ["input"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, input="", chapter_title="Untitled", max_words=800, **kwargs):
        prompt = (
            f"Source material:\n\n--- SOURCE ---\n{input}\n--- END ---\n\n"
            f"Outline a chapter titled '{chapter_title}'. Then draft it. Lead with one "
            f"concrete scene from the source. Plain prose. Single H1. Under {max_words} words. "
            f"Sign off as @writer."
        )
        return _llm_call(SOUL, prompt)


# ─── Inlined LLM dispatch (Azure OpenAI / OpenAI / fallback) ───────────
# Lives in this file by design: makes the agent.py truly single-file
# portable. Same shape exists at the bottom of every persona agent.

def _llm_call(soul: str, user_prompt: str) -> str:
    messages = [{"role": "system", "content": soul},
                {"role": "user", "content": user_prompt}]
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
    api_key  = os.environ.get("AZURE_OPENAI_API_KEY", "")
    deployment = (os.environ.get("AZURE_OPENAI_DEPLOYMENT")
                  or os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", ""))
    if endpoint and api_key:
        is_v1 = "/openai/v1/" in endpoint
        url = endpoint
        if "/chat/completions" not in url:
            url = url.rstrip("/") + f"/openai/deployments/{deployment}/chat/completions?api-version=2025-01-01-preview"
        elif not is_v1 and "?" not in url:
            url += "?api-version=2025-01-01-preview"
        return _post(url, {"messages": messages, "model": deployment},
                      {"Content-Type": "application/json", "api-key": api_key})
    if os.environ.get("OPENAI_API_KEY"):
        return _post("https://api.openai.com/v1/chat/completions",
                      {"model": os.environ.get("OPENAI_MODEL", "gpt-4o"), "messages": messages},
                      {"Content-Type": "application/json",
                       "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    return "(no LLM configured — set AZURE_OPENAI_* or OPENAI_API_KEY)"


def _post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                  headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            j = json.loads(resp.read().decode("utf-8"))
        choices = j.get("choices") or []
        return (choices[0]["message"].get("content") or "") if choices else ""
    except urllib.error.HTTPError as e:
        return f"(LLM HTTP {e.code}: {e.read().decode('utf-8')[:200]})"
    except urllib.error.URLError as e:
        return f"(LLM network error: {e})"