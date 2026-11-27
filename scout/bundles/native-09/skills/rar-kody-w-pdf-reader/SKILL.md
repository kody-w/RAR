---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "f32c63b6bf188ad530fec3f956c43a342f2ca399dad7031ae5a2c9e1e7379fc4", "source_kind": "rar-agent", "source_commit": "0a21fc0c745dd4b34563309973a15ce5ffea2c3b", "version": "1.0.4", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 f32c63b6bf188ad5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

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
    "version": "1.0.4",
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
        facts = _facts(reader, total, cap)
        return {"file": name, "pages": total, "found": [],
                "note": f"Nothing in {name} uses the words {' '.join(words)}. These lines hold its dates and amounts; "
                        f"quote the line that best answers them (a move-in or handover date is usually the start date), with its page.",
                "dates_and_amounts": facts}
    return {"file": name, "pages": total, "found": lines}


_FACT = None


def _facts(reader, total, cap, limit=15):
    """Lines carrying a date, a year or an amount: what people usually ask a document for."""
    import re
    global _FACT
    _FACT = _FACT or re.compile(r"(\b(19|20)\d\d\b|\$\s?\d|\b\d[\d,.]*\s*(dollars?|percent|%|days|months|years)\b|"
                                r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.? \d)", re.I)
    out, size = [], 0
    for i in range(total):
        for line in (reader.pages[i].extract_text() or "").splitlines():
            if _FACT.search(line) and size + len(line) <= cap and len(out) < limit:
                out.append(f"page {i + 1}: {line.strip()}")
                size += len(line)
    return out


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
