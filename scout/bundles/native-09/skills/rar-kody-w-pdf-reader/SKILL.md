---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "92ad7d498f0e23e5c5e98be8e08a9391ba9af1f8f1e7f5c26e60db585d7dce2e", "source_kind": "rar-agent", "source_commit": "f59505e415253a09bd0b49ee93aec270ec1880b0", "version": "1.0.1", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/pdf_reader_agent`. The original RAPP
agent is preserved byte-for-byte in `pdf_reader_agent.py` and in the RCI capsule.

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

PDF Reader — lists the PDFs you have handed to your Brainstem and reads the text of one, page by page.

Where it looks: the folder named by the BRAINSTEM_FILES setting (on a phone, the files you give your agents),
otherwise ~/Documents. It only reads; it never changes or sends a file.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "file": {
      "description": "The PDF's file name from the list, or \"\" to list the PDFs available.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 92ad7d498f0e23e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

```bash
python3 pdf_reader_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pdf_reader_agent.py   # or on stdin
python3 pdf_reader_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/pdf_reader_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pdf_reader_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/pdf_reader_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
# /// script
# dependencies = ["pypdf>=5"]
# ///
"""
PDF Reader — lists the PDFs you have handed to your Brainstem and reads the text of one, page by page.

Where it looks: the folder named by the BRAINSTEM_FILES setting (on a phone, the files you give your agents),
otherwise ~/Documents. It only reads; it never changes or sends a file.
"""

import json
import os

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/pdf_reader_agent",
    "version": "1.0.1",
    "display_name": "PDF Reader",
    "description": "Lists the PDFs handed to this Brainstem and reads the text of one, a page range at a time; read-only, no network.",
    "author": "kody-w",
    "tags": ["pdf", "documents", "reader", "phone", "offline"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # other hosts
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent  # type: ignore

MAX_CHARS = 6000


def _folder():
    return os.path.expanduser(os.environ.get("BRAINSTEM_FILES") or "~/Documents")


def _pdfs():
    folder = _folder()
    try:
        names = sorted(n for n in os.listdir(folder) if n.lower().endswith(".pdf"))
    except OSError:
        names = []
    return folder, names


class PdfReaderAgent(BasicAgent):
    def __init__(self):
        self.name = "PdfReader"
        self.metadata = {
            "name": self.name,
            "description": "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file": {"type": "string", "description": "The PDF's file name from the list, or \"\" to list the PDFs available."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        """Tells the chat which PDFs it holds, so "my lease" or "that document" reaches this agent."""
        _, names = _pdfs()
        if not names:
            return None
        shown = ", ".join(names[:12]) + (f", and {len(names) - 12} more" if len(names) > 12 else "")
        return (f"The person has given you these PDFs: {shown}. When they ask about any of them, even as "
                f"\"my lease\" or \"that document\", call PdfReader with the file name first.")

    def perform(self, file="", first_page=1, last_page=None, **kwargs):
        folder, names = _pdfs()
        if not str(file or "").strip():
            if not names:
                return json.dumps({"pdfs": [], "note": "No PDFs here yet. Hand one to your agents first."})
            return json.dumps({"pdfs": names})
        want = os.path.basename(str(file)).strip().lower()
        match = next((n for n in names if n.lower() == want), None) or \
            next((n for n in names if want.replace(".pdf", "") in n.lower()), None)
        if not match:
            return json.dumps({"error": f"No PDF named {file!r}.", "pdfs": names})
        try:
            from pypdf import PdfReader
        except ImportError:
            return json.dumps({"error": "pypdf is not installed here (pip install pypdf, or install this agent's card)."})
        try:
            reader = PdfReader(os.path.join(folder, match))
            total = len(reader.pages)
            def num(v, default):
                try:
                    v = int(float(v))
                except (TypeError, ValueError):
                    return default
                return v if v > 0 else default
            first = min(num(first_page, 1), total)
            last = min(max(num(last_page, first + 2), first), total)
            parts = []
            for i in range(first - 1, last):
                parts.append(f"--- page {i + 1} ---\n{(reader.pages[i].extract_text() or '').strip()}")
            text = "\n".join(parts)
        except Exception as e:  # a damaged or locked PDF should say so, not crash the chat
            return json.dumps({"error": f"Could not read {match}: {type(e).__name__}: {e}"})
        cut = len(text) > MAX_CHARS
        return json.dumps({"file": match, "pages": total, "read": [first, last],
                           "text": text[:MAX_CHARS], "truncated": cut})
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
