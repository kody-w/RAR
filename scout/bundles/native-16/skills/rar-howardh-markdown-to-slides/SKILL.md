---
name: "rar-howardh-markdown-to-slides"
description: "Converts markdown documents into structured JSON slide decks for presentations or video rendering."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/markdown_to_slides_agent", "rar_sha256": "ab0a2046a0a241148fdae0bfb68ce8f4f16317e96cfe9beabb0f285aaded07b7", "source_kind": "rar-agent", "source_commit": "fd516f31dfe3dc22441098daa43af4b5af84e047", "version": "1.1.0", "author": "RAPP Contributor", "tags": ["markdown", "slides", "presentation", "converter", "deck", "pipeline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `markdown_to_slides_agent.py` and embedded as the fenced Python below (sha256 ab0a2046a0a24114…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `markdown_to_slides_agent.py` first:

```bash
python3 markdown_to_slides_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 markdown_to_slides_agent.py   # or on stdin
python3 markdown_to_slides_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
