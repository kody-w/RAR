---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "aead7efc9eca21d1fff112ee0657a10a097b88516de1a8b5bc91fa3f69dc3aa4", "source_kind": "rar-agent", "source_commit": "699bbd0e9cb73876bf536cc3ed7d57c07b5b9873", "version": "1.0.7", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 aead7efc9eca21d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

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
    "version": "1.0.7",
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


def _lines(reader, total):
    """(page, line) for every non-empty line."""
    out = []
    for i in range(total):
        for line in (reader.pages[i].extract_text() or "").splitlines():
            if line.strip():
                out.append((i + 1, line.strip()))
    return out


def _shape(line):
    """A line with its numbers removed, to spot repeated headers and boilerplate."""
    import re
    return re.sub(r"\d+", "#", line.lower())


def _distinct(lines, cap, limit=40):
    """Lines that occur once in the document (numbers ignored): its real content, like a table of contents."""
    seen = {}
    for _, line in lines:
        seen[_shape(line)] = seen.get(_shape(line), 0) + 1
    out, size = [], 0
    for page, line in lines:
        if seen[_shape(line)] == 1 and len(line) > 25 and size + len(line) <= cap and len(out) < limit:
            out.append(f"page {page}: {line}")
            size += len(line)
    return out


def _find(reader, name, total, words, limit=12, cap=2500):
    """The lines that mention the most search words (stems, rare words weigh more), best first, with their pages."""
    lines = _lines(reader, total)
    stems = {w[:4] if len(w) >= 5 else w for w in words}
    pages_with = {st: len({p for p, l in lines if st in l.lower()}) for st in stems}
    common = {st for st, n in pages_with.items() if total >= 5 and n > total / 2}
    useful = stems - common or stems
    hits = []
    for page, line in lines:
        low = line.lower()
        score = sum(1.0 / (1 + pages_with[st]) for st in useful if st in low)
        if score:
            hits.append((-score, page, line))
    hits.sort()
    out, size = [], 0
    for _, page, line in hits[:limit]:
        if size + len(line) > cap:
            break
        out.append(f"page {page}: {line}")
        size += len(line)
    if not out or useful != stems and not any(st in l.lower() for _, _, l in hits[:1] for st in useful):
        facts = _facts(reader, total, cap // 2)
        return {"file": name, "pages": total, "found": [],
                "note": f"Nothing in {name} uses the words {' '.join(words)}. Below are its dates and amounts and its "
                        f"distinct lines; if one answers them under other words, quote it with its page.",
                "dates_and_amounts": facts, "distinct_lines": _distinct(lines, cap)}
    return {"file": name, "pages": total, "found": out}


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


_TOPICS = {}


def _topics(path, limit=10):
    """A short list of what a PDF covers, from its distinct lines (cached by modification time)."""
    try:
        key = (path, os.path.getmtime(path))
    except OSError:
        return ""
    if key not in _TOPICS:
        try:
            from pypdf import PdfReader
            reader = PdfReader(path)
            total = min(len(reader.pages), 300)
            names = []
            for line in _distinct(_lines(reader, total), 4000, 60):
                text = line.split(": ", 1)[1]
                head = text.split(":", 1)[0] if ":" in text[:40] else " ".join(text.split()[:3])
                head = head.strip(" .,;").lower()
                if head and head not in names:
                    names.append(head)
            _TOPICS[key] = ", ".join(names[:limit])
        except Exception:
            _TOPICS[key] = ""
    return _TOPICS[key]


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
            topics = _topics(os.path.join(folder, n))
            about = f"; covers: {topics}" if topics else ""
            shown.append(f"{n} (starts: \"{hint}\"{about})" if hint else n)
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
            out["more"] = (f"This is only part of a {total}-page PDF. Its distinct lines from every page are below; "
                           f"answer from one with its page, or call PdfReader again with look_for.")
            out["distinct_lines"] = _distinct(_lines(reader, total), 2000)
        return json.dumps(out)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
