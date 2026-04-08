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
    "name": "@borg/markdown_to_slides_agent",
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
