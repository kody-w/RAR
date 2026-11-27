---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "79d90ed177b957de0b2d8deadee3d51bc172ce4e5201a971948ea63bae347e51", "source_kind": "rar-agent", "source_commit": "2f5c2b3882956962f4c915df5872636a026d48bd", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 79d90ed177b957de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

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
    "version": "1.0.0",
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
