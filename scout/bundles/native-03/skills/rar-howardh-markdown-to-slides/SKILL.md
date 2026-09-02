---
name: "rar-howardh-markdown-to-slides"
description: "Converts markdown documents into structured JSON slide decks for presentations or video rendering."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/markdown_to_slides_agent", "rar_sha256": "ab0a2046a0a241148fdae0bfb68ce8f4f16317e96cfe9beabb0f285aaded07b7", "source_kind": "rar-agent", "source_commit": "fd516f31dfe3dc22441098daa43af4b5af84e047", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "markdown_to_slides_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/markdown-to-slides:afb37723e03f30010df3e59338836bf8175d0cbce2c1a91a2334a419364a72d8", "kind": "skill"}, "version": "1.1.0", "author": "RAPP Contributor", "tags": ["markdown", "slides", "presentation", "converter", "deck", "pipeline"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/markdown_to_slides_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `markdown_to_slides_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZaZOiyJv/KoT/F9O9VpcICFgbvbHghSKXIqhTE9UJJJByyiFq73z3TdTqY3p2NjZifVGdkPlcv+dM+msH1FWYFZ2XzkrQdWKUpVWBnLrCr546HizdAuUVylJ8AO+dYFGVRAKKyMualPAyt05gil+htMqIsipqt6oL6BGLtaYSZYw8SHjQjUrCzwoiL2CJT4OWX0ngFye8nxEFTD1YoDR4xiLhGSR5DMvOy+9/PHUQXndevnbcGJT4VUd5SDazdcu7FALMD1PFIA3wdn7BtqT4OYcFFpjgVx70icfThxLG/tM37T+/dl47T0SFqhg+1mV1ua2dLPba53/7t6gBRVB+JD79R2vdy2tKPH7IJ9Ks+g4FtubH52d8GuUfPv5A0f4KiOFJidfOpCiy4oX47f38b0QOCpDAChYEKvG5Y41aHEHqEUldVjfmDiRgkleXZ6xt+p3xDeaS+Ey8YR4lfHvn+VZlb/e9D++vPv5I9y9Cw/4sWh/dQGhtyousdYr3k6H33VaVh6jvy9/JP54DWH147VSXHL52PhKfP2PzbhSvnb9Y/43kd3wCnqvXzh9Y6/vZbwdh/C7xb6mfUVriIPxAPhFf34W+fJf4RLyzfrkzaV+UtfOuENE6+s+fYGjjE6vx9Wdp3214mI8d/OHvDMDaPlCBcQkx3Sa9EeAA+vj0V573ky3T++rvD7y5WZ3eTIhh+hD6N7zaYL2xahc/bP/5o3WPiDuUWfrs1UlefmjtfcIJ6+HU+Uw9ETAtccq+gdJF6PMUYCM+dv7EqZfe07nNVZxH//oXoSC3yMrMr4g1VrAiCqwkSmArzQxx0JoZKCscs1/W8ny5fE68L20oV2FbAnxQxxUxKwCK2xg7wBtjIvOJL/8ZZjjJvLD3a9y+gTa/vzwTZojFZAUKUApi4lapblutADdsC0ydfDq1MrB8lN6ErkZzwgV5Wcfw34kv/xPz5/zSqvmaYqAASjF5hXMsK0CB4gsBcKwTzqWCn3BdcrHJWRw7AMdL+6fOn1vb7RCmD0RckBLwDN26gkScuVhVH+Fa9oS9UGbxCedZi1MZoTgmPJzfLi6zl1s2YSxfWmZfvnxxQBm+pvdSRhP3Alz28IFvChOfPuFS6scoCKvXFLphRvz29c/fiP8i/onqxryVoeNaekOogFjDW6XGRe5bIcc+BN7NM1//vEPfapfiwoSrBfIRvBFjbt/d3Fpw98e7M7DNrYqweEj6GTeiCVFbbyqMFiqrNg1aFhk+WjQIZ9EDxDvxHfp3797ltD4pHxhiP/lFltzO3iKsdaabFd4zMfeJb0hhc7Ffq9ajYYYrqgfztvGk7gVTguq7C9tSW+ImVfqXJ6Iusakt5y8OZt2Ck7y5+PgXQhnpRJVlMf7TAnQTj6mzFLWOf4Tn/TVmUvyGY0x8Z/FMqBCjeSv6eViAEt7O+eAeEbjWvNNj5oBIYUO0rRAm7+3zFnl/7YbErR0SrzVF9hni/9Kuf+jUN84miOAPhA2qQiLEYYGbNPasU8cxxF4jjnVWteHdOs/NMAcHR3107w84y73abZvFa/qXaeCOd5ssuKO5uL5grTzs0p8GhBu2tymhRUbHDs4rM7PaiQFHy83Qdqb4PjwQ6zq/O7jMIdb/1pCx/BMChGQqSywpuVl/s3Ce5nX1QhSg+W5m27PT4DXV6uq2+Ve1bzA8ugpWu8LMnm52P5C4AxHjiH5Qte2pbMcT5OIqCzsvKUbuqZPiRv83w0w7t7wPAWU79WAI8ehSIXh7elezXf88mK1+NaINSvceAA9nv4todcI092Ntob+1j1+ZWqiscRzfdokQPeBuRWBSCJIH8m2Gf3jU9xeiHZw+tlNcWuPh6/fbIIUfE5SiBMR4lcLbfIYLftL542+UuaH7qzLfBpV7+Nwa8gecVXiuRAWGW+q/D2TvA8zHX03F7N/nqla3b3h+1yNz2sbU6pHHoLpPkBh43Bk8UIF2fa9f95qKCf6hq2D536rBW8sKtAS32n+brG+IvQHs3jbrf9gK2hL2dq9gnRecoxADCHBMIBCj620y7tzlY8W/91LMATetT2VbxXr9ZxJzwrUlb5WOcLP/QUD7Gnm38+3i5ZcG/KnKPt2teQG+Q3McRUOS9mmS7JOeT8PBkKZ5nmYdn+9zA490HRdSbh8M+4CiaQYw/SHNMoCjPB6LK3FPSMBDXK/foosV/Qbh/9r+O/fzZQioAYsJgEMCimRYgP9h+n2G9z0AScd3WN6FvM/4fZbuc3DIuj4cOhA4DulT/AAAHBUk53Atv0c7ugt4e2/972iXWV247RSWJKhV0fcGfdan+54Pac+lKIbpk0PeA4Chgc84A+DzDCSZlvOD9IF465C7DW3w3apbcWrlfH14sI0olsEnJaacC/ffqMeT++1ed6rTzDs1y9hbg/XSm9LcaTWNaBXtB0uQ+vnBV/3IAP5xLsrr3UKZjHci3S8COmL9brAEPXLZjeqmNuYolrWDvzDH57MpzDjUo+F5PVearhD3u7zp7Sv/mFWbRSk3+aVe2T1nMOh1L1x/1Z1zRn+pK81yOj0n7ozamTKNwqS4DJFtI1OZjxfLlX6Fq8m0uXjdpVgdq2pWU9PDZdV1jwolL5QNJYUMqeXFXOzBPdvYgtSdx5YQSMzWRlY8nq4YXoXLPssD8TriBrkz1WfuUrDRQNjv1lUVCOgwFqSltx64zTFeHRN1IiyHESiK5WjLRjDIjIU2QYPQZEp+sjoyuFJP7ZUhh6Y9FTSmfxlMaA8pA0hzAz4ZNpsJWAe0ceKPMjlhnQFn7ScbwTZGFruNT4BdLpRZsVzns5G0nCKkrmfrkyjDsSUW+Ip1SSaj3bzZjEV/wZ23I3Za+spAo6AvBPueEWqnleuMR0bZXzLZ+eKb2XKcqSuK6Q0GqUDbvS2bO8Vep7JdatX9/VVTJHV0DMdCX9htwmuYbnaqMY+oFV9S/LwK+4mYa8n0sGzSDGy7c16yyX0Z0WaSmPPZdQUbyrQa50ICdnu+Lj2d5s5i0VjOcpItwZkb8bkt9ux4x69kzZjPIDzvKJNf+qWtekC/iGNxZiwnxtE9S5quznY2N13DTJGwTX0+coC53WbhQE55Sa3z9Tgh55J8EmbBeeetm2p6jTw+8DgVRMZWThRvrclsb2WUPTsVDjuKvwhLcinkSXjmFvSq3lrVeS/udCsx8rXN6LYymVw3zWwHh2FUbxxDYhKlHOFJKQjXOZS35ZgtlKjb7VtFLrLmaDGfHCZRSS6LjNpxvQJk0yPItJnk6JfJSaLART1o9EgKuBlvwG55Hox8N9xZwAqZ0WzkjC4TIVqd6dHucDzQ9CxvNlqpnW0bB5NrzeccGDeTQg6l2XI53YlIhGTJjeTexZ0gYZKJmuRylX3cjabFIDm6gbSaSVkik5mAmsrsbsrj2NMoXblSssh456tt04sFLwlM2B0L1ViYm/2AyXUkxap2hec5dT0ZpJ3IlMd5ALli1eD4W0IxHHGoKCKeyydLZaWh3mJO07QJhO4sEAUx8fWcU+SCpoxFfmFAINTmQI6lBafWQ3BMScXXHFSVx4NkWONIB/lM2vJwOEL73nEnnXok6hlZ4YbKnLX4ei/3jmx57vYuJ587IV/kh9v+0Pd6tsun1zhjjdyKa9GQhlAESB+oucZpExz3ZTXcWbHMCI007537JkuXqTzVvYvIwdmYVKdlM94mhy7yolMcrOkVLgdTlxqqbmJmdOJIV56l0v5c7huyZgWLs6WRsu/o1CbaYkQTPVBta3KEGz7MbGp5nI4m4m4v1UfK7Tb2MQpVk2u8Ax+cUFlwK3uXarnWnaqubA6E47zaKGFuqpvNcSP2a9jzkBrJVL82IGnVcpTx8yGvlyOI8HBCTfgNVy0MSHW5ULdMGqwXXalGQzRkvMhJitNEazzS4NT9XmOsPJfVnRH1S21kkMpxZFi6cFDOh8aS41F90MiBeR7MnfE66+6snXGVuoJKZ3txdGbWg3Ph+PDst+kgTwczJHmzTaSnbMKMoaKMSn3GLDeKOXYH5ZmkZ45zme3XJOqG14wXu2NWm9DN5XTdCdlE7/X4lD2dOVXfs/rEK5Sxxs974XEkTc1ojuRTTXLdTZLMUGxZkXLNwLC7rbf82lkzF3rNscIoohqJrYf2sNSs6oKjo1/F6XA6pXSbtpa643qI5E+ro69bgZdt6am/juccqUTMjqX59BxOD4XopAJiBluDOfiHDUCyt/QaF9eYtXwxLrk7CRYB1TswEQN6jXrspWsBlrMlh6SKOua9cQrJ5CyxzD4eFANulVTDGpeJse1kZApPGnUabshNfd36Z6T3VpuDNO/64SgAQuHGRoZHH2a0DXg+nCbrlc8v/JV4XC3KdABTXeDtQ31UZnvBs6dbkgppJreS7VKVhdmKHHOlhPqbsopOw9lA8sxQsU+Ujbq4N3q4qW2G6vRQVaQi7cAWiPUFyofuOI3SojC4C6J2e/+ssUF+agxcb/nTJRbMC0cvTJfhhI2UXasmTLtnUe1vPToDi7VxmCYnsTGVgVWfLTktan+7WCxSlemSgzJm8D43Z6HfDBf8JqL9/mwOA20qA1MfdKGaDKCHZ5+ljUHlh9ZEWJ0vWT+ktxNgWsqM4mfy8LoBRXmOl3Wf1w8C2pp7fiINZ9qCGTNXWwo9neJmnL0q0WRgJLQve8A66uMEe2Cog6Cg1WDHDq9d4yqm0VgZZdRgSI5EK6voec0O5ysPTI0FkNWpHtjj48TjuwinhZNcuJzT6xlVd+kVzSrHeiedU/YCgIPDaH1SK7rujbXh9NT0xHxHDk+5tqFi8WiLk2kljwEt8ZxyDKKxqM0sNYx7s9Ny5myZ4SDau/uDSW7liGx8exsMV7HOm8rWiRbchd7Y15o9BatuLG9TGU26VJxy7OG6m/iBqfemxn67UNS5umASL1s0PZ2W1zITUsejYPfW0oHWg3QgU5ehGeTeeGT3pjVzmnj1gT3P5YFgikI+PwsrzpbSRF8sMt2c8nFvi1Kq2el0pkArsyclO5PW0lRG6nDVLVKz8AbbjDpsFznnG4cdvbfOW9JiG82fnZcyaxmZ25fdMR+dVqKyn2893EuMtdfdkQyjxVZZbbp0fa1UMVGOVdLIrGmbo5TTh+mC07z62Bz4YVD1+SkrR8WUU4+D6lRvZigfX7V1vZtFihl4qlNs66TgRrXhH7zseuLqWSOaG+2a8EFqoSCYSPXwKu/XNpf0e5vK5nbL7a7ONiQP1V6tT/exeVJWtT7nSpE86tHJODH0pRa30/osdMFktUhWVhIosjqXy2QjpLrEdHeXCZWf9xfHVoqrdEXNeJ/NF+p+dhCG/FxQD7sNte5urzVnW4x1XI+cSgnVhc+sNQNqQNLDyUBymOVShcG8Doxkl2wo8ZRf16Gob3uHNLoIjGZPeoyjHOBYWHdHe4at6hWecyQJDqyVVLGctFMvO2PhKmuVbvDsNM4n591uJWSkoImX3XJjjIoyOcphNm08dN53j1qAx5jAt7ao3o5oVAzTcsOb/iQuICPv9GpkyMOIBlp8mXUj65B6M4pl4vSyGiFXGqVlyCgBbceRdbyumKZgUivR6knX2OynPVEvaHYtj6R6vUP6XGWWFy7brOxwfs4P0STv2aU2zOuRgTS0OTXhUofGlI6UYCizp4Kp1S0o+VrvXi11gxyDIVeQnlhdSK49mDe1i8w9DhA/UiOgBM2k1NbCftTQXd5zSjQlRbHn10Ezk9SIFVmIEyLtDnNmesXuHofcXAgyplhpBzzgMGZBn3ihoCupzlwf300+4yvO7dNb54Unuf5Tp/2++fic8c934eCK8rcHKcVQQ3xV+n+70N0vV9kJa5K6sL0fFxB4LzfpL/+kFr5AFy7CKtzvy2VcB49b2+NS+unXK3F77nL/DNh+AjpX7191KhCUP31XeOp8o/jxw1b7YeD+ZQbe/4/NjdoTKIcxvoS2OuG98n6j7z+3mv353y1ABTOmGwAA -->
