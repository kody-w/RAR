---
name: "rar-howardh-markdown-to-slides"
description: "Converts markdown documents into structured JSON slide decks for presentations or video rendering."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/markdown_to_slides_agent", "rar_sha256": "b895958c9b7f074a4a51ca5456c3aa3b3e54061291f6ea4fe19d5eb4ae1c95cb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.0", "author": "RAPP Contributor", "tags": ["markdown", "slides", "presentation", "converter", "deck", "pipeline"]}
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
