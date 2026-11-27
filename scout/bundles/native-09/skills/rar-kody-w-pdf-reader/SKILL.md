---
name: "rar-kody-w-pdf-reader"
description: "Reads a PDF the person has handed to this Brainstem and returns its text. Call it whenever they name a PDF or ask what is in one. With no file it lists their PDFs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/pdf_reader_agent", "rar_sha256": "ca40733518a8bc1efca3eecb91f159ade3ea75e1d216e8adf27b31ded68aefde", "source_kind": "rar-agent", "source_commit": "fa6ec14804a94ec0b3f2f4a3970dcb6f18aac266", "version": "1.0.6", "author": "kody-w", "tags": ["pdf", "documents", "reader", "phone", "offline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pdf_reader_agent.py` and embedded as the fenced Python below (sha256 ca40733518a8bc1e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pdf_reader_agent.py` first:

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
    "version": "1.0.6",
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
            out["more"] = (f"This is only part of a {total}-page PDF. If the answer is not here, call PdfReader again "
                           f"with look_for set to a few words for what they asked.")
        return json.dumps(out)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
