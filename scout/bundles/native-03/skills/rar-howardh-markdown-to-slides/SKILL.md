---
name: "rar-howardh-markdown-to-slides"
description: "Converts markdown documents into structured JSON slide decks for presentations or video rendering."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/markdown_to_slides_agent", "rar_sha256": "b895958c9b7f074a4a51ca5456c3aa3b3e54061291f6ea4fe19d5eb4ae1c95cb", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.0", "author": "RAPP Contributor", "tags": ["markdown", "slides", "presentation", "converter", "deck", "pipeline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/markdown_to_slides_agent`. The original RAPP
agent is preserved byte-for-byte in `markdown_to_slides_agent.py` and in the RCI capsule.

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

MarkdownToSlides Agent — Converts markdown documents into structured slide decks.

Takes markdown with headings, bullets, quotes, and code blocks and produces a
JSON slide deck that can be consumed by presentation tools or the PromptToVideo
agent for rendering. Supports speaker notes via HTML comments.

Input: raw markdown string
Output: JSON slide deck with title, content, code, quote, and list slide types

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "markdown": {
      "description": "Raw markdown string to convert into slides",
      "type": "string"
    },
    "style": {
      "description": "Visual style hint for downstream renderers (default: bold)",
      "enum": [
        "bold",
        "minimal",
        "neon",
        "warm"
      ],
      "type": "string"
    },
    "title": {
      "description": "Override deck title (uses first H1 if not provided)",
      "type": "string"
    }
  },
  "required": [
    "markdown"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `markdown_to_slides_agent.py` and embedded as the fenced Python below (sha256 b895958c9b7f074a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `markdown_to_slides_agent.py` first:

```bash
python3 markdown_to_slides_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 markdown_to_slides_agent.py   # or on stdin
python3 markdown_to_slides_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/markdown_to_slides_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/markdown_to_slides_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/markdown_to_slides_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
MarkdownToSlides Agent — Converts markdown documents into structured slide decks.

Takes markdown with headings, bullets, quotes, and code blocks and produces a
JSON slide deck that can be consumed by presentation tools or the PromptToVideo
agent for rendering. Supports speaker notes via HTML comments.

Input: raw markdown string
Output: JSON slide deck with title, content, code, quote, and list slide types
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/markdown_to_slides_agent",
    "version": "1.1.0",
    "display_name": "MarkdownToSlides",
    "description": "Converts markdown documents into structured JSON slide decks for presentations or video rendering.",
    "author": "RAPP Contributor",
    "tags": ["markdown", "slides", "presentation", "converter", "deck", "pipeline"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import re

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent


def _parse_markdown_to_slides(markdown: str) -> list[dict]:
    """Parse markdown into a list of slide dicts."""
    slides = []
    current_slide = None

    lines = markdown.strip().split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # H1 = title slide
        if line.startswith("# ") and not line.startswith("##"):
            if current_slide:
                slides.append(current_slide)
            current_slide = {
                "type": "title",
                "text": line[2:].strip(),
                "subtitle": "",
                "notes": "",
            }

        # H2 = new content slide
        elif line.startswith("## "):
            if current_slide:
                slides.append(current_slide)
            current_slide = {
                "type": "content",
                "text": line[3:].strip(),
                "subtitle": "",
                "items": [],
                "notes": "",
            }

        # Code block → code slide
        elif line.startswith("```"):
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code_text = "\n".join(code_lines)
            if current_slide and current_slide["type"] == "content" and not current_slide.get("subtitle"):
                current_slide["type"] = "code"
                current_slide["subtitle"] = code_text
                current_slide["language"] = lang or "text"
            else:
                if current_slide:
                    slides.append(current_slide)
                current_slide = {
                    "type": "code",
                    "text": lang.title() if lang else "Code",
                    "subtitle": code_text,
                    "language": lang or "text",
                    "notes": "",
                }

        # Blockquote → quote slide
        elif line.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].startswith("> "):
                quote_lines.append(lines[i][2:].strip())
                i += 1
            i -= 1  # back up one since loop will advance
            quote_text = " ".join(quote_lines)

            # Check for attribution (line starting with — or --)
            attribution = ""
            match = re.match(r"^(.+?)\s*[—–\-]{1,2}\s*(.+)$", quote_text)
            if match:
                quote_text = match.group(1).strip()
                attribution = match.group(2).strip()

            if current_slide:
                slides.append(current_slide)
            current_slide = {
                "type": "quote",
                "text": quote_text,
                "subtitle": attribution,
                "notes": "",
            }

        # Bullet list items
        elif re.match(r"^[\-\*]\s", line):
            if current_slide is None:
                current_slide = {"type": "list", "text": "", "items": [], "notes": ""}
            if current_slide.get("type") not in ("content", "list"):
                slides.append(current_slide)
                current_slide = {"type": "list", "text": "", "items": [], "notes": ""}
            if "items" not in current_slide:
                current_slide["items"] = []
            current_slide["items"].append(line[2:].strip())

        # HTML comment → speaker notes
        elif line.strip().startswith("<!--") and "-->" in line:
            note = re.sub(r"<!--\s*|\s*-->", "", line).strip()
            if current_slide:
                current_slide["notes"] = note

        # Regular text → subtitle/body
        elif line.strip() and current_slide:
            if current_slide["type"] == "title" and not current_slide.get("subtitle"):
                current_slide["subtitle"] = line.strip()
            elif current_slide.get("type") == "content":
                existing = current_slide.get("subtitle", "")
                current_slide["subtitle"] = (existing + " " + line.strip()).strip()

        i += 1

    if current_slide:
        slides.append(current_slide)

    # If no slides parsed, create a single content slide
    if not slides:
        slides.append({
            "type": "content",
            "text": "Untitled",
            "subtitle": markdown.strip()[:500],
        })

    return slides


class MarkdownToSlidesAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "markdown": {
                        "type": "string",
                        "description": "Raw markdown string to convert into slides"
                    },
                    "title": {
                        "type": "string",
                        "description": "Override deck title (uses first H1 if not provided)"
                    },
                    "style": {
                        "type": "string",
                        "enum": ["bold", "minimal", "neon", "warm"],
                        "description": "Visual style hint for downstream renderers (default: bold)"
                    }
                },
                "required": ["markdown"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, markdown="", title="", style="bold", **kwargs) -> str:
        if not markdown or not markdown.strip():
            return "Error: 'markdown' parameter is required and must not be empty."

        slides = _parse_markdown_to_slides(markdown)

        # Override title if provided
        if title and slides and slides[0].get("type") == "title":
            slides[0]["text"] = title
        elif title:
            slides.insert(0, {"type": "title", "text": title, "subtitle": ""})

        deck = {
            "title": title or (slides[0]["text"] if slides else "Untitled"),
            "slides": slides,
            "slide_count": len(slides),
            "style": style,
        }

        return json.dumps(deck, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    sample = """# RAPP Agent Registry
The open ecosystem for AI agents

## What is RAPP?
A single-file agent registry where every agent is one .py file with an embedded manifest.

- Agents return strings
- No network calls in __init__
- Secrets via environment variables

## The Seed Protocol
> Every card is forged from its data. The seed IS the card. — RAPP Whitepaper

## Getting Started
```python
from agents.basic_agent import BasicAgent

class MyAgent(BasicAgent):
    def perform(self, **kwargs):
        return "Hello from RAPP"
```

<!-- This is a speaker note for the presenter -->
"""
    agent = MarkdownToSlidesAgent()
    print(agent.perform(markdown=sample))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
