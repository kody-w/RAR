---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "9ec0f532ccdc706c1c217241536823ab03a1310f95ea8ba5cfb34281e242e0fb", "source_kind": "rar-agent", "source_commit": "d28f8ea9dbfb92c646c182fa375cfff7b9fb2a72", "version": "1.0.3", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
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
    },
    "look_for": {
      "description": "A few words for what they asked about, like \"rent\" or \"start date\". Fill it whenever they ask a question, so the answer is found on any page.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 9ec0f532ccdc706c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

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
    "version": "1.0.3",
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


_STOP = {"the", "and", "for", "what", "when", "does", "say", "about", "how", "much", "this", "that", "with",
         "my", "is", "are", "of", "on", "in", "to", "a", "an", "it", "do", "i", "pdf", "file", "document"}


def _words(text):
    """Lowercased search words without filler; "dates" also matches "date"."""
    out = []
    for w in "".join(c.lower() if c.isalnum() else " " for c in str(text or "")).split():
        if len(w) > 2 and w not in _STOP:
            out.append(w[:-1] if w.endswith("s") and len(w) > 4 else w)
    return out


def _find(reader, name, total, words, limit=12, cap=2500):
    """The lines that mention the most search words, best first, each tagged with its page."""
    hits = []
    for i in range(total):
        for line in (reader.pages[i].extract_text() or "").splitlines():
            low = line.lower()
            score = sum(1 for w in set(words) if w in low)
            if score:
                hits.append((-score, i + 1, line.strip()))
    hits.sort()
    lines, size = [], 0
    for _, page, line in hits[:limit]:
        if size + len(line) > cap:
            break
        lines.append(f"page {page}: {line}")
        size += len(line)
    if not lines:
        return {"file": name, "pages": total, "found": [], "note": f"Nothing in {name} mentions {' '.join(words)}."}
    return {"file": name, "pages": total, "found": lines}


_PREVIEWS = {}


def _preview(path, limit=80):
    """The first words of page 1, cached by modification time; "" when unreadable."""
    try:
        key = (path, os.path.getmtime(path))
    except OSError:
        return ""
    if key not in _PREVIEWS:
        try:
            from pypdf import PdfReader
            text = (PdfReader(path).pages[0].extract_text() or "").split()
            _PREVIEWS[key] = " ".join(text)[:limit]
        except Exception:
            _PREVIEWS[key] = ""
    return _PREVIEWS[key]


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
                    "look_for": {"type": "string", "description": "A few words for what they asked about, like \"rent\" or \"start date\". Fill it whenever they ask a question, so the answer is found on any page."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        """Tells the chat which PDFs it holds, each with its opening words, so "my lease", "that document"
        or "is a burst pipe covered?" reaches this agent."""
        folder, names = _pdfs()
        if not names:
            return None
        shown = []
        for n in names[:12]:
            hint = _preview(os.path.join(folder, n))
            shown.append(f"{n} (starts: \"{hint}\")" if hint else n)
        more = f", and {len(names) - 12} more" if len(names) > 12 else ""
        return (f"The person has given you these PDFs: {'; '.join(shown)}{more}. When they ask about anything "
                f"these could answer, even as \"my lease\" or \"that document\", call PdfReader with the file name first.")

    def perform(self, file="", first_page=1, last_page=None, look_for="", **kwargs):
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
            words = _words(look_for)
            if words:
                return json.dumps(_find(reader, match, total, words))
            first = min(num(first_page, 1), total)
            last = min(max(num(last_page, first + 2), first), total)
            parts = []
            for i in range(first - 1, last):
                parts.append(f"--- page {i + 1} ---\n{(reader.pages[i].extract_text() or '').strip()}")
            text = "\n".join(parts)
        except Exception as e:  # a damaged or locked PDF should say so, not crash the chat
            return json.dumps({"error": f"Could not read {match}: {type(e).__name__}: {e}"})
        cut = len(text) > MAX_CHARS
        out = {"file": match, "pages": total, "read": [first, last], "text": text[:MAX_CHARS], "truncated": cut}
        if last < total or cut:
            out["more"] = (f"This is only part of a {total}-page PDF. If the answer is not here, call PdfReader again "
                           f"with look_for set to a few words for what they asked.")
        return json.dumps(out)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
