"""
persona_publisher_agent.py — the Publisher persona, single sacred agent.py.
Takes edited content + CEO note, outputs a publication-ready markdown file.
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
    "name": "@rarbookworld/persona_publisher",
    "version": "0.1.0",
    "display_name": "Publisher Persona",
    "description": "Indie-press publisher. Takes edited prose plus a CEO note and outputs publication-ready markdown with YAML frontmatter.",
    "author": "rarbookworld",
    "tags": [
        "persona",
        "creative-pipeline",
        "publisher"
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
            "input": "edited",
            "ceo_note": "ship with one edit"
        }
    }
}


SOUL = """You are an indie-press publisher. You ship artifacts, not opinions.
You take edited prose plus a CEO note, apply the requested change, and produce
a publication-ready markdown file with proper YAML frontmatter (title, author,
date, chapter_number). You output nothing but the markdown."""


class PersonaPublisherAgent(BasicAgent):
    def __init__(self):
        self.name = "Publisher"
        self.metadata = {
            "name": self.name,
            "description": "The Publisher persona. Assembles publication-ready markdown.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input":    {"type": "string", "description": "Edited content"},
                    "ceo_note": {"type": "string", "description": "CEO's review note"},
                    "title":    {"type": "string", "description": "Final title"},
                    "author":   {"type": "string", "description": "Author byline"},
                },
                "required": ["input"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, input="", ceo_note="", title="Untitled",
                author="Unknown", **kwargs):
        prompt = (
            f"Edited prose:\n--- EDITED ---\n{input}\n--- END ---\n\n"
            f"CEO note:\n--- CEO ---\n{ceo_note}\n--- END ---\n\n"
            f"Apply the CEO's requested change. Output ONLY the final chapter as one "
            f"publication-ready markdown file. Use YAML frontmatter with: "
            f"title=\"{title}\", author=\"{author}\", date today, chapter_number=1. "
            f"No commentary, no explanation, no preamble — JUST the markdown file."
        )
        return _llm_call(SOUL, prompt)


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