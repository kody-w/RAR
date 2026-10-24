---
name: "rar-kody-w-transcript2prototype"
description: "Turns a business transcript into a working prototype \u2014 demo script, injected M365 demo iframe, generated agents, twin test runs, factory export."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/transcript2prototype", "rar_sha256": "73d95878bc3f14510eefa8dd16707d5cc49e9c51becd7f2f4e4351197bdce939", "source_kind": "rar-agent", "source_commit": "44617333b6154dfbad78f7cde3291fb032b5c73d", "version": "1.0.4", "author": "Kody Wildfeuer", "tags": ["rapplication", "pipeline", "prototype", "demo", "cubby", "factory", "twin", "m365"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/transcript2prototype`. The original RAPP
agent is preserved byte-for-byte in `transcript2prototype_agent.py` and in the RCI capsule.

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

Transcript2PrototypeAgent - transcript in, working prototype out, one cubby per prototype.

A single-file rapplication for the RAPP brainstem. Paste a business transcript
and this agent walks the full prototyping pipeline conversationally, keeping
every prototype isolated in its own cubby (~/.brainstem/cubbies/<slug>/, the
same rapp-cubby/1.0 anatomy RappAgent uses, so cubby_list / super_rar /
cubby_egg all see it).

THE PIPELINE (one prototype, one cubby, one state machine):

  1. start      transcript -> analysis -> turn-by-turn demo script ->
                the static M365 Copilot demo template is generated with the
                script injected, base64-encoded ("bytecode"), and surfaced in
                an iframe inside the rapplication shell HTML. Scripted mode:
                every send is answered from the embedded script. Drive it
                with the Up arrow + Enter, exactly like the house demos.
  2. adjust     conversational edits to any turn, at any stage, regenerate
                the injected bytecode in place. The iframe always reflects
                the current demo script.
  3. build      the ACTUAL agent.py files are generated into the cubby's
                agents/ folder, grounded in the same analysis the demo used.
  4. test local the generated agent.pys are loaded in-process (a local twin)
                and the demo script is replayed against them turn by turn,
                scored, and reported.
  5. test twin  the agent.pys are injected into a live twin/brainstem
                (hot-reload, git-invisible to the twin) and the SAME demo is
                replayed over HTTP against /chat. The same rapplication
                iframe is regenerated in live mode pointed at the twin, so
                the demo you rehearsed now drives the real agents.
  6. export     everything is bundled into ONE factory singleton
                <slug>_factory_agent.py in the cubby's exports/ folder.
                THIS IS A GATE: the pipeline stops here. The singleton is
                the handoff artifact for the next stage of the process.

Browse prototypes with list / search (super-rar style, metadata + file
content) and pick one with focus. Everything runs fully local.

THE CALLER CONTRACT (nothing hardcoded): the LLM hosting this agent is the
intelligence; this file is the plumbing. Every input arrives as a parameter
and every parameter description tells the caller exactly what to provide -
that metadata is ALL the caller has. The preferred start path is the caller
analyzing the transcript itself and passing capabilities= (see the parameter
description for the exact JSON shape); the built-in keyword heuristic is only
the documented floor, and even its knobs (pain_markers, capability_vocabulary,
max_capabilities) are parameters. Free-text adjust instructions are returned
to the caller with the current script so the CALLER decides the wording and
re-calls with structured edits.

MIT (c) Kody Wildfeuer.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `transcript2prototype_agent.py` and embedded as the fenced Python below (sha256 73d95878bc3f1451…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `transcript2prototype_agent.py` first:

```bash
python3 transcript2prototype_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 transcript2prototype_agent.py   # or on stdin
python3 transcript2prototype_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""Transcript2PrototypeAgent - transcript in, working prototype out, one cubby per prototype.

A single-file rapplication for the RAPP brainstem. Paste a business transcript
and this agent walks the full prototyping pipeline conversationally, keeping
every prototype isolated in its own cubby (~/.brainstem/cubbies/<slug>/, the
same rapp-cubby/1.0 anatomy RappAgent uses, so cubby_list / super_rar /
cubby_egg all see it).

THE PIPELINE (one prototype, one cubby, one state machine):

  1. start      transcript -> analysis -> turn-by-turn demo script ->
                the static M365 Copilot demo template is generated with the
                script injected, base64-encoded ("bytecode"), and surfaced in
                an iframe inside the rapplication shell HTML. Scripted mode:
                every send is answered from the embedded script. Drive it
                with the Up arrow + Enter, exactly like the house demos.
  2. adjust     conversational edits to any turn, at any stage, regenerate
                the injected bytecode in place. The iframe always reflects
                the current demo script.
  3. build      the ACTUAL agent.py files are generated into the cubby's
                agents/ folder, grounded in the same analysis the demo used.
  4. test local the generated agent.pys are loaded in-process (a local twin)
                and the demo script is replayed against them turn by turn,
                scored, and reported.
  5. test twin  the agent.pys are injected into a live twin/brainstem
                (hot-reload, git-invisible to the twin) and the SAME demo is
                replayed over HTTP against /chat. The same rapplication
                iframe is regenerated in live mode pointed at the twin, so
                the demo you rehearsed now drives the real agents.
  6. export     everything is bundled into ONE factory singleton
                <slug>_factory_agent.py in the cubby's exports/ folder.
                THIS IS A GATE: the pipeline stops here. The singleton is
                the handoff artifact for the next stage of the process.

Browse prototypes with list / search (super-rar style, metadata + file
content) and pick one with focus. Everything runs fully local.

THE CALLER CONTRACT (nothing hardcoded): the LLM hosting this agent is the
intelligence; this file is the plumbing. Every input arrives as a parameter
and every parameter description tells the caller exactly what to provide -
that metadata is ALL the caller has. The preferred start path is the caller
analyzing the transcript itself and passing capabilities= (see the parameter
description for the exact JSON shape); the built-in keyword heuristic is only
the documented floor, and even its knobs (pain_markers, capability_vocabulary,
max_capabilities) are parameters. Free-text adjust instructions are returned
to the caller with the current script so the CALLER decides the wording and
re-calls with structured edits.

MIT (c) Kody Wildfeuer.
"""

from __future__ import annotations

import base64
import glob
import hashlib
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/transcript2prototype",
    "version": "1.0.4",
    "display_name": "Transcript2Prototype",
    "description": ("Turns a business transcript into a working prototype \u2014 demo script, injected M365 demo iframe, generated agents, twin test runs, factory export."),
    "author": "Kody Wildfeuer",
    "tags": ["rapplication", "pipeline", "prototype", "demo", "cubby",
             "factory", "twin", "m365"],
    "category": "workflow",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

PROTO_SCHEMA = "t2p-prototype/1.0"
RESULT_SCHEMA = "t2p-result/1.0"
CUBBY_SCHEMA = "rapp-cubby/1.0"
CUBBY_ANATOMY = ("agents", "organs", "senses", "rapplications",
                 "neighborhoods", "eggs", "show-and-tell")
STAGES = ("demo", "built", "local_passed", "twin_passed", "exported")
# a dedicated twin = a full kernel copy with its OWN agents, soul, auth and
# .brainstem_data (memory lives next to local_storage.py, so isolation is
# total). One twin per prototype - they run completely separately.
TWIN_KERNEL_FILES = ("brainstem.py", "local_storage.py", "index.html",
                     "VERSION", "requirements.txt")
TWIN_AUTH_FILES = (".copilot_token", ".copilot_session")
TWIN_KERNEL_AGENTS = ("basic_agent.py", "context_memory_agent.py",
                      "manage_memory_agent.py")
TWIN_PORT_BASE = 7311
# the public agent-stack library (kody-w.github.io/AI-Agent-Templates),
# surfaced as raw GitHub user data - overridable via templates_source=
TEMPLATES_SOURCE_DEFAULT = "https://raw.githubusercontent.com/kody-w/AI-Agent-Templates/main"
_SLUG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can", "do",
    "for", "from", "get", "had", "has", "have", "i", "if", "in", "into",
    "is", "it", "its", "just", "lot", "me", "my", "no", "not", "of", "on",
    "or", "our", "out", "so", "some", "than", "that", "the", "their",
    "them", "then", "there", "these", "they", "this", "to", "up", "us",
    "was", "we", "were", "what", "when", "where", "which", "who", "will",
    "with", "would", "you", "your", "really", "also", "very", "every",
    "about", "all", "one", "two", "could", "should", "right", "now",
    "like", "want", "need", "wish", "time", "way", "things", "thing",
    "going", "know", "yeah", "okay", "well", "team", "people", "someone",
    "still", "even", "back", "over", "more", "much", "today", "currently",
    "because", "takes", "make", "makes", "gets", "goes", "comes", "keeps",
    "honestly", "basically", "biggest", "same", "own", "each", "other",
}

# DEFAULT capability vocabulary (prefix match) for the no-capabilities
# fallback ONLY - callers override it with capability_vocabulary=, or skip
# the heuristic entirely by passing capabilities= (the preferred path).
DEFAULT_CAP_LEXICON = (
    "setup", "configur", "assist", "train", "deliver", "proposal", "creat",
    "content", "customiz", "pricing", "price", "optimiz", "onboard", "triag",
    "draft", "letter", "template", "search", "resolution", "claim", "email",
    "queue", "invoice", "contract", "report", "schedul", "approval", "return",
    "order", "ticket", "support", "integration", "workflow", "summar",
    "escalat", "routing", "compliance", "audit", "forecast", "renewal",
    "quote", "catalog", "inventory", "payment", "billing", "enrollment",
    "intake", "walkthrough", "adoption", "guided", "document", "tracking",
)

# speaker labels like "Maria (Ops Lead):" / "Priya:" at the start of a line -
# 1-3 capitalized words + optional (role). A sentence that happens to contain
# a colon ("Pricing optimization never happens: we ...") does NOT match.
_SPEAKER_RE = re.compile(
    r"^[A-Z][a-zA-Z.'-]{1,15}(?: [A-Z][a-zA-Z.'-]{1,15}){0,2}\s*"
    r"(?:\([^)]{0,40}\))?\s*:\s*")
# DEFAULT pain/need sentence markers for the fallback analyzer ONLY -
# callers override with pain_markers=, or bypass via capabilities=.
DEFAULT_PAIN_MARKERS = (
    "we need", "we want", "wish we", "would love", "problem", "manually",
    "by hand", "takes hours", "takes days", "takes weeks", "spend", "spends",
    "every time", "hard to", "difficult", "slow", "error-prone", "errors",
    "no way to", "can't", "cannot", "have to", "struggle", "pain", "bottleneck",
    "tedious", "repetitive", "falls through", "miss", "missed", "backlog",
)


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------
def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _slugify(text, fallback="prototype"):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:48] or fallback


def _camel(text):
    parts = re.split(r"[^A-Za-z0-9]+", text or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _words(text):
    return [w for w in re.findall(r"[a-zA-Z][a-zA-Z'-]+", (text or "").lower())
            if w not in _STOPWORDS and len(w) > 2]


def _sentences(text):
    raw = re.split(r"(?<=[.!?])\s+|\n{2,}", text or "")
    out = []
    for s in raw:
        s = " ".join(s.split())
        s = _SPEAKER_RE.sub("", s).strip()
        if len(s) > 12:
            out.append(s)
    return out


def _lex_hit(word, lexicon):
    return any(word.startswith(lx) for lx in lexicon)


def _csv_tuple(raw):
    """'a, b,c' -> ('a','b','c') lowercased; None/empty -> ()."""
    return tuple(w.strip().lower() for w in (raw or "").split(",") if w.strip())


CAPABILITIES_SCHEMA_HINT = (
    'capabilities must be a JSON array of 1-8 objects: [{"name": "2-3 word '
    'capability name", "description": "one sentence on what it does for the '
    'customer", "triggers": ["4-6", "lowercase", "routing", "keywords"], '
    '"knowledge": ["2-3 short facts quoted or derived from the transcript"], '
    '"response": "the ideal assistant reply for the demo (markdown ok, no '
    'emojis); SHOULD contain every trigger keyword - any missing ones are '
    'appended automatically", "demo_user": "what the user types in the demo '
    'to invoke this capability - SELF-CONTAINED, with any example details '
    'inline (name a specific letter/record/id) so the agent never has to ask '
    'for missing input", "synthetic_records": [2-4 flat JSON objects '
    'of realistic INVENTED demo data this capability operates over (ids, '
    'names, statuses, dates, amounts) - synthetic data fills the gaps, NEVER '
    'real customer data; auto-generated if omitted], "produces_file": '
    'optional - true or "filename.pdf" makes every reply DELIVER a real PDF '
    'as an M365-style attachment card, false suppresses it; omitted = '
    'document-sounding capabilities (pdf/report/letter/proposal...) get one '
    'automatically}]')


def _synthesize_records(key, name, triggers, company, n=3):
    """Deterministic, believable synthetic demo data for a capability -
    synthetic data fills gaps so no customer data is ever needed."""
    people = ("Avery Chen", "Jordan Patel", "Riley Gomez", "Sam Okafor")
    statuses = ("new", "in progress", "completed", "escalated")
    recs = []
    for i in range(n):
        t = triggers[i % len(triggers)] if triggers else key
        recs.append({
            "id": f"{re.sub('[^A-Za-z]', '', key)[:3].upper() or 'REC'}-{1001 + i}",
            "account": company,
            "title": f"{name} example {i + 1}: {t}",
            "owner": people[i % len(people)],
            "status": statuses[i % len(statuses)],
            "date": f"2026-06-{8 + i:02d}",
        })
    return recs


def _coerce_records(raw_records):
    """Caller-provided synthetic records -> list of flat str:str dicts."""
    out = []
    for r in (raw_records or [])[:6]:
        if isinstance(r, dict) and r:
            out.append({str(k)[:40]: str(v)[:200] for k, v in list(r.items())[:10]})
    return out


def _coerce_capabilities(raw, company="the customer"):
    """Validate + repair caller-provided capabilities. Raises ValueError with
    an instructive message; auto-repairs everything repairable so a slightly
    sloppy caller still succeeds (triggers from name, response gets missing
    trigger keywords appended, demo_user defaulted, synthetic demo data
    generated when the caller didn't invent any)."""
    parsed = json.loads(raw) if isinstance(raw, str) else raw
    if isinstance(parsed, dict):
        parsed = parsed.get("capabilities") or parsed.get("items")
    if not isinstance(parsed, list) or not parsed:
        raise ValueError(CAPABILITIES_SCHEMA_HINT)
    caps, used_keys = [], set()
    for i, c in enumerate(parsed[:8]):
        if not isinstance(c, dict) or not str(c.get("name") or "").strip():
            raise ValueError(f"capabilities[{i}] needs at least a 'name'. "
                             + CAPABILITIES_SCHEMA_HINT)
        name = str(c["name"]).strip()
        key = _slugify(name, f"cap{i + 1}").replace("-", "_")
        if key in used_keys:
            key = f"{key}_{i + 1}"
        used_keys.add(key)
        triggers = [str(t).strip().lower() for t in (c.get("triggers") or [])
                    if str(t).strip()][:6]
        if not triggers:
            triggers = [w for w in _words(name)][:4] or [key]
        description = str(c.get("description") or f"{name} capability").strip()
        knowledge = [str(k).strip() for k in (c.get("knowledge") or [])
                     if str(k).strip()][:3]
        response = str(c.get("response") or "").strip()
        if not response:
            response = (f"Here is how the prototype handles **{name}**: "
                        f"{description}")
        missing = [t for t in triggers if t not in response.lower()]
        if missing:
            response += "\n\nKey elements: " + ", ".join(triggers) + "."
        demo_user = str(c.get("demo_user") or "").strip() \
            or f"Show me how you handle {name.lower()}."
        synthetic = _coerce_records(c.get("synthetic_records")) \
            or _synthesize_records(key, name, triggers, company)
        caps.append({"key": key, "name": name,
                     "class_name": _camel(name) or f"Capability{i + 1}",
                     "description": description, "triggers": triggers,
                     "knowledge": knowledge, "response": response,
                     "demo_user": demo_user, "synthetic_records": synthetic,
                     # caller's call: False=never, True=always, str=filename,
                     # None=artifact-marker lexicon decides
                     "produces_file": c.get("produces_file")})
    return caps


def _kw_score(expected, actual_text):
    """Fraction of expected keywords present in actual_text (case-blind)."""
    if not expected:
        return 1.0, []
    t = (actual_text or "").lower()
    hits = [w for w in expected if w and w.lower() in t]
    return len(hits) / max(1, len(expected)), hits


# ---------------------------------------------------------------------------
# real file artifacts - capabilities that promise a document DELIVER one,
# rendered by the demo as an M365 Copilot style attachment card
# ---------------------------------------------------------------------------
DEFAULT_ARTIFACT_MARKERS = (
    "pdf", "document", "report", "letter", "proposal", "quote",
    "invoice", "contract", "statement", "deck", "summary sheet")


def _pdf_bytes(title, lines):
    """A tiny, valid, single-page PDF 1.4 - stdlib only, so generated agents
    and twins can produce real documents with zero dependencies."""
    def esc(t):
        return (str(t).replace("\\", r"\\").replace("(", r"\(")
                .replace(")", r"\)"))
    body = ["BT /F1 16 Tf 54 760 Td (" + esc(title[:90]) + ") Tj ET"]
    y = 728
    for ln in lines:
        chunks = [str(ln)[i:i + 95] for i in range(0, len(str(ln)), 95)] or [""]
        for chunk in chunks:
            body.append("BT /F1 10 Tf 54 %d Td (%s) Tj ET" % (y, esc(chunk)))
            y -= 16
            if y < 60:
                break
        if y < 60:
            break
    stream = "\n".join(body).encode("latin-1", "replace")
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
        + stream + b"\nendstream",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offs = []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += str(i).encode() + b" 0 obj\n" + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 " + str(len(objs) + 1).encode() + b"\n0000000000 65535 f \n"
    for off in offs:
        out += ("%010d 00000 n \n" % off).encode()
    out += (b"trailer\n<< /Size " + str(len(objs) + 1).encode()
            + b" /Root 1 0 R >>\nstartxref\n" + str(xref).encode()
            + b"\n%%EOF\n")
    return bytes(out)


def _png_square(size, rgba):
    """A tiny valid solid-color PNG - stdlib only, for Teams app icons."""
    import struct
    import zlib as _z

    def chunk(t, d):
        c = t + d
        return struct.pack(">I", len(d)) + c + struct.pack(">I", _z.crc32(c) & 0xffffffff)
    raw = b"".join(b"\x00" + bytes(rgba) * size for _ in range(size))
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", _z.compress(raw))
            + chunk(b"IEND", b""))


def _attachment_marker(name, blob, mime="application/pdf"):
    """The transport convention: the demo template extracts these markers
    from assistant text and renders them as clickable attachment cards."""
    return ('\n\n[[attachment name="%s" mime="%s" b64="%s"]]'
            % (name, mime, base64.b64encode(blob).decode("ascii")))


def _cap_artifact(cap, markers=None):
    """Decide whether a capability delivers a real file, and its filename.
    The caller stays in charge: capability `produces_file` may be False
    (never), True (always), or an explicit filename; otherwise the
    artifact marker lexicon (a parameter too) decides."""
    explicit = cap.get("produces_file")
    if explicit is False:
        return None
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    if explicit is not True:
        hay = " ".join([
            str(cap.get("name") or ""), str(cap.get("description") or ""),
            str(cap.get("response") or ""),
            " ".join(cap.get("triggers") or [])]).lower()
        if not any(m in hay for m in (markers or DEFAULT_ARTIFACT_MARKERS)):
            return None
    base = re.sub(r"[^a-z0-9]+", "_",
                  str(cap.get("name") or "document").lower()).strip("_")
    return (base or "document") + ".pdf"


def _http_ok(url, timeout=4):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return 200 <= r.status < 400
    except Exception:  # noqa: BLE001
        return False


def _get_json(url, timeout=6):
    """GET JSON -> parsed|None. stdlib only, never raises."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None


def _free_port(start, tries=60):
    for p in range(start, start + tries):
        with socket.socket() as s:
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    return start


def _post_json(url, payload, timeout=90):
    """POST JSON -> (parsed_json|None, error|None). stdlib only."""
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", "replace")), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001 - offline must never crash an agent
        return None, str(e)


# ---------------------------------------------------------------------------
# the injected M365 Copilot demo template ("bytecode" payload)
# tokens are replaced with .replace() - never .format() (CSS braces).
# ---------------------------------------------------------------------------
M365_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body { font-family: "Segoe UI Variable Text","Segoe UI","Segoe UI Web (West European)",-apple-system,BlinkMacSystemFont,Roboto,"Helvetica Neue",sans-serif; background: #ffffff; color: #242424; display: flex; flex-direction: column; overflow: hidden; font-size: 14px; }
.ic { display: inline-block; vertical-align: middle; flex-shrink: 0; }
/* ── suite header ── */
.suite { height: 48px; background: #ffffff; border-bottom: 1px solid #e0e0e0; display: flex; align-items: center; padding: 0 14px 0 10px; gap: 10px; flex-shrink: 0; }
.suite .waffle { width: 36px; height: 36px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #616161; cursor: pointer; }
.suite .waffle:hover { background: #f0f0f0; }
.suite .brand { display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: #242424; }
.suite .sp { flex: 1; }
.suite .hbtn { width: 32px; height: 32px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #424242; font-size: 14px; cursor: pointer; }
.suite .hbtn:hover { background: #f0f0f0; }
.suite .me { width: 28px; height: 28px; border-radius: 50%; background: #e6e6e6; color: #616161; display: flex; align-items: center; justify-content: center; }
/* ── app body ── */
.app { flex: 1; display: flex; min-height: 0; }
/* module rail */
.rail { width: 68px; background: #f5f5f5; display: flex; flex-direction: column; align-items: center; padding: 8px 0; gap: 2px; flex-shrink: 0; }
.rail .item { width: 60px; padding: 7px 0 5px; border-radius: 6px; display: flex; flex-direction: column; align-items: center; gap: 3px; color: #424242; font-size: 10px; cursor: pointer; position: relative; }
.rail .item:hover { background: #ebebeb; }
.rail .item.sel { color: #0F6CBD; font-weight: 600; }
.rail .item.sel::before { content: ""; position: absolute; left: -4px; top: 50%; transform: translateY(-50%); width: 3px; height: 20px; border-radius: 2px; background: #0F6CBD; }
/* conversation pane */
.pane { width: 300px; background: #fafafa; border-right: 1px solid #e0e0e0; display: flex; flex-direction: column; flex-shrink: 0; padding: 10px 8px; gap: 4px; overflow-y: auto; }
.pane .top { display: flex; align-items: center; gap: 6px; padding: 0 4px 8px; }
.pane .psearch { flex: 1; display: flex; align-items: center; gap: 6px; background: #ffffff; border: 1px solid #d1d1d1; border-radius: 4px; padding: 5px 8px; color: #616161; font-size: 13px; }
.pane .pbtn { width: 32px; height: 32px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #424242; cursor: pointer; }
.pane .pbtn:hover { background: #f0f0f0; }
.pane .sect { font-size: 11px; font-weight: 600; color: #616161; padding: 10px 8px 4px; }
.pane .row { display: flex; align-items: center; gap: 8px; padding: 7px 8px; border-radius: 4px; font-size: 13px; color: #242424; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.pane .row:hover { background: #f0f0f0; }
.pane .row.sel { background: #ebebeb; font-weight: 600; }
.pane .row .rt { overflow: hidden; text-overflow: ellipsis; }
.pane .row .tile { width: 18px; height: 18px; border-radius: 4px; }
.pane .link { color: #115EA3; font-size: 13px; padding: 6px 8px; cursor: pointer; }
/* chat column */
.chatcol { flex: 1; display: flex; flex-direction: column; min-width: 0; background: #ffffff; }
.agent-hdr { height: 48px; border-bottom: 1px solid #f0f0f0; display: flex; align-items: center; gap: 10px; padding: 0 16px; flex-shrink: 0; }
.agent-hdr .tile { width: 26px; height: 26px; border-radius: 6px; }
.agent-hdr .an { font-size: 14px; font-weight: 600; }
.agent-hdr .sp { flex: 1; }
.agent-hdr .hbtn { width: 32px; height: 32px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #424242; cursor: pointer; }
.agent-hdr .hbtn:hover { background: #f0f0f0; }
/* canvas */
.canvas { flex: 1; overflow-y: auto; }
.thread { max-width: 768px; margin: 0 auto; padding: 24px 24px 12px; display: flex; flex-direction: column; gap: 18px; min-height: 100%; }
/* zero state */
.welcome { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 12px; margin: auto 0; }
.welcome .tile { width: 56px; height: 56px; border-radius: 14px; margin-bottom: 14px; }
.welcome h1 { font-size: 24px; font-weight: 600; color: #242424; }
.welcome .byline { font-size: 13px; color: #616161; margin-top: 3px; }
.welcome p { font-size: 14px; color: #616161; line-height: 1.5; max-width: 560px; margin-top: 10px; }
.starters { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 26px; width: 100%; max-width: 640px; }
.starter { background: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px 14px; text-align: left; cursor: pointer; box-shadow: 0 0 2px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.14); transition: box-shadow .12s; }
.starter:hover { box-shadow: 0 0 2px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.14); }
.starter .st { font-size: 13.5px; font-weight: 600; color: #242424; margin-bottom: 3px; }
.starter .ss { font-size: 12.5px; color: #616161; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
/* messages */
.msg-user { align-self: flex-end; max-width: 76%; background: #EBF3FC; border-radius: 12px; padding: 10px 14px; font-size: 14px; line-height: 1.45; color: #242424; white-space: pre-wrap; word-wrap: break-word; }
.msg-ai { align-self: stretch; font-size: 15px; line-height: 1.55; color: #242424; word-wrap: break-word; }
.msg-ai .body p { margin: 0 0 10px; }
.msg-ai .body p:last-child { margin-bottom: 0; }
.msg-ai .body h1, .msg-ai .body h2, .msg-ai .body h3 { margin: 14px 0 6px; color: #242424; }
.msg-ai .body h1 { font-size: 18px; } .msg-ai .body h2 { font-size: 16px; } .msg-ai .body h3 { font-size: 15px; }
.msg-ai .body strong { font-weight: 600; }
.msg-ai .body code { background: #f5f5f5; border: 1px solid #e0e0e0; padding: 1px 5px; border-radius: 4px; font-size: 13px; font-family: Consolas, Monaco, monospace; }
.msg-ai .body pre { background: #f5f5f5; border: 1px solid #e0e0e0; padding: 12px; border-radius: 8px; overflow-x: auto; margin: 8px 0; }
.msg-ai .body pre code { background: none; border: none; padding: 0; }
.msg-ai .body blockquote { border-left: 3px solid #d1d1d1; padding: 4px 12px; margin: 8px 0; color: #424242; }
.msg-ai .body ul, .msg-ai .body ol { padding-left: 24px; margin: 6px 0 10px; }
.msg-ai .body li { margin: 3px 0; }
.msg-ai .body table { border-collapse: collapse; margin: 10px 0; font-size: 13.5px; width: 100%; }
.msg-ai .body th { text-transform: none; font-weight: 600; text-align: left; border-bottom: 1.5px solid #d1d1d1; padding: 6px 10px; color: #424242; }
.msg-ai .body td { border-bottom: 1px solid #f0f0f0; padding: 6px 10px; }
.msg-ai .body a { color: #115EA3; text-decoration: none; }
.msg-ai .body a:hover { text-decoration: underline; }
.msg-ai .body hr { border: none; border-top: 1px solid #e0e0e0; margin: 12px 0; }
.ftr-row { display: flex; align-items: center; gap: 2px; margin-top: 10px; }
.ftr-btn { width: 28px; height: 28px; border: none; background: none; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #616161; cursor: pointer; }
.ftr-btn:hover { background: #f0f0f0; color: #242424; }
.ftr-btn .ic { width: 16px; height: 16px; }
.ftr-note { margin-left: auto; font-size: 11px; color: #616161; }
/* widget card (MCP app) */
.widget-card { border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden; margin-top: 4px; box-shadow: 0 0 2px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.14); }
.widget-hdr { display: flex; align-items: center; gap: 6px; padding: 7px 12px; font-size: 12px; color: #616161; border-bottom: 1px solid #f0f0f0; background: #fafafa; }
.widget-card iframe { width: 100%; height: 440px; border: none; display: block; background: #fff; }
/* shimmer (streaming) */
.replay-divider { text-align: center; font-size: 11px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase; color: #5b5fc7; padding: 8px 0 2px; }
.replay-divider .sub { display: block; font-weight: 400; text-transform: none; letter-spacing: 0; color: #616161; font-size: 11.5px; margin-top: 2px; }
.test-chip { display: inline-block; margin-top: 8px; font-size: 10.5px; font-weight: 700; letter-spacing: 0.5px; padding: 2px 10px; border-radius: 9px; }
.test-chip.pass { background: #f1faf1; color: #107c10; border: 1px solid #9fd89f; }
.test-chip.fail { background: #fdf3f4; color: #b10e1c; border: 1px solid #eeacb2; }
.shimmer-row { display: flex; gap: 10px; align-items: flex-start; }
.shimmer-lines { flex: 1; display: flex; flex-direction: column; gap: 8px; padding-top: 2px; }
.shimmer { height: 12px; border-radius: 6px; background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 37%, #f0f0f0 63%); background-size: 400% 100%; animation: shm 1.4s ease infinite; }
@keyframes shm { 0% { background-position: 100% 50%; } 100% { background-position: 0 50%; } }
/* attachment cards - M365 Copilot file-card look */
.file-card { display: flex; align-items: center; gap: 10px; border: 1px solid #d1d1d1; border-radius: 8px; padding: 10px 12px; margin-top: 10px; max-width: 340px; cursor: pointer; background: #fff; transition: box-shadow .1s, border-color .1s; }
.file-card:hover { border-color: #b5b5b5; box-shadow: 0 2px 6px rgba(0,0,0,.1); }
.file-card .fc-icon { width: 30px; height: 36px; flex-shrink: 0; }
.file-card .fc-name { font-size: 13.5px; font-weight: 600; color: #242424; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.file-card .fc-meta { font-size: 11.5px; color: #616161; margin-top: 1px; }
/* composer */
.dock { flex-shrink: 0; padding: 8px 24px 10px; }
.dock-inner { max-width: 768px; margin: 0 auto; }
.composer { background: #ffffff; border: 1px solid #d1d1d1; border-radius: 12px; box-shadow: 0 1px 2px rgba(0,0,0,.06); padding: 10px 12px 8px; transition: border-color .1s; }
.composer:focus-within { border-color: #0F6CBD; }
.composer input { width: 100%; border: none; outline: none; font-size: 15px; color: #242424; font-family: inherit; padding: 2px 4px 10px; background: none; }
.composer input::placeholder { color: #707070; }
.comp-row { display: flex; align-items: center; gap: 4px; }
.cbtn { width: 32px; height: 32px; border: none; background: none; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #424242; cursor: pointer; }
.cbtn:hover { background: #f0f0f0; }
.comp-row .sp { flex: 1; }
.send { width: 36px; height: 36px; border: none; border-radius: 50%; background: #e0e0e0; color: #ffffff; display: flex; align-items: center; justify-content: center; cursor: default; transition: background .1s; }
.send.ready { background: #0F6CBD; cursor: pointer; }
.send.ready:hover { background: #115EA3; }
.disclaim { text-align: center; font-size: 11px; color: #616161; padding: 7px 0 0; }
/* teleprompter (presenter only) */
.prompter { position: fixed; bottom: 96px; right: 18px; width: 340px; background: #1e1e1e; border: 1px solid #333; border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.4); z-index: 9999; overflow: hidden; transition: opacity 0.2s; }
.prompter.hidden { opacity: 0; pointer-events: none; }
.prompter-bar { display: flex; align-items: center; gap: 8px; padding: 8px 14px; background: #2b2b2b; border-bottom: 1px solid #333; }
.pr-title { font-size: 11px; color: #9fa3ff; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
.pr-count { margin-left: auto; font-size: 11px; color: #888; font-family: monospace; }
.pr-toggle { background: none; border: none; color: #666; font-size: 14px; cursor: pointer; }
.prompter-body { padding: 12px 14px; }
.pr-step { font-size: 12px; color: #ccc; line-height: 1.5; margin-bottom: 8px; }
.pr-num { color: #9fa3ff; font-weight: 700; margin-right: 6px; }
.pr-expect { font-size: 11px; color: #4ade80; line-height: 1.5; padding: 6px 10px; background: rgba(74,222,128,0.08); border-radius: 6px; border-left: 3px solid #4ade80; }
.pr-expect::before { content: "EXPECT: "; font-weight: 700; font-size: 10px; }
.pr-keys { padding: 6px 14px 10px; font-size: 10px; color: #555; text-align: center; border-top: 1px solid #333; }
.pr-keys kbd { background: #333; padding: 1px 6px; border-radius: 3px; border: 1px solid #444; color: #aaa; }
@media (max-width: 1100px) { .pane { display: none; } }
@media (max-width: 800px) { .rail { display: none; } }
</style>
</head>
<body>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden"><defs><radialGradient id="mkg0" cx="85.44%" cy="100.65%" r="105.12%" gradientTransform="scale(-.8553 -1) rotate(50.927 2.041 -1.946)"><stop offset=".096" stop-color="#00AEFF"/><stop offset=".773" stop-color="#2253CE"/><stop offset="1" stop-color="#0736C4"/></radialGradient><radialGradient id="mkg1" cx="18.14%" cy="32.93%" r="95.61%" gradientTransform="scale(.8897 1) rotate(52.069 .193 .352)"><stop offset="0" stop-color="#FFB657"/><stop offset=".634" stop-color="#FF5F3D"/><stop offset=".923" stop-color="#C02B3C"/></radialGradient><linearGradient id="mkg2" x1="39.46%" y1="12.12%" x2="46.88%" y2="103.77%"><stop offset=".156" stop-color="#0D91E1"/><stop offset=".487" stop-color="#52B471"/><stop offset=".652" stop-color="#98BD42"/><stop offset=".937" stop-color="#FFC800"/></linearGradient><radialGradient id="mkg4" cx="82.99%" cy="-9.79%" r="140.62%" gradientTransform="scale(-1 -.9441) rotate(-70.872 .142 1.17)"><stop offset=".066" stop-color="#8C48FF"/><stop offset=".5" stop-color="#F2598A"/><stop offset=".896" stop-color="#FFB152"/></radialGradient><linearGradient id="cpt" x1="0" y1="0" x2="28" y2="28" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#33CCFF"/><stop offset=".4" stop-color="#3B6CEB"/><stop offset=".72" stop-color="#9B5CF7"/><stop offset="1" stop-color="#FF63B8"/></linearGradient></defs><symbol id="i-chat" viewBox="0 0 20 20"><path fill="currentColor" d="M10 2C14.42 2 18 5.58 18 10C18 14.42 14.42 18 10 18C8.73 18 7.5 17.7 6.39 17.14L6.27 17.07L2.62 17.99C2.31 18.06 2.03 17.84 2 17.54L2 17.46L2.01 17.38L2.92 13.73L2.86 13.62C2.41 12.72 2.12 11.74 2.03 10.73L2.01 10.35L2 10C2 5.58 5.58 2 10 2ZM10 3C6.13 3 3 6.13 3 10C3 11.22 3.31 12.39 3.89 13.42C3.94 13.51 3.96 13.6 3.96 13.7L3.94 13.79L3.19 16.81L6.21 16.06C6.27 16.04 6.34 16.04 6.4 16.05L6.49 16.07L6.58 16.11C7.61 16.69 8.78 17 10 17C13.87 17 17 13.87 17 10C17 6.13 13.87 3 10 3ZM10.5 11C10.78 11 11 11.22 11 11.5C11 11.75 10.82 11.95 10.59 11.99L10.5 12H7.5C7.22 12 7 11.78 7 11.5C7 11.25 7.18 11.05 7.41 11.01L7.5 11H10.5ZM12.5 8C12.78 8 13 8.22 13 8.5C13 8.75 12.82 8.95 12.59 8.99L12.5 9H7.5C7.22 9 7 8.78 7 8.5C7 8.25 7.18 8.05 7.41 8.01L7.5 8H12.5Z"/></symbol><symbol id="i-search" viewBox="0 0 20 20"><path fill="currentColor" d="M13.73 14.44C12.59 15.41 11.12 16 9.5 16C5.91 16 3 13.09 3 9.5C3 5.91 5.91 3 9.5 3C13.09 3 16 5.91 16 9.5C16 11.12 15.41 12.59 14.44 13.73L17.85 17.15C18.05 17.34 18.05 17.66 17.85 17.85C17.68 18.03 17.41 18.05 17.22 17.91L17.15 17.85L13.73 14.44ZM13.02 13.73C13.28 13.51 13.51 13.28 13.73 13.02C14.52 12.07 15 10.84 15 9.5C15 6.46 12.54 4 9.5 4C6.46 4 4 6.46 4 9.5C4 12.54 6.46 15 9.5 15C10.84 15 12.07 14.52 13.02 13.73Z"/></symbol><symbol id="i-notebook" viewBox="0 0 20 20"><path fill="currentColor" d="M5.5 5C5.22 5 5 5.22 5 5.5V7.5C5 7.78 5.22 8 5.5 8H12.5C12.78 8 13 7.78 13 7.5V5.5C13 5.22 12.78 5 12.5 5H5.5ZM6 7V6H12V7H6ZM3 4C3 2.9 3.9 2 5 2H13C14.1 2 15 2.9 15 4V16C15 17.1 14.1 18 13 18H5C3.9 18 3 17.1 3 16V4ZM5 3C4.45 3 4 3.45 4 4V16C4 16.55 4.45 17 5 17H13C13.55 17 14 16.55 14 16V4C14 3.45 13.55 3 13 3H5ZM16 6H16.5C16.78 6 17 6.22 17 6.5V8C17 8.28 16.78 8.5 16.5 8.5H16V6ZM16.5 9.5H16V12H16.5C16.78 12 17 11.78 17 11.5V10C17 9.72 16.78 9.5 16.5 9.5ZM16 13H16.5C16.78 13 17 13.22 17 13.5V15C17 15.28 16.78 15.5 16.5 15.5H16V13Z"/></symbol><symbol id="i-pen" viewBox="0 0 20 20"><path fill="currentColor" d="M17.18 2.93C16.03 1.71 14.1 1.69 12.92 2.87L3.55 12.25C3.22 12.57 2.99 12.99 2.89 13.44L2.01 17.39C1.97 17.56 2.03 17.73 2.15 17.85C2.27 17.97 2.44 18.02 2.61 17.99L6.53 17.11C7 17.01 7.43 16.78 7.77 16.44L15.75 8.46L16.09 8.79C16.48 9.18 16.48 9.82 16.09 10.21L15.15 11.15C14.95 11.34 14.95 11.66 15.15 11.85C15.34 12.05 15.66 12.05 15.85 11.85L16.79 10.91C17.57 10.13 17.57 8.87 16.79 8.09L16.46 7.75L17.13 7.08C18.27 5.94 18.29 4.1 17.18 2.93ZM13.63 3.58C14.41 2.79 15.69 2.81 16.45 3.61C17.19 4.39 17.18 5.61 16.42 6.37L7.06 15.73C6.86 15.93 6.6 16.08 6.32 16.14L3.16 16.84L3.87 13.66C3.93 13.39 4.06 13.15 4.25 12.95L13.63 3.58Z"/></symbol><symbol id="i-apps" viewBox="0 0 20 20"><path fill="currentColor" d="M4.5 17C3.72 17 3.08 16.41 3.01 15.65L3 15.5V4.5C3 3.72 3.59 3.08 4.36 3.01L4.5 3H9C9.78 3 10.42 3.6 10.49 4.36L10.5 4.5V4.76L12.69 2.49C13.23 1.93 14.1 1.88 14.7 2.35L14.81 2.45L17.57 5.17C18.12 5.72 18.16 6.59 17.68 7.19L17.58 7.3L15.27 9.5L15.5 9.5C16.28 9.5 16.92 10.1 16.99 10.86L17 11V15.5C17 16.28 16.41 16.92 15.64 16.99L15.5 17H4.5ZM9.5 10.5H4V15.5C4 15.72 4.14 15.9 4.33 15.97L4.41 15.99L4.5 16H9.5V10.5ZM15.5 10.5H10.5V16H15.5C15.75 16 15.95 15.82 15.99 15.59L16 15.5V11C16 10.76 15.82 10.55 15.59 10.51L15.5 10.5ZM10.5 7.71V9.5H12.29L10.5 7.71ZM9 4H4.5C4.25 4 4.05 4.18 4.01 4.41L4 4.5V9.5H9.5V4.5C9.5 4.29 9.36 4.1 9.17 4.03L9.09 4.01L9 4ZM14.12 3.17C13.94 3 13.67 2.98 13.48 3.12L13.41 3.18L10.79 5.89C10.63 6.07 10.61 6.33 10.74 6.52L10.8 6.59L13.41 9.21C13.58 9.38 13.84 9.4 14.03 9.28L14.11 9.22L16.87 6.59C17.04 6.42 17.06 6.15 16.92 5.95L16.87 5.89L14.12 3.17Z"/></symbol><symbol id="i-bot" viewBox="0 0 20 20"><path fill="currentColor" d="M12 5.5C11.45 5.5 11 5.95 11 6.5C11 7.05 11.45 7.5 12 7.5C12.55 7.5 13 7.05 13 6.5C13 5.95 12.55 5.5 12 5.5ZM7 6.5C7 5.95 7.45 5.5 8 5.5C8.55 5.5 9 5.95 9 6.5C9 7.05 8.55 7.5 8 7.5C7.45 7.5 7 7.05 7 6.5ZM10.5 2.5C10.5 2.22 10.28 2 10 2C9.72 2 9.5 2.22 9.5 2.5V3H6.5C5.67 3 5 3.67 5 4.5V8.5C5 9.33 5.67 10 6.5 10H13.5C14.33 10 15 9.33 15 8.5V4.5C15 3.67 14.33 3 13.5 3H10.5V2.5ZM6.5 4H13.5C13.78 4 14 4.22 14 4.5V8.5C14 8.78 13.78 9 13.5 9H6.5C6.22 9 6 8.78 6 8.5V4.5C6 4.22 6.22 4 6.5 4ZM10.25 18C12.87 17.96 14.44 17.4 15.37 16.56C16.25 15.76 16.46 14.78 16.49 14H16.5V13.31C16.5 12.31 15.69 11.5 14.69 11.5H11.5V11.5H8.5V11.5H5.31C4.31 11.5 3.5 12.31 3.5 13.31V14H3.51C3.54 14.78 3.75 15.76 4.63 16.56C5.56 17.4 7.13 17.96 9.75 18V18H10.25V18ZM5.31 12.5H14.69C15.14 12.5 15.5 12.87 15.5 13.31V13.75C15.5 14.44 15.37 15.21 14.7 15.82C14.01 16.45 12.66 17 10 17C7.34 17 5.99 16.45 5.3 15.82C4.63 15.21 4.5 14.44 4.5 13.75V13.31C4.5 12.87 4.86 12.5 5.31 12.5Z"/></symbol><symbol id="i-add" viewBox="0 0 20 20"><path fill="currentColor" d="M10 2.5C10.28 2.5 10.5 2.72 10.5 3V9.5H17C17.28 9.5 17.5 9.72 17.5 10C17.5 10.28 17.28 10.5 17 10.5H10.5V17C10.5 17.28 10.28 17.5 10 17.5C9.72 17.5 9.5 17.28 9.5 17V10.5H3C2.72 10.5 2.5 10.28 2.5 10C2.5 9.72 2.72 9.5 3 9.5H9.5V3C9.5 2.72 9.72 2.5 10 2.5Z"/></symbol><symbol id="i-send" viewBox="0 0 20 20"><path fill="currentColor" d="M2.72 2.05C2.55 1.96 2.34 1.99 2.18 2.11C2.03 2.24 1.97 2.44 2.02 2.63L3.51 8.25C3.57 8.44 3.72 8.58 3.92 8.61L10.77 9.75C11.05 9.8 11.05 10.2 10.77 10.25L3.92 11.39C3.72 11.42 3.57 11.56 3.51 11.75L2.02 17.37C1.97 17.56 2.03 17.76 2.18 17.89C2.34 18.01 2.55 18.04 2.72 17.95L17.72 10.45C17.89 10.36 18 10.19 18 10C18 9.81 17.89 9.64 17.72 9.55L2.72 2.05Z"/></symbol><symbol id="i-mic" viewBox="0 0 20 20"><path fill="currentColor" d="M10 13C11.66 13 13 11.66 13 10V5C13 3.34 11.66 2 10 2C8.34 2 7 3.34 7 5V10C7 11.66 8.34 13 10 13ZM10 12C8.9 12 8 11.1 8 10V5C8 3.9 8.9 3 10 3C11.1 3 12 3.9 12 5V10C12 11.1 11.1 12 10 12ZM5 9.5C5.28 9.5 5.5 9.72 5.5 10C5.5 12.49 7.51 14.5 10 14.5C12.49 14.5 14.5 12.49 14.5 10C14.5 9.72 14.72 9.5 15 9.5C15.28 9.5 15.5 9.72 15.5 10C15.5 12.87 13.3 15.22 10.5 15.48V17.5C10.5 17.78 10.28 18 10 18C9.72 18 9.5 17.78 9.5 17.5V15.48C6.7 15.22 4.5 12.87 4.5 10C4.5 9.72 4.72 9.5 5 9.5Z"/></symbol><symbol id="i-attach" viewBox="0 0 20 20"><path fill="currentColor" d="M4.83 10.48L10.48 4.83C11.66 3.66 13.56 3.66 14.73 4.83C15.9 6 15.9 7.9 14.73 9.07L8.01 15.79C7.42 16.37 6.47 16.37 5.89 15.79C5.3 15.2 5.3 14.25 5.89 13.67L11.9 7.66C12.09 7.46 12.09 7.14 11.9 6.95C11.7 6.75 11.39 6.75 11.19 6.95L5.18 12.96C4.21 13.94 4.21 15.52 5.18 16.5C6.16 17.47 7.74 17.47 8.72 16.5L15.43 9.78C17 8.22 17 5.68 15.43 4.12C13.87 2.56 11.34 2.56 9.78 4.12L4.12 9.78C3.93 9.97 3.93 10.29 4.12 10.48C4.32 10.68 4.63 10.68 4.83 10.48Z"/></symbol><symbol id="i-copy" viewBox="0 0 20 20"><path fill="currentColor" d="M8 2C6.9 2 6 2.9 6 4V14C6 15.1 6.9 16 8 16H14C15.1 16 16 15.1 16 14V4C16 2.9 15.1 2 14 2H8ZM7 4C7 3.45 7.45 3 8 3H14C14.55 3 15 3.45 15 4V14C15 14.55 14.55 15 14 15H8C7.45 15 7 14.55 7 14V4ZM4 6C4 5.26 4.4 4.61 5 4.27V14.5C5 15.88 6.12 17 7.5 17H13.73C13.39 17.6 12.74 18 12 18H7.5C5.57 18 4 16.43 4 14.5V6Z"/></symbol><symbol id="i-like" viewBox="0 0 20 20"><path fill="currentColor" d="M10.05 2.29C10.39 1.32 11.68 0.87 12.48 1.7C12.65 1.87 12.81 2.06 12.92 2.22C13.24 2.7 13.37 3.34 13.42 3.95C13.47 4.58 13.44 5.25 13.37 5.86C13.31 6.48 13.21 7.04 13.13 7.45C13.13 7.47 13.13 7.48 13.12 7.5H14.01C15.88 7.5 17.29 9.2 16.96 11.04L16.27 14.8C15.8 17.39 13.21 19.03 10.66 18.33L5.06 16.81C4.15 16.56 3.45 15.81 3.27 14.89L2.92 13.12C2.64 11.73 3.7 10.56 4.83 10.12C5.15 9.99 5.44 9.83 5.67 9.63C7.38 8.11 7.99 6.9 9.05 4.78C9.41 4.07 9.77 3.1 10.05 2.29ZM12.02 7.88L12.02 7.88L12.02 7.87L12.03 7.84C12.03 7.81 12.04 7.77 12.05 7.71C12.08 7.61 12.11 7.45 12.15 7.26C12.23 6.87 12.32 6.33 12.38 5.76C12.44 5.18 12.47 4.58 12.43 4.03C12.38 3.48 12.27 3.05 12.09 2.78C12.03 2.69 11.91 2.56 11.76 2.39C11.56 2.19 11.13 2.23 11 2.62C10.71 3.44 10.33 4.45 9.95 5.22C8.88 7.36 8.19 8.72 6.33 10.37C5.99 10.68 5.59 10.89 5.2 11.05C4.32 11.39 3.75 12.19 3.9 12.92L4.25 14.69C4.36 15.25 4.78 15.69 5.33 15.84L10.93 17.37C12.91 17.91 14.92 16.64 15.29 14.62L15.97 10.86C16.2 9.63 15.25 8.5 14.01 8.5H12.5C12.35 8.5 12.2 8.43 12.11 8.31C12.01 8.19 11.98 8.03 12.02 7.88C12.02 7.88 12.02 7.88 12.02 7.88Z"/></symbol><symbol id="i-dislike" viewBox="0 0 20 20"><path fill="currentColor" d="M10.05 17.71C10.39 18.68 11.68 19.13 12.48 18.3C12.65 18.13 12.81 17.94 12.92 17.78C13.24 17.3 13.37 16.66 13.42 16.05C13.47 15.42 13.44 14.75 13.37 14.13C13.31 13.52 13.21 12.96 13.13 12.55C13.13 12.53 13.13 12.52 13.12 12.5H14.01C15.88 12.5 17.29 10.8 16.96 8.96L16.27 5.2C15.8 2.61 13.21 0.97 10.66 1.66L5.06 3.19C4.15 3.44 3.45 4.19 3.27 5.11L2.92 6.88C2.64 8.27 3.7 9.44 4.83 9.88C5.15 10.01 5.44 10.17 5.67 10.37C7.38 11.89 7.99 13.1 9.05 15.22C9.41 15.93 9.77 16.9 10.05 17.71ZM12.02 12.12L12.02 12.12L12.02 12.13L12.03 12.16C12.03 12.19 12.04 12.23 12.05 12.28C12.08 12.39 12.11 12.55 12.15 12.74C12.23 13.13 12.32 13.66 12.38 14.24C12.44 14.82 12.47 15.42 12.43 15.97C12.38 16.52 12.27 16.95 12.09 17.22C12.03 17.31 11.91 17.44 11.76 17.61C11.56 17.81 11.13 17.77 11 17.38C10.71 16.56 10.33 15.55 9.95 14.78C8.88 12.64 8.19 11.28 6.33 9.63C5.99 9.32 5.59 9.11 5.2 8.95C4.32 8.61 3.75 7.81 3.9 7.08L4.25 5.31C4.36 4.75 4.78 4.31 5.33 4.16L10.93 2.63C12.91 2.09 14.92 3.36 15.29 5.38L15.97 9.14C16.2 10.37 15.25 11.5 14.01 11.5H12.5C12.35 11.5 12.2 11.57 12.11 11.69C12.01 11.81 11.98 11.97 12.02 12.12C12.02 12.12 12.02 12.12 12.02 12.12Z"/></symbol><symbol id="i-more" viewBox="0 0 20 20"><path fill="currentColor" d="M6.25 10C6.25 10.69 5.69 11.25 5 11.25C4.31 11.25 3.75 10.69 3.75 10C3.75 9.31 4.31 8.75 5 8.75C5.69 8.75 6.25 9.31 6.25 10ZM11.25 10C11.25 10.69 10.69 11.25 10 11.25C9.31 11.25 8.75 10.69 8.75 10C8.75 9.31 9.31 8.75 10 8.75C10.69 8.75 11.25 9.31 11.25 10ZM15 11.25C15.69 11.25 16.25 10.69 16.25 10C16.25 9.31 15.69 8.75 15 8.75C14.31 8.75 13.75 9.31 13.75 10C13.75 10.69 14.31 11.25 15 11.25Z"/></symbol><symbol id="i-history" viewBox="0 0 20 20"><path fill="currentColor" d="M10 4C13.31 4 16 6.69 16 10C16 13.31 13.31 16 10 16C6.69 16 4 13.31 4 10C4 9.84 4.01 9.69 4.02 9.54C4.04 9.26 3.83 9.02 3.56 9C3.28 8.98 3.04 9.19 3.02 9.46C3.01 9.64 3 9.82 3 10C3 13.87 6.13 17 10 17C13.87 17 17 13.87 17 10C17 6.13 13.87 3 10 3C8.04 3 6.27 3.8 5 5.1V3.5C5 3.22 4.78 3 4.5 3C4.22 3 4 3.22 4 3.5V6.5C4 6.78 4.22 7 4.5 7H7.5C7.78 7 8 6.78 8 6.5C8 6.22 7.78 6 7.5 6H5.53C6.63 4.77 8.22 4 10 4ZM10 6.5C10 6.22 9.78 6 9.5 6C9.22 6 9 6.22 9 6.5V10.5C9 10.78 9.22 11 9.5 11H12.5C12.78 11 13 10.78 13 10.5C13 10.22 12.78 10 12.5 10H10V6.5Z"/></symbol><symbol id="i-speaker" viewBox="0 0 20 20"><path fill="currentColor" d="M12 3.01C12 2.13 10.96 1.68 10.32 2.27L6.44 5.87C6.35 5.95 6.23 6 6.1 6H3.5C2.67 6 2 6.67 2 7.5V12.5C2 13.33 2.67 14 3.5 14H6.1C6.23 14 6.35 14.05 6.44 14.13L10.32 17.73C10.96 18.32 12 17.87 12 16.99V3.01ZM7.12 6.6L11 3.01V16.99L7.12 13.4C6.85 13.14 6.48 13 6.1 13H3.5C3.22 13 3 12.78 3 12.5V7.5C3 7.22 3.22 7 3.5 7H6.1C6.48 7 6.85 6.86 7.12 6.6ZM15.26 4.63C15.46 4.44 15.78 4.46 15.96 4.67C18.68 7.7 18.68 12.3 15.96 15.33C15.78 15.54 15.46 15.56 15.26 15.37C15.05 15.19 15.03 14.87 15.22 14.67C17.59 12.01 17.59 7.99 15.22 5.33C15.03 5.13 15.05 4.81 15.26 4.63ZM14.08 12.93C13.84 12.8 13.76 12.49 13.9 12.25C14.67 10.9 14.73 9.19 13.9 7.75C13.76 7.51 13.84 7.2 14.08 7.07C14.32 6.93 14.62 7.01 14.76 7.25C15.78 9.01 15.71 11.11 14.76 12.75C14.63 12.99 14.32 13.07 14.08 12.93Z"/></symbol><symbol id="i-compose" viewBox="0 0 20 20"><path fill="currentColor" d="M10.5 4C10.78 4 11 4.22 11 4.5C11 4.78 10.78 5 10.5 5H6C4.9 5 4 5.9 4 7V14C4 15.1 4.9 16 6 16H13C14.1 16 15 15.1 15 14V9.5C15 9.22 15.22 9 15.5 9C15.78 9 16 9.22 16 9.5V14C16 15.66 14.66 17 13 17H6C4.34 17 3 15.66 3 14V7C3 5.34 4.34 4 6 4H10.5ZM16.15 3.15C16.34 2.95 16.66 2.95 16.85 3.15C17.05 3.34 17.05 3.66 16.85 3.85L9.06 11.65L8 12L8.35 10.94L16.15 3.15Z"/></symbol><symbol id="i-agents" viewBox="0 0 20 20"><path fill="currentColor" d="M5.21 2.82C5.53 2.31 6.09 2 6.69 2H9.5C9.78 2 10 2.22 10 2.5C10 2.78 9.78 3 9.5 3H6.69C6.43 3 6.19 3.13 6.06 3.35L2.11 9.6C1.96 9.84 1.96 10.16 2.11 10.4L5.98 16.53C6.16 16.82 6.49 17 6.84 17C7.3 17 7.7 16.69 7.82 16.25L11.22 3.49C11.45 2.61 12.25 2 13.16 2C13.86 2 14.5 2.36 14.87 2.95L18.79 9.24C19.08 9.71 19.08 10.29 18.79 10.76L14.79 17.18C14.47 17.69 13.91 18 13.31 18H10.5C10.22 18 10 17.78 10 17.5C10 17.22 10.22 17 10.5 17H13.31C13.57 17 13.81 16.87 13.94 16.65L17.94 10.23C18.03 10.09 18.03 9.91 17.94 9.77L14.02 3.48C13.83 3.18 13.51 3 13.16 3C12.7 3 12.3 3.31 12.18 3.75L8.78 16.5C8.55 17.39 7.75 18 6.84 18C6.14 18 5.5 17.64 5.13 17.06L1.27 10.93C0.91 10.36 0.91 9.64 1.27 9.07L5.21 2.82Z"/></symbol><symbol id="i-waffle" viewBox="0 0 20 20"><circle cx="4" cy="4" r="1.6" fill="currentColor"/><circle cx="10" cy="4" r="1.6" fill="currentColor"/><circle cx="16" cy="4" r="1.6" fill="currentColor"/><circle cx="4" cy="10" r="1.6" fill="currentColor"/><circle cx="10" cy="10" r="1.6" fill="currentColor"/><circle cx="16" cy="10" r="1.6" fill="currentColor"/><circle cx="4" cy="16" r="1.6" fill="currentColor"/><circle cx="10" cy="16" r="1.6" fill="currentColor"/><circle cx="16" cy="16" r="1.6" fill="currentColor"/></symbol><symbol id="i-person" viewBox="0 0 20 20"><path fill="currentColor" d="M10 2a4 4 0 110 8 4 4 0 010-8zm0 9c3.87 0 7 1.79 7 4v.5A2.5 2.5 0 0114.5 18h-9A2.5 2.5 0 013 15.5V15c0-2.21 3.13-4 7-4z"/></symbol><symbol id="i-doc" viewBox="0 0 20 20"><path fill="currentColor" d="M6 2h4.59L15 6.41V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4a2 2 0 012-2zm4 1H6a1 1 0 00-1 1v12a1 1 0 001 1h7a1 1 0 001-1V7h-3a1 1 0 01-1-1V3zm1 .41V6h2.59L11 3.41z"/></symbol><symbol id="i-mark" viewBox="0 0 24 24"><path d="M17.533 1.829A2.528 2.528 0 0015.11 0h-.737a2.531 2.531 0 00-2.484 2.087l-1.263 6.937.314-1.08a2.528 2.528 0 012.424-1.833h4.284l1.797.706 1.731-.706h-.505a2.528 2.528 0 01-2.423-1.829l-.715-2.453z" fill="url(#mkg0)" transform="translate(0 1)"/><path d="M6.726 20.16A2.528 2.528 0 009.152 22h1.566c1.37 0 2.49-1.1 2.525-2.48l.17-6.69-.357 1.228a2.528 2.528 0 01-2.423 1.83h-4.32l-1.54-.842-1.667.843h.497c1.124 0 2.113.75 2.426 1.84l.697 2.432z" fill="url(#mkg1)" transform="translate(0 1)"/><path d="M15 0H6.252c-2.5 0-4 3.331-5 6.662-1.184 3.947-2.734 9.225 1.75 9.225H6.78c1.13 0 2.12-.753 2.43-1.847.657-2.317 1.809-6.359 2.713-9.436.46-1.563.842-2.906 1.43-3.742A1.97 1.97 0 0115 0" fill="url(#mkg2)" transform="translate(0 1)"/><path d="M9 22h8.749c2.5 0 4-3.332 5-6.663 1.184-3.948 2.734-9.227-1.75-9.227H17.22c-1.129 0-2.12.754-2.43 1.848a1149.2 1149.2 0 01-2.713 9.437c-.46 1.564-.842 2.907-1.43 3.743A1.97 1.97 0 019 22" fill="url(#mkg4)" transform="translate(0 1)"/></symbol><symbol id="i-tile" viewBox="0 0 28 28"><rect width="28" height="28" rx="7" fill="url(#cpt)"/><path d="M11 8.6h6L20.4 14 17 19.4h-6L7.6 14Z" stroke="#fff" stroke-width="2.6" stroke-linejoin="round" fill="none"/></symbol></svg>
<div class="suite">
  <div class="waffle"><svg class="ic" width="18" height="18"><use href="#i-waffle"/></svg></div>
  <div class="brand"><svg class="ic" width="22" height="22"><use href="#i-mark"/></svg><span>Microsoft 365 Copilot</span></div>
  <div class="sp"></div>
  <div class="hbtn" title="Help">?</div>
  <div class="me"><svg class="ic" width="16" height="16"><use href="#i-person"/></svg></div>
</div>
<div class="app">
  <nav class="rail">
    <div class="item" title="Search"><svg class="ic" width="20" height="20"><use href="#i-search"/></svg><span>Search</span></div>
    <div class="item sel" title="Chat"><svg class="ic" width="20" height="20"><use href="#i-chat"/></svg><span>Chat</span></div>
    <div class="item" title="Agents"><svg class="ic" width="20" height="20"><use href="#i-agents"/></svg><span>Agents</span></div>
    <div class="item" title="Pages"><svg class="ic" width="20" height="20"><use href="#i-doc"/></svg><span>Pages</span></div>
    <div class="item" title="Notebooks"><svg class="ic" width="20" height="20"><use href="#i-notebook"/></svg><span>Notebooks</span></div>
    <div class="item" title="Create"><svg class="ic" width="20" height="20"><use href="#i-pen"/></svg><span>Create</span></div>
    <div class="item" title="Apps"><svg class="ic" width="20" height="20"><use href="#i-apps"/></svg><span>Apps</span></div>
  </nav>
  <aside class="pane">
    <div class="top">
      <div class="psearch"><svg class="ic" width="14" height="14"><use href="#i-search"/></svg><span>Search chats</span></div>
      <div class="pbtn" title="New chat"><svg class="ic" width="18" height="18"><use href="#i-compose"/></svg></div>
    </div>
    <div class="sect">Today</div>
    <div class="row sel"><svg class="ic tile" width="18" height="18"><use href="#i-tile"/></svg><span class="rt">__AGENT_NAME__</span></div>
    <div class="row"><svg class="ic" width="16" height="16" style="color:#616161"><use href="#i-chat"/></svg><span class="rt">Summarize my unread email</span></div>
    <div class="sect">Past 7 days</div>
    <div class="row"><svg class="ic" width="16" height="16" style="color:#616161"><use href="#i-chat"/></svg><span class="rt">Draft a project status update</span></div>
    <div class="row"><svg class="ic" width="16" height="16" style="color:#616161"><use href="#i-chat"/></svg><span class="rt">Prep for my next customer meeting</span></div>
    <div class="sect">Agents</div>
    <div class="row sel"><svg class="ic tile" width="18" height="18"><use href="#i-tile"/></svg><span class="rt">__AGENT_NAME__</span></div>
    <div class="row"><svg class="ic" width="16" height="16" style="color:#616161"><use href="#i-agents"/></svg><span class="rt">All agents</span></div>
    <div class="link">Get agents</div>
  </aside>
  <main class="chatcol">
    <div class="agent-hdr">
      <svg class="ic tile" width="26" height="26"><use href="#i-tile"/></svg>
      <span class="an">__AGENT_NAME__</span>
      <span class="sp"></span>
      <div class="hbtn" title="New chat"><svg class="ic" width="18" height="18"><use href="#i-compose"/></svg></div>
      <div class="hbtn" title="More options"><svg class="ic" width="18" height="18"><use href="#i-more"/></svg></div>
    </div>
    <div class="canvas" id="chat">
      <div class="thread" id="chat-inner">
        <div class="welcome" id="zero">
          <svg class="ic tile" width="56" height="56"><use href="#i-tile"/></svg>
          <h1>__AGENT_NAME__</h1>
          <div class="byline">By __CUSTOMER__</div>
          <p>__WELCOME_TEXT__</p>
          <div class="starters" id="starters"></div>
        </div>
      </div>
    </div>
    <div class="dock">
      <div class="dock-inner">
        <div class="composer">
          <input type="text" id="input" placeholder="Message __AGENT_NAME__" autocomplete="off" autofocus>
          <div class="comp-row">
            <input type="file" id="up-file" style="display:none">
            <button class="cbtn" title="Add content" onclick="document.getElementById('up-file').click()"><svg class="ic" width="18" height="18"><use href="#i-add"/></svg></button>
            <span class="sp"></span>
            <button class="cbtn" title="Start dictation"><svg class="ic" width="18" height="18"><use href="#i-mic"/></svg></button>
            <button class="send" id="send-btn" title="Send"><svg class="ic" width="16" height="16"><use href="#i-send"/></svg></button>
          </div>
        </div>
        <div class="disclaim">AI-generated content may be incorrect</div>
      </div>
    </div>
  </main>
</div>
<div class="prompter" id="prompter">
  <div class="prompter-bar">
    <span class="pr-title">Demo Script</span>
    <span class="pr-count" id="pr-count"></span>
    <button class="pr-toggle" id="pr-toggle" title="Hide">&times;</button>
  </div>
  <div class="prompter-body" id="pr-body"></div>
  <div class="pr-keys"><kbd>&#8593;</kbd> queue next &nbsp; <kbd>Enter</kbd> send &nbsp; <kbd>&#8595;</kbd> previous &nbsp; <kbd>Esc</kbd> toggle script</div>
</div>
<script>
var MODE = "__MODE__";                 // "scripted" | "live" | "mcp"
var API_URL = "__API_URL__";
var GUID = "__GUID__";
var DEMO = __DEMO_JSON__;              // [{q, e, a}]
var TEST_REPLAY = __TEST_REPLAY__;     // last test run: sent/returned per turn
var conversationHistory = [];
var demoIdx = -1;
var sending = false;

function icon(name, size) {
  return '<svg class="ic" width="' + size + '" height="' + size + '"><use href="#i-' + name + '"/></svg>';
}

function updatePrompter() {
  var body = document.getElementById('pr-body');
  var count = document.getElementById('pr-count');
  if (demoIdx < 0 || demoIdx >= DEMO.length) {
    body.innerHTML = '<div class="pr-step" style="color:#888">Press <kbd style="background:#333;padding:1px 4px;border-radius:2px;border:1px solid #444;color:#aaa">&#8593;</kbd> to queue the first demo step</div>';
    count.textContent = '0 / ' + DEMO.length;
    return;
  }
  var s = DEMO[demoIdx];
  body.innerHTML = '<div class="pr-step"><span class="pr-num">' + (demoIdx + 1) + '.</span>' + s.q + '</div><div class="pr-expect">' + s.e + '</div>';
  count.textContent = (demoIdx + 1) + ' / ' + DEMO.length;
}

// attachment markers ride inside assistant text; render them as file cards
function extractAttachments(text) {
  var files = [];
  var clean = String(text || '').replace(
    /\n*\[\[attachment name="([^"]+)" mime="([^"]+)" b64="([^"]*)"\]\]/g,
    function (_m, name, mime, b64) {
      files.push({ name: name, mime: mime, b64: b64 });
      return '';
    });
  return { text: clean.trim(), files: files };
}
function fileCard(f) {
  var card = document.createElement('div');
  card.className = 'file-card';
  card.title = 'Download ' + f.name;
  var kb = Math.max(1, Math.round(f.b64.length * 3 / 4 / 1024));
  var ext = (f.name.split('.').pop() || 'file').toUpperCase();
  card.innerHTML =
    '<svg class="fc-icon" viewBox="0 0 30 36"><path d="M3 2.5C3 1.7 3.7 1 4.5 1H19l8 8v24.5c0 .8-.7 1.5-1.5 1.5h-21c-.8 0-1.5-.7-1.5-1.5V2.5Z" fill="#fff" stroke="#d1d1d1"/><path d="M19 1l8 8h-7c-.6 0-1-.4-1-1V1Z" fill="#f0f0f0" stroke="#d1d1d1"/><rect x="0" y="17" width="24" height="13" rx="2" fill="' + (ext === 'PDF' ? '#D13438' : '#0F6CBD') + '"/><text x="12" y="26.5" font-family="Segoe UI, sans-serif" font-size="8" font-weight="700" fill="#fff" text-anchor="middle">' + ext.slice(0, 4) + '</text></svg>'
    + '<div style="min-width:0"><div class="fc-name"></div><div class="fc-meta">' + ext + ' - ' + kb + ' KB</div></div>';
  card.querySelector('.fc-name').textContent = f.name;
  card.onclick = function () {
    var bytes = atob(f.b64);
    var arr = new Uint8Array(bytes.length);
    for (var i = 0; i < bytes.length; i++) arr[i] = bytes.charCodeAt(i);
    var url = URL.createObjectURL(new Blob([arr], { type: f.mime }));
    var a = document.createElement('a');
    a.href = url; a.download = f.name;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 2000);
  };
  return card;
}
function renderMarkdown(text) {
  var html = String(text || '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/```(\w*)\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>')
    .replace(/^---$/gm, '<hr>');
  html = html.replace(/(^\|.+\|$\n?)+/gm, function (block) {
    var rows = block.trim().split('\n').filter(function (r) { return !r.match(/^\|[\s\-:|]+\|$/); });
    if (!rows.length) return block;
    var t = '<table>';
    rows.forEach(function (row, i) {
      var cells = row.split('|').filter(function (c) { return c.trim() !== ''; });
      var tag = i === 0 ? 'th' : 'td';
      t += '<tr>' + cells.map(function (c) { return '<' + tag + '>' + c.trim() + '</' + tag + '>'; }).join('') + '</tr>';
    });
    return t + '</table>';
  });
  html = html.replace(/^[-*] (.+)$/gm, '<li>$1</li>');
  html = html.replace(/^\d+\. (.+)$/gm, '<li>$1</li>');
  html = html.replace(/(<li>[\s\S]*?<\/li>\n?)+/g, '<ul>$&</ul>');
  html = html.replace(/\n\n/g, '</p><p>');
  html = '<p>' + html + '</p>';
  html = html.replace(/<p>\s*(<h[123]|<table|<ul|<hr|<blockquote|<pre)/g, '$1');
  html = html.replace(/(<\/h[123]>|<\/table>|<\/ul>|<hr>|<\/blockquote>|<\/pre>)\s*<\/p>/g, '$1');
  return html;
}

var chatInner = document.getElementById('chat-inner');
var chatArea = document.getElementById('chat');
var input = document.getElementById('input');
var sendBtn = document.getElementById('send-btn');

function scrollBottom() { chatArea.scrollTop = chatArea.scrollHeight; }
function removeWelcome() {
  var welcome = chatInner.querySelector('.welcome');
  if (welcome) welcome.remove();
}

function addMessage(role, text) {
  removeWelcome();
  if (role === 'user') {
    var u = document.createElement('div');
    u.className = 'msg-user';
    u.textContent = text;
    chatInner.appendChild(u);
  } else {
    var a = document.createElement('div');
    a.className = 'msg-ai';
    var parts = extractAttachments(text);
    text = parts.text;
    var body = document.createElement('div');
    body.className = 'body';
    body.innerHTML = renderMarkdown(text);
    a.appendChild(body);
    parts.files.forEach(function (f) { a.appendChild(fileCard(f)); });
    var ftr = document.createElement('div');
    ftr.className = 'ftr-row';
    var names = [['like', 'Like'], ['dislike', 'Dislike'], ['copy', 'Copy'],
                 ['speaker', 'Read aloud'], ['more', 'More options']];
    names.forEach(function (n) {
      var b = document.createElement('button');
      b.className = 'ftr-btn';
      b.title = n[1];
      b.innerHTML = icon(n[0], 16);
      if (n[0] === 'copy') {
        b.onclick = function () {
          if (navigator.clipboard) navigator.clipboard.writeText(text);
        };
      }
      ftr.appendChild(b);
    });
    var note = document.createElement('span');
    note.className = 'ftr-note';
    note.textContent = 'AI-generated content may be incorrect';
    ftr.appendChild(note);
    a.appendChild(ftr);
    chatInner.appendChild(a);
  }
  scrollBottom();
}

function showTyping() {
  removeWelcome();
  var row = document.createElement('div');
  row.className = 'shimmer-row';
  row.id = 'typing';
  row.innerHTML = icon('mark', 20)
    + '<div class="shimmer-lines"><div class="shimmer" style="width:88%"></div>'
    + '<div class="shimmer" style="width:70%"></div>'
    + '<div class="shimmer" style="width:45%"></div></div>';
  chatInner.appendChild(row);
  scrollBottom();
}
function hideTyping() { var el = document.getElementById('typing'); if (el) el.remove(); }

function overlap(a, b) {
  var wa = String(a).toLowerCase().match(/[a-z]{3,}/g) || [];
  var wb = {};
  (String(b).toLowerCase().match(/[a-z]{3,}/g) || []).forEach(function (w) { wb[w] = 1; });
  if (!wa.length) return 0;
  var hit = 0;
  wa.forEach(function (w) { if (wb[w]) hit++; });
  return hit / wa.length;
}

// ── MCP App preview: speak real MCP to the LOCAL server and render UI-bearing
// tools as inline widgets, exactly like Copilot Studio / M365 Copilot does. ──
var MCP_TOOLS = null;
var MCP_WIDGETS = {};
function mcpRpc(method, params) {
  return fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ jsonrpc: '2.0', id: Math.floor(Math.random() * 99999),
                           method: method, params: params || {} })
  }).then(function (r) { return r.json(); }).then(function (d) {
    if (d.error) throw new Error(d.error.message);
    return d.result;
  });
}
async function mcpEnsureTools() {
  if (MCP_TOOLS) return;
  try {
    await mcpRpc('initialize', { protocolVersion: '2025-06-18', capabilities: {},
                                 clientInfo: { name: 'rapp-mcp-preview' } });
  } catch (e) { /* stateless server - initialize is best-effort */ }
  MCP_TOOLS = (await mcpRpc('tools/list')).tools;
}
function mcpPickTool(text) {
  var low = text.toLowerCase();
  if (/\b(demo|show me the|walkthrough|present|open the)\b/.test(low)) {
    var openers = MCP_TOOLS.filter(function (t) {
      var hasInput = t.inputSchema && t.inputSchema.properties && t.inputSchema.properties.user_input;
      return !hasInput && t._meta && t._meta['ui/resourceUri'];
    });
    if (openers.length) return openers[0];
  }
  var best = null, bestScore = 0;
  MCP_TOOLS.forEach(function (t) {
    var hasInput = t.inputSchema && t.inputSchema.properties && t.inputSchema.properties.user_input;
    if (!hasInput) return; // opener tools are picked only via the demo intent above
    var s = overlap(low, (t.name + ' ' + (t.title || '') + ' ' + (t.description || '')).toLowerCase());
    if (s > bestScore) { bestScore = s; best = t; }
  });
  return bestScore > 0.08 ? best : null;
}
function addWidget(title, html, toolInput, toolResult) {
  removeWelcome();
  var wrap = document.createElement('div');
  wrap.className = 'msg-ai';
  var card = document.createElement('div');
  card.className = 'widget-card';
  var hdr = document.createElement('div');
  hdr.className = 'widget-hdr';
  hdr.innerHTML = icon('agents', 14) + '<span>' + title + '</span>';
  var frame = document.createElement('iframe');
  frame.srcdoc = html;
  // ── bona fide MCP Apps HOST bridge: the widget iframe can speak the real
  // ext-apps postMessage protocol (ui/initialize handshake, tool-input/
  // tool-result notifications, and full server passthrough for tools/call,
  // resources/read, ...) - so SDK-built widgets work in this mock exactly
  // like they do inside M365 Copilot. ──
  window.addEventListener('message', async function (ev) {
    if (!frame.contentWindow || ev.source !== frame.contentWindow) return;
    var msg = ev.data;
    if (!msg || msg.jsonrpc !== '2.0' || !msg.method) return;
    function reply(result, error) {
      if (msg.id === undefined || msg.id === null) return;
      var resp = { jsonrpc: '2.0', id: msg.id };
      if (error) { resp.error = { code: -32000, message: String(error) }; }
      else { resp.result = result; }
      ev.source.postMessage(resp, '*');
    }
    function notify(method, params) {
      ev.source.postMessage({ jsonrpc: '2.0', method: method, params: params || {} }, '*');
    }
    try {
      if (msg.method === 'ui/initialize') {
        reply({ protocolVersion: (msg.params && msg.params.protocolVersion) || '2025-11-21',
                hostInfo: { name: 'rapp-mcp-preview-host', version: '1.0.0' },
                hostCapabilities: { openLink: {}, message: {} },
                hostContext: { displayMode: 'inline', theme: 'light' } });
      } else if (msg.method === 'ui/notifications/initialized') {
        notify('ui/notifications/tool-input', { arguments: toolInput || {} });
        if (toolResult) notify('ui/notifications/tool-result', { result: toolResult });
      } else if (msg.method === 'ui/notifications/size-changed') {
        var h = msg.params && msg.params.height;
        if (h) frame.style.height = Math.min(680, Math.max(200, h)) + 'px';
      } else if (msg.method === 'ui/message') {
        reply({});
        var txt = ((msg.params && msg.params.content) || [])
          .map(function (c) { return c.text || ''; }).join(' ').trim();
        if (txt) send(txt);
      } else if (msg.method === 'ui/open-link') {
        window.open(msg.params && msg.params.url, '_blank');
        reply({});
      } else if (msg.id !== undefined) {
        // server passthrough - the widget talks to the real local MCP server
        reply(await mcpRpc(msg.method, msg.params));
      }
    } catch (err) { reply(null, err.message); }
  });
  card.appendChild(hdr);
  card.appendChild(frame);
  wrap.appendChild(card);
  chatInner.appendChild(wrap);
  scrollBottom();
}
async function mcpAnswer(text) {
  await mcpEnsureTools();
  var tool = mcpPickTool(text);
  if (!tool) {
    return 'This is the MCP App preview - the agent would pick one of these tools: '
      + MCP_TOOLS.map(function (t) { return t.name; }).join(', ')
      + '. Try mentioning a capability, or say "show me the demo".';
  }
  var hasInput = tool.inputSchema && tool.inputSchema.properties && tool.inputSchema.properties.user_input;
  var args = hasInput ? { user_input: text } : {};
  var result = await mcpRpc('tools/call', { name: tool.name, arguments: args });
  // exactly like M365 Copilot: a UI-bearing tool invocation renders its
  // widget inline, fed with tool-input + tool-result over the host bridge
  var uri = (tool._meta && tool._meta['ui/resourceUri'])
    || (result._meta && result._meta['ui/resourceUri']);
  if (uri) {
    if (!MCP_WIDGETS[uri]) {
      var read = await mcpRpc('resources/read', { uri: uri });
      MCP_WIDGETS[uri] = read.contents[0].text;
    }
    addWidget(tool.title || tool.name, MCP_WIDGETS[uri], args, result);
  }
  return (result.content && result.content[0] && result.content[0].text)
    || (uri ? 'Widget opened.' : '(empty tool result)');
}

function scriptedAnswer(text) {
  if (demoIdx >= 0 && demoIdx < DEMO.length && overlap(DEMO[demoIdx].q, text) > 0.7) {
    return DEMO[demoIdx].a;
  }
  var best = -1, bestScore = 0.34;
  for (var i = 0; i < DEMO.length; i++) {
    var s = overlap(DEMO[i].q, text);
    if (s > bestScore) { bestScore = s; best = i; }
  }
  if (best >= 0) return DEMO[best].a;
  return 'This panel is playing the scripted demo preview. Use the Up arrow to queue the next scripted step, or adjust the script through your brainstem ("adjust turn N ...") and regenerate.';
}

// composer attachments work like M365 Copilot: text-ish files ride into the
// conversation as context; anything else is referenced by name
document.getElementById('up-file').addEventListener('change', function (e) {
  var f = e.target.files[0];
  if (!f) return;
  var texty = /\.(txt|md|markdown|json|csv|log|yaml|yml)$/i.test(f.name)
    || /^text\//.test(f.type || '');
  if (texty) {
    var reader = new FileReader();
    reader.onload = function () {
      var content = String(reader.result || '').slice(0, 6000);
      send('I attached "' + f.name + '". Use it as context:\n\n' + content);
    };
    reader.readAsText(f);
  } else {
    send('I attached a file named "' + f.name + '" ('
         + (f.type || 'unknown type') + '). Use it as context for this conversation.');
  }
  e.target.value = '';
});
async function send(text) {
  if (!text.trim() || sending) return;
  sending = true;
  input.disabled = true;
  sendBtn.classList.remove('ready');
  addMessage('user', text);
  conversationHistory.push({ role: 'user', content: text });
  showTyping();
  var response = '';
  if (MODE === 'scripted') {
    await new Promise(function (r) { setTimeout(r, 700); });
    response = scriptedAnswer(text);
  } else if (MODE === 'mcp') {
    try {
      response = await mcpAnswer(text);
    } catch (err) {
      response = 'Error talking to the local MCP App server at ' + API_URL + ': '
        + err.message + '. Start it with the command in the rapplication chat '
        + '(or say "bring the MCP app up").';
    }
  } else {
    try {
      var res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_input: text,
          user_guid: GUID,
          conversation_history: conversationHistory.slice(-12)
        })
      });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      var data = await res.json();
      response = (data.response || data.assistant_response || '').split('|||VOICE|||')[0].trim();
      if (!response) response = '(empty response from twin)';
    } catch (err) {
      response = 'Error reaching the twin at ' + API_URL + ': ' + err.message + '. Make sure the twin/brainstem is running.';
    }
  }
  hideTyping();
  addMessage('assistant', response);
  conversationHistory.push({ role: 'assistant', content: response });
  sending = false;
  input.disabled = false;
  input.value = '';
  input.focus();
}

// agent conversation starters (from the demo script, like manifest starters)
(function () {
  var box = document.getElementById('starters');
  if (!box) return;
  DEMO.slice(0, 4).forEach(function (t, i) {
    var firstStop = t.q.search(/[.?!:]/);
    var title = firstStop > 0 && firstStop < 60 ? t.q.slice(0, firstStop + 1) : t.q.split(' ').slice(0, 7).join(' ');
    var rest = t.q.slice(title.length).trim();
    if (rest.length > 90) rest = rest.slice(0, 87) + '...';
    var card = document.createElement('div');
    card.className = 'starter';
    card.innerHTML = '<div class="st"></div><div class="ss"></div>';
    card.querySelector('.st').textContent = title;
    card.querySelector('.ss').textContent = rest || 'Select to send this prompt';
    card.onclick = function () { demoIdx = i; updatePrompter(); send(t.q); };
    box.appendChild(card);
  });
})();

// ── visual test replay: the REAL sent/returned pairs from a test run play
// in this Copilot frame so testing is something the user SEES, live. ──
var REPLAY_DATA = null;
var replayShown = 0;
var replayKey = null;
var replayPlaying = false;
function addReplayDivider(d) {
  removeWelcome();
  var el = document.createElement('div');
  el.className = 'replay-divider';
  el.innerHTML = (d.target === 'drive' ? 'Live drive'
                  : 'Test run - ' + (d.target === 'twin' ? 'live twin' : 'local twin'))
    + '<span class="sub">' + (d.target === 'drive'
        ? 'watching what is sent and what the prototype answers, live'
        : 'replaying exactly what was sent and what the prototype returned') + '</span>';
  chatInner.appendChild(el);
  scrollBottom();
}
function addReplayFooter(d) {
  var el = document.createElement('div');
  el.className = 'replay-divider';
  el.innerHTML = (d.target === 'drive' ? 'End of live drive'
                  : (d.passed === d.total ? 'All ' + d.total + ' turns passed'
                     : d.passed + ' of ' + d.total + ' turns passed'))
    + '<span class="sub">' + (d.target === 'drive'
        ? 'the conversation above really happened against the twin just now'
        : 'end of test replay - keep chatting normally, or press Up arrow for the demo script') + '</span>';
  chatInner.appendChild(el);
  scrollBottom();
}
async function playReplay(data, restart) {
  if (!data || !data.turns || !data.turns.length) return;
  var key = data.at + ':' + data.target;
  if (restart || replayKey !== key) {
    replayKey = key;
    replayShown = 0;
    addReplayDivider(data);
  }
  REPLAY_DATA = data;
  if (replayPlaying) return;   // the running loop picks up the new turns
  replayPlaying = true;
  while (replayShown < REPLAY_DATA.turns.length) {
    var t = REPLAY_DATA.turns[replayShown++];
    addMessage('user', t.user);
    await new Promise(function (r) { setTimeout(r, 350); });
    addMessage('assistant', t.actual || '(no reply)');
    var last = chatInner.querySelectorAll('.msg-ai');
    if (last.length && (typeof t.score === 'number' || t.passed === false)) {
      var chip = document.createElement('span');
      chip.className = 'test-chip ' + (t.passed ? 'pass' : 'fail');
      chip.textContent = (t.passed ? 'PASS' : 'FAIL')
        + (typeof t.score === 'number' ? ' ' + Math.round(t.score * 100) + '%' : '');
      last[last.length - 1].appendChild(chip);
    }
    await new Promise(function (r) { setTimeout(r, 350); });
  }
  replayPlaying = false;
  if (REPLAY_DATA.done) addReplayFooter(REPLAY_DATA);
}
window.addEventListener('message', function (ev) {
  var m = ev.data;
  if (m && m.type === 't2p-replay') playReplay(m.replay, !!m.restart);
});
// a test running RIGHT NOW (page loaded mid-run) starts playing immediately
if (TEST_REPLAY && !TEST_REPLAY.done) playReplay(TEST_REPLAY);
sendBtn.addEventListener('click', function () { send(input.value); });
input.addEventListener('input', function () {
  sendBtn.classList.toggle('ready', !!input.value.trim());
});
input.addEventListener('keydown', function (e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    send(input.value);
    if (demoIdx >= 0 && demoIdx < DEMO.length - 1) { demoIdx++; updatePrompter(); }
  } else if (e.key === 'ArrowUp') {
    e.preventDefault();
    if (demoIdx < DEMO.length - 1) {
      demoIdx++;
      input.value = DEMO[demoIdx].q;
      sendBtn.classList.add('ready');
      updatePrompter();
    }
  } else if (e.key === 'ArrowDown') {
    e.preventDefault();
    if (demoIdx > 0) { demoIdx--; input.value = DEMO[demoIdx].q; updatePrompter(); }
    else if (demoIdx === 0) { demoIdx = -1; input.value = ''; updatePrompter(); }
    sendBtn.classList.toggle('ready', !!input.value.trim());
  } else if (e.key === 'Escape') {
    e.preventDefault();
    document.getElementById('prompter').classList.toggle('hidden');
  }
});
document.getElementById('pr-toggle').addEventListener('click', function () {
  document.getElementById('prompter').classList.toggle('hidden');
});
updatePrompter();
// dev/recording hook: ?autoplay=N plays the first N scripted turns on load
(function () {
  var m = /[?&]autoplay=(\d+)/.exec(location.search || '');
  if (!m) return;
  var n = Math.min(parseInt(m[1], 10) || 0, DEMO.length);
  var i = 0;
  (async function play() {
    while (i < n) { demoIdx = i; updatePrompter(); await send(DEMO[i].q); i++; }
  })();
})();
</script>
</body>
</html>
"""

# the MCP App WIDGET: a compact, purpose-built workspace (NOT the chat page -
# rendering the full chat inside Copilot's chat would double the chrome).
# It speaks the bona fide MCP Apps bridge: ui/initialize handshake to the
# host, then tools/call THROUGH the host (postMessage JSON-RPC); standalone
# (opened directly) it falls back to direct HTTP against the local server.
MCP_WIDGET_TEMPLATE = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__AGENT_NAME__</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Segoe UI Variable Text","Segoe UI",-apple-system,sans-serif; background: #ffffff; color: #242424; font-size: 13px; padding: 14px 16px; }
.hd { display: flex; align-items: center; gap: 9px; margin-bottom: 10px; }
.hd .nm { font-size: 14px; font-weight: 600; }
.hd .sub { font-size: 11px; color: #616161; }
.hd .st { margin-left: auto; font-size: 10.5px; color: #616161; }
.tabs { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px; }
.tab { border: 1px solid #d1d1d1; background: #fff; border-radius: 14px; padding: 4px 12px; font-size: 12px; color: #424242; cursor: pointer; font-family: inherit; }
.tab.on { background: #0F6CBD; border-color: #0F6CBD; color: #fff; font-weight: 600; }
.desc { font-size: 12.5px; color: #616161; line-height: 1.45; margin-bottom: 8px; }
table { border-collapse: collapse; width: 100%; font-size: 12px; margin-bottom: 10px; }
th { text-align: left; font-weight: 600; color: #424242; border-bottom: 1.5px solid #d1d1d1; padding: 4px 8px; white-space: nowrap; }
td { border-bottom: 1px solid #f0f0f0; padding: 4px 8px; color: #242424; }
.run { display: flex; gap: 6px; margin-bottom: 8px; }
.run input { flex: 1; border: 1px solid #d1d1d1; border-radius: 6px; padding: 7px 10px; font-size: 12.5px; font-family: inherit; outline: none; }
.run input:focus { border-color: #0F6CBD; }
.run button { border: none; background: #0F6CBD; color: #fff; border-radius: 6px; padding: 7px 16px; font-size: 12.5px; font-weight: 600; cursor: pointer; font-family: inherit; }
.run button:hover { background: #115EA3; }
.out { background: #fafafa; border: 1px solid #e0e0e0; border-radius: 8px; padding: 10px 12px; font-size: 12.5px; line-height: 1.5; white-space: pre-wrap; display: none; max-height: 150px; overflow-y: auto; }
.note { font-size: 10.5px; color: #616161; margin-top: 8px; }
</style>
</head>
<body>
<div class="hd">
  <svg width="28" height="28" viewBox="0 0 28 28"><defs><linearGradient id="wt" x1="0" y1="0" x2="28" y2="28" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#33CCFF"/><stop offset=".4" stop-color="#3B6CEB"/><stop offset=".72" stop-color="#9B5CF7"/><stop offset="1" stop-color="#FF63B8"/></linearGradient></defs><rect width="28" height="28" rx="7" fill="url(#wt)"/><path d="M11 8.6h6L20.4 14 17 19.4h-6L7.6 14Z" stroke="#fff" stroke-width="2.6" stroke-linejoin="round" fill="none"/></svg>
  <div><div class="nm">__AGENT_NAME__</div><div class="sub">Prototype workspace for __CUSTOMER__</div></div>
  <div class="st" id="st">connecting...</div>
</div>
<div class="tabs" id="tabs"></div>
<div class="desc" id="desc"></div>
<div id="records"></div>
<div class="run">
  <input type="text" id="q" placeholder="Try this capability - ask it anything">
  <button id="go">Run</button>
</div>
<div class="out" id="out"></div>
<div class="note">All example data is synthetic demo data - no customer data needed.</div>
<script>
var CAPS = __CAPS_JSON__;
var SERVER_URL = "__SERVER_URL__";
var active = 0;
var pending = {};
var seq = 1;
var BRIDGED = false;

function setStatus(t) { document.getElementById('st').textContent = t; }
function hostRpc(method, params, timeoutMs) {
  return new Promise(function (resolve, reject) {
    var id = seq++;
    pending[id] = { ok: resolve, err: reject };
    try {
      window.parent.postMessage({ jsonrpc: '2.0', id: id, method: method, params: params || {} }, '*');
    } catch (e) { delete pending[id]; reject(e); return; }
    setTimeout(function () {
      if (pending[id]) { delete pending[id]; reject(new Error('no host response')); }
    }, timeoutMs || 4000);
  });
}
function applyResult(res) {
  if (!res) return;
  var sc = res.structuredContent || {};
  if (sc.capability) {
    var idx = CAPS.findIndex(function (c) { return c.name === sc.capability; });
    if (idx >= 0) { active = idx; renderTabs(); renderPanel(); }
  }
  var text = (res.content && res.content[0] && res.content[0].text) || '';
  if (text) {
    var out = document.getElementById('out');
    out.style.display = 'block';
    out.textContent = text.replace(/\n*\[\[attachment name="([^"]+)"[^\]]*\]\]/g, '\n[attachment delivered: $1 - view it in the full demo]').replace(/\*\*/g, '');
  }
}
window.addEventListener('message', function (ev) {
  var m = ev.data;
  if (!m || m.jsonrpc !== '2.0') return;
  if (m.method === 'ui/notifications/tool-result') {
    applyResult(m.params && m.params.result);
    return;
  }
  if (m.method !== undefined) return;   // other notifications/requests
  // responses: no method, an id we are waiting on
  if (m.id !== undefined && pending[m.id]) {
    var p = pending[m.id];
    delete pending[m.id];
    if (m.error) { p.err(new Error(m.error.message)); } else { p.ok(m.result); }
  }
});
async function callTool(name, args) {
  if (BRIDGED) {
    return hostRpc('tools/call', { name: name, arguments: args }, 30000);
  }
  var r = await fetch(SERVER_URL, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ jsonrpc: '2.0', id: Math.floor(Math.random() * 99999),
                           method: 'tools/call', params: { name: name, arguments: args } })
  });
  var d = await r.json();
  if (d.error) throw new Error(d.error.message);
  return d.result;
}
function renderTabs() {
  var tabs = document.getElementById('tabs');
  tabs.innerHTML = '';
  CAPS.forEach(function (c, i) {
    var b = document.createElement('button');
    b.className = 'tab' + (i === active ? ' on' : '');
    b.textContent = c.name;
    b.onclick = function () { active = i; renderTabs(); renderPanel(); };
    tabs.appendChild(b);
  });
}
function renderPanel() {
  var c = CAPS[active];
  document.getElementById('desc').textContent = c.description;
  var recs = c.synthetic_records || [];
  var holder = document.getElementById('records');
  holder.innerHTML = '';
  if (recs.length) {
    var cols = Object.keys(recs[0]).slice(0, 4);
    var t = document.createElement('table');
    var html = '<tr>' + cols.map(function (k) { return '<th>' + k.replace(/_/g, ' ') + '</th>'; }).join('') + '</tr>';
    recs.slice(0, 3).forEach(function (r) {
      html += '<tr>' + cols.map(function (k) { return '<td>' + String(r[k] === undefined ? '' : r[k]) + '</td>'; }).join('') + '</tr>';
    });
    t.innerHTML = html;
    holder.appendChild(t);
  }
  document.getElementById('out').style.display = 'none';
  document.getElementById('q').placeholder = 'Try ' + c.name + ' - ask it anything';
}
async function run() {
  var c = CAPS[active];
  var q = document.getElementById('q').value.trim() || ('Show me an example of ' + c.name.toLowerCase());
  var out = document.getElementById('out');
  out.style.display = 'block';
  out.textContent = 'Running ' + c.name + '...';
  try {
    var res = await callTool(c.key, { user_input: q });
    var text = (res.content && res.content[0] && res.content[0].text) || '(no result)';
    out.textContent = text.replace(/\n*\[\[attachment name="([^"]+)"[^\]]*\]\]/g, '\n[attachment delivered: $1 - view it in the full demo]').replace(/\*\*/g, '');
  } catch (e) {
    out.textContent = 'Error: ' + e.message;
  }
}
document.getElementById('go').addEventListener('click', run);
document.getElementById('q').addEventListener('keydown', function (e) {
  if (e.key === 'Enter') { e.preventDefault(); run(); }
});
renderTabs();
renderPanel();
// bona fide MCP Apps lifecycle: handshake with the host; fall back to
// direct server access when opened standalone.
(async function init() {
  if (window.parent === window) { setStatus('standalone - direct MCP'); return; }
  try {
    await hostRpc('ui/initialize', {
      appInfo: { name: '__UNIQUE_NAME__-widget', version: '1.0.0' },
      appCapabilities: {}, protocolVersion: '2025-11-21' }, 1500);
    window.parent.postMessage({ jsonrpc: '2.0', method: 'ui/notifications/initialized', params: {} }, '*');
    BRIDGED = true;
    setStatus('connected via MCP Apps host');
  } catch (e) {
    setStatus('standalone - direct MCP');
  }
})();
</script>
</body>
</html>
'''

# single-file MCP Apps server template (stdlib only) - makes the prototype a
# NATIVE Copilot Studio / M365 Copilot app: capabilities become MCP tools and
# the compact workspace widget above is the app's interactive UI, per the MCP
# Apps extension (tool _meta "ui/resourceUri" -> ui:// resource, mime
# "text/html;profile=mcp-app"). Tokens are .replace()'d - never .format().
MCP_APP_TEMPLATE = r'''"""__DISPLAY_NAME__ - MCP App server (generated by Transcript2Prototype).

Makes the prototype NATIVE to Microsoft Copilot Studio / M365 Copilot using
the MCP Apps pattern (https://github.com/modelcontextprotocol/ext-apps,
https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps):
each prototype capability is an MCP tool, and a compact prototype workspace
ships as the app's UI widget (resource ui mime text/html;profile=mcp-app).

Run it (stdlib only, no pip installs):

    python3 __FILE_NAME__            # listens on PORT (default __PORT__)

Wire it into Copilot Studio:

    1. Expose the server publicly:  devtunnel host -p __PORT__ --allow-anonymous
       (or any https tunnel / app service)
    2. Copilot Studio -> your agent -> Tools -> Add a tool ->
       Model Context Protocol -> Streamable HTTP -> paste <tunnel-url>/mcp
    3. Ask the agent to "open the __DISPLAY_NAME__ demo" - the interactive
       widget renders inline; the capability tools answer with the same
       grounded responses and synthetic demo data as the prototype.
"""

import base64
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

SERVER_NAME = "__UNIQUE_NAME__-mcp-app"
SERVER_VERSION = "1.0.0"
DEFAULT_PORT = int(os.environ.get("PORT", "__PORT__"))
UI_URI = "ui://__UNIQUE_NAME__/app.html"
UI_MIME = "text/html;profile=mcp-app"
PROTOCOL_FALLBACK = "2025-06-18"

CAPABILITIES = __CAPABILITIES_JSON__

WIDGET_HTML_B64 = "__WIDGET_HTML_B64__"


def widget_html():
    return base64.b64decode(WIDGET_HTML_B64).decode("utf-8")


def capability_reply(cap, user_input):
    reply = cap["response"]
    if cap.get("knowledge"):
        reply += "\n\nGrounded in what the customer told us:\n" + "\n".join(
            "- " + k for k in cap["knowledge"])
    records = cap.get("synthetic_records") or []
    if records:
        words = [w for w in (user_input or "").lower().split() if len(w) > 3]
        hits = [r for r in records
                if any(w in json.dumps(r).lower() for w in words)] or records[:2]
        reply += "\n\nWorked example (synthetic demo data - no customer data needed):"
        for r in hits[:2]:
            reply += "\n- " + ", ".join(str(k) + ": " + str(v) for k, v in r.items())
    return reply, records


def list_tools():
    tools = [{
        "name": "open_demo",
        "title": "__DISPLAY_NAME__ workspace",
        "description": ("Open the interactive __DISPLAY_NAME__ prototype "
                        "workspace for __CUSTOMER__ - capabilities, synthetic "
                        "demo data, and a try-it panel. Use when the user wants "
                        "to see the demo, open the app, or explore the prototype."),
        "inputSchema": {"type": "object", "properties": {}},
        "annotations": {"readOnlyHint": True},
        "_meta": {"ui/resourceUri": UI_URI,
                  "ui": {"resourceUri": UI_URI}},
    }]
    for cap in CAPABILITIES:
        tools.append({
            "name": cap["key"],
            "title": cap["name"],
            "description": cap["description"] + " Keywords: "
                           + ", ".join(cap.get("triggers") or []),
            "inputSchema": {"type": "object", "properties": {
                "user_input": {"type": "string",
                               "description": "The user's request, in their own words."}},
                "required": ["user_input"]},
            "annotations": {"readOnlyHint": True},
            "_meta": {"ui/resourceUri": UI_URI,
                      "ui": {"resourceUri": UI_URI}},
        })
    return tools


def handle_rpc(req):
    method = req.get("method")
    params = req.get("params") or {}
    if method == "initialize":
        return {"protocolVersion": params.get("protocolVersion") or PROTOCOL_FALLBACK,
                "capabilities": {"tools": {}, "resources": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION,
                               "title": "__DISPLAY_NAME__"}}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": list_tools()}
    if method == "tools/call":
        name = (params.get("name") or "").strip()
        args = params.get("arguments") or {}
        if name == "open_demo":
            return {"content": [{"type": "text",
                                 "text": ("Opened the __DISPLAY_NAME__ workspace - explore "
                                          "each capability and its synthetic demo data, or "
                                          "keep asking here in the chat.")}],
                    "_meta": {"ui/resourceUri": UI_URI}}
        cap = next((c for c in CAPABILITIES if c["key"] == name), None)
        if cap is None:
            return {"content": [{"type": "text",
                                 "text": "Unknown tool " + repr(name)}],
                    "isError": True}
        reply, records = capability_reply(cap, args.get("user_input", ""))
        return {"content": [{"type": "text", "text": reply}],
                "structuredContent": {"capability": cap["name"],
                                      "synthetic_records": records},
                "_meta": {"ui/resourceUri": UI_URI}}
    if method == "resources/list":
        return {"resources": [{"uri": UI_URI, "name": "__DISPLAY_NAME__ workspace",
                               "description": "Interactive prototype workspace widget (MCP App UI)",
                               "mimeType": UI_MIME}]}
    if method == "resources/read":
        if (params.get("uri") or "") != UI_URI:
            raise ValueError("unknown resource " + repr(params.get("uri")))
        return {"contents": [{"uri": UI_URI, "mimeType": UI_MIME,
                              "text": widget_html()}]}
    raise LookupError(method or "(no method)")


class MCPHandler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type, mcp-session-id, mcp-protocol-version")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self._send(200, b"")

    def do_GET(self):
        self._send(200, "<html><body style=\"font-family:sans-serif\">"
                        "<h1>__DISPLAY_NAME__ MCP App</h1>"
                        "<p>POST JSON-RPC to /mcp (Streamable HTTP). Tools: "
                        + ", ".join(t["name"] for t in list_tools())
                        + "</p></body></html>", "text/html")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        try:
            req = json.loads(self.rfile.read(length) or b"{}")
        except ValueError:
            self._send(400, json.dumps({"jsonrpc": "2.0", "id": None,
                                        "error": {"code": -32700, "message": "parse error"}}))
            return
        if isinstance(req, dict) and req.get("method", "").startswith("notifications/"):
            self._send(202, b"")
            return
        rid = req.get("id") if isinstance(req, dict) else None
        try:
            result = handle_rpc(req)
            self._send(200, json.dumps({"jsonrpc": "2.0", "id": rid, "result": result}))
        except LookupError as e:
            self._send(200, json.dumps({"jsonrpc": "2.0", "id": rid,
                                        "error": {"code": -32601, "message": f"method not found: {e}"}}))
        except Exception as e:
            self._send(200, json.dumps({"jsonrpc": "2.0", "id": rid,
                                        "error": {"code": -32603, "message": str(e)}}))

    def log_message(self, *args):
        pass


def serve(port=None):
    port = port or DEFAULT_PORT
    server = HTTPServer(("0.0.0.0", port), MCPHandler)
    print(f"__DISPLAY_NAME__ MCP App server on http://localhost:{port}/mcp")
    print("Expose it with: devtunnel host -p " + str(port) + " --allow-anonymous")
    server.serve_forever()


if __name__ == "__main__":
    serve()
'''

# the rapplication shell: stage tracker + the demo iframe injected as bytecode
SHELL_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
/* AIdeate light theme (kody-w.github.io/aideate, [data-theme="light"]):
   white / #f5f5f5 surfaces, #d1d1d1 strokes, #242424 ink, #616161 muted,
   #0F6CBD brand, #107C10 / #D13438 states - no gradients. */
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: #faf9f8; color: #242424; height: 100vh; display: flex; flex-direction: column; }
.hdr { padding: 12px 20px 8px; border-bottom: 1px solid #d1d1d1; background: rgba(255,255,255,0.88); }
.hdr-row { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; }
.hdr .mslogo { align-self: center; flex-shrink: 0; }
.hdr h1 { font-size: 16px; font-weight: 700; color: #242424; }
.hdr .sub { font-size: 12px; color: #616161; }
.hdr .mode { margin-left: auto; font-size: 11px; font-weight: 700; letter-spacing: 0.6px; padding: 3px 10px; border-radius: 10px; background: #EBF3FC; color: #0F6CBD; border: 1px solid rgba(15,108,189,0.4); }
.hdr .newproto { font-size: 11px; font-weight: 600; padding: 5px 13px; border-radius: 12px; border: 1px solid rgba(15,108,189,0.45); background: rgba(15,108,189,0.06); color: #0F6CBD; cursor: pointer; font-family: inherit; }
.hdr .newproto:hover { background: rgba(15,108,189,0.14); }
.np-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.45); display: none; align-items: center; justify-content: center; z-index: 999; }
.np-overlay.show { display: flex; }
.np-box { background: #ffffff; border: 1px solid #d1d1d1; border-radius: 12px; padding: 20px 22px; width: 420px; box-shadow: 0 12px 40px rgba(0,0,0,0.18); }
.np-box h3 { font-size: 14px; color: #242424; margin-bottom: 4px; }
.np-box .s { font-size: 12px; color: #616161; margin-bottom: 14px; line-height: 1.5; }
.np-box button { display: block; width: 100%; text-align: left; margin: 7px 0; padding: 10px 14px; border-radius: 8px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #242424; font-size: 12.5px; cursor: pointer; font-family: inherit; line-height: 1.45; }
.np-box button:hover { border-color: #0F6CBD; background: #EBF3FC; }
.np-box button strong { color: #0F6CBD; }
.np-box .cancel { text-align: center; color: #616161; border: none; background: none; }
.th-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); display: none; align-items: center; justify-content: center; z-index: 998; }
.th-overlay.show { display: flex; }
.th-box { background: #ffffff; border: 1px solid #d1d1d1; border-radius: 14px; width: 720px; max-width: 92vw; height: 78vh; display: flex; flex-direction: column; box-shadow: 0 16px 60px rgba(0,0,0,0.22); }
.th-hd { display: flex; align-items: center; gap: 10px; padding: 12px 18px; border-bottom: 1px solid #d1d1d1; }
.th-hd .t { font-size: 13.5px; font-weight: 700; color: #242424; }
.th-hd .prog { font-size: 11px; color: #616161; font-family: monospace; }
.th-hd .sp { flex: 1; }
.th-hd button { font-size: 11px; padding: 4px 11px; border-radius: 10px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #242424; cursor: pointer; font-family: inherit; }
.th-hd button.on { border-color: #0F6CBD; color: #0F6CBD; background: #EBF3FC; }
.th-body { flex: 1; overflow-y: auto; padding: 14px 18px; display: flex; flex-direction: column; gap: 9px; }
.th-note { font-size: 11.5px; color: #616161; border-left: 2px solid #0F6CBD; padding: 3px 10px; }
.th-user { align-self: flex-end; max-width: 80%; background: #EBF3FC; color: #242424; border-radius: 10px; padding: 8px 12px; font-size: 12.5px; }
.th-reply { align-self: flex-start; max-width: 92%; background: #f5f5f5; border: 1px solid #d1d1d1; color: #242424; border-radius: 10px; padding: 8px 12px; font-size: 12.5px; white-space: pre-wrap; }
.th-chip { display: inline-block; margin-left: 8px; font-size: 9.5px; font-weight: 700; padding: 1px 8px; border-radius: 8px; }
.th-chip.pass { background: #DFF6DD; color: #107C10; }
.th-chip.fail { background: #FDE7E9; color: #D13438; }
.th-empty { color: #616161; font-size: 12.5px; text-align: center; margin: auto; }
.tour-hole { position: fixed; border-radius: 10px; box-shadow: 0 0 0 9999px rgba(0,0,0,0.45), 0 0 0 3px #0F6CBD; z-index: 1000; pointer-events: none; transition: all 0.25s; }
.tour-card { position: fixed; left: 50%; transform: translateX(-50%); bottom: 26px; width: 480px; background: #ffffff; border: 1px solid #0F6CBD; border-radius: 12px; padding: 16px 18px; z-index: 1001; box-shadow: 0 12px 40px rgba(0,0,0,0.2); display: none; }
.tour-card.show { display: block; }
.tour-card h3 { font-size: 13.5px; color: #242424; margin-bottom: 6px; }
.tour-card .tx { font-size: 12.5px; color: #616161; line-height: 1.55; margin-bottom: 12px; }
.tour-card .row { display: flex; gap: 8px; align-items: center; }
.tour-card .row .nav { font-size: 12px; padding: 6px 14px; border-radius: 8px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #242424; cursor: pointer; font-family: inherit; }
.tour-card .row .go { border-color: #0F6CBD; background: #EBF3FC; color: #0F6CBD; font-weight: 600; }
.tour-card .row .skip { margin-left: auto; border: none; background: none; color: #616161; font-size: 11.5px; cursor: pointer; }
.tour-card .prog { font-size: 10.5px; color: #707070; margin-left: 4px; }
.stages { display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap; }
.stage { font-size: 11px; padding: 3px 11px; border-radius: 12px; border: 1px solid #d1d1d1; color: #616161; background: #f5f5f5; }
.stage.done { border-color: #107C10; color: #107C10; background: #DFF6DD; }
.stage.current { border-color: #0F6CBD; color: #0F6CBD; background: #EBF3FC; font-weight: 700; }
.stage.gate { border-style: dashed; }
.row { flex: 1; display: flex; min-height: 0; }
.frame-wrap { flex: 1; padding: 12px; min-width: 0; }
iframe { width: 100%; height: 100%; border: 1px solid #d1d1d1; border-radius: 10px; background: #fff; box-shadow: 0 4px 18px rgba(0,0,0,0.07); }
.side { width: 390px; flex-shrink: 0; display: flex; flex-direction: column; border-left: 1px solid #d1d1d1; background: #ffffff; }
.side-hdr { padding: 10px 14px 8px; border-bottom: 1px solid #d1d1d1; }
.side-hdr .t { font-size: 13px; font-weight: 700; color: #242424; }
.side-hdr .s { font-size: 11px; color: #616161; margin-top: 2px; line-height: 1.5; }
.fb-msgs { flex: 1; overflow-y: auto; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px; }
.fb-msg { font-size: 12.5px; line-height: 1.55; border-radius: 10px; padding: 8px 12px; max-width: 95%; word-wrap: break-word; white-space: pre-wrap; }
.fb-msg.you { background: #EBF3FC; color: #242424; align-self: flex-end; }
.fb-msg.bs { background: #f5f5f5; border: 1px solid #d1d1d1; color: #242424; align-self: flex-start; }
.fb-msg.bs code { background: #EBF3FC; color: #0F6CBD; padding: 0 5px; border-radius: 3px; font-size: 11.5px; }
.fb-msg.sys { color: #707070; font-size: 11px; align-self: center; background: none; padding: 2px; }
.fb-msg.act { background: none; border-left: 2px solid #0F6CBD; border-radius: 0; color: #616161; font-size: 11.5px; padding: 3px 10px; align-self: stretch; max-width: 100%; }
/* simple mode (KISS, the default): load -> generate -> demo/adjust -> deploy.
   Advanced mode is the full surface; the toggle remembers the choice. */
.view-toggle { font-size: 11px; font-weight: 600; padding: 5px 13px; border-radius: 12px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #616161; cursor: pointer; font-family: inherit; }
.view-toggle:hover { border-color: #0F6CBD; color: #0F6CBD; }
.simple-bar { display: none; flex-direction: column; gap: 8px; padding: 12px 14px; border-bottom: 1px solid #d1d1d1; }
.simple-btn { display: flex; align-items: center; gap: 10px; width: 100%; text-align: left; padding: 11px 14px; border-radius: 8px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #242424; font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; }
.simple-btn .n { width: 22px; height: 22px; border-radius: 50%; background: #e0e0e0; color: #616161; font-size: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.simple-btn .d { font-size: 11px; color: #616161; font-weight: 400; margin-top: 1px; }
.simple-btn:hover { border-color: #0F6CBD; }
.simple-btn.next { border-color: #0F6CBD; background: #EBF3FC; box-shadow: 0 0 0 1px rgba(15,108,189,0.35); }
.simple-btn.next .n { background: #0F6CBD; color: #fff; }
.simple-tpl { width: 100%; max-width: none; padding: 9px 12px; font-size: 12.5px; border-radius: 8px; margin-top: -2px; }
body.simple .steps-bar, body.simple .stages, body.simple .dl, body.simple .ftr, body.simple .hdr .newproto, body.simple .hdr .mode { display: none; }
/* resets are not an advanced-only need: in simple mode the Start new
   prototype button takes the mode badge's spot (top right) */
body.simple .hdr #np-btn { display: inline-block; margin-left: auto; }
body.simple .simple-bar { display: flex; }
.steps-bar { display: flex; flex-wrap: wrap; gap: 6px; padding: 10px 14px; border-bottom: 1px solid #d1d1d1; }
.step-btn { font-size: 11px; padding: 6px 11px; border-radius: 12px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #242424; cursor: pointer; }
.step-btn:hover { border-color: #0F6CBD; color: #0F6CBD; }
.step-btn.next { border-color: #0F6CBD; background: #EBF3FC; color: #0F6CBD; font-weight: 700; box-shadow: 0 0 0 1px rgba(15,108,189,0.35); }
.step-btn.done-step { border-color: #107C10; color: #107C10; background: #DFF6DD; }
.tpl-select { font-size: 11px; padding: 6px 8px; border-radius: 12px; border: 1px solid #d1d1d1; background: #f5f5f5; color: #242424; cursor: pointer; max-width: 200px; font-family: inherit; }
.tpl-select:hover, .tpl-select:focus { border-color: #0F6CBD; color: #0F6CBD; outline: none; }
/* tpicker: branded, searchable, grouped replacement for the native template
   dropdown (progressive enhancement over the hidden <select>) */
.tpicker { position: relative; display: inline-block; }
.simple-tpl-wrap { display: block; width: 100%; margin-top: -2px; }
.tpicker-trigger { display: flex; align-items: center; gap: 8px; width: 100%; text-align: left; background: #f5f5f5; border: 1px solid #d1d1d1; border-radius: 12px; padding: 6px 11px; font-size: 11px; font-family: inherit; color: #242424; cursor: pointer; }
.simple-tpl-wrap .tpicker-trigger { border-radius: 8px; padding: 9px 12px; font-size: 12.5px; }
.tpicker:not(.simple-tpl-wrap) .tpicker-trigger { max-width: 220px; }
.tpicker-trigger:hover, .tpicker.open .tpicker-trigger { border-color: #0F6CBD; }
.tpicker.open .tpicker-trigger { background: #fff; box-shadow: 0 0 0 2px rgba(15,108,189,0.15); }
.tpicker-trigger .lbl { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #616161; }
.tpicker-trigger .chev { color: #0F6CBD; font-size: 9px; transition: transform .15s; }
.tpicker.open .tpicker-trigger .chev { transform: rotate(180deg); }
.tpicker-pop { position: absolute; top: calc(100% + 5px); left: 0; z-index: 60; min-width: 300px; background: #fff; border: 1px solid #d1d1d1; border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.18); display: none; flex-direction: column; max-height: 380px; overflow: hidden; }
.simple-tpl-wrap .tpicker-pop { right: 0; min-width: 0; }
.tpicker.open .tpicker-pop { display: flex; }
.tpicker-srch { padding: 8px; border-bottom: 1px solid #eee; }
.tpicker-srch input { width: 100%; border: 1px solid #d1d1d1; border-radius: 7px; padding: 7px 10px; font-size: 12px; font-family: inherit; outline: none; }
.tpicker-srch input:focus { border-color: #0F6CBD; box-shadow: 0 0 0 2px rgba(15,108,189,0.15); }
.tpicker-list { overflow-y: auto; padding: 4px; }
.tpicker-grp { font-size: 9.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .05em; color: #8a8a8a; padding: 9px 10px 4px; position: sticky; top: 0; background: #fff; }
.tpicker-opt { display: flex; align-items: center; gap: 8px; padding: 7px 10px; font-size: 12.5px; border-radius: 6px; cursor: pointer; color: #242424; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.tpicker-opt::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: #c8c8c8; flex-shrink: 0; }
.tpicker-opt:hover, .tpicker-opt.hi { background: #EBF3FC; color: #0F6CBD; }
.tpicker-opt:hover::before, .tpicker-opt.hi::before { background: #0F6CBD; }
.tpicker-empty { padding: 16px 12px; font-size: 12px; color: #8a8a8a; text-align: center; }
.fb-input { display: flex; gap: 8px; padding: 10px 12px; border-top: 1px solid #d1d1d1; }
.fb-input input { flex: 1; background: #ffffff; border: 1px solid #d1d1d1; border-radius: 18px; color: #242424; font-size: 12.5px; padding: 9px 14px; outline: none; }
.fb-input input:focus { border-color: #0F6CBD; box-shadow: 0 0 0 2px rgba(15,108,189,0.15); }
.fb-input button { width: 34px; height: 34px; border-radius: 50%; border: none; background: #0F6CBD; color: #fff; font-size: 14px; cursor: pointer; }
.fb-input button:disabled { background: #d1d1d1; }
.dl { border-top: 1px solid #d1d1d1; padding: 8px 14px; }
.dl .t { font-size: 11px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; color: #616161; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 7px; padding: 2px 0; }
.dl .t:hover { color: #0F6CBD; }
.dl .t .chev { font-size: 8.5px; color: #707070; transition: transform 0.15s; }
.dl .t .cnt { margin-left: auto; font-weight: 400; letter-spacing: 0; text-transform: none; color: #707070; font-size: 11px; }
.dl .dl-body { margin-top: 6px; max-height: 170px; overflow-y: auto; }
.dl.closed .chev { transform: rotate(-90deg); }
.dl.closed .dl-body { display: none; }
.dl-item { display: flex; align-items: center; gap: 8px; font-size: 12px; color: #242424; padding: 4px 0; }
.dl-item button { margin-left: auto; font-size: 10.5px; padding: 3px 11px; border-radius: 10px; border: 1px solid rgba(15,108,189,0.45); background: none; color: #0F6CBD; cursor: pointer; }
.dl-item button:hover { background: rgba(15,108,189,0.08); }
.dl-empty { font-size: 11.5px; color: #707070; }
.beacon { position: fixed; right: 10px; bottom: 10px; width: 16px; height: 16px; border-radius: 4px; background: transparent; z-index: 60; }
.beacon.on { background: #19ff6e; }
.beacon-label { position: fixed; right: 32px; bottom: 11px; font-size: 10px; color: #707070; display: none; z-index: 60; }
.beacon-label.on { display: block; }
.toast { position: fixed; bottom: 18px; left: 18px; background: #DFF6DD; color: #107C10; border: 1px solid rgba(16,124,16,0.35); font-size: 12px; padding: 8px 16px; border-radius: 8px; opacity: 0; transition: opacity 0.3s; z-index: 99; }
.toast.show { opacity: 1; }
.ftr { padding: 7px 20px 9px; border-top: 1px solid #d1d1d1; background: rgba(255,255,255,0.88); font-size: 11px; color: #616161; line-height: 1.6; }
.ftr code { background: #EBF3FC; color: #0F6CBD; padding: 1px 6px; border-radius: 4px; font-size: 10.5px; }
</style>
</head>
<body>
<div class="hdr">
  <div class="hdr-row">
    <svg class="mslogo" width="15" height="15" viewBox="0 0 23 23" aria-hidden="true"><rect x="1" y="1" width="10" height="10" fill="#F25022"/><rect x="12" y="1" width="10" height="10" fill="#7FBA00"/><rect x="1" y="12" width="10" height="10" fill="#00A4EF"/><rect x="12" y="12" width="10" height="10" fill="#FFB900"/></svg>
    <h1>__TITLE__</h1>
    <span class="sub">__SUBTITLE__</span>
    <button class="newproto" id="th-btn" onclick="theaterStart()">Watch session</button>
    <button class="newproto" onclick="tourStart()">Tutorial</button>
    <button class="newproto" id="np-btn" onclick="document.getElementById('np-overlay').classList.add('show')">Start new prototype</button>
    <button class="view-toggle" id="view-toggle" onclick="viewToggle()">Advanced</button>
    <span class="mode">__MODE_BADGE__</span>
  </div>
  <div class="stages" id="stages">__STAGES_HTML__</div>
</div>
<div class="row">
  <div class="frame-wrap">
    <iframe id="demo-frame" src="data:text/html;base64,__BYTECODE__" title="M365 Copilot demo"></iframe>
  </div>
  <div class="side">
    <div class="side-hdr">
      <div class="t">Prototyping chat</div>
      <div class="s">Click the highlighted step button, or type in plain language ("adjust turn 2 to cover refunds"). The demo on the left updates as the prototype changes.</div>
    </div>
    <div class="simple-bar" id="simple-bar">
      <button class="simple-btn" data-skey="load" onclick="document.getElementById('tx-file').click()">
        <span class="n">1</span><span>Load a transcript<div class="d">Pick the meeting transcript file - and/or pick an industry template below</div></span>
      </button>
      <select class="tpl-select simple-tpl" id="tpl-select-simple" title="Industry templates from the library">
        <option value="">...or start from an industry template</option>
        <option value="__generic__">Generic starter prototype (blank)</option>
      </select>
      <button class="simple-btn" data-skey="generate" onclick="simpleGenerate()">
        <span class="n">2</span><span>Generate the agents<div class="d">Builds and tests them, then the demo on the left goes LIVE</div></span>
      </button>
      <button class="simple-btn" data-skey="deploy" onclick="simpleDeploy()">
        <span class="n">3</span><span>Deploy to Copilot Studio<div class="d">Happy with the demo? Ship it. Adjust below and redeploy any time</div></span>
      </button>
    </div>
    <div class="steps-bar" id="steps-bar">
      <input type="file" id="tx-file" accept=".txt,.md,.text,text/plain" style="display:none">
      <button class="step-btn" data-key="start" onclick="document.getElementById('tx-file').click()">1 Attach transcript</button>
      <select class="tpl-select" id="tpl-select" title="Start from a template instead">
        <option value="">or start from a template...</option>
      </select>
      <button class="step-btn" data-key="build" onclick="stepSend('build')">2 Build the agents</button>
      <button class="step-btn" data-key="test_local" onclick="stepSend('test_local')">3 Test locally</button>
      <button class="step-btn" data-key="test_twin" onclick="stepSend('test_twin')">4 Run on the twin</button>
      <button class="step-btn" data-key="deploy" onclick="stepSend('deploy')">5 Copilot Studio</button>
      <button class="step-btn" id="replay-btn" onclick="replayLastTest()" style="display:none">Replay last test</button>
    </div>
    <div class="fb-msgs" id="fb-msgs">
      <div class="fb-msg sys">Connected to the prototyping brainstem for cubby __SLUG__.</div>
    </div>
    <div class="fb-input">
      <input type="text" id="fb-input" placeholder="Tell the brainstem what to change...">
      <button id="fb-send" title="Send">&#8593;</button>
    </div>
    <div class="dl" data-panel="creds">
      <div class="t" onclick="dlToggle(this)"><span class="chev">&#9660;</span>Deployment credentials</div>
      <div class="dl-body">
        <div class="dl-item"><span id="creds-status">__CREDS_STATUS__</span></div>
        <div class="dl-item">
          <input type="file" id="creds-file" accept=".json" style="display:none">
          <button onclick="document.getElementById('creds-file').click()">Load settings file</button>
          <button onclick="credsExport()">Export to a file</button>
        </div>
        <div class="dl-empty">Your app registration + Power Platform details (a local.settings.json with the DYNAMICS_365_* values). Static import/export - never sent through chat; powers autonomous Copilot Studio deploys.</div>
      </div>
    </div>
    <div class="dl" data-panel="egg">
      <div class="t" onclick="dlToggle(this)"><span class="chev">&#9660;</span>Prototype backup (.egg)</div>
      <div class="dl-body">
        <div class="dl-item">
          <input type="file" id="egg-file" accept=".egg,.zip" style="display:none">
          <button onclick="eggExport()">Export .egg</button>
          <button onclick="document.getElementById('egg-file').click()">Import .egg</button>
        </div>
        <div class="dl-empty">Backs up the whole prototype - cubby, twin memory and soul - as one portable file. Import it back any time (optionally under a new name) for a different use case.</div>
      </div>
    </div>
    <div class="dl" data-panel="outputs">
      <div class="t" onclick="dlToggle(this)"><span class="chev">&#9660;</span>Outputs - take these with you<span class="cnt" id="dl-cnt"></span></div>
      <div class="dl-body">
        <div id="dl-list"></div>
      </div>
    </div>
  </div>
</div>
<div class="ftr">
  <span>Demo: click into the panel, Up arrow queues each step, Enter sends.</span>
  <span>Outputs refresh automatically after every rebuild and export.</span>
</div>
<div class="np-overlay" id="np-overlay">
  <div class="np-box">
    <h3>Start a new prototype</h3>
    <div class="s">This prototype stays saved in its cubby either way.</div>
    <button onclick="npChoice('tab')"><strong>Open in a new tab</strong> - hatch a fresh prototype on its own twin and run it side by side with this one</button>
    <button onclick="npChoice('save')"><strong>Snapshot, then reset this page</strong> - save this prototype as a local egg, then start fresh here</button>
    <button onclick="npChoice('reset')"><strong>Reset this page</strong> - start fresh here (the cubby keeps its files, no snapshot)</button>
    <button class="cancel" onclick="document.getElementById('np-overlay').classList.remove('show')">Cancel</button>
  </div>
</div>
<div class="th-overlay" id="th-overlay">
  <div class="th-box">
    <div class="th-hd">
      <span class="t">Session replay - the autonomous run, as it happened</span>
      <span class="prog" id="th-prog"></span>
      <span class="sp"></span>
      <button id="th-play" onclick="thToggle()">Pause</button>
      <button onclick="thSpeed(900)" id="ths-1" class="on">1x</button>
      <button onclick="thSpeed(420)" id="ths-2">2x</button>
      <button onclick="thSpeed(150)" id="ths-3">4x</button>
      <button onclick="thRestart()">Restart</button>
      <button onclick="thSkip()">Skip to end</button>
      <button onclick="document.getElementById('th-overlay').classList.remove('show'); thPaused = true;">Close</button>
    </div>
    <div class="th-body" id="th-body"></div>
  </div>
</div>
<div class="tour-hole" id="tour-hole" style="display:none"></div>
<div class="tour-card" id="tour-card">
  <h3 id="tour-title"></h3>
  <div class="tx" id="tour-text"></div>
  <div class="row">
    <button class="nav" id="tour-back" onclick="tourMove(-1)">Back</button>
    <button class="nav" id="tour-next" onclick="tourMove(1)">Next</button>
    <button class="nav go" id="tour-do" onclick="tourDo()">Do this step</button>
    <span class="prog" id="tour-prog"></span>
    <button class="skip" onclick="tourEnd()">Skip tour</button>
  </div>
</div>
<div class="beacon" id="beacon"></div>
<span class="beacon-label" id="beacon-label">working</span>
<div class="toast" id="toast">Demo updated</div>
<script>
var SLUG = "__SLUG__";
var BRAINSTEM_URL = "__BRAINSTEM_URL__";
var PERFORM_URL = "__PERFORM_URL__";
var DOWNLOADS = __DOWNLOADS_JSON__;
var NEXT_STEP = "__NEXT_STEP__";
var TEST_REPLAY = __SHELL_TEST_REPLAY__;
var ACTIVITY = __ACTIVITY_JSON__;
var activitySeen = {};
ACTIVITY.forEach(function (a) { activitySeen[a.at + a.text] = 1; });
var lastReplayKey = TEST_REPLAY ? (TEST_REPLAY.at + ':' + TEST_REPLAY.turns.length + ':' + TEST_REPLAY.done) : '';
var lastReplayPushTs = 0;
var fbHistory = [];
var sending = false;
var lastChangeTs = Date.now();   // page load counts as activity
function markBusy() { lastChangeTs = Date.now(); }
setInterval(function () {
  var busy = sending || (Date.now() - lastChangeTs) < 6000;
  document.getElementById('beacon').classList.toggle('on', busy);
  document.getElementById('beacon-label').classList.toggle('on', busy);
}, 400);

var TEMPLATES_URL = "__TEMPLATES_URL__";
(function () {
  // one library, two dropdowns: the advanced steps bar and simple mode's
  // "and/or pick an industry template" under Load a transcript
  var sels = [document.getElementById('tpl-select'),
              document.getElementById('tpl-select-simple')].filter(Boolean);
  fetch(TEMPLATES_URL).then(function (r) { return r.json(); }).then(function (m) {
    // group the stacks by industry into optgroups (the picker renders each
    // group as a section header) - the redundant "(industry)" suffix is gone
    sels.forEach(function (sel) {
      var groups = {};
      (m.stacks || []).forEach(function (s) {
        var ind = s.industry || 'Starter';
        var og = groups[ind];
        if (!og) { og = groups[ind] = document.createElement('optgroup'); og.label = ind; sel.appendChild(og); }
        var o = document.createElement('option');
        o.value = s.id;
        o.textContent = s.name;
        og.appendChild(o);
      });
      if (sel._tpickerSync) sel._tpickerSync();
    });
  }).catch(function () {
    sels.forEach(function (sel) {
      sel.options[0].textContent = 'template library unreachable';
      if (sel._tpickerSync) sel._tpickerSync();
    });
  });
  // M365 agent templates (HPAs) ride alongside the industry library - each
  // one's README is the capability spec and goes through the same
  // transcript-shaped start. Multiple public repos, one optgroup each.
  var HPA_SOURCES = [
    { repo: 'microsoft/m365-agent-templates', label: 'Microsoft 365 agent templates' },
    { repo: 'kody-w/m365-agent-templates', label: 'M365 agent templates (kody-w)' }
  ];
  HPA_SOURCES.forEach(function (src) {
    fetch('https://api.github.com/repos/' + src.repo + '/contents')
      .then(function (r) { return r.json(); })
      .then(function (list) {
        var dirs = (Array.isArray(list) ? list : []).filter(function (e) {
          return e && e.type === 'dir' && e.name.indexOf('.') !== 0;
        });
        if (!dirs.length) return;
        sels.forEach(function (sel) {
          var og = document.createElement('optgroup');
          og.label = src.label;
          dirs.forEach(function (d) {
            var o = document.createElement('option');
            o.value = 'hpa:' + src.repo + ':' + d.name;
            o.textContent = d.name;
            og.appendChild(o);
          });
          sel.appendChild(og);
          if (sel._tpickerSync) sel._tpickerSync();
        });
      }).catch(function () {});
  });
  function pick(sel) {
    var id = sel.value;
    if (!id) return;
    var label = sel.options[sel.selectedIndex].textContent;
    sel.selectedIndex = 0;
    if (id.indexOf('hpa:') === 0) {
      var parts = id.slice(4).split(':');
      var repo = parts[0];
      var nm = parts.slice(1).join(':');
      addFb('you', 'Start from M365 template: ' + nm + ' (' + repo + ')');
      addFb('sys', 'Fetching the template description...');
      fetch('https://raw.githubusercontent.com/' + repo + '/main/'
            + encodeURIComponent(nm) + '/README.md')
        .then(function (r) { if (!r.ok) { throw new Error('HTTP ' + r.status); } return r.text(); })
        .then(function (md) {
          sendPayload('(prototype cubby: ' + SLUG + ') The user picked the M365 agent '
            + 'template "' + nm + '" (' + repo + '). Its README is below - treat '
            + 'it as the input exactly like an attached transcript: if this cubby is still fresh '
            + '(stage demo, nothing built) regenerate THIS cubby with action=start name=' + SLUG
            + ' force=true, MERGING its existing capabilities (keep every non-starter one) with '
            + 'capabilities authored from this README; otherwise start a NEW prototype. Always '
            + 'pass hpa_source="' + repo + ':' + nm + '" so the prototype keeps its HPA lineage '
            + '(action=hpa op=export later injects mutations back into the template). Author the '
            + 'capabilities yourself (invented synthetic_records, no emojis anywhere), '
            + 'agent_name "' + nm + '". Then tell the user the next step is the Generate/Build '
            + 'button. README:\n' + md.slice(0, 12000),
            'Start a prototype from the M365 template ' + nm + '.');
        })
        .catch(function (err) { addFb('sys', 'Could not fetch the template: ' + err.message); });
      return;
    }
    if (id === '__generic__') {
      // the blank generic starter - same as a reset to a fresh prototype
      addFb('sys', 'Starting a generic blank prototype...');
      performCall({ action: 'new_prototype', name: SLUG, force: true })
        .then(function (r) {
          if (r.status === 'success') { addFb('sys', 'Fresh start - reloading.'); setTimeout(function () { if (r.url) { location.href = r.url; } else { location.reload(); } }, 1200); }
          else { addFb('sys', 'Could not start fresh: ' + (r.error || r.status)); }
        })
        .catch(function (err) { addFb('sys', 'Could not start fresh: ' + err.message); });
      return;
    }
    addFb('you', 'Start from template: ' + label);
    sendPayload('(prototype cubby: ' + SLUG + ') The user picked the template "' + id
      + '" from the library dropdown. Run Transcript2Prototype action=template op=use template_id=' + id
      + ' right away (no questions). If THIS cubby already has capabilities from a transcript or '
      + 'an HPA and nothing built yet, add name=' + SLUG + ' merge=true so the template FOLDS INTO '
      + 'it (capability union) instead of replacing it. Then tell the user the prototype is ready, where its '
      + 'rapplication is, and that their next step is the Generate/Build button - or that '
      + 'saying "one-click ' + id + '" runs the whole journey to Copilot Studio.',
      'Start a prototype from the library template ' + id + '.');
  }
  sels.forEach(function (sel) {
    sel.addEventListener('change', function () { pick(sel); });
  });
  // progressive enhancement: a branded, searchable, grouped popover that
  // DRIVES the hidden native <select> - all the pick() logic above is
  // untouched (we just set value + fire change). Both dropdowns, and any
  // option/optgroup added async, are reflected because the list re-renders
  // from the live <select> every time it opens.
  function enhanceSelect(sel) {
    var wrap = document.createElement('div');
    wrap.className = 'tpicker' + (sel.classList.contains('simple-tpl') ? ' simple-tpl-wrap' : '');
    sel.parentNode.insertBefore(wrap, sel);
    wrap.appendChild(sel);
    sel.style.display = 'none';
    sel.setAttribute('tabindex', '-1');
    var trig = document.createElement('button');
    trig.type = 'button';
    trig.className = 'tpicker-trigger';
    trig.innerHTML = '<span class="lbl"></span><span class="chev">▼</span>';
    var lbl = trig.querySelector('.lbl');
    sel._tpickerSync = function () { lbl.textContent = sel.options[0] ? sel.options[0].textContent : 'Select a template'; };
    sel._tpickerSync();
    wrap.appendChild(trig);
    var pop = document.createElement('div');
    pop.className = 'tpicker-pop';
    pop.innerHTML = '<div class="tpicker-srch"><input type="text" placeholder="Search templates and stacks..."></div><div class="tpicker-list"></div>';
    wrap.appendChild(pop);
    var srch = pop.querySelector('input');
    var listEl = pop.querySelector('.tpicker-list');
    var rows = [], hiIdx = -1;
    function addOpt(o) {
      var r = document.createElement('div');
      r.className = 'tpicker-opt';
      r.appendChild(document.createTextNode(o.textContent));
      r.onclick = function () { choose(o.value); };
      listEl.appendChild(r);
      rows.push(r);
    }
    function render(filter) {
      listEl.innerHTML = ''; rows = []; hiIdx = -1;
      filter = (filter || '').toLowerCase();
      Array.prototype.forEach.call(sel.children, function (node) {
        if (node.tagName === 'OPTGROUP') {
          var matches = Array.prototype.filter.call(node.children, function (o) {
            return o.textContent.toLowerCase().indexOf(filter) >= 0;
          });
          if (!matches.length) return;
          var h = document.createElement('div'); h.className = 'tpicker-grp';
          h.textContent = node.label; listEl.appendChild(h);
          matches.forEach(addOpt);
        } else if (node.tagName === 'OPTION' && node.value !== '') {
          if (node.textContent.toLowerCase().indexOf(filter) >= 0) addOpt(node);
        }
      });
      if (!rows.length) {
        var e = document.createElement('div'); e.className = 'tpicker-empty';
        e.textContent = filter ? 'No templates match that search' : 'Template library still loading...';
        listEl.appendChild(e);
      }
    }
    function choose(val) { close(); sel.value = val; sel.dispatchEvent(new Event('change')); }
    function setHi(i) {
      if (rows[hiIdx]) rows[hiIdx].classList.remove('hi');
      hiIdx = i;
      if (rows[hiIdx]) { rows[hiIdx].classList.add('hi'); rows[hiIdx].scrollIntoView({ block: 'nearest' }); }
    }
    function onKey(e) {
      if (e.key === 'Escape') { close(); trig.focus(); }
      else if (e.key === 'ArrowDown') { e.preventDefault(); setHi(Math.min(hiIdx + 1, rows.length - 1)); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setHi(Math.max(hiIdx - 1, 0)); }
      else if (e.key === 'Enter' && rows[hiIdx]) { e.preventDefault(); rows[hiIdx].click(); }
    }
    function outside(e) { if (!wrap.contains(e.target)) close(); }
    function open() {
      render(''); srch.value = '';
      wrap.classList.add('open');
      setTimeout(function () { srch.focus(); }, 0);
      document.addEventListener('mousedown', outside, true);
      document.addEventListener('keydown', onKey, true);
    }
    function close() {
      wrap.classList.remove('open');
      document.removeEventListener('mousedown', outside, true);
      document.removeEventListener('keydown', onKey, true);
    }
    trig.onclick = function () { wrap.classList.contains('open') ? close() : open(); };
    srch.addEventListener('input', function () { render(srch.value); });
  }
  sels.forEach(enhanceSelect);
})();
var STEP_PAYLOADS = {
  build: ['Build the agents for this prototype (action=build). Then tell me in one short sentence what was built and that my next step is the "3 Test locally" button.',
          'Build the agents.'],
  test_local: ['Run the local test (action=test target=local). Summarize the pass rate in plain words and tell me my next step is the "4 Run on the twin" button.',
               'Run the local test.'],
  test_twin: ['Run the demo against the twin (action=test target=twin). Summarize the pass rate and remind me the demo panel on the left is now live.',
              'Run it on the twin.'],
  deploy: ['Deploy this prototype to Copilot Studio (action=deploy). It runs the gated factory export itself first when needed - ONE call. If credentials are missing, tell me to use the Load settings file button; if the gate refuses, tell me to run step 4 (the twin test) first. When done, tell me where to find the agent and that the factory singleton is in the Outputs list.',
           'Export the factory singleton and deploy to Copilot Studio.']
};

function stepSend(key) {
  var p = STEP_PAYLOADS[key];
  if (!p || sending) return;
  addFb('you', p[1]);
  sendPayload('(prototype cubby: ' + SLUG + ') ' + p[0],
              '(prototype cubby: ' + SLUG + ') ' + p[1]);
}

function pushReplay(restart) {
  if (!TEST_REPLAY) return;
  var frame = document.getElementById('demo-frame');
  if (frame && frame.contentWindow) {
    frame.contentWindow.postMessage({ type: 't2p-replay', replay: TEST_REPLAY,
                                      restart: !!restart }, '*');
  }
}
function replayLastTest() { pushReplay(true); }
function replayBtnSync() {
  var b = document.getElementById('replay-btn');
  if (b) b.style.display = TEST_REPLAY ? '' : 'none';
}
function highlightNext() {
  var btns = document.querySelectorAll('.step-btn');
  btns.forEach(function (b) { b.classList.remove('next'); });
  var hit = document.querySelector('.step-btn[data-key="' + NEXT_STEP + '"]');
  if (hit) hit.classList.add('next');
  // simple mode mirrors the same pipeline position onto its 3 buttons
  var skey = '';
  if (NEXT_STEP === 'start') skey = 'load';
  else if (NEXT_STEP === 'build' || NEXT_STEP === 'test_local' || NEXT_STEP === 'test_twin') skey = 'generate';
  else if (NEXT_STEP === 'deploy') skey = 'deploy';
  document.querySelectorAll('.simple-btn').forEach(function (b) {
    b.classList.toggle('next', !!skey && b.dataset.skey === skey);
  });
}

// ── simple vs advanced view - KISS by default, the choice sticks ───────────
function viewApply(mode) {
  document.body.classList.toggle('simple', mode !== 'advanced');
  var t = document.getElementById('view-toggle');
  if (t) t.textContent = mode === 'advanced' ? 'Simple mode' : 'Advanced';
}
function viewToggle() {
  var now = document.body.classList.contains('simple') ? 'advanced' : 'simple';
  try { localStorage.setItem('t2p-view', now); } catch (e) {}
  viewApply(now);
}
(function () {
  var saved = null;
  try { saved = localStorage.getItem('t2p-view'); } catch (e) {}
  viewApply(saved || 'simple');
})();
async function simpleGenerate() {
  // deterministic chain over /perform - build, prove it, go live. No LLM.
  if (sending) return;
  addFb('sys', 'Generating the agents from your transcript...');
  try {
    var b = await performCall({ action: 'build', cubby: SLUG });
    if (b.status !== 'success') { addFb('sys', 'Build failed: ' + (b.error || b.note || b.status)); return; }
    addFb('sys', 'Agents built (' + (b.agents || []).length + '). Checking they answer correctly...');
    var t = await performCall({ action: 'test', target: 'local', cubby: SLUG });
    if (t.status !== 'success') { addFb('sys', 'Self-check did not pass: ' + (t.error || t.status) + '. Adjust below and Generate again.'); return; }
    addFb('sys', 'Self-check passed. Starting the live demo...');
    var u = await performCall({ action: 'twin', op: 'up', cubby: SLUG });
    if (u.status === 'success') {
      addFb('sys', 'The demo on the left is LIVE. Try it, adjust it in plain language below ("make the pricing answer mention discounts"), and deploy when it feels right.');
    } else {
      addFb('sys', 'Demo start hit a snag: ' + (u.error || u.status));
    }
  } catch (err) {
    addFb('sys', 'Generate failed: ' + err.message);
  }
}
async function simpleDeploy() {
  if (sending) return;
  addFb('sys', 'Packaging and deploying to Copilot Studio...');
  try {
    var r = await performCall({ action: 'deploy', cubby: SLUG, skip_twin: true });
    if (r.status === 'success') {
      addFb('sys', 'Deployed. Open copilotstudio.microsoft.com and find "' + (r.agent_name || 'your agent') + '" - run the same demo there.');
    } else if (r.status === 'needs_credentials') {
      addFb('sys', 'One thing first: load your settings file (app registration) so the deploy can run sign-in free. Pick it now.');
      document.getElementById('creds-file').click();
    } else {
      addFb('sys', 'Deploy: ' + (r.error || r.note || r.status));
    }
  } catch (err) {
    addFb('sys', 'Deploy failed: ' + err.message);
  }
}

function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function mdLite(t) {
  return esc(t)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');
}
function addFb(role, text) {
  markBusy();
  var m = document.getElementById('fb-msgs');
  var d = document.createElement('div');
  d.className = 'fb-msg ' + role;
  if (role === 'bs') { d.innerHTML = mdLite(text); } else { d.textContent = text; }
  m.appendChild(d);
  m.scrollTop = m.scrollHeight;
}
function dlToggle(t) {
  var box = t.parentElement;
  box.classList.toggle('closed');
  try { localStorage.setItem('t2p-panel-' + box.dataset.panel,
                             box.classList.contains('closed') ? '1' : '0'); } catch (e) {}
}
// panels start collapsed so the chat gets the room; each remembers its state
document.querySelectorAll('.dl[data-panel]').forEach(function (box) {
  var saved = null;
  try { saved = localStorage.getItem('t2p-panel-' + box.dataset.panel); } catch (e) {}
  if (saved === null || saved === '1') box.classList.add('closed');
});
function renderDownloads() {
  var list = document.getElementById('dl-list');
  var cnt = document.getElementById('dl-cnt');
  if (cnt) cnt.textContent = DOWNLOADS.length ? DOWNLOADS.length + ' file' + (DOWNLOADS.length === 1 ? '' : 's') : '';
  list.innerHTML = '';
  if (!DOWNLOADS.length) {
    list.innerHTML = '<div class="dl-empty">Nothing yet - the demo script appears after start, agent.py files after a build, the factory singleton after export.</div>';
    return;
  }
  DOWNLOADS.forEach(function (f) {
    var row = document.createElement('div');
    row.className = 'dl-item';
    var name = document.createElement('span');
    name.textContent = f.name;
    var btn = document.createElement('button');
    btn.textContent = 'Download';
    btn.onclick = function () {
      var bytes = atob(f.b64);
      var arr = new Uint8Array(bytes.length);
      for (var i = 0; i < bytes.length; i++) arr[i] = bytes.charCodeAt(i);
      var a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([arr]));
      a.download = f.name;
      a.click();
      URL.revokeObjectURL(a.href);
    };
    row.appendChild(name);
    row.appendChild(btn);
    list.appendChild(row);
  });
}
function toast(msg) {
  var t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(function () { t.classList.remove('show'); }, 2500);
}
var canRefresh = location.protocol.indexOf('http') === 0;
async function refreshArtifacts() {
  if (!canRefresh) return;
  try {
    var res = await fetch(location.pathname + '?t=' + Date.now(), { cache: 'no-store' });
    var txt = await res.text();
    var m = txt.match(/data:text\/html;base64,([A-Za-z0-9+\/=]+)/);
    var frame = document.getElementById('demo-frame');
    if (m && frame.src.indexOf(m[1].slice(0, 60)) === -1) {
      frame.src = 'data:text/html;base64,' + m[1];
      markBusy();
      toast('Demo updated');
      if (TEST_REPLAY && (!TEST_REPLAY.done
          || (Date.now() - lastReplayPushTs) < 30000)) {
        // a swap mid-replay reloads the frame - re-play what testing did
        setTimeout(function () { pushReplay(true); }, 1100);
      }
    }
    var s = txt.match(/<div class="stages" id="stages">([\s\S]*?)<\/div>/);
    if (s) document.getElementById('stages').innerHTML = s[1];
    var c = txt.match(/id="creds-status">([^<]*)</);
    if (c) document.getElementById('creds-status').textContent = c[1];
    var n = txt.match(/var NEXT_STEP = "([a-z_]*)"/);
    if (n && n[1] !== NEXT_STEP) { NEXT_STEP = n[1]; markBusy(); highlightNext(); }
    var jm = txt.match(/var JOURNAL = (\[[^\n]*\]);\n/);
    if (jm) { try { JOURNAL = JSON.parse(jm[1]); } catch (e) {} }
    var av = txt.match(/var ACTIVITY = (\[[^\n]*\]);\n/);
    if (av) {
      try {
        JSON.parse(av[1]).forEach(function (a) {
          var k = a.at + a.text;
          if (!activitySeen[k]) {
            activitySeen[k] = 1;
            addFb('act', a.text);   // backend work, watched live in the UI
          }
        });
      } catch (e) { /* mid-write - next poll catches it */ }
    }
    var tr = txt.match(/var TEST_REPLAY = (.*);\n/);
    if (tr) {
      try {
        var nr = JSON.parse(tr[1]);
        var key = nr ? (nr.at + ':' + nr.turns.length + ':' + nr.done) : '';
        if (key && key !== lastReplayKey) {
          lastReplayKey = key;
          markBusy();
          TEST_REPLAY = nr;
          replayBtnSync();
          lastReplayPushTs = Date.now();
          setTimeout(function () { pushReplay(false); }, 1000); // play it live
        }
      } catch (e) { /* mid-write - next poll catches it */ }
    }
    var d = txt.match(/var DOWNLOADS = (\[[^\n]*\]);/);
    if (d) {
      var nd = JSON.parse(d[1]);
      if (JSON.stringify(nd.map(function (x) { return x.name; })) !==
          JSON.stringify(DOWNLOADS.map(function (x) { return x.name; })) ||
          JSON.stringify(nd) !== JSON.stringify(DOWNLOADS)) {
        DOWNLOADS = nd;
        markBusy();
        renderDownloads();
      }
    }
  } catch (e) { /* file:// or twin briefly down - retry next tick */ }
}
async function sendPayload(payload, histText) {
  if (sending) return;
  sending = true;
  document.getElementById('fb-send').disabled = true;
  addFb('sys', 'brainstem is working...');
  try {
    var res = await fetch(BRAINSTEM_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_input: payload, conversation_history: fbHistory.slice(-12) })
    });
    var data = await res.json();
    var reply = (data.response || data.assistant_response || '').split('|||VOICE|||')[0].trim();
    var msgs = document.getElementById('fb-msgs');
    msgs.removeChild(msgs.lastChild);
    addFb('bs', reply || 'The brainstem finished working but returned no text - it was likely mid-way through a multi-step change. Say "continue" or "status" to pick it back up.');
    // history keeps the MASKED form so secrets are never re-sent on later turns
    fbHistory.push({ role: 'user', content: histText || payload });
    fbHistory.push({ role: 'assistant', content: reply });
    sending = false;
    document.getElementById('fb-send').disabled = false;
    refreshArtifacts();
    setTimeout(refreshArtifacts, 4000);
    return reply;
  } catch (err) {
    var msgs2 = document.getElementById('fb-msgs');
    msgs2.removeChild(msgs2.lastChild);
    addFb('sys', 'Could not reach the prototyping brainstem at ' + BRAINSTEM_URL + ' (' + err.message + '). Is it running?');
  }
  sending = false;
  document.getElementById('fb-send').disabled = false;
  refreshArtifacts();
  setTimeout(refreshArtifacts, 4000);
  return null;
}
async function fbSend() {
  var input = document.getElementById('fb-input');
  var text = input.value.trim();
  if (!text || sending) return;
  addFb('you', text);
  input.value = '';
  var payload = '(prototype cubby: ' + SLUG + ') ' + text;
  await sendPayload(payload, payload);
  input.focus();
}
document.getElementById('tx-file').addEventListener('change', function (e) {
  var f = e.target.files[0];
  if (!f) return;
  var reader = new FileReader();
  reader.onload = function () {
    var txt = String(reader.result || '').trim();
    if (txt.length < 40) { addFb('sys', 'That file looks empty - attach the transcript as a plain text file.'); return; }
    addFb('you', 'Attach transcript: ' + f.name + ' (' + txt.length + ' characters)');
    sendPayload('A user attached a transcript file named "' + f.name + '" from the rapplication. '
                + 'FIRST check this cubby (' + SLUG + ') with action=status: if it is still fresh '
                + '(stage demo, nothing built) - e.g. a starter or a just-picked industry template - '
                + 'regenerate THIS cubby with action=start name=' + SLUG + ' force=true, authoring '
                + 'capabilities from BOTH its existing capabilities AND the transcript (merge them; '
                + 'the template capabilities the user picked must survive). Otherwise start a NEW '
                + 'prototype. Either way: author the capabilities yourself (with invented '
                + 'synthetic_records), pick a good customer_name from the content, pass the '
                + 'transcript verbatim. Then tell the user it worked, give them the rapplication URL '
                + 'once the twin is up, and that their next step is the Generate/Build button. '
                + 'TRANSCRIPT:\n' + txt,
                'Attached transcript ' + f.name + '.');
  };
  reader.readAsText(f);
  e.target.value = '';
});
// ── static transport: settings-grade ops never ride through chat ──────────
// Credentials and .egg backups go straight to the host's direct-dispatch
// endpoint (POST PERFORM_URL) - deterministic, no LLM, no secrets in any
// conversation. Chat stays for steering the prototype, not for settings.
async function performCall(args) {
  markBusy();
  var res = await fetch(PERFORM_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ agent: 'Transcript2Prototype', args: args })
  });
  if (!res.ok) throw new Error('HTTP ' + res.status);
  var data = await res.json();
  if (data.error) throw new Error(data.error);
  var out = data.result !== undefined ? data.result : data;
  if (typeof out === 'string') { try { out = JSON.parse(out); } catch (e) { out = { note: out }; } }
  return out;
}
function saveBlob(name, blob) {
  var a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = name;
  document.body.appendChild(a);
  a.click();
  setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
}
document.getElementById('creds-file').addEventListener('change', function (e) {
  var f = e.target.files[0];
  if (!f) return;
  var reader = new FileReader();
  reader.onload = async function () {
    try {
      var obj = JSON.parse(reader.result);
      var v = obj.Values || obj;
      var need = ['DYNAMICS_365_CLIENT_ID', 'DYNAMICS_365_CLIENT_SECRET',
                  'DYNAMICS_365_TENANT_ID', 'DYNAMICS_365_RESOURCE'];
      var missing = need.filter(function (k) { return !v[k]; });
      if (missing.length) { addFb('sys', 'Settings file is missing: ' + missing.join(', ')); return; }
      var res = await performCall({ action: 'credentials', op: 'import',
                                    credentials: { Values: v } });
      if (res.status === 'success') {
        document.getElementById('creds-status').textContent =
          'Saved: ' + res.resource + ' (client ' + String(res.client_id).slice(0, 8) + '...)';
        addFb('sys', 'Deployment credentials saved from ' + f.name
              + ' (static import - nothing went through chat).');
      } else {
        addFb('sys', 'Credentials import failed: ' + (res.error || res.note || 'unknown'));
      }
    } catch (err) {
      addFb('sys', 'Credentials import failed: ' + err.message);
    }
  };
  reader.readAsText(f);
  e.target.value = '';
});
async function credsExport() {
  try {
    var res = await performCall({ action: 'credentials', op: 'download' });
    if (res.status !== 'success') { addFb('sys', res.note || res.error || 'Nothing saved yet.'); return; }
    saveBlob(res.filename || 't2p_deploy.local.settings.json',
             new Blob([JSON.stringify(res.settings, null, 2)], { type: 'application/json' }));
    addFb('sys', 'Deployment credentials exported to a file (static download - kept out of chat).');
  } catch (err) {
    addFb('sys', 'Credentials export failed: ' + err.message);
  }
}
async function eggExport() {
  addFb('sys', 'Building the .egg backup...');
  try {
    var res = await performCall({ action: 'egg', op: 'export', cubby: SLUG, return_b64: true });
    if (res.status !== 'success') { addFb('sys', 'Egg export failed: ' + (res.error || 'unknown')); return; }
    var bytes = atob(res.egg_b64);
    var arr = new Uint8Array(bytes.length);
    for (var i = 0; i < bytes.length; i++) arr[i] = bytes.charCodeAt(i);
    saveBlob(res.egg_name || (SLUG + '.egg'), new Blob([arr], { type: 'application/zip' }));
    addFb('sys', 'Egg exported (' + res.files + ' files, ' + res.size_bytes + ' bytes, sha256 '
          + String(res.sha256).slice(0, 12) + '...).');
  } catch (err) {
    addFb('sys', 'Egg export failed: ' + err.message);
  }
}
document.getElementById('egg-file').addEventListener('change', function (e) {
  var f = e.target.files[0];
  if (!f) return;
  var nm = prompt('Import "' + f.name + '" under which prototype name?\nLeave empty to keep its original name.') || '';
  var reader = new FileReader();
  reader.onload = async function () {
    try {
      var b64 = String(reader.result).split(',')[1] || '';
      var args = { action: 'egg', op: 'import', egg_b64: b64 };
      if (nm.trim()) args.name = nm.trim();
      var res = await performCall(args);
      if (res.status === 'already_exists' && confirm('A prototype named "' + res.cubby + '" exists. Overwrite it?')) {
        args.force = true;
        res = await performCall(args);
      }
      if (res.status === 'success') {
        addFb('sys', 'Egg imported as "' + res.cubby + '". Say "bring the twin up for '
              + res.cubby + '" to run it.');
      } else {
        addFb('sys', 'Egg import failed: ' + (res.error || res.note || res.status));
      }
    } catch (err) {
      addFb('sys', 'Egg import failed: ' + err.message);
    }
  };
  reader.readAsDataURL(f);
  e.target.value = '';
});
// ── session theater: watch the autonomous run, any time, like a recording ──
var JOURNAL = __JOURNAL_JSON__;
var thIdx = 0, thPaused = false, thDelay = 900, thTimer = null;
function thRender(ev) {
  var body = document.getElementById('th-body');
  if (ev.kind === 'note') {
    var n = document.createElement('div');
    n.className = 'th-note';
    n.textContent = ev.text;
    body.appendChild(n);
  } else {
    var u = document.createElement('div');
    u.className = 'th-user';
    u.textContent = ev.user;
    body.appendChild(u);
    var r = document.createElement('div');
    r.className = 'th-reply';
    r.textContent = (ev.reply || '(no reply)').slice(0, 700);
    if (typeof ev.score === 'number' || ev.passed === false) {
      var c = document.createElement('span');
      c.className = 'th-chip ' + (ev.passed ? 'pass' : 'fail');
      c.textContent = ev.passed ? 'PASS' : 'FAIL';
      r.appendChild(c);
    }
    body.appendChild(r);
  }
  body.scrollTop = body.scrollHeight;
}
function thTick() {
  if (thPaused) return;
  if (thIdx >= JOURNAL.length) {
    document.getElementById('th-prog').textContent = JOURNAL.length + ' / ' + JOURNAL.length + ' - end';
    return;
  }
  thRender(JOURNAL[thIdx++]);
  document.getElementById('th-prog').textContent = thIdx + ' / ' + JOURNAL.length;
  thTimer = setTimeout(thTick, thDelay);
}
function theaterStart() {
  var body = document.getElementById('th-body');
  body.innerHTML = '';
  if (!JOURNAL.length) {
    body.innerHTML = '<div class="th-empty">Nothing recorded yet - run a step (build, test, drive...) and the session journal fills itself.</div>';
  }
  thIdx = 0; thPaused = false;
  document.getElementById('th-overlay').classList.add('show');
  document.getElementById('th-play').textContent = 'Pause';
  clearTimeout(thTimer);
  thTick();
}
function thToggle() {
  thPaused = !thPaused;
  document.getElementById('th-play').textContent = thPaused ? 'Play' : 'Pause';
  if (!thPaused) thTick();
}
function thSpeed(d) {
  thDelay = d;
  ['ths-1', 'ths-2', 'ths-3'].forEach(function (id) { document.getElementById(id).classList.remove('on'); });
  ({900: 'ths-1', 420: 'ths-2', 150: 'ths-3'})[d] && document.getElementById(({900: 'ths-1', 420: 'ths-2', 150: 'ths-3'})[d]).classList.add('on');
}
function thRestart() { document.getElementById('th-body').innerHTML = ''; thIdx = 0; thPaused = false; clearTimeout(thTimer); thTick(); }
function thSkip() { thPaused = true; clearTimeout(thTimer); var b = document.getElementById('th-body'); b.innerHTML = ''; JOURNAL.forEach(thRender); thIdx = JOURNAL.length; document.getElementById('th-prog').textContent = thIdx + ' / ' + JOURNAL.length + ' - end'; }
// the journal also refreshes live so a reopened theater has the latest run
// (refreshArtifacts swaps it below)

// ── click-through tutorial: the Priya proposal-generation demo ──
var TOUR = [
  { t: 'Welcome - the proposal generation walkthrough', target: null,
    x: 'This short tour trains you on the whole loop using Priya\'s use case: start from the Proposal Generation template, have the brainstem make sure it also generates PDF proposals, then build, test, and deploy to Copilot Studio. Next walks you through; "Do this step" runs each step for real; Skip any time.' },
  { t: '1. Start from the template', target: '#tpl-select',
    x: 'Instead of pasting a transcript, pick "Proposal Generation Stack" from this dropdown. The pipeline snaps the prototype to it: capabilities, demo script and agent plan come from the template.',
    payload: ['The user picked the template "proposal_generation_stack" from the library dropdown. Run Transcript2Prototype action=template op=use template_id=proposal_generation_stack right away. Then say what was created and that the tour continues with the feedback step.',
              'Start a prototype from the Proposal Generation Stack template.'] },
  { t: '2. Ask for what is missing - in plain language', target: '#fb-input',
    x: 'Priya also needs the agent to actually generate PDF proposals. Just ask for it here - the brainstem mutates the prototype: a new capability is added, the demo regenerates and the agents rebuild, live.',
    payload: ['Make sure this prototype ALSO generates PDF proposals and outputs them for the user, alongside its default capabilities. Add that capability (with synthetic records that simulate the PDFs) and confirm what changed.',
              'Make sure it also generates PDF proposals for the user.'] },
  { t: '3. Build the agents', target: '.step-btn[data-key="build"]',
    x: 'One click writes the real agent.py files - one per capability, grounded in the template and your feedback.', step: 'build' },
  { t: '4. Test locally', target: '.step-btn[data-key="test_local"]',
    x: 'The demo script replays against the generated agents in-process and every turn is scored. Green means the prototype does what the demo promises.', step: 'test_local' },
  { t: '5. Run on the twin', target: '.step-btn[data-key="test_twin"]',
    x: 'The prototype gets its OWN twin - separate process, port and memory - and the demo panel on the left flips LIVE against it. What you demo is the real thing.', step: 'test_twin' },
  { t: '6. Copilot Studio - export + deploy', target: '.step-btn[data-key="deploy"]',
    x: 'One step: everything bundles into ONE factory agent.py (the gate - the hand-off artifact in the outputs), then the prototype imports into Copilot Studio autonomously with your loaded app registration - no sign-in. Feedback after the gate reopens the loop.', step: 'deploy' },
  { t: 'Take it with you', target: '#dl-list',
    x: 'The session guide (a runbook anyone can present from), the demo script, every agent.py, the factory singleton and the MCP App server - all downloadable here. Export a .egg backup any time to save this exact prototype.' },
  { t: 'Run more side by side', target: null,
    x: 'Start new prototype (top right) hatches another rapplication on its own twin, so you can run several use cases in parallel. That is the whole loop - you are trained.' }
];
var tourIdx = -1;
function tourStart() { tourIdx = 0; tourShow(); }
function tourEnd() {
  tourIdx = -1;
  document.getElementById('tour-hole').style.display = 'none';
  document.getElementById('tour-card').classList.remove('show');
}
function tourMove(d) {
  tourIdx += d;
  if (tourIdx < 0) tourIdx = 0;
  if (tourIdx >= TOUR.length) { tourEnd(); return; }
  tourShow();
}
function tourShow() {
  var s = TOUR[tourIdx];
  var hole = document.getElementById('tour-hole');
  if (s.target) {
    var el = document.querySelector(s.target);
    if (el) {
      var r = el.getBoundingClientRect();
      hole.style.display = 'block';
      hole.style.left = (r.left - 6) + 'px';
      hole.style.top = (r.top - 6) + 'px';
      hole.style.width = (r.width + 12) + 'px';
      hole.style.height = (r.height + 12) + 'px';
    } else { hole.style.display = 'none'; }
  } else {
    hole.style.display = 'block';
    hole.style.left = '50%'; hole.style.top = '40%';
    hole.style.width = '0px'; hole.style.height = '0px';
  }
  document.getElementById('tour-title').textContent = s.t;
  document.getElementById('tour-text').textContent = s.x;
  document.getElementById('tour-prog').textContent = (tourIdx + 1) + ' / ' + TOUR.length;
  document.getElementById('tour-back').style.display = tourIdx === 0 ? 'none' : '';
  document.getElementById('tour-do').style.display = (s.payload || s.step) ? '' : 'none';
  document.getElementById('tour-next').textContent = tourIdx === TOUR.length - 1 ? 'Finish' : 'Next';
  document.getElementById('tour-card').classList.add('show');
}
function tourDo() {
  var s = TOUR[tourIdx];
  if (s.step) { stepSend(s.step); }
  else if (s.payload) {
    addFb('you', s.payload[1]);
    sendPayload('(prototype cubby: ' + SLUG + ') ' + s.payload[0],
                '(prototype cubby: ' + SLUG + ') ' + s.payload[1]);
  }
  tourMove(1);
}
async function npChoice(kind) {
  document.getElementById('np-overlay').classList.remove('show');
  if (kind === 'tab') {
    // open the tab on the user gesture so popup blockers allow it; navigate
    // it once the brainstem hands back the new twin URL
    var w = window.open('', '_blank');
    if (w) { try { w.document.write('<body style="font-family:sans-serif;background:#f5f5f5;color:#616161;display:flex;align-items:center;justify-content:center;height:100vh">Hatching your new prototype twin...</body>'); } catch (e) {} }
    addFb('you', 'Start a new prototype in a new tab (side by side).');
    var reply = await sendPayload('(prototype cubby: ' + SLUG + ') Call Transcript2Prototype action=new_prototype '
      + '(ONE call, no other tools). Then reply with the new twin URL on its own line.',
      'Start a new prototype in a new tab.');
    var m = reply && reply.match(/https?:\/\/[\w.\-]+:\d+/);
    if (m && w) { w.location = m[0]; }
    else if (w) { w.close(); if (reply) addFb('sys', 'No twin URL found in the reply - say "status" to find it.'); }
  } else if (kind === 'save') {
    // deterministic two-step: snapshot then reset, straight over /perform
    addFb('sys', 'Snapshotting this prototype, then resetting...');
    try {
      var snap = await performCall({ action: 'egg', op: 'export', cubby: SLUG });
      if (snap.status !== 'success') { addFb('sys', 'Snapshot failed: ' + (snap.error || snap.status) + ' - nothing was reset.'); return; }
      addFb('sys', 'Snapshot saved: ' + snap.egg);
      var rst = await performCall({ action: 'new_prototype', name: SLUG, force: true });
      if (rst.status === 'success') { addFb('sys', 'Reset done - reloading.'); setTimeout(function () { if (rst.url) { location.href = rst.url; } else { location.reload(); } }, 1200); }
      else { addFb('sys', 'Reset failed: ' + (rst.error || rst.status)); }
    } catch (err) {
      addFb('sys', 'Snapshot and reset failed: ' + err.message);
    }
  } else if (kind === 'reset') {
    addFb('sys', 'Resetting this prototype to a fresh start...');
    try {
      var r = await performCall({ action: 'new_prototype', name: SLUG, force: true });
      if (r.status === 'success') { addFb('sys', 'Reset done - reloading.'); setTimeout(function () { if (r.url) { location.href = r.url; } else { location.reload(); } }, 1200); }
      else { addFb('sys', 'Reset failed: ' + (r.error || r.status)); }
    } catch (err) {
      addFb('sys', 'Reset failed: ' + err.message);
    }
  }
}
document.getElementById('fb-send').addEventListener('click', fbSend);
document.getElementById('fb-input').addEventListener('keydown', function (e) {
  if (e.key === 'Enter') { e.preventDefault(); fbSend(); }
});
renderDownloads();
highlightNext();
replayBtnSync();
if (canRefresh) setInterval(refreshArtifacts, 8000);
else addFb('sys', 'Opened from disk - live refresh of the demo panel is off. Serve this page from the twin (twin op=up gives the URL) for real-time updates.');
</script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# generated-agent source template
# ---------------------------------------------------------------------------
AGENT_IMPORT_BLOCK = '''try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}
'''

AGENT_CLASS_TEMPLATE = '''
class {class_name}(BasicAgent):
    """{description}"""

    KNOWLEDGE = {knowledge!r}
    TRIGGERS = {triggers!r}
    RESPONSE = {response!r}
    # invented demo data - synthetic data fills the gaps, no customer data needed
    SYNTHETIC_DATA = {synthetic!r}
    # when set, every reply DELIVERS this real PDF as an attachment card
    DOC_NAME = {doc_name!r}
    CUSTOMER = {customer!r}

    def __init__(self):
        self.name = {agent_name!r}
        self.metadata = {{
            "name": self.name,
            "description": {tool_description!r},
            "parameters": {{
                "type": "object",
                "properties": {{
                    "user_input": {{
                        "type": "string",
                        "description": "The user's request, in their own words.",
                    }}
                }},
                "required": ["user_input"],
            }},
        }}
        super().__init__(self.name, self.metadata)

    @staticmethod
    def _pdf(title, lines):
        # tiny valid single-page PDF 1.4 - stdlib only, no dependencies
        def esc(t):
            t = str(t).replace("\\\\", "\\\\\\\\")
            return t.replace("(", "\\\\(").replace(")", "\\\\)")
        body = ["BT /F1 16 Tf 54 760 Td (" + esc(title[:90]) + ") Tj ET"]
        y = 728
        for ln in lines:
            chunks = [str(ln)[i:i + 95]
                      for i in range(0, len(str(ln)), 95)] or [""]
            for chunk in chunks:
                body.append("BT /F1 10 Tf 54 %d Td (%s) Tj ET" % (y, esc(chunk)))
                y -= 16
                if y < 60:
                    break
            if y < 60:
                break
        stream = "\\n".join(body).encode("latin-1", "replace")
        objs = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            b"<< /Length " + str(len(stream)).encode() + b" >>\\nstream\\n"
            + stream + b"\\nendstream",
        ]
        out = bytearray(b"%PDF-1.4\\n")
        offs = []
        for i, o in enumerate(objs, 1):
            offs.append(len(out))
            out += str(i).encode() + b" 0 obj\\n" + o + b"\\nendobj\\n"
        xref = len(out)
        out += (b"xref\\n0 " + str(len(objs) + 1).encode()
                + b"\\n0000000000 65535 f \\n")
        for off in offs:
            out += ("%010d 00000 n \\n" % off).encode()
        out += (b"trailer\\n<< /Size " + str(len(objs) + 1).encode()
                + b" /Root 1 0 R >>\\nstartxref\\n" + str(xref).encode()
                + b"\\n%%EOF\\n")
        return bytes(out)

    def perform(self, **kwargs):
        user_input = kwargs.get("user_input", "")
        grounding = "\\n".join("- " + k for k in self.KNOWLEDGE)
        reply = self.RESPONSE
        if grounding:
            reply += "\\n\\nGrounded in what you told us:\\n" + grounding
        hits = []
        if self.SYNTHETIC_DATA:
            words = [w for w in user_input.lower().split() if len(w) > 3]
            hits = [r for r in self.SYNTHETIC_DATA
                    if any(w in json.dumps(r).lower() for w in words)]
            if not hits:
                hits = self.SYNTHETIC_DATA[:2]
            reply += ("\\n\\nWorked example (synthetic demo data - "
                      "no customer data needed):")
            for r in hits[:2]:
                reply += "\\n- " + ", ".join(
                    str(k) + ": " + str(v) for k, v in r.items())
        if user_input:
            reply += "\\n\\n(Responding to: " + user_input[:160] + ")"
        if self.DOC_NAME:
            # a capability that promises a document DELIVERS one - the demo
            # renders this marker as an M365-style attachment card
            lines = ["Prepared for " + self.CUSTOMER, ""]
            lines += [str(k) for k in self.KNOWLEDGE]
            for r in hits[:3]:
                lines.append("")
                lines += [str(k) + ": " + str(v) for k, v in r.items()]
            lines += ["", "Synthetic demo data - no customer data was needed."]
            blob = self._pdf(self.metadata["description"][:80], lines)
            reply += ('\\n\\n[[attachment name="' + self.DOC_NAME
                      + '" mime="application/pdf" b64="'
                      + base64.b64encode(blob).decode("ascii") + '"]]')
        return reply
'''

FACTORY_TEMPLATE = '''"""{display_name} factory singleton - the whole {slug} prototype in one file.

Exported by Transcript2Prototype (the gate artifact for the next stage).
Drop this single file into any brainstem's agents/ directory: it carries
every generated agent for the prototype plus a factory that lists, calls,
and keyword-routes across them.

Generated {generated_at} from cubby '{slug}'.
"""

import base64
import json

{import_block}

{member_classes}

MEMBER_CLASSES = [{member_class_names}]


class {factory_class}(BasicAgent):
    """Factory singleton over the {display_name} prototype agents."""

    def __init__(self):
        self.name = {factory_name!r}
        self.members = {{}}
        for cls in MEMBER_CLASSES:
            inst = cls()
            self.members[inst.name] = inst
        self.metadata = {{
            "name": self.name,
            "description": (
                "Factory singleton for the {display_name} prototype. "
                "action=manifest lists member agents; action=call runs one by "
                "name; action=route keyword-routes user_input to the best member."
            ),
            "parameters": {{
                "type": "object",
                "properties": {{
                    "action": {{
                        "type": "string",
                        "enum": ["manifest", "call", "route"],
                        "description": "what to do",
                    }},
                    "agent": {{
                        "type": "string",
                        "description": "call: the member agent name",
                    }},
                    "user_input": {{
                        "type": "string",
                        "description": "call/route: the user's request",
                    }},
                }},
                "required": ["action"],
            }},
        }}
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        import json as _json
        action = (kwargs.get("action") or "manifest").lower()
        if action == "manifest":
            return _json.dumps({{
                "schema": "t2p-factory/1.0",
                "factory": self.name,
                "prototype": {slug!r},
                "members": [
                    {{"name": n, "description": a.metadata.get("description", "")}}
                    for n, a in sorted(self.members.items())
                ],
            }}, indent=2)
        if action == "call":
            name = kwargs.get("agent") or ""
            agent = self.members.get(name)
            if not agent:
                return _json.dumps({{"status": "error",
                                     "error": "unknown member agent " + repr(name),
                                     "members": sorted(self.members)}})
            return agent.perform(user_input=kwargs.get("user_input", ""))
        if action == "route":
            text = (kwargs.get("user_input") or "").lower()
            best, best_score = None, 0
            for agent in self.members.values():
                hay = (agent.metadata.get("description", "") + " "
                       + " ".join(getattr(agent, "TRIGGERS", []))).lower()
                score = sum(1 for w in set(text.split()) if len(w) > 3 and w in hay)
                if score > best_score:
                    best, best_score = agent, score
            if best is None:
                best = next(iter(self.members.values()))
            return best.perform(user_input=kwargs.get("user_input", ""))
        return _json.dumps({{"status": "error", "error": "action must be manifest | call | route"}})
'''


# ---------------------------------------------------------------------------
# the agent
# ---------------------------------------------------------------------------
class Transcript2PrototypeAgent(BasicAgent):
    def __init__(self):
        self.name = "Transcript2Prototype"
        self.metadata = {
            "name": self.name,
            "description": (
                "Turn a pasted business transcript into a working agent prototype, "
                "end to end, one isolated cubby per prototype: generate a turn-by-turn "
                "demo script, surface it as a static M365 Copilot demo injected as "
                "base64 bytecode in the rapplication iframe, adjust it conversationally, "
                "build the actual agent.py files, replay the demo against them on a "
                "local twin and then a live twin, and export everything as one factory "
                "singleton agent.py (the gate). Browse prototypes with list/search/focus."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["help", "spec", "start", "list", "search", "focus",
                                 "status", "show_demo", "adjust", "build", "test", "drive",
                                 "twin", "export", "deploy", "mcp_app",
                                 "credentials", "capability", "template",
                                 "new_prototype", "egg", "open", "hpa", "declarative"],
                        "description": "what to do (help for the map)",
                    },
                    "transcript": {
                        "type": "string",
                        "description": ("start (REQUIRED): the full transcript text, "
                                        "verbatim, exactly as the user pasted it. Do "
                                        "not summarize it - pass the whole thing.")},
                    "capabilities": {
                        "type": "string",
                        "description": ("start (STRONGLY PREFERRED): YOU are the "
                                        "analyst. Read the transcript yourself, "
                                        "identify the 3-5 concrete things the customer "
                                        "needs an agent to do, and pass them here as a "
                                        "JSON array string. " + CAPABILITIES_SCHEMA_HINT
                                        + " If you omit this, a deterministic keyword "
                                        "heuristic analyzes the transcript instead - "
                                        "it works but your analysis is better.")},
                    "name": {"type": "string",
                             "description": ("start: short prototype name; becomes the "
                                             "cubby slug, e.g. 'contoso-claims'. "
                                             "Defaults from customer/transcript. "
                                             "capability op=remove: the capability "
                                             "name to remove.")},
                    "serve": {"type": "boolean",
                              "description": ("new_prototype: start the prototype's own "
                                              "twin and return its URL (default true) - "
                                              "that twin serves another full rapplication "
                                              "so prototypes run side by side.")},
                    "template_id": {
                        "type": "string",
                        "description": ("template op=use/oneclick: the stack id from the "
                                        "AI-Agent-Templates library (op=search lists "
                                        "them, e.g. proposal_generation_stack).")},
                    "templates_source": {
                        "type": "string",
                        "description": ("template: base of the library - a raw-GitHub "
                                        "URL or local mirror dir. Default "
                                        "https://raw.githubusercontent.com/kody-w/"
                                        "AI-Agent-Templates/main (the public site's "
                                        "data).")},
                    "capability": {
                        "type": "string",
                        "description": ("capability op=add/update: ONE JSON object you "
                                        "author from the user's NEW requirement - same "
                                        "shape as a capabilities[] item (name, "
                                        "description, triggers, knowledge, response, "
                                        "demo_user, synthetic_records). Invent "
                                        "synthetic_records that SIMULATE the requested "
                                        "artifact (e.g. a generated PDF proposal as "
                                        "records with file_name, pages, status, deal). "
                                        "One call regenerates demo + agents.")},
                    "customer_name": {"type": "string",
                                      "description": ("start: the customer/company the "
                                                      "prototype is for; appears in the "
                                                      "demo UI. Extract it from the "
                                                      "transcript if you can.")},
                    "agent_name": {"type": "string",
                                   "description": ("start: display name of the demoed "
                                                   "copilot, e.g. 'Northwind Onboarding "
                                                   "Assistant'. Default: '<customer> "
                                                   "Assistant'.")},
                    "pain_markers": {
                        "type": "string",
                        "description": ("start, fallback analyzer only: comma-separated "
                                        "phrases that mark a pain/need sentence in this "
                                        "transcript (e.g. 'we need,takes hours,no way "
                                        "to'). Only used when capabilities= is omitted; "
                                        "sensible defaults exist.")},
                    "capability_vocabulary": {
                        "type": "string",
                        "description": ("start, fallback analyzer only: comma-separated "
                                        "domain words (prefixes ok) that make good "
                                        "capability names for this customer (e.g. "
                                        "'triage,claims,drafting'). Only used when "
                                        "capabilities= is omitted; defaults exist.")},
                    "max_capabilities": {
                        "type": "integer",
                        "description": ("start, fallback analyzer only: cap on how many "
                                        "capabilities to extract (default 5).")},
                    "brainstem_url": {
                        "type": "string",
                        "description": ("start: /chat URL of the PROTOTYPING brainstem "
                                        "that the rapplication's built-in feedback chat "
                                        "talks to (the brainstem hosting this agent). "
                                        "Default http://localhost:7071/chat.")},
                    "cubby": {"type": "string",
                              "description": "focus/status/...: prototype cubby slug"},
                    "query": {"type": "string",
                              "description": "search: term to find across prototype cubbies"},
                    "turn": {"type": "integer",
                             "description": "adjust: 1-based demo turn number"},
                    "turns": {"type": "integer",
                              "description": ("drive: play the first N demo-script turns "
                                              "against the twin (default: all). The open "
                                              "rapplication shows each exchange live.")},
                    "user_input": {"type": "string",
                                   "description": ("drive: a single message to send to the "
                                                   "twin and play in the UI - use this to "
                                                   "SHOW the user something in their open "
                                                   "rapplication instead of describing it.")},
                    "user": {"type": "string",
                             "description": "adjust: replacement user message for the turn"},
                    "assistant": {"type": "string",
                                  "description": "adjust: replacement scripted response"},
                    "expect": {"type": "string",
                               "description": "adjust: comma-separated expected keywords"},
                    "remove": {"type": "boolean",
                               "description": "adjust: remove the turn instead"},
                    "add": {"type": "boolean",
                            "description": "adjust: append a new turn (user= and assistant=)"},
                    "instruction": {
                        "type": "string",
                        "description": ("adjust: free-text change request. The agent "
                                        "does NOT interpret it - it returns the current "
                                        "demo script so YOU can decide the new wording "
                                        "and re-call adjust with the structured fields "
                                        "(turn=, user=, assistant=, expect=, remove=, "
                                        "add=). Prefer the structured fields directly.")},
                    "target": {"type": "string", "enum": ["local", "twin"],
                               "description": "test: local in-process twin or live twin over HTTP"},
                    "twin_url": {"type": "string",
                                 "description": ("test target=twin: EXPLICIT twin /chat base url. "
                                                 "Omit it (default) and the prototype's OWN dedicated "
                                                 "twin is provisioned and started automatically - a "
                                                 "completely separate process, port, memory and agent "
                                                 "set per prototype. Only pass this to target some "
                                                 "other twin.")},
                    "twin_dir": {"type": "string",
                                 "description": ("test target=twin with explicit twin_url only: "
                                                 "agents dir to inject into. Ignored for the "
                                                 "dedicated-twin default.")},
                    "inject": {"type": "boolean",
                               "description": ("test target=twin with explicit twin_url only: copy "
                                               "the built agent.pys into twin_dir first (default true)")},
                    "op": {"type": "string",
                           "enum": ["up", "down", "status", "provision",
                                    "import", "export", "download", "add",
                                    "update", "remove", "search", "use",
                                    "oneclick"],
                           "description": ("declarative: export (package the prototype as a "
                                           "Microsoft 365 DECLARATIVE AGENT - a Teams-"
                                           "sideloadable app zip in the HPA reference "
                                           "shape; use when asked to output for Teams / "
                                           "sideload / declarative agent). "
                                           "twin: up (provision/refresh + start + repoint the "
                                           "iframe; allowed past the gate) | down | status | "
                                           "provision. credentials: import (save the user's app "
                                           "registration + Power Platform details from a "
                                           "local.settings.json) | export (write them back out as "
                                           "a file to move machines) | download (return the raw "
                                           "values for a client-side file save - used by the "
                                           "rapplication's static export button, not for chat) | "
                                           "status. capability: add | "
                                           "update | remove (evolve the prototype from new "
                                           "requirements). template: search | use | oneclick "
                                           "(agent stacks from the template library as "
                                           "pipeline inputs; oneclick = prototype + build + "
                                           "tests + export + autonomous Copilot Studio "
                                           "deploy in one call).")},
                    "path": {"type": "string",
                             "description": ("credentials op=import: path to the settings file to "
                                             "read. op=export: where to write it (default "
                                             "~/Desktop/rapp_deploy.local.settings.json). "
                                             "egg op=import: the .egg file to reload. "
                                             "egg op=export: where to write the .egg "
                                             "(default ~/Desktop/t2p-<slug>-<date>.egg).")},
                    "twin_source": {"type": "string",
                                    "description": ("twin: brainstem kernel dir to copy from "
                                                    "(default: the brainstem hosting this agent, "
                                                    "else ~/.brainstem/src/rapp_brainstem)")},
                    "credentials": {"type": "object",
                                    "description": ("deploy / credentials op=import: a "
                                                    "local.settings.json object (or its Values) "
                                                    "with the user's app registration + Power "
                                                    "Platform details: DYNAMICS_365_CLIENT_ID, "
                                                    "DYNAMICS_365_CLIENT_SECRET, "
                                                    "DYNAMICS_365_TENANT_ID, DYNAMICS_365_RESOURCE. "
                                                    "Saved creds are used automatically when "
                                                    "omitted; never echo the secret back.")},
                    "credentials_path": {"type": "string",
                                         "description": ("deploy / credentials op=import: path to a "
                                                         "local.settings.json holding the "
                                                         "DYNAMICS_365_* values.")},
                    "deploy_agent_path": {"type": "string",
                                          "description": ("deploy: path to copilot_studio_deploy_"
                                                          "agent.py if it is not already next to "
                                                          "this agent in the brainstem.")},
                    "egg_b64": {"type": "string",
                                "description": ("egg op=import: the .egg bytes as base64 - the "
                                                "rapplication's static upload path (alternative "
                                                "to path=).")},
                    "pattern_from": {"type": "string",
                                     "description": ("deploy: EXPLICITLY borrow a BUILT HPA's "
                                                     "solution anatomy ('owner/repo:Template "
                                                     "Name') - topics, actions, workflows, "
                                                     "Dataverse/connector wiring - filled with "
                                                     "this prototype's content. When omitted "
                                                     "the the work distro mcs_solution packager builds "
                                                     "the solution natively (the default).")},
                    "packager_path": {"type": "string",
                                      "description": ("deploy: dir containing wrapper_generator/"
                                                      "solution_packager.py (the the work distro "
                                                      "utility). Default discovery: T2P_PACKAGER "
                                                      "env, then the known repo locations. "
                                                      "'off' disables it (skeleton fallback).")},
                    "publisher": {"type": "string",
                                  "description": ("deploy: solution publisher display "
                                                  "name (default: Microsoft Research "
                                                  "and Development, the the work distro library "
                                                  "publisher - NEVER the pattern HPA's)")},
                    "publisher_prefix": {"type": "string",
                                         "description": ("deploy: schema customization "
                                                         "prefix, 2-8 lowercase alnum "
                                                         "(default msrnd)")},
                    "pattern_zip_path": {"type": "string",
                                         "description": ("deploy: local path to an HPA solution "
                                                         "zip to borrow (offline override of "
                                                         "pattern_from).")},
                    "hpa_source": {"type": "string",
                                   "description": ("start: HPA template lineage as "
                                                   "'owner/repo:Template Name' (e.g. "
                                                   "'kody-w/m365-agent-templates:Know My "
                                                   "Customer'). Recorded on the prototype so "
                                                   "action=hpa op=export can inject the "
                                                   "prototype's mutations back into that "
                                                   "template (updated README + instructions in "
                                                   "exports/hpa_update/).")},
                    "merge": {"type": "boolean",
                              "description": ("template op=use: fold the template INTO the "
                                              "existing prototype (capability union, transcripts "
                                              "concatenate, identity and HPA lineage survive) "
                                              "instead of replacing it - how a transcript, an "
                                              "HPA and an industry template compose into ONE "
                                              "prototype.")},
                    "artifact_markers": {"type": "string",
                                         "description": ("build: comma-separated words that mark "
                                                         "a capability as document-producing "
                                                         "(default: pdf,document,report,letter,"
                                                         "proposal,quote,invoice,contract,...). "
                                                         "Matching capabilities deliver a real "
                                                         "generated PDF as an attachment card in "
                                                         "every reply. Per-capability override: "
                                                         "produces_file in capabilities=.")},
                    "return_b64": {"type": "boolean",
                                   "description": ("egg op=export: include the .egg bytes as "
                                                   "base64 in the result so a browser can save "
                                                   "the file itself (static download).")},
                    "threshold": {"type": "number",
                                  "description": "test: pass threshold for keyword score (local 0.6, twin 0.35)"},
                    "skip_twin": {"type": "boolean",
                                  "description": "export: allow exporting with only the local run passed"},
                    "force": {"type": "boolean",
                              "description": "start: overwrite an existing prototype cubby"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        return (
            "Transcript2Prototype is loaded: the transcript-to-prototype pipeline "
            "rapplication. YOU do the thinking; the agent does the plumbing - every "
            "input is a parameter, nothing is hardcoded. When a user pastes a "
            "meeting/discovery transcript and wants a prototype, demo, or agents "
            "built from it: (1) read the transcript YOURSELF, identify the 3-5 "
            "capabilities the customer needs, and call action=start with "
            "transcript=<full verbatim text>, customer_name=, name=, and "
            "capabilities=<JSON array per the parameter description> - that is the "
            "high-quality path; omitting capabilities falls back to a keyword "
            "heuristic. (2) When the user asks for changes in plain language ('make "
            "turn 2 about refunds'), decide the new wording yourself and call "
            "action=adjust with the structured fields (turn=, user=, assistant=, "
            "expect=, add=, remove=) - one call per turn changed; the iframe bytecode "
            "regenerates automatically. (3) Then action=build, action=test "
            "target=local, action=test target=twin, action=export (the GATE - the "
            "pipeline stops there and hands off the factory singleton). Browse "
            "prototypes with action=list / search / focus. ALWAYS relay the returned "
            "rapplication HTML path so the user can open the demo in a browser, and "
            "summarize test pass rates when tests run. THE RAPPLICATION IS THE USER'S "
            "WHOLE SURFACE: it serves at the prototype's twin URL (twin op=up returns "
            "it - relay that URL, it is what the user opens) and contains the demo "
            "iframe, a feedback chat that talks to YOU (messages arrive prefixed "
            "'(prototype cubby: <slug>)' - treat that slug as the cubby= for every "
            "call), and downloadable outputs (demo script + agent.pys + factory). "
            "When a feedback-chat user pastes a NEW use case or transcript, run the "
            "whole pipeline for them: start (author the capabilities yourself, "
            "including invented synthetic_records - synthetic data fills gaps, never "
            "ask for customer data), build, test target=local, test target=twin, and "
            "give them the new twin URL to open; they should never need anything "
            "but the rapplication. After changing the demo or rebuilding, the open "
            "rapplication refreshes itself - tell the user what changed. After the "
            "export gate, action=deploy packages the prototype as a Copilot Studio "
            "agent and imports it into the environment autonomously using the saved "
            "app registration (if none is saved, tell the user to click 'Load "
            "settings file' in the rapplication's Deployment credentials panel). "
            "action=credentials op=import path=<their "
            "local.settings.json> saves the user's app registration + Power Platform "
            "details for autonomous deploys (op=export writes them back out to move "
            "machines; never echo the secret). action=mcp_app generates a single-file "
            "MCP App server making the prototype NATIVE to Copilot Studio - "
            "capabilities as MCP tools, the demo as the interactive widget; relay the "
            "run + devtunnel + add-tool steps from its note. The downloads include a "
            "SESSION GUIDE - the human-runnable script; point non-technical users at "
            "that, never at the raw JSON. TO SHOW RATHER THAN TELL: action=drive user_input=<one message> (or "
            "turns=N for demo-script turns) sends it to the live twin and the open "
            "rapplication plays the exchange in the Copilot frame like a ghost user "
            "- use it whenever seeing beats describing. BACKUPS: action=egg op=export snapshots the whole prototype (cubby + twin "
            "memory + soul) to a portable .egg; egg op=import path=... [name=...] "
            "reloads it - then twin op=up serves it. Use it before risky changes and "
            "to keep per-use-case variants. WHEN THE USER WANTS ANOTHER PROTOTYPE RUNNING SIDE BY SIDE (the Start new "
            "prototype button), call action=new_prototype - ONE call hatches a starter "
            "prototype on its own twin; reply with the returned URL on its own line so "
            "the page can open it. With name=<current cubby> force=true it resets the "
            "current prototype in place (snapshot first with the rapp agent's "
            "cubby_egg if asked). THE TEMPLATE LIBRARY IS A PIPELINE INPUT TOO: action=template op=search "
            "lists agent stacks from kody-w.github.io/AI-Agent-Templates (raw GitHub "
            "data); op=use template_id=<id> starts a prototype from one; op=oneclick "
            "template_id=<id> runs the WHOLE journey - prototype, build, tests, "
            "export and autonomous Copilot Studio deploy (using the imported app "
            "registration) - then the user gives feedback in the rapplication and "
            "capability changes regenerate it in real time. WHEN FEEDBACK BRINGS A NEW REQUIREMENT "
            "('can it also generate a PDF proposal?'), call action=capability op=add "
            "with capability=<ONE JSON object you author> - include synthetic_records "
            "that SIMULATE the artifact (a generated PDF as records with file_name, "
            "pages, status); that one call regenerates the demo and rebuilds the "
            "agents; then chain test target=local, test target=twin, mcp_app op=up "
            "(rebakes the MCP app so the new capability appears as a tool + widget "
            "tab), export, deploy. Do at most a couple of tool calls per turn and "
            "ALWAYS end your turn with a short text summary - never an empty reply.")

    # ---- context -----------------------------------------------------------
    def _home(self, kwargs):
        # T2P_HOME lets constrained hosts (e.g. Azure Functions, where the
        # user home is not writable) relocate all state, e.g. /tmp/t2p_home.
        return (kwargs.get("_home_dir") or os.environ.get("T2P_HOME")
                or os.path.expanduser("~"))

    def _cubby_root(self, kwargs):
        return os.path.join(self._home(kwargs), ".brainstem", "cubbies")

    def _focus_file(self, kwargs):
        return os.path.join(self._home(kwargs), ".brainstem", "t2p_focus.json")

    def _bs_agents_dir(self, kwargs):
        explicit = kwargs.get("twin_dir")
        if explicit:
            return explicit
        return os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agents")

    def _env(self, action, status, **fields):
        return json.dumps({"schema": RESULT_SCHEMA, "action": action,
                           "status": status, **fields},
                          indent=2, ensure_ascii=False)

    def _resolve(self, kwargs, need_proto=True):
        """-> (slug, cubby_dir, proto|None, error_json|None)"""
        root = self._cubby_root(kwargs)
        slug = (kwargs.get("cubby") or kwargs.get("name") or "").strip()
        if not slug:
            focus = _read_json(self._focus_file(kwargs)) or {}
            slug = focus.get("cubby") or ""
        if not slug:
            return None, None, None, self._env(
                kwargs.get("action", "?"), "error",
                error="no prototype in focus - pass cubby=<slug> or run action=focus first.",
                hint="action=list shows every prototype cubby.")
        if not _SLUG_RE.match(slug):
            return None, None, None, self._env(
                kwargs.get("action", "?"), "error", error="unsafe cubby slug")
        cubby = os.path.join(root, slug)
        proto = _read_json(os.path.join(cubby, "prototype.json"))
        if need_proto and not proto:
            return None, None, None, self._env(
                kwargs.get("action", "?"), "error",
                error=f"'{slug}' is not a prototype cubby (no prototype.json).",
                hint="action=start transcript=... name=... creates one.")
        return slug, cubby, proto, None

    def _save(self, cubby, proto):
        proto["updated_at"] = _now()
        _write_json(os.path.join(cubby, "prototype.json"), proto)

    # ---- perform -----------------------------------------------------------
    # actions that mutate a prototype narrate themselves into the open
    # rapplication (the activity feed) so the user WATCHES backend work
    # land in their UI in real time. Values = the "working..." line; None
    # means only the completion is narrated (no prototype exists yet, or
    # the action is its own visual).
    _NARRATED = {
        "adjust": "adjusting the demo script...",
        "build": "building the agent.py files...",
        "test": "running the test - watch the demo panel...",
        "twin": None,
        "export": "exporting the factory singleton...",
        "deploy": "packaging and deploying to Copilot Studio...",
        "mcp_app": None,
        "capability": "applying the capability change - regenerating the demo and agents...",
        "template": None,
        "new_prototype": None,
        "egg": None,
        "drive": None,
        "start": None,
    }

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "help").lower()
        handlers = {
            "start": self._start, "list": self._list, "search": self._search,
            "focus": self._focus, "status": self._status,
            "show_demo": self._show_demo, "adjust": self._adjust,
            "build": self._build, "test": self._test, "drive": self._drive,
            "twin": self._twin, "export": self._export, "deploy": self._deploy,
            "hpa": self._hpa, "declarative": self._declarative,
            "mcp_app": self._mcp_app, "credentials": self._credentials,
            "capability": self._capability, "template": self._template,
            "new_prototype": self._new_prototype, "egg": self._egg,
            "open": self._open,
        }
        try:
            if action == "help":
                return self._help()
            if action == "spec":
                return self._spec()
            fn = handlers.get(action)
            if fn is None:
                return self._help()
            if self._NARRATED.get(action):
                self._activity_append(kwargs, None, self._NARRATED[action])
            out = fn(kwargs)
            if action in self._NARRATED:
                self._activity_finish(kwargs, action, out)
            return out
        except Exception as e:  # noqa: BLE001 - agents must not crash the loop
            return self._env(action, "error", error=f"{type(e).__name__}: {e}")

    # ---- the activity feed: backend work, visible in the open UI ------------
    def _activity_append(self, kwargs, slug, text):
        """Best-effort: append a line to the prototype's activity feed and
        refresh the served page so the open rapplication shows it live."""
        try:
            if slug is None:
                slug = (kwargs.get("cubby")
                        or (_read_json(self._focus_file(kwargs)) or {}).get("cubby"))
            if not slug or not _SLUG_RE.match(str(slug)):
                return
            cubby = os.path.join(self._cubby_root(kwargs), slug)
            proto = _read_json(os.path.join(cubby, "prototype.json"))
            if not proto:
                return
            feed = proto.setdefault("activity", [])
            feed.append({"at": _now(), "text": str(text)[:200]})
            del feed[:-25]
            journal = proto.setdefault("journal", [])
            journal.append({"at": _now(), "kind": "note", "text": str(text)[:200]})
            del journal[:-300]
            html = proto.get("html") or {}
            self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                             api_url=html.get("api_url") or "")
            _write_json(os.path.join(cubby, "prototype.json"), proto)
        except Exception:  # noqa: BLE001 - narration never breaks the work
            pass

    def _activity_finish(self, kwargs, action, out):
        try:
            parsed = json.loads(out) if isinstance(out, str) else {}
        except ValueError:
            return
        slug = parsed.get("cubby")
        if not slug:
            return
        if action == "twin" and (kwargs.get("op") or "status") == "status":
            return  # read-only - not work worth narrating
        detail = (parsed.get("changed") or parsed.get("error")
                  or (parsed.get("note") or "").split(". ")[0])
        line = f"{action} {parsed.get('status', '?')}"
        if parsed.get("pass_rate") is not None:
            line += f" ({int(parsed['pass_rate'] * 100)}% pass)"
        if detail:
            line += f" - {detail}"
        self._activity_append(kwargs, slug, line)

    # ---- orient ------------------------------------------------------------
    def _help(self):
        return (
            "Transcript2Prototype - transcript in, working prototype out. One cubby per prototype.\n"
            "  start    transcript=<text> capabilities=<JSON you authored - preferred>\n"
            "           [name=...] [customer_name=...] [agent_name=...]\n"
            "           (fallback tuning: pain_markers=, capability_vocabulary=, max_capabilities=)\n"
            "           -> cubby + demo script + M365 demo iframe rapplication (scripted bytecode)\n"
            "  egg op=export [path=...] | op=import path=<file.egg> [name=<new slug>] [force=true]\n"
            "           -> back the WHOLE prototype up (cubby + twin memory + soul) as a portable\n"
            "           .egg, and reload it - optionally renamed - for a different use case\n"
            "  new_prototype [name=... force=true] [serve=false] -> hatch a fresh starter\n"
            "           prototype on its OWN twin (side-by-side rapplications); with name+force\n"
            "           it resets an existing prototype in place\n"
            "  template op=search [query=...] | op=use template_id=... | op=oneclick template_id=...\n"
            "           -> agent stacks from the AI-Agent-Templates library as pipeline inputs;\n"
            "           oneclick = prototype -> build -> tests -> export -> Copilot Studio, one call\n"
            "  capability op=add|update|remove [capability=<JSON you author>] [name=...]\n"
            "           -> EVOLVE the prototype from new requirements: one call regenerates the\n"
            "           demo script and rebuilds the agents (reopens the gate if exported)\n"
            "  adjust   turn=N [user=...] [assistant=...] [expect=a,b] [remove=true] | add=true | instruction=...\n"
            "           -> edits the demo script, regenerates the injected bytecode (any stage)\n"
            "  build    -> generates the real agent.py files into the cubby's agents/\n"
            "  drive    [user_input=... | turns=N] -> play the twin THROUGH the open rapplication;\n"
            "           each sent/answered exchange renders live in the Copilot frame\n"
            "  test     target=local  -> replay the demo against the generated agents in-process\n"
            "           target=twin -> the prototype's OWN dedicated twin is provisioned + started\n"
            "           automatically (separate process/port/memory per prototype); demo replays\n"
            "           over HTTP and the iframe goes live against it. (twin_url= to target another)\n"
            "  twin     op=up|down|status|provision -> manage the dedicated twin (up works even\n"
            "           after the export gate; it re-points the rapplication iframe)\n"
            "  export   [skip_twin=true] -> ONE factory singleton agent.py in exports/ - THE GATE (stops here)\n"
            "  deploy   -> the stage AFTER the gate: package the prototype as a Copilot Studio\n"
            "           agent and import it into the environment, autonomously, using the saved\n"
            "           app registration (load it once via credentials op=import or the\n"
            "           rapplication's Deployment credentials panel)\n"
            "  mcp_app  -> generate a single-file MCP App server (stdlib): capabilities as MCP\n"
            "           tools, the demo page as the interactive UI widget - the prototype NATIVE\n"
            "           to Copilot Studio / M365 Copilot (MCP Apps pattern)\n"
            "  credentials op=import path=<local.settings.json> | op=export [path=...] | op=status\n"
            "           -> save / move / inspect the app-registration + Power Platform details the\n"
            "           deploy stage uses (secret stays on this machine, always masked in replies)\n"
            "  browse   list | search query=... | focus cubby=... | status | show_demo | open\n"
            "  orient   spec (the pipeline map)\n")

    def _spec(self):
        return (
            "# Transcript2Prototype pipeline\n\n"
            "Stages per prototype (state in <cubby>/prototype.json):\n"
            "  intake+demo -> built -> local_passed -> twin_passed -> exported (GATE)\n\n"
            "1. start: the transcript is analyzed (LLM when reachable, deterministic\n"
            "   heuristics otherwise) into capabilities. A turn-by-turn demo script is\n"
            "   generated and injected into a static M365 Copilot demo template; that\n"
            "   page is base64-encoded and embedded as the iframe bytecode of the\n"
            "   rapplication shell (rapplications/<slug>_rapplication.html). Scripted\n"
            "   mode: sends are answered from the embedded script.\n"
            "2. adjust: any turn can be edited conversationally at any stage; the\n"
            "   bytecode is regenerated so the iframe always plays the current script.\n"
            "   Adjusting after a test run invalidates the test results.\n"
            "3. build: one agent.py per capability lands in <cubby>/agents/, grounded\n"
            "   in the same analysis the demo script came from.\n"
            "4. test target=local: the agent.pys are loaded in-process (the local twin)\n"
            "   and every demo turn is replayed and scored against its expected\n"
            "   keywords. Report: show-and-tell/test_report_local.json.\n"
            "5. test target=twin: the prototype's OWN dedicated twin is provisioned\n"
            "   under ~/.rapp/twins/ (full kernel copy: own process, own port, own\n"
            "   soul, own auth, own .brainstem_data memory - twins run completely\n"
            "   separately) and the SAME demo replays over HTTP against its /chat.\n"
            "   The rapplication iframe is regenerated in live mode pointed at THAT\n"
            "   twin. Report: show-and-tell/test_report_twin.json.\n"
            "6. export: all generated agents are bundled into ONE factory singleton\n"
            "   <slug>_factory_agent.py in <cubby>/exports/. THE PIPELINE STOPS HERE -\n"
            "   the singleton is the handoff artifact for the next stage.\n\n"
            "Cubbies are standard rapp-cubby/1.0 (RappAgent's cubby_list, super_rar and\n"
            "cubby_egg all work on them). Everything is local-first; no cloud required.\n")

    # ---- start -------------------------------------------------------------
    def _start(self, kwargs):
        transcript = (kwargs.get("transcript") or "").strip()
        if len(transcript) < 40:
            return self._env("start", "error",
                             error="pass transcript=<the pasted transcript text> (at least a few sentences).")
        customer = (kwargs.get("customer_name") or "").strip()
        name = (kwargs.get("name") or "").strip()
        slug = _slugify(name or customer or " ".join(transcript.split()[:4]))
        root = self._cubby_root(kwargs)
        cubby = os.path.join(root, slug)
        existing = _read_json(os.path.join(cubby, "prototype.json"))
        if existing and not kwargs.get("force"):
            return self._env("start", "already_exists", cubby=slug, path=cubby,
                             stage=existing.get("stage"),
                             hint=("prototype cubby already exists - focus cubby=%s to work on it, "
                                   "or pass force=true to overwrite." % slug))

        # cubby anatomy (first-class rapp-cubby/1.0 so RappAgent sees it)
        for d in CUBBY_ANATOMY:
            os.makedirs(os.path.join(cubby, d), exist_ok=True)
            gk = os.path.join(cubby, d, ".gitkeep")
            if not os.path.exists(gk):
                open(gk, "w").close()
        os.makedirs(os.path.join(cubby, "exports"), exist_ok=True)
        if not os.path.isfile(os.path.join(cubby, "cubby.json")):
            _write_json(os.path.join(cubby, "cubby.json"), {
                "schema": CUBBY_SCHEMA, "github_login": None, "slug": slug,
                "display_name": slug,
                "what_im_cooking": f"transcript2prototype pipeline for {customer or slug}",
                "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                "streamable": {"agents": True}})
        _write_text(os.path.join(cubby, "transcript.txt"), transcript)

        try:
            analysis, source = self._analyze(transcript, customer, kwargs)
        except (ValueError, TypeError) as e:
            msg = f"capabilities parameter invalid: {e}"
            if "JSON array" not in msg:
                msg += ". " + CAPABILITIES_SCHEMA_HINT
            return self._env("start", "error", error=msg)
        demo_script = self._demo_script(analysis)
        sources = {}
        if kwargs.get("hpa_source"):
            # "owner/repo:Template Name" lineage - hpa op=export injects the
            # prototype's mutations back into this HPA template
            sources["hpa"] = str(kwargs["hpa_source"])
        proto = {
            "schema": PROTO_SCHEMA, "slug": slug,
            "display_name": analysis.get("agent_name") or _camel(slug),
            "sources": sources,
            "brainstem_url": (kwargs.get("brainstem_url")
                              or "http://localhost:7071/chat"),
            "customer": analysis.get("company") or customer or "the customer",
            "created_at": _now(), "updated_at": _now(),
            "stage": "demo", "stages_done": ["intake", "demo"],
            "analysis_source": source,
            "analysis": analysis,
            "demo_script": demo_script,
            "agents_built": [],
            "tests": {},
            "export": None,
            "gate": {"stopped": False},
        }
        paths = self._regen_html(cubby, proto, mode="scripted")
        self._save(cubby, proto)
        _write_json(self._focus_file(kwargs), {"cubby": slug, "at": _now()})
        return self._env(
            "start", "success", cubby=slug, path=cubby, stage="demo",
            analysis_source=source, customer=proto["customer"],
            capabilities=[c["name"] for c in analysis["capabilities"]],
            demo_turns=len(demo_script),
            rapplication=paths["shell"], demo_page=paths["demo"],
            note=("demo script generated and injected into the M365 demo iframe as "
                  "base64 bytecode (scripted playback). Open the rapplication HTML, "
                  "drive it with Up arrow + Enter. Adjust any turn conversationally, "
                  "then 'build' when the demo tells the right story."))

    # ---- analysis ----------------------------------------------------------
    def _analyze(self, transcript, customer, kwargs):
        """Caller-provided capabilities are the preferred path (the caller is
        the analyst); the deterministic heuristic is the documented floor."""
        raw = kwargs.get("capabilities")
        if raw:
            caps = _coerce_capabilities(raw, customer or "the customer")
            company = customer or "the customer"
            agent_name = (kwargs.get("agent_name")
                          or (f"{company} Assistant" if company != "the customer"
                              else "Prototype Assistant"))
            return {
                "company": company,
                "agent_name": agent_name,
                "summary": (f"Prototype agent set for {company} drawn from the "
                            "transcript: "
                            + ", ".join(c["name"] for c in caps) + "."),
                "capabilities": caps,
            }, "caller"
        analysis = self._analyze_offline(transcript, customer, kwargs)
        if kwargs.get("agent_name"):
            analysis["agent_name"] = str(kwargs["agent_name"]).strip()
        return analysis, "deterministic_fallback"

    def _analyze_offline(self, transcript, customer, kwargs):
        sentences = _sentences(transcript)
        company = customer
        if not company:
            m = re.search(r"(?:Customer|Company|Client)\s*[:\-]\s*([A-Z][\w&. ]{2,40})",
                          transcript)
            if m:
                company = m.group(1).strip().rstrip(".")
        if not company:
            m = re.search(r"\b(?:at|for|with)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b",
                          transcript)
            company = m.group(1) if m else "the customer"

        markers = _csv_tuple(kwargs.get("pain_markers")) or DEFAULT_PAIN_MARKERS
        lexicon = _csv_tuple(kwargs.get("capability_vocabulary")) or DEFAULT_CAP_LEXICON
        max_caps = max(1, min(8, int(kwargs.get("max_capabilities") or 5)))
        pains = []
        for i, s in enumerate(sentences):
            low = s.lower()
            if any(marker in low for marker in markers):
                pains.append((i, s))
        if not pains:
            pains = list(enumerate(sentences))[:3]

        tf = {}
        for s in sentences:
            for w in _words(s):
                tf[w] = tf.get(w, 0) + 1

        caps, seen, used_prefixes, consumed = [], set(), set(), set()
        for i, s in pains:
            if i in consumed:
                continue  # restatement of a capability we already captured
            kws = _words(s)
            if not kws:
                continue
            # score every distinct word: capability vocabulary + transcript
            # frequency + length; penalize words already naming another
            # capability so five pains don't all become "Proposal ...".
            scored, first_pos = [], {}
            for pos, w in enumerate(kws):
                if w in first_pos:
                    continue
                first_pos[w] = pos
                score = ((3 if _lex_hit(w, lexicon) else 0)
                         + min(tf.get(w, 0), 3)
                         + (1 if len(w) > 5 else 0)
                         - (4 if w[:6] in used_prefixes else 0))
                scored.append((score, pos, w))
            best = sorted(scored, key=lambda t: (-t[0], t[1]))[:2]
            name_words = [w for _, _, w in sorted(best, key=lambda t: t[1])]
            used_prefixes.update(w[:6] for w in name_words)
            top = list(name_words)
            for w in kws:
                if w not in top:
                    top.append(w)
                if len(top) == 6:
                    break
            name = " ".join(w.capitalize() for w in name_words) or f"Capability {len(caps) + 1}"
            key = _slugify(name).replace("-", "_")
            if key in seen:
                continue
            seen.add(key)
            consumed.add(i)
            neighbor = sentences[i + 1] if i + 1 < len(sentences) else ""
            if neighbor.endswith("?"):
                neighbor = ""  # interviewer question, not customer knowledge
            knowledge = [s] + ([neighbor] if neighbor else [])
            if neighbor:
                consumed.add(i + 1)
            response = (
                f"Here is how the prototype handles **{name}** for {company}:\n\n"
                f"- It addresses the situation you described: \"{s[:180]}\"\n"
                f"- Key elements it works with: {', '.join(top)}.\n"
                f"- Next step: confirm this matches the workflow, then we wire it to "
                f"your real systems.")
            caps.append({
                "key": key, "name": name, "class_name": _camel(name),
                "description": f"Handles {name.lower()} for {company}: {s[:140]}",
                "triggers": top,
                "knowledge": knowledge,
                "response": response,
                "demo_user": f"Show me how you handle {name.lower()}. {s[:120]}",
                "synthetic_records": _synthesize_records(key, name, top, company),
            })
            if len(caps) == max_caps:
                break
        if not caps:
            caps = [{
                "key": "general_assist", "name": "General Assist",
                "class_name": "GeneralAssist",
                "description": f"General assistant for {company}",
                "triggers": ["assist", "general", "help"],
                "knowledge": sentences[:2] or [transcript[:200]],
                "response": (f"Here is how the prototype can assist {company} - "
                             f"general help grounded in the transcript."),
                "demo_user": "What can you help me with?",
                "synthetic_records": _synthesize_records(
                    "general_assist", "General Assist",
                    ["assist", "general", "help"], company),
            }]
        agent_name = f"{company} Assistant" if company != "the customer" else "Prototype Assistant"
        return {
            "company": company,
            "agent_name": agent_name,
            "summary": f"Prototype agent set for {company} drawn from the transcript: "
                       + ", ".join(c["name"] for c in caps) + ".",
            "capabilities": caps,
        }

    # ---- demo script -------------------------------------------------------
    def _demo_script(self, analysis):
        caps = analysis["capabilities"]
        turns = []
        overview = ("Here is what this prototype covers for "
                    f"{analysis['company']}:\n\n"
                    + "\n".join(f"- **{c['name']}** - {c['description']}" for c in caps)
                    + "\n\nQueue the next demo step to see each one in action.")
        turns.append({
            "turn": 1, "agent": None,
            "user": "What can you help me with?",
            "assistant": overview,
            "expect": [c["name"].split()[0].lower() for c in caps][:4],
        })
        for c in caps:
            assistant = c["response"]
            doc_name = _cap_artifact(c)
            if doc_name:
                # the scripted preview delivers the SAME real artifact the
                # built agent will - an attachment card, not a promise
                lines = ["Prepared for " + str(analysis.get("company") or
                                               "the customer"), ""]
                lines += [str(k) for k in (c.get("knowledge") or [])]
                for r in (c.get("synthetic_records") or [])[:3]:
                    lines.append("")
                    lines += [f"{k}: {v}" for k, v in r.items()]
                lines += ["", "Synthetic demo data - no customer data was needed."]
                assistant += _attachment_marker(
                    doc_name, _pdf_bytes(c["name"], lines))
            turns.append({
                "turn": len(turns) + 1, "agent": c["key"],
                "user": c["demo_user"],
                "assistant": assistant,
                "expect": list(c["triggers"][:4]),
            })
        turns.append({
            "turn": len(turns) + 1, "agent": None,
            "user": "Summarize what we just set up.",
            "assistant": (f"We walked through the {analysis['agent_name']} prototype: "
                          + ", ".join(c["name"] for c in caps)
                          + ". Each capability is grounded in your transcript and is "
                            "generated as a real agent.py in the next stage."),
            "expect": ["prototype"],
        })
        return turns

    # ---- html generation ---------------------------------------------------
    def _render_demo_page(self, proto, mode, api_url=""):
        analysis = proto["analysis"]
        demo = [{"q": t["user"], "e": ", ".join(t.get("expect") or []),
                 "a": t.get("assistant") or ""} for t in proto["demo_script"]]
        chips = "".join(f'<span class="chip">{c["name"]}</span>'
                        for c in analysis["capabilities"])
        badge = {"scripted": "SCRIPTED PREVIEW", "live": "LIVE TWIN",
                 "mcp": "MCP APP PREVIEW"}.get(mode, "PREVIEW")
        html = (M365_TEMPLATE
                .replace("__TITLE__", f"M365 Copilot - {analysis['agent_name']} Demo")
                .replace("__AGENT_NAME__", analysis["agent_name"])
                .replace("__AGENT_SUB__", f"{proto['customer']} - Copilot Agent")
                .replace("__CUSTOMER__", proto["customer"])
                .replace("__WELCOME_TEXT__", analysis.get("summary") or
                         "Drive the demo with the Up arrow, then Enter to send.")
                .replace("__CHIPS_HTML__", chips)
                .replace("__BADGE__", badge)
                .replace("__MODE__", mode)
                .replace("__API_URL__", api_url or "")
                .replace("__GUID__", f"t2p-{proto['slug']}")
                .replace("__TEST_REPLAY__",
                         json.dumps(proto.get("last_test_replay"),
                                    ensure_ascii=False))
                .replace("__DEMO_JSON__", json.dumps(demo, ensure_ascii=False)))
        return html

    def _render_session_guide(self, proto):
        """The HUMAN version of the demo script: a self-contained runbook a
        non-technical presenter can run a customer session from. Plain words,
        verbatim lines to send, what to expect, what to say."""
        a = proto["analysis"]
        caps = {c["key"]: c for c in a["capabilities"]}
        twin_url = (proto.get("twin") or {}).get("url")
        dep = proto.get("deploy") or {}

        def esc(t):
            return (str(t).replace("&", "&amp;").replace("<", "&lt;")
                    .replace(">", "&gt;"))

        steps = []
        for t in proto["demo_script"]:
            cap = caps.get(t.get("agent"))
            if cap:
                say = (f"This is the {esc(cap['name'])} capability: "
                       f"{esc(cap['description'])} The data on screen is "
                       "synthetic demo data - no customer data was needed to "
                       "build this.")
            elif t["turn"] == 1:
                say = ("This opening turn lets the agent introduce everything "
                       "it covers. Use it to set the agenda for the session.")
            else:
                say = ("This is a wrap-up beat - the agent summarizes what was "
                       "shown. Good moment to ask for feedback.")
            expect = ", ".join(t.get("expect") or []) or "a confident, on-topic reply"
            steps.append(
                f'<div class="step"><div class="step-n">Step {t["turn"]} of '
                f'{len(proto["demo_script"])}</div>'
                f'<div class="lbl">Press the Up arrow once - it types this line for you - then press Enter:</div>'
                f'<div class="line">{esc(t["user"])}</div>'
                f'<div class="lbl">What you should see in the reply:</div>'
                f'<div class="expect">It should mention: {esc(expect)}.</div>'
                f'<div class="lbl">What you can say while it answers:</div>'
                f'<div class="say">{say}</div></div>')

        cap_list = "".join(f"<li><strong>{esc(c['name'])}</strong> - "
                           f"{esc(c['description'])}</li>"
                           for c in a["capabilities"])
        outputs = ("<li><strong>Session guide</strong> (this document) - how to run the session.</li>"
                   "<li><strong>Demo script JSON</strong> - the same script in machine form, for the engineers.</li>"
                   "<li><strong>agent.py files</strong> - the working prototype agents themselves.</li>"
                   "<li><strong>Factory singleton agent.py</strong> - all of the above in ONE file; "
                   "this is the hand-off artifact the next team deploys.</li>")
        studio = ""
        if dep.get("status") == "deployed":
            kfiles = dep.get("knowledge_files") or []
            ksteps = ""
            if kfiles:
                ksteps = (
                    '<div class="step"><div class="step-n">Optional - attach the stubbed '
                    'knowledge sources</div><p>The agent\'s instructions already carry the '
                    'grounded library, so the demo runs immediately. For the full production '
                    'look, download the knowledge pack from the Outputs list ('
                    + ", ".join(f"<code>{esc(f)}</code>" for f in kfiles[:6])
                    + ') and in Copilot Studio open <strong>Knowledge &gt; Add knowledge &gt; '
                    'Files</strong>, then drag the whole pack in. Each file is one capability\'s '
                    'approved facts, records and exemplar reply - the same corpus the prototype '
                    'demos from.</p></div>')
            studio = (
                '<h2>Bonus: the same prototype in Copilot Studio</h2>'
                f'<p>This prototype was also deployed as a Microsoft Copilot Studio agent named '
                f'<strong>{esc(dep.get("agent_name") or proto["display_name"])}</strong> in '
                f'<code>{esc(dep.get("environment_url") or "")}</code>. '
                'Open <a href="https://copilotstudio.microsoft.com/">copilotstudio.microsoft.com</a>, '
                'find the agent, and run THIS SAME script in its test pane - the steps and expected '
                'replies are the same: every point answered from the grounded library, gaps flagged '
                'as needing a source, and a document you provide mid-conversation is used for the '
                'answers that follow. This is how the customer sees it inside Microsoft 365.</p>'
                + ksteps)
        open_line = (f'Open <code>{esc(twin_url)}/</code> in a browser.' if twin_url
                     else 'Open the rapplication HTML you were given in a browser.')
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(proto['display_name'])} - Demo Session Guide</title>
<style>
/* Microsoft-branded light tokens - same family as the rapplication shell */
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: #fff; color: #242424; line-height: 1.65; }}
.page {{ max-width: 760px; margin: 0 auto; padding: 44px 28px 80px; }}
h1 {{ font-size: 26px; margin-bottom: 4px; color: #242424; }}
.sub {{ color: #616161; font-size: 14px; margin-bottom: 26px; }}
h2 {{ font-size: 18px; color: #0F6CBD; margin: 30px 0 10px; }}
p, li {{ font-size: 14px; }}
ul, ol {{ padding-left: 22px; margin: 8px 0; }}
li {{ margin: 5px 0; }}
code {{ background: #EBF3FC; color: #0F6CBD; padding: 1px 7px; border-radius: 4px; font-size: 13px; }}
.step {{ border: 1px solid #d1d1d1; border-left: 4px solid #0F6CBD; border-radius: 8px; padding: 14px 18px; margin: 14px 0; page-break-inside: avoid; }}
.step-n {{ font-size: 11px; font-weight: 700; letter-spacing: 0.7px; text-transform: uppercase; color: #0F6CBD; margin-bottom: 8px; }}
.lbl {{ font-size: 11.5px; font-weight: 700; color: #616161; margin: 10px 0 3px; }}
.line {{ background: #EBF3FC; border-radius: 8px; padding: 10px 14px; font-size: 14.5px; font-weight: 600; }}
.expect {{ background: #DFF6DD; border-left: 3px solid #107C10; border-radius: 0 6px 6px 0; padding: 8px 12px; font-size: 13px; }}
.say {{ background: #f5f5f5; border-radius: 6px; padding: 8px 12px; font-size: 13px; color: #616161; }}
.callout {{ background: #FFF4CE; border: 1px solid #C19C00; border-radius: 8px; padding: 12px 16px; font-size: 13.5px; margin: 12px 0; }}
@media print {{ .page {{ padding: 0; }} }}
</style>
</head>
<body>
<div class="page">
<h1>{esc(proto['display_name'])} - Demo Session Guide</h1>
<div class="sub">Customer: {esc(proto['customer'])}. You do not need any technical background to run this session - every step tells you exactly what to press and what to say.</div>

<h2>What you are demoing</h2>
<p>{esc(a.get('summary') or '')}</p>
<ul>{cap_list}</ul>

<h2>Before the session - 60 seconds</h2>
<ol>
<li>{open_line}</li>
<li>The big panel on the left is the demo your customer sees. The chat on the right is YOUR control channel - the customer does not need to see it.</li>
<li>Click once inside the demo panel so your keyboard talks to it.</li>
<li>The small DEMO SCRIPT box in the corner of the demo is your teleprompter - it shows you each step. Press Esc to hide or show it.</li>
</ol>

<h2>Run the session - step by step</h2>
<p>Each step is the same two keys: <strong>Up arrow</strong> (types the line for you), then <strong>Enter</strong> (sends it). The replies come from the real prototype agents, live.</p>
{''.join(steps)}

<h2>If the customer asks something off the script</h2>
<p>Go ahead and type it - this is a live agent, not a recording. When you want to get back on script, press the Up arrow and it queues the next step again.</p>

<h2>If something needs to change during or after the session</h2>
<div class="callout">Use the Prototyping chat on the right side of the page. Say what you want in plain language - for example: "change step 2 to be about refunds", "add a step about invoices", "rebuild and run the tests". The demo updates in place while you watch. You never need to edit a file.</div>

<h2>What the customer walks away with</h2>
<ul>{outputs}</ul>
<p>All of these are download buttons at the bottom right of the rapplication page.</p>
{studio}
<p style="margin-top:34px;color:#9a9aa3;font-size:11.5px">Generated by Transcript2Prototype from the cubby '{esc(proto['slug'])}'. All example data shown in the demo is synthetic.</p>
</div>
</body>
</html>
"""

    def _downloads(self, cubby, proto):
        """The take-with-you outputs embedded in the rapplication: the session
        guide (the human-runnable script), the demo script JSON (for the
        engineers), every generated agent.py, and the factory singleton."""
        items = []

        def add(name, text):
            items.append({"name": name,
                          "b64": base64.b64encode(text.encode("utf-8")).decode("ascii")})

        add(f"{proto['slug']}_session_guide.html",
            self._render_session_guide(proto))
        add(f"{proto['slug']}_demo_script.json",
            json.dumps(proto["demo_script"], indent=2, ensure_ascii=False))
        for rec in proto.get("agents_built") or []:
            p = os.path.join(cubby, "agents", rec["file"])
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as f:
                    add(rec["file"], f.read())
        exp = proto.get("export") or {}
        if exp.get("path") and os.path.isfile(exp["path"]):
            with open(exp["path"], encoding="utf-8") as f:
                add(exp["file"], f.read())
        mcp = proto.get("mcp_app") or {}
        if mcp.get("path") and os.path.isfile(mcp["path"]):
            with open(mcp["path"], encoding="utf-8") as f:
                add(mcp["file"], f.read())
        dec = proto.get("declarative") or {}
        if dec.get("path") and os.path.isfile(dec["path"]):
            with open(dec["path"], "rb") as f:
                items.append({"name": dec["file"],
                              "b64": base64.b64encode(f.read()).decode("ascii")})
        hu = proto.get("hpa_update") or {}
        for fn in hu.get("files") or []:
            p = os.path.join(hu.get("dir") or "", fn)
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as f:
                    add("hpa_update_" + fn, f.read())
        # the stubbed Copilot Studio knowledge pack (one file per capability)
        kdir = os.path.join(cubby, "exports", "knowledge")
        for fn in (proto.get("deploy") or {}).get("knowledge_files") or []:
            p = os.path.join(kdir, fn)
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as f:
                    add(fn, f.read())
        return items

    def _shell_brainstem_url(self, proto):
        # These markers only exist on a real Azure host - WEBSITE_INSTANCE_ID
        # on classic plans, WEBSITE_POD_NAME / LEGION_SERVICE_HOST on Flex
        # Consumption (which never sets WEBSITE_INSTANCE_ID). func start
        # spoofs WEBSITE_HOSTNAME but none of these. There a localhost
        # brainstem is unreachable from the visitor's browser, so the
        # feedback chat is routed to the host's same-origin /chat adapter.
        url = proto.get("brainstem_url") or ""
        on_azure = any(os.environ.get(k) for k in (
            "WEBSITE_INSTANCE_ID", "WEBSITE_POD_NAME", "LEGION_SERVICE_HOST"))
        if on_azure and (not url or "localhost" in url or "127.0.0.1" in url):
            return "/api/t2p/chat"
        return url or "http://localhost:7071/chat"

    def _shell_perform_url(self, proto):
        # Settings-grade operations (credentials, .egg backups) must NOT ride
        # through chat - secrets do not belong in an LLM conversation and the
        # result must be deterministic. The static transport lives NEXT TO
        # the chat endpoint on the PROTOTYPING brainstem (which hosts this
        # agent) - never on the twin, whose registry only carries the
        # prototype's generated agents. .../chat -> .../perform.
        url = self._shell_brainstem_url(proto)
        if url.endswith("/chat"):
            return url[:-len("/chat")] + "/perform"
        return "/perform"

    def _render_shell(self, cubby, proto, demo_html, mode):
        bytecode = base64.b64encode(demo_html.encode("utf-8")).decode("ascii")
        # cubby sits at <home>/.brainstem/cubbies/<slug> - derive home so the
        # credentials status reflects the same file the deploy stage reads.
        home = os.path.dirname(os.path.dirname(os.path.dirname(cubby)))
        saved = self._creds_extract(
            _read_json(os.path.join(home, ".rapp_deploy_settings.json")))
        creds_status = (
            f"Saved: {saved['DYNAMICS_365_RESOURCE']} "
            f"(client {saved['DYNAMICS_365_CLIENT_ID'][:8]}...)" if saved
            else "None saved - load your local.settings.json to enable autonomous deploys")
        stage = proto["stage"]
        dep = proto.get("deploy") or {}
        deployed = dep.get("status") == "deployed"
        order = ["demo", "built", "local_passed", "twin_passed", "exported"]
        # export (the gate) and the Copilot Studio deploy are ONE user step -
        # deploy runs the gated export itself, so they share one chip
        labels = {"demo": "1 Demo script", "built": "2 Agents built",
                  "local_passed": "3 Local twin run", "twin_passed": "4 Live twin run",
                  "exported": ("5 Copilot Studio (gate) - deployed" if deployed
                               else "5 Copilot Studio (gated export + deploy)")}
        idx = order.index(stage) if stage in order else 0
        chips = []
        for i, key in enumerate(order):
            cls = "stage"
            if i < idx or (i == idx and key == "exported" and deployed):
                cls += " done"
            elif i == idx:
                cls += " current"  # exported-but-not-deployed stays current
            if key == "exported":
                cls += " gate"
            chips.append(f'<span class="{cls}">{labels[key]}</span>')
        # which guided-step button to highlight for run-by-buttons users
        next_step = {"demo": "build", "built": "test_local",
                     "local_passed": "test_twin", "twin_passed": "deploy",
                     "exported": "deploy"}.get(stage, "build")
        cap_names = [c.get("name") for c in proto["analysis"]["capabilities"]]
        if stage in ("demo", "built") and cap_names == ["Getting Started"]:
            next_step = "start"  # a starter waits for its transcript/template
        if deployed:
            next_step = ""  # pipeline complete - nothing to push
        mode_badge = {"scripted": "SCRIPTED BYTECODE",
                      "live": "LIVE BYTECODE - TWIN",
                      "mcp": "MCP BYTECODE - APP PREVIEW"}.get(
                          mode, "BYTECODE")
        return (SHELL_TEMPLATE
                .replace("__TITLE__", f"{proto['display_name']} - Transcript2Prototype")
                .replace("__SUBTITLE__",
                         f"{proto['customer']} | cubby: {proto['slug']}")
                .replace("__MODE_BADGE__", mode_badge)
                .replace("__STAGES_HTML__", "".join(chips))
                .replace("__SLUG__", proto["slug"])
                .replace("__BRAINSTEM_URL__", self._shell_brainstem_url(proto))
                .replace("__PERFORM_URL__", self._shell_perform_url(proto))
                .replace("__CREDS_STATUS__", creds_status)
                .replace("__NEXT_STEP__", next_step)
                .replace("__TEMPLATES_URL__",
                         ((proto.get("template") or {}).get("source")
                          or TEMPLATES_SOURCE_DEFAULT).rstrip("/")
                         + "/manifest.json")
                .replace("__SHELL_TEST_REPLAY__",
                         json.dumps(proto.get("last_test_replay"),
                                    ensure_ascii=False))
                .replace("__ACTIVITY_JSON__",
                         json.dumps(proto.get("activity") or [],
                                    ensure_ascii=False))
                .replace("__JOURNAL_JSON__",
                         json.dumps((proto.get("journal") or [])[-200:],
                                    ensure_ascii=False))
                .replace("__DOWNLOADS_JSON__",
                         json.dumps(self._downloads(cubby, proto), ensure_ascii=False))
                .replace("__BYTECODE__", bytecode))

    def _regen_html(self, cubby, proto, mode, api_url=""):
        demo_html = self._render_demo_page(proto, mode, api_url)
        shell_html = self._render_shell(cubby, proto, demo_html, mode)
        rapps = os.path.join(cubby, "rapplications")
        demo_path = os.path.join(rapps, f"{proto['slug']}_demo.html")
        shell_path = os.path.join(rapps, f"{proto['slug']}_rapplication.html")
        guide_path = os.path.join(rapps, f"{proto['slug']}_session_guide.html")
        _write_text(demo_path, demo_html)
        _write_text(shell_path, shell_html)
        _write_text(guide_path, self._render_session_guide(proto))
        proto["html"] = {"demo": demo_path, "shell": shell_path,
                         "mode": mode, "api_url": api_url,
                         "bytecode_sha256": _sha256_text(demo_html)}
        # the twin serves the rapplication at its root - keep it current so
        # the feedback chat's auto-refresh always sees the latest bytecode,
        # stage chips and downloadable outputs.
        twin_dir = (proto.get("twin") or {}).get("dir")
        if twin_dir and os.path.isdir(twin_dir):
            _write_text(os.path.join(twin_dir, "index.html"), shell_html)
            proto["html"]["twin_index"] = os.path.join(twin_dir, "index.html")
        return {"demo": demo_path, "shell": shell_path}

    # ---- browse ------------------------------------------------------------
    def _list(self, kwargs):
        root = self._cubby_root(kwargs)
        focus = (_read_json(self._focus_file(kwargs)) or {}).get("cubby")
        out = []
        if os.path.isdir(root):
            for slug in sorted(os.listdir(root)):
                proto = _read_json(os.path.join(root, slug, "prototype.json"))
                if not proto:
                    continue
                out.append({"cubby": slug, "display_name": proto.get("display_name"),
                            "customer": proto.get("customer"),
                            "stage": proto.get("stage"),
                            "gated": bool((proto.get("gate") or {}).get("stopped")),
                            "demo_turns": len(proto.get("demo_script") or []),
                            "agents_built": len(proto.get("agents_built") or []),
                            "focused": slug == focus})
        return self._env("list", "success", root=root, prototypes=out,
                         count=len(out), focused=focus)

    def _search(self, kwargs):
        q = (kwargs.get("query") or "").strip().lower()
        if not q:
            return self._env("search", "error", error="pass query=<term>")
        root = self._cubby_root(kwargs)
        hits = []
        if os.path.isdir(root):
            for slug in sorted(os.listdir(root)):
                cubby = os.path.join(root, slug)
                proto = _read_json(os.path.join(cubby, "prototype.json"))
                if not proto:
                    continue
                for path in sorted(glob.glob(os.path.join(cubby, "**", "*"),
                                             recursive=True)):
                    if not os.path.isfile(path) or os.path.basename(path).startswith("."):
                        continue
                    rel = os.path.relpath(path, cubby)
                    matched_on = None
                    if q in rel.lower() or q in slug.lower():
                        matched_on = "name"
                    elif (os.path.getsize(path) <= 1024 * 1024
                          and os.path.splitext(path)[1] in
                          (".py", ".json", ".txt", ".md", ".html")):
                        try:
                            with open(path, encoding="utf-8", errors="ignore") as f:
                                if q in f.read().lower():
                                    matched_on = "content"
                        except OSError:
                            pass
                    if matched_on:
                        hits.append({"cubby": slug, "stage": proto.get("stage"),
                                     "path": rel, "matched_on": matched_on})
        by_cubby = {}
        for h in hits:
            by_cubby.setdefault(h["cubby"], 0)
            by_cubby[h["cubby"]] += 1
        return self._env("search", "success", query=q, matches=len(hits),
                         by_cubby=by_cubby, results=hits[:40],
                         hint="action=focus cubby=<slug> to work on one.")

    def _focus(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        _write_json(self._focus_file(kwargs), {"cubby": slug, "at": _now()})
        return self._env("focus", "success", cubby=slug, stage=proto.get("stage"),
                         display_name=proto.get("display_name"),
                         note="prototype in focus - status / adjust / build / test / export now target it.")

    def _status(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        gate = proto.get("gate") or {}
        return self._env(
            "status", "success", cubby=slug, path=cubby,
            display_name=proto.get("display_name"), customer=proto.get("customer"),
            stage=proto.get("stage"), stages_done=proto.get("stages_done"),
            analysis_source=proto.get("analysis_source"),
            demo_turns=len(proto.get("demo_script") or []),
            capabilities=[c["name"] for c in proto["analysis"]["capabilities"]],
            agents_built=proto.get("agents_built"),
            tests={k: {kk: v.get(kk) for kk in ("passed", "pass_rate", "at", "target")}
                   for k, v in (proto.get("tests") or {}).items()},
            export=proto.get("export"),
            gated=bool(gate.get("stopped")), gate_note=gate.get("note"),
            html=proto.get("html"),
            twin={**proto["twin"], "running": bool(self._twin_health(proto))}
            if proto.get("twin") else None,
            next=self._next_hint(proto))

    def _next_hint(self, proto):
        stage = proto.get("stage")
        if (proto.get("gate") or {}).get("stopped"):
            return ("GATE: exported and stopped. The factory singleton is the handoff "
                    "for the next stage of the process.")
        return {
            "demo": "review the demo in the rapplication iframe; adjust turns, then action=build",
            "built": "action=test target=local (replay the demo against the generated agents)",
            "local_passed": "action=test target=twin (inject into the live twin and replay over HTTP)",
            "twin_passed": "action=export (bundle the factory singleton - the gate)",
            "exported": "gate reached - pipeline stopped",
        }.get(stage, "action=status")

    def _show_demo(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        return self._env("show_demo", "success", cubby=slug,
                         mode=(proto.get("html") or {}).get("mode"),
                         demo_script=proto["demo_script"])

    def _open(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        html = proto.get("html") or {}
        return self._env("open", "success", cubby=slug,
                         rapplication=html.get("shell"), demo_page=html.get("demo"),
                         mode=html.get("mode"),
                         note="open the rapplication path in a browser; the demo plays in the iframe.")

    # ---- adjust ------------------------------------------------------------
    def _adjust(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        reopened = False
        if (proto.get("gate") or {}).get("stopped"):
            # the feedback loop outranks the gate: adjusting an exported
            # prototype reopens it - re-run tests and export to gate again.
            proto["gate"] = {"stopped": False, "reopened_at": _now(),
                             "note": ("gate reopened by adjust - the previous factory "
                                      "export still exists; rebuild, re-test and "
                                      "re-export to gate again.")}
            proto["stage"] = "built" if proto.get("agents_built") else "demo"
            reopened = True
        script = proto["demo_script"]
        changed = []

        instruction = (kwargs.get("instruction") or "").strip()
        if instruction and not kwargs.get("user") and not kwargs.get("assistant") \
                and not kwargs.get("remove") and not kwargs.get("add"):
            # the agent does not interpret free text - the CALLER is the
            # intelligence. Hand back the script and the exact follow-up calls.
            return self._env(
                "adjust", "needs_structured", cubby=slug,
                instruction=instruction,
                demo_script=proto["demo_script"],
                note=("CALLER: apply the instruction yourself - the current demo "
                      "script is included above. Decide the new wording and call "
                      "this agent again with the structured form: adjust turn=N "
                      "user=... assistant=... expect=a,b (or remove=true, or "
                      "add=true user=... assistant=...). One call per turn you "
                      "change."))
        elif kwargs.get("add"):
            n = len(script) + 1
            script.append({
                "turn": n, "agent": None,
                "user": kwargs.get("user") or f"Demo step {n}",
                "assistant": kwargs.get("assistant") or "(scripted response)",
                "expect": [w.strip() for w in (kwargs.get("expect") or "").split(",") if w.strip()],
            })
            changed.append(f"added turn {n}")
        else:
            turn_no = kwargs.get("turn")
            if not turn_no:
                return self._env("adjust", "error",
                                 error="pass turn=N (1-based) with user=/assistant=/expect=/remove=, "
                                       "add=true for a new turn, or instruction=... for an LLM rewrite.")
            turn_no = int(turn_no)
            if turn_no < 1 or turn_no > len(script):
                return self._env("adjust", "error",
                                 error=f"turn {turn_no} out of range 1..{len(script)}")
            if kwargs.get("remove"):
                script.pop(turn_no - 1)
                for i, t in enumerate(script):
                    t["turn"] = i + 1
                changed.append(f"removed turn {turn_no}")
            else:
                t = script[turn_no - 1]
                if kwargs.get("user"):
                    t["user"] = kwargs["user"]
                    changed.append(f"turn {turn_no} user")
                if kwargs.get("assistant"):
                    t["assistant"] = kwargs["assistant"]
                    changed.append(f"turn {turn_no} assistant")
                if kwargs.get("expect"):
                    t["expect"] = [w.strip() for w in kwargs["expect"].split(",") if w.strip()]
                    changed.append(f"turn {turn_no} expect")
                if not changed:
                    return self._env("adjust", "error",
                                     error="nothing to change - pass user=, assistant=, expect= or remove=true.")

        # downstream invalidation: demo changed -> prior test runs are stale
        stale = bool(proto.get("tests"))
        proto["tests"] = {}
        if proto["stage"] in ("local_passed", "twin_passed"):
            proto["stage"] = "built" if proto.get("agents_built") else "demo"
        html = proto.get("html") or {}
        paths = self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                                 api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env("adjust", "success", cubby=slug, changed=changed,
                         demo_turns=len(proto["demo_script"]),
                         tests_invalidated=stale, stage=proto["stage"],
                         gate_reopened=reopened,
                         rapplication=paths["shell"],
                         note=("bytecode regenerated - the iframe now plays the updated "
                               "script." + (" The export gate was REOPENED by this "
                                            "adjust; rebuild, re-test and re-export to "
                                            "gate again." if reopened else "")))

    # ---- egg backup: export/import the whole prototype (+ twin memory) ------
    def _egg(self, kwargs):
        """Back a prototype up as a portable .egg (standard cubby-egg layout,
        so RappAgent can hatch it too) including the twin's memory and soul;
        reimport it - optionally under a new name - for a different use case."""
        op = (kwargs.get("op") or "export").lower()
        if op == "export":
            slug, cubby, proto, err = self._resolve(kwargs)
            if err:
                return err
            import io as _io
            buf = _io.BytesIO()
            files = 0
            twin_dir = (proto.get("twin") or {}).get("dir") \
                or self._twin_dir(kwargs, slug)
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                z.writestr("manifest.json", json.dumps({
                    "schema": "brainstem-egg/2.3-cubby", "type": "cubby",
                    "version": "1.0", "slug": slug,
                    "cubby_schema": CUBBY_SCHEMA, "minted_at": _now(),
                    "anatomy": list(CUBBY_ANATOMY),
                    "t2p": {"schema": PROTO_SCHEMA, "slug": slug,
                            "display_name": proto.get("display_name"),
                            "customer": proto.get("customer"),
                            "stage": proto.get("stage"),
                            "has_twin_state": os.path.isdir(
                                os.path.join(twin_dir, ".brainstem_data"))},
                    "organism": "A Transcript2Prototype prototype - hatch with "
                                "Transcript2Prototype action=egg op=import "
                                "(or RappAgent cubby_import for the cubby part)."},
                    indent=2))
                z.writestr("HATCH.md",
                           f"# Prototype egg: {slug}\n\nReload it into the "
                           "rapplication with Transcript2Prototype action=egg "
                           "op=import path=<this file> [name=<new slug>], then "
                           "twin op=up. The twin/ section restores the twin's "
                           "memory and soul.\n")
                for dp, _dirs, fns in os.walk(cubby):
                    if "__pycache__" in dp:
                        continue
                    for fn in fns:
                        ap = os.path.join(dp, fn)
                        z.write(ap, "cubby/" + os.path.relpath(ap, cubby))
                        files += 1
                # twin state: memory + soul travel with the prototype
                for rel_root in (".brainstem_data", ):
                    troot = os.path.join(twin_dir, rel_root)
                    if os.path.isdir(troot):
                        for dp, _dirs, fns in os.walk(troot):
                            for fn in fns:
                                ap = os.path.join(dp, fn)
                                z.write(ap, "twin/" + os.path.relpath(ap, twin_dir))
                                files += 1
                soul = os.path.join(twin_dir, "soul.md")
                if os.path.isfile(soul):
                    z.write(soul, "twin/soul.md")
                    files += 1
            blob = buf.getvalue()
            stamp = _now()[:10]
            dest = os.path.expanduser(
                kwargs.get("path")
                or os.path.join(self._home(kwargs), "Desktop",
                                f"t2p-{slug}-{stamp}.egg"))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as f:
                f.write(blob)
            extra = {}
            if str(kwargs.get("return_b64", "")).lower() in ("true", "1", "yes"):
                # for the rapplication's static export button: the bytes ride
                # back in the response so the browser saves the file itself.
                extra = {"egg_b64": base64.b64encode(blob).decode("ascii"),
                         "egg_name": os.path.basename(dest)}
            return self._env("egg", "success", op="export", cubby=slug,
                             egg=dest, files=files, size_bytes=len(blob),
                             sha256=hashlib.sha256(blob).hexdigest(),
                             note="portable backup - reload anywhere with egg "
                                  "op=import path=... (optionally name=<new slug> "
                                  "for a different use case).", **extra)

        if op != "import":
            return self._env("egg", "error", error="op must be export | import")

        src_path = os.path.expanduser(kwargs.get("path") or "")
        if not src_path and kwargs.get("egg_b64"):
            # static import: the browser uploads the .egg bytes directly
            try:
                blob = base64.b64decode(kwargs["egg_b64"])
            except (ValueError, TypeError):
                return self._env("egg", "error", error="egg_b64 is not valid base64")
            tmp = tempfile.NamedTemporaryFile(suffix=".egg", delete=False)
            tmp.write(blob)
            tmp.close()
            src_path = tmp.name
        if not src_path or not os.path.isfile(src_path):
            return self._env("egg", "error",
                             error="pass path=<the .egg file to import> "
                                   "or egg_b64=<its base64 bytes>")
        try:
            z = zipfile.ZipFile(src_path)
        except zipfile.BadZipFile:
            return self._env("egg", "error", error="not a valid .egg (zip)")
        try:
            mani = json.loads(z.read("manifest.json"))
        except (KeyError, ValueError):
            mani = {}
        orig = (mani.get("t2p") or {}).get("slug") or mani.get("slug") or "imported"
        slug = _slugify(kwargs.get("name") or orig)
        root = self._cubby_root(kwargs)
        cubby = os.path.join(root, slug)
        if os.path.isdir(cubby) and os.listdir(cubby) and not kwargs.get("force"):
            return self._env("egg", "already_exists", cubby=slug,
                             note="a cubby with that name exists - pass force=true "
                                  "to overwrite, or name=<different slug>.")
        twin_dir = self._twin_dir(kwargs, slug)
        landed = twin_files = 0
        skipped = []
        for n in z.namelist():
            if n.endswith("/"):
                continue
            base = os.path.basename(n)
            if re.search(r"(secret|token|credential|password|\.env$|\.pem$|\.key$)",
                         base, re.IGNORECASE):
                skipped.append(n)
                continue
            if n.startswith("cubby/"):
                target_root, rel = cubby, n[len("cubby/"):]
            elif n.startswith("twin/"):
                target_root, rel = twin_dir, n[len("twin/"):]
            else:
                continue
            target = os.path.normpath(os.path.join(target_root, rel))
            if not target.startswith(os.path.normpath(target_root) + os.sep):
                skipped.append(n)
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "wb") as f:
                f.write(z.read(n))
            if n.startswith("twin/"):
                twin_files += 1
            else:
                landed += 1
        proto = _read_json(os.path.join(cubby, "prototype.json"))
        if not proto:
            return self._env("egg", "error", cubby=slug,
                             error="egg unpacked but no prototype.json inside - "
                                   "was this a t2p prototype egg?")
        # fix machine/slug-specific state: paths re-anchor to the new cubby,
        # live surfaces (twin, html mode, pids) reset for re-provisioning.
        proto["slug"] = slug
        exp = proto.get("export") or {}
        if exp.get("file"):
            np = os.path.join(cubby, "exports", exp["file"])
            proto["export"] = {**exp, "path": np} if os.path.isfile(np) else None
        mcp = proto.get("mcp_app") or {}
        if mcp.get("file"):
            np = os.path.join(cubby, "exports", mcp["file"])
            if os.path.isfile(np):
                mcp.update({"path": np, "pid": None})
                proto["mcp_app"] = mcp
            else:
                proto["mcp_app"] = None
        for t, rec in (proto.get("tests") or {}).items():
            if rec.get("report"):
                rec["report"] = os.path.join(cubby, "show-and-tell",
                                             os.path.basename(rec["report"]))
        proto["twin"] = None
        self._regen_html(cubby, proto, mode="scripted")
        self._save(cubby, proto)
        _write_json(self._focus_file(kwargs), {"cubby": slug, "at": _now()})
        return self._env(
            "egg", "success", op="import", cubby=slug, renamed=slug != orig,
            original=orig, stage=proto.get("stage"), files=landed,
            twin_state_restored=twin_files, skipped_secret_shaped=skipped,
            rapplication=proto["html"]["shell"],
            note=("prototype reloaded" + (f" as '{slug}'" if slug != orig else "")
                  + " - twin op=up serves it (its memory and soul came along); "
                    "the pipeline state, demo and agents are exactly as exported."))

    # ---- new prototype: hatch another rapplication twin (or reset here) -----
    def _new_prototype(self, kwargs):
        """One call = a fresh starter prototype with its OWN twin serving its
        own rapplication - so prototypes run side by side. With name=+force=
        it resets an existing prototype in place (same cubby, same page)."""
        root = self._cubby_root(kwargs)
        name = _slugify(kwargs.get("name") or "") if kwargs.get("name") else ""
        force = bool(kwargs.get("force"))
        if not name:
            i = 1
            while os.path.isdir(os.path.join(root, f"prototype-{i}")):
                i += 1
            name = f"prototype-{i}"
        if force and os.path.isdir(os.path.join(root, name)):
            # stop the old twin first so the same port frees up for the reset
            try:
                self._twin({**({"_home_dir": kwargs["_home_dir"]}
                               if "_home_dir" in kwargs else {}),
                            "cubby": name, "op": "down"})
            except Exception:  # noqa: BLE001
                pass
            # a RESET means a fresh twin too: wipe its memory so the old
            # prototype's conversations and capabilities cannot leak into the
            # fresh one (Snapshot-then-reset is the keep-my-state path - the
            # .egg carries .brainstem_data)
            shutil.rmtree(os.path.join(self._twin_dir(kwargs, name),
                                       ".brainstem_data"),
                          ignore_errors=True)
        customer = (kwargs.get("customer_name") or "New Customer").strip()
        seed_caps = [{
            "name": "Getting Started",
            "description": ("Starter capability - attach a transcript or pick a "
                            "template from the dropdown and the real capabilities "
                            "replace this one."),
            "triggers": ["start", "transcript", "template", "prototype"],
            "knowledge": ["This is a fresh prototype waiting for its first input."],
            "response": ("This **prototype** is a fresh start. Attach a "
                         "**transcript** with the step bar button, or pick a "
                         "**template** from the dropdown - either one replaces "
                         "this starter and the pipeline takes it from there. "
                         "Say 'start' in the chat any time for the next step."),
            "demo_user": "How do I get started?",
            "synthetic_records": [
                {"step": "1", "action": "Attach a transcript or pick a template",
                 "where": "the step bar above the chat"},
                {"step": "2", "action": "Build, test, export, deploy",
                 "where": "the numbered buttons - the next one is highlighted"}],
        }]
        transcript = (f"Starter prototype.\nCustomer: {customer}\n\n"
                      "We need a working agent prototype. Attach a discovery "
                      "transcript or pick an agent stack template to shape it - "
                      "the pipeline regenerates everything from that input.")
        start_kwargs = {
            "transcript": transcript, "name": name, "customer_name": customer,
            "agent_name": kwargs.get("agent_name") or "New Prototype",
            "capabilities": json.dumps(seed_caps, ensure_ascii=False),
            "force": force, "brainstem_url": kwargs.get("brainstem_url"),
        }
        if "_home_dir" in kwargs:
            start_kwargs["_home_dir"] = kwargs["_home_dir"]
        started = json.loads(self._start(start_kwargs))
        if started.get("status") == "already_exists":
            return self._env("new_prototype", "already_exists", cubby=name,
                             note="that prototype already exists - pass force=true "
                                  "to reset it in place, or omit name= to hatch a "
                                  "fresh prototype-N alongside it.")
        if started.get("status") != "success":
            return self._env("new_prototype", started.get("status", "error"),
                             start=started)
        if kwargs.get("serve", True):
            up_kwargs = {k: kwargs[k] for k in
                         ("_home_dir", "twin_source") if k in kwargs}
            # the twin needs at least the starter agent to serve
            built = json.loads(self._build({**up_kwargs, "cubby": name}))
            if built.get("status") != "success":
                return self._env("new_prototype", "partial", cubby=name,
                                 rapplication=started.get("rapplication"),
                                 build=built,
                                 note="prototype created but the starter build failed.")
            up = json.loads(self._twin({**up_kwargs, "cubby": name, "op": "up"}))
            if up.get("status") == "success":
                return self._env(
                    "new_prototype", "success", cubby=name, url=up.get("url"),
                    rapplication=up.get("rapplication"),
                    reset=force,
                    note=(("reset in place - the open page refreshes itself."
                           if force else
                           f"fresh prototype hatched on its own twin - open "
                           f"{up.get('url')} to run it side by side with the "
                           "others.")
                          + " Attach a transcript or pick a template to shape it."))
            return self._env("new_prototype", "partial", cubby=name,
                             rapplication=started.get("rapplication"), twin=up,
                             note="prototype created but its twin did not start - "
                                  "twin op=up to retry, or open the rapplication "
                                  "file directly.")
        return self._env("new_prototype", "success", cubby=name, served=False,
                         rapplication=started.get("rapplication"), reset=force,
                         note="starter prototype created (twin not started).")

    # ---- template library: agent stacks as one-click pipeline inputs --------
    def _templates_fetch(self, source, rel):
        """Read manifest/metadata from the library - a raw-GitHub base URL or
        a local directory (tests / offline mirrors). None on any miss."""
        if source.startswith(("http://", "https://")):
            try:
                with urllib.request.urlopen(source.rstrip("/") + "/" + rel,
                                            timeout=25) as r:
                    return r.read().decode("utf-8", "replace")
            except Exception:  # noqa: BLE001
                return None
        path = os.path.join(os.path.expanduser(source), rel)
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                return f.read()
        return None

    def _stack_to_inputs(self, stack, meta, customer):
        """Derive prototype inputs (agent name, capabilities, pseudo-transcript)
        from a stack's metadata.json - deterministic floor; callers can still
        pass capabilities= to override."""
        stack_name = meta.get("name") or stack.get("name") or stack.get("id")
        desc = meta.get("description") or ""
        features = [str(f) for f in (meta.get("features") or [])][:5]
        use_cases = [str(u) for u in (meta.get("useCases") or [])]
        benefits = [str(b) for b in (meta.get("benefits") or [])]
        integrations = [str(i) for i in ((meta.get("technicalRequirements") or {})
                                         .get("integrations") or [])]
        base = re.sub(r"\s*Agent\s*Stack$|\s*Stack$", "", stack_name).strip() or stack_name
        agent_name = f"{base} Assistant"
        caps = []
        for i, feat in enumerate(features or [base]):
            triggers = (_words(feat) + _words(" ".join(integrations)))[:5] or [_slugify(feat)]
            knowledge = ([desc] if desc else []) + benefits[:2]
            response = (f"I handle **{feat.lower()}** for {customer}: {desc} "
                        f"Key elements: {', '.join(triggers)}."
                        + (f" Wired for {', '.join(integrations[:3])}." if integrations else ""))
            demo_user = (use_cases[i] + " - show me." if i < len(use_cases)
                         else f"Show me {feat.lower()} in action.")
            caps.append({"name": feat[:60], "description": f"{feat} - from the {stack_name} template. {desc}"[:280],
                         "triggers": triggers, "knowledge": knowledge,
                         "response": response, "demo_user": demo_user})
        transcript = (f"Template intake - {stack_name}\nCustomer: {customer}\n\n"
                      f"{desc}\n\nWhat the customer needs:\n"
                      + "\n".join(f"- {f}" for f in features)
                      + "\n\nWhy it matters:\n"
                      + "\n".join(f"- {b}" for b in benefits)
                      + (f"\n\nIntegrations in play: {', '.join(integrations)}." if integrations else ""))
        return agent_name, caps, transcript

    def _template(self, kwargs):
        source = kwargs.get("templates_source") or TEMPLATES_SOURCE_DEFAULT
        op = (kwargs.get("op") or
              ("use" if kwargs.get("template_id") else "search")).lower()
        text = self._templates_fetch(source, "manifest.json")
        if text is None:
            return self._env("template", "needs_network",
                             source=source,
                             error="could not reach the template library manifest - "
                                   "check the network or pass templates_source=<base "
                                   "url or local dir of an AI-Agent-Templates mirror>.")
        try:
            manifest = json.loads(text)
        except ValueError as e:
            return self._env("template", "error", error=f"manifest unreadable: {e}")
        stacks = manifest.get("stacks") or []

        if op == "search":
            q = (kwargs.get("query") or "").strip().lower()
            hits = [s for s in stacks
                    if not q or q in json.dumps(s).lower()]
            view = [{"id": s.get("id"), "name": s.get("name"),
                     "industry": s.get("industry")} for s in hits[:30]]
            return self._env(
                "template", "success", op="search", source=source,
                query=q or None, matches=len(hits), stacks=view,
                note=("pick one: action=template op=use template_id=<id> starts a "
                      "prototype from it (feedback then adjusts it in real time); "
                      "op=oneclick template_id=<id> runs the WHOLE journey - "
                      "prototype, build, tests, export and autonomous Copilot "
                      "Studio deploy."))

        tid = (kwargs.get("template_id") or kwargs.get("query") or "").strip().lower()
        if not tid:
            return self._env("template", "error",
                             error="pass template_id=<stack id> (action=template "
                                   "op=search lists them).")
        stack = (next((s for s in stacks if (s.get("id") or "").lower() == tid), None)
                 or next((s for s in stacks
                          if tid in (s.get("name") or "").lower()
                          or tid in (s.get("id") or "").lower()), None))
        if stack is None:
            close = [s.get("id") for s in stacks
                     if any(w in json.dumps(s).lower() for w in tid.split())][:8]
            return self._env("template", "error",
                             error=f"no stack matching {tid!r}",
                             close_matches=close)
        meta_text = self._templates_fetch(source, stack.get("path", "") + "/metadata.json")
        meta = {}
        if meta_text:
            try:
                meta = json.loads(meta_text)
            except ValueError:
                meta = {}
        customer = (kwargs.get("customer_name") or "the customer").strip()
        agent_name, caps, transcript = self._stack_to_inputs(stack, meta, customer)
        slug = _slugify(kwargs.get("name") or stack.get("id") or tid)
        carried_sources = None
        if str(kwargs.get("merge", "")).lower() in ("true", "1", "yes"):
            # merge=true folds the template INTO an existing prototype (a
            # transcript- or HPA-started one) instead of replacing it: the
            # capability sets union (existing first, dedup by name), the
            # transcripts concatenate, and identity + lineage survive - so a
            # transcript, an HPA and an industry template compose into ONE
            # first stab, in any order.
            target = (_slugify(kwargs.get("name") or "")
                      or (_read_json(self._focus_file(kwargs)) or {}).get("cubby"))
            existing = _read_json(os.path.join(
                self._cubby_root(kwargs), target or "", "prototype.json")) if target else None
            if existing:
                slug = target
                ex_caps = [c for c in existing["analysis"]["capabilities"]
                           if c.get("name") != "Getting Started"]
                have = {c["name"] for c in ex_caps}
                caps = ex_caps + [c for c in caps if c["name"] not in have]
                txp = os.path.join(self._cubby_root(kwargs), slug, "transcript.txt")
                if os.path.isfile(txp):
                    ex_tx = open(txp, encoding="utf-8").read()
                    if ex_tx.strip() and not ex_tx.startswith("Starter prototype."):
                        transcript = (ex_tx + "\n\n--- merged input: template "
                                      + str(stack.get("id")) + " ---\n\n" + transcript)
                if existing.get("display_name") not in (None, "", "New Prototype"):
                    agent_name = existing["display_name"]
                if (existing.get("customer") or "") not in ("", "the customer",
                                                            "New Customer"):
                    customer = existing["customer"]
                carried_sources = existing.get("sources") or None
                kwargs = {**kwargs, "force": True}
        start_kwargs = {
            "transcript": transcript, "name": slug, "customer_name": customer,
            "agent_name": kwargs.get("agent_name") or agent_name,
            "capabilities": kwargs.get("capabilities") or json.dumps(caps, ensure_ascii=False),
            "force": kwargs.get("force"),
            "brainstem_url": kwargs.get("brainstem_url"),
        }
        if carried_sources and carried_sources.get("hpa"):
            start_kwargs["hpa_source"] = carried_sources["hpa"]
        if "_home_dir" in kwargs:
            start_kwargs["_home_dir"] = kwargs["_home_dir"]
        started = json.loads(self._start(start_kwargs))
        if started.get("status") == "already_exists" and op == "oneclick":
            pass  # continue the journey on the existing prototype
        elif started.get("status") not in ("success",):
            return self._env("template", started.get("status", "error"), op=op,
                             template=stack.get("id"), start=started)
        # provenance on the prototype
        cubby = os.path.join(self._cubby_root(kwargs), slug)
        proto = _read_json(os.path.join(cubby, "prototype.json"))
        if proto is not None:
            proto["template"] = {"id": stack.get("id"), "name": stack.get("name"),
                                 "industry": stack.get("industry"),
                                 "source": source, "path": stack.get("path"),
                                 "used_at": _now()}
            self._save(cubby, proto)
        if op == "use":
            return self._env(
                "template", "success", op="use", template=stack.get("id"),
                cubby=slug, capabilities=[c["name"] for c in caps],
                rapplication=started.get("rapplication"),
                note=("prototype created from the template - open the rapplication "
                      "and give feedback; capability/adjust calls regenerate it in "
                      "real time. action=template op=oneclick (same id) or the step "
                      "buttons take it the rest of the way to Copilot Studio."))

        # ── oneclick: the WHOLE journey - build, tests, export, deploy ──
        base = {k: kwargs[k] for k in
                ("_home_dir", "twin_url", "twin_dir", "twin_source", "threshold",
                 "deploy_agent_path", "credentials", "credentials_path")
                if k in kwargs}
        base["cubby"] = slug
        steps = {"start": "success"}

        def stop(envelope, status="partial"):
            return self._env("template", status, op="oneclick",
                             template=stack.get("id"), cubby=slug, steps=steps,
                             detail=envelope,
                             note="one-click stopped here - fix and re-run "
                                  "template op=oneclick with the same id; completed "
                                  "steps are kept.")

        b = json.loads(self._build(dict(base)))
        steps["build"] = b.get("status")
        if b.get("status") != "success":
            return stop(b)
        tl = json.loads(self._test({**base, "target": "local"}))
        steps["test_local"] = tl.get("status")
        if tl.get("status") != "success":
            return stop(tl)
        tw = json.loads(self._test({**base, "target": "twin"}))
        steps["test_twin"] = tw.get("status")
        twin_ok = tw.get("status") == "success"
        ex_kwargs = dict(base)
        if not twin_ok:
            ex_kwargs["skip_twin"] = True
        ex = json.loads(self._export(ex_kwargs))
        steps["export"] = ex.get("status")
        if ex.get("status") != "success":
            return stop(ex)
        dep = json.loads(self._deploy(dict(base)))
        steps["deploy"] = dep.get("status")
        proto = _read_json(os.path.join(cubby, "prototype.json")) or {}
        status = ("success" if dep.get("status") == "success"
                  else dep.get("status", "partial"))
        return self._env(
            "template", status, op="oneclick", template=stack.get("id"),
            cubby=slug, steps=steps,
            capabilities=[c["name"] for c in (proto.get("analysis") or {}).get("capabilities", [])],
            twin_url=(proto.get("twin") or {}).get("url"),
            rapplication=(proto.get("html") or {}).get("shell"),
            environment_url=dep.get("environment_url"),
            factory=(proto.get("export") or {}).get("path"),
            note=("ONE-CLICK COMPLETE: template -> prototype -> agents -> tested "
                  "twin -> factory singleton -> Copilot Studio. Open the twin URL "
                  "to give feedback - capability changes regenerate everything in "
                  "real time, then re-run the steps to redeploy."
                  if status == "success" else
                  "one-click ran to deploy but credentials are needed - load the "
                  "settings file in the rapplication, then re-run template "
                  "op=oneclick with the same id."))

    # ---- capability evolution: new requirements regenerate the prototype ----
    def _capability(self, kwargs):
        """The dynamic-regeneration verb: when feedback brings a NEW
        requirement ('can it also generate a PDF proposal?'), the caller
        authors the capability and this cascades the whole prototype -
        demo script regenerated, agents rebuilt, gate reopened, downloads
        and the open rapplication refreshed."""
        # name= targets the CAPABILITY here, never the cubby - resolve without it
        slug, cubby, proto, err = self._resolve(
            {k: v for k, v in kwargs.items() if k != "name"})
        if err:
            return err
        op = (kwargs.get("op") or "add").lower()
        if op in ("up", "down", "status", "provision", "import", "export"):
            return self._env("capability", "error",
                             error="capability ops are add | update | remove "
                                   "(twin/credentials ops do not apply here).")
        analysis = proto["analysis"]
        caps = analysis["capabilities"]
        reopened = False
        if (proto.get("gate") or {}).get("stopped"):
            proto["gate"] = {"stopped": False, "reopened_at": _now(),
                             "note": ("gate reopened by a capability change - the "
                                      "previous exports still exist; re-test and "
                                      "re-export to gate again.")}
            reopened = True

        changed = None
        if op == "remove":
            target = (kwargs.get("name") or "").strip().lower()
            if not target:
                return self._env("capability", "error",
                                 error="pass name=<capability name or key> to remove.")
            idx = next((i for i, c in enumerate(caps)
                        if c["key"] == target.replace(" ", "_")
                        or c["name"].lower() == target), None)
            if idx is None:
                return self._env("capability", "error",
                                 error=f"no capability matching {target!r}",
                                 capabilities=[c["name"] for c in caps])
            if len(caps) == 1:
                return self._env("capability", "refused",
                                 error="refusing to remove the last capability - a "
                                       "prototype needs at least one.")
            changed = f"removed {caps.pop(idx)['name']}"
        else:  # add | update -> upsert by key/name
            raw = kwargs.get("capability")
            if not raw:
                return self._env(
                    "capability", "error",
                    error=("pass capability=<ONE JSON object> that YOU author from "
                           "the user's new requirement - same shape as a "
                           "capabilities[] item, including invented "
                           "synthetic_records that simulate the artifact (e.g. a "
                           "generated PDF as a record with file name, pages, "
                           "status). " + CAPABILITIES_SCHEMA_HINT))
            try:
                if isinstance(raw, str):
                    raw = json.loads(raw)
                new_cap = _coerce_capabilities([raw], proto["customer"])[0]
            except (ValueError, TypeError) as e:
                return self._env("capability", "error",
                                 error=f"capability invalid: {e}. "
                                       + CAPABILITIES_SCHEMA_HINT)
            idx = next((i for i, c in enumerate(caps)
                        if c["key"] == new_cap["key"]
                        or c["name"].lower() == new_cap["name"].lower()), None)
            if idx is None:
                caps.append(new_cap)
                changed = f"added {new_cap['name']}"
            else:
                caps[idx] = new_cap
                changed = f"updated {new_cap['name']}"

        analysis["summary"] = (f"Prototype agent set for {proto['customer']} drawn "
                               "from the transcript and live feedback: "
                               + ", ".join(c["name"] for c in caps) + ".")
        # cascade: demo script regenerated from the new capability set (manual
        # turn tweaks are superseded), tests invalidated, agents rebuilt.
        proto["demo_script"] = self._demo_script(analysis)
        proto["tests"] = {}
        proto["stage"] = "demo"
        self._save(cubby, proto)
        build = json.loads(self._build(
            {**{k: v for k, v in kwargs.items() if k != "name"}, "cubby": slug}))
        if build.get("status") != "success":
            return self._env("capability", "error", cubby=slug, changed=changed,
                             error="capability applied but rebuild failed",
                             build=build)
        return self._env(
            "capability", "success", cubby=slug, op=op, changed=changed,
            capabilities=[c["name"] for c in caps],
            demo_turns=len(proto["demo_script"]),
            agents=build.get("agents"), gate_reopened=reopened,
            stage="built", tests_invalidated=True,
            note=("prototype regenerated from the new requirement: demo script "
                  "rebuilt (manual turn edits superseded), agent.py files "
                  "rebuilt, downloads refreshed. Next: test target=local, test "
                  "target=twin, mcp_app op=up to rebake the MCP app with the new "
                  "capability, then export (and deploy) to close the gate again."))

    # ---- build -------------------------------------------------------------
    def _build(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if (proto.get("gate") or {}).get("stopped"):
            return self._env("build", "gated", cubby=slug, note="exported and gated.")
        slug_camel = _camel(slug)
        agents_dir = os.path.join(cubby, "agents")
        built, errors = [], []
        for cap in proto["analysis"]["capabilities"]:
            class_name = f"{slug_camel}{cap['class_name']}Agent"
            agent_name = f"{slug_camel}{cap['class_name']}"
            filename = f"{slug.replace('-', '_')}_{cap['key']}_agent.py"
            markers = kwargs.get("artifact_markers")
            if isinstance(markers, str):
                markers = [m.strip() for m in markers.split(",") if m.strip()]
            source = (
                f'"""{cap["name"]} agent for the {proto["display_name"]} prototype.\n\n'
                f'Generated by Transcript2Prototype from cubby {slug!r}.\n'
                f'{cap["description"]}\n"""\n\n'
                + "import base64\nimport json\n\n"
                + AGENT_IMPORT_BLOCK
                + AGENT_CLASS_TEMPLATE.format(
                    class_name=class_name,
                    description=cap["description"].replace('"', "'"),
                    knowledge=cap["knowledge"],
                    triggers=cap["triggers"],
                    response=cap["response"],
                    synthetic=cap.get("synthetic_records") or [],
                    doc_name=_cap_artifact(cap, markers),
                    customer=proto["customer"],
                    agent_name=agent_name,
                    tool_description=(f"{cap['name']} for {proto['customer']}: "
                                      f"{cap['description']}")[:300],
                ))
            try:
                compile(source, filename, "exec")
            except SyntaxError as e:
                errors.append({"file": filename, "error": str(e)})
                continue
            path = os.path.join(agents_dir, filename)
            _write_text(path, source)
            built.append({"file": filename, "class": class_name,
                          "agent": agent_name, "capability": cap["key"],
                          "sha256": _sha256_text(source)})
        if errors:
            return self._env("build", "error", cubby=slug, errors=errors, built=built)
        proto["agents_built"] = built
        proto["stage"] = "built"
        if "build" not in proto["stages_done"]:
            proto["stages_done"].append("build")
        proto["tests"] = {}
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env("build", "success", cubby=slug,
                         agents=[b["file"] for b in built],
                         path=agents_dir, stage="built",
                         note="real agent.py files generated. Next: action=test target=local "
                              "to replay the demo against them on the local twin.")

    # ---- the local twin: load generated agents in-process -------------------
    def _load_built_agents(self, cubby, proto):
        """exec each generated agent file -> {agent_name: instance}. The inline
        BasicAgent fallback in every generated file makes this hermetic."""
        registry = {}
        agents_dir = os.path.join(cubby, "agents")
        for rec in proto.get("agents_built") or []:
            path = os.path.join(agents_dir, rec["file"])
            with open(path, encoding="utf-8") as f:
                source = f.read()
            ns = {"__name__": f"t2p_local.{rec['capability']}"}
            exec(compile(source, path, "exec"), ns)  # noqa: S102 - our own generated file
            cls = ns.get(rec["class"])
            if cls:
                inst = cls()
                registry[inst.name] = inst
        return registry

    def _grade_turns(self, proto, respond, threshold, live, progress=None):
        """Replay every demo turn through respond(turn)->text and score it.
        progress(results_so_far) fires after each turn so the test can be
        SEEN playing in the Copilot iframe while it runs."""
        results, all_pass = [], True
        for t in proto["demo_script"]:
            expected = t.get("expect") or []
            narrative = t.get("agent") is None
            if narrative and not live:
                results.append({"turn": t["turn"], "mode": "narrative",
                                "passed": True,
                                "actual": t.get("assistant") or "",
                                "note": "scripted narrative turn - no generated agent behind it"})
            else:
                actual, err = respond(t)
                if err:
                    results.append({"turn": t["turn"], "passed": False,
                                    "error": err, "actual": err})
                    all_pass = False
                elif narrative:
                    ok = bool((actual or "").strip())
                    results.append({"turn": t["turn"], "mode": "narrative",
                                    "passed": ok,
                                    "actual": (actual or "")[:1500],
                                    "actual_excerpt": (actual or "")[:200]})
                    all_pass = all_pass and ok
                else:
                    eff = expected
                    scored_text = actual or ""
                    if live:
                        # a live twin's LLM paraphrases - multi-word trigger
                        # phrases rarely survive verbatim, so score on the
                        # significant WORDS of each phrase, against the reply
                        # PLUS the invoked agent's raw output (score_extra)
                        seen = set()
                        eff = [w for p in expected
                               for w in re.split(r"[^a-z0-9]+", str(p).lower())
                               if len(w) > 3
                               and not (w in seen or seen.add(w))]
                        scored_text += "\n" + str(
                            getattr(respond, "score_extra", "") or "")
                    score, hits = _kw_score(eff, scored_text)
                    ok = score >= threshold and bool((actual or "").strip())
                    results.append({"turn": t["turn"], "agent": t.get("agent"),
                                    "expected": expected, "hit": hits,
                                    "score": round(score, 2), "passed": ok,
                                    "actual": (actual or "")[:1500],
                                    "actual_excerpt": (actual or "")[:200]})
                    all_pass = all_pass and ok
            if progress:
                try:
                    progress(list(results))
                except Exception:  # noqa: BLE001 - progress is best-effort
                    pass
        graded = [r for r in results if "score" in r]
        pass_rate = (sum(1 for r in results if r["passed"]) / max(1, len(results)))
        return results, all_pass, round(pass_rate, 2), graded

    def _replay_payload(self, proto, target, started, results, done):
        """The sent/returned transcript the Copilot iframe replays visually."""
        script = proto["demo_script"]
        turns = []
        for i, r in enumerate(results):
            user = script[i]["user"] if i < len(script) else ""
            turns.append({"user": user, "actual": (r.get("actual") or "")[:1500],
                          "passed": bool(r.get("passed")),
                          "score": r.get("score")})
        passed = sum(1 for r in results if r.get("passed"))
        return {"target": target, "at": started, "done": done,
                "passed": passed, "total": len(script), "turns": turns}

    def _journal_exchanges(self, proto):
        """Persist the just-finished replay's sent/answered pairs into the
        session journal so the whole autonomous run can be watched later."""
        replay = proto.get("last_test_replay") or {}
        journal = proto.setdefault("journal", [])
        journal.append({"at": _now(), "kind": "note",
                        "text": ("live drive against the twin"
                                 if replay.get("target") == "drive" else
                                 f"{replay.get('target')} test replay - "
                                 f"{replay.get('passed')}/{replay.get('total')} passed")})
        for t in replay.get("turns") or []:
            journal.append({"at": _now(), "kind": "exchange",
                            "src": replay.get("target"),
                            "user": (t.get("user") or "")[:400],
                            "reply": (t.get("actual") or "")[:1200],
                            "passed": t.get("passed"),
                            "score": t.get("score")})
        del journal[:-300]

    def _test(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if (proto.get("gate") or {}).get("stopped"):
            return self._env("test", "gated", cubby=slug, note="exported and gated.")
        if not proto.get("agents_built"):
            return self._env("test", "error", cubby=slug,
                             error="no agents built yet - action=build first.")
        target = (kwargs.get("target") or
                  ("twin" if proto["stage"] == "local_passed" else "local")).lower()
        if target == "local":
            return self._test_local(kwargs, slug, cubby, proto)
        return self._test_twin(kwargs, slug, cubby, proto)

    def _test_local(self, kwargs, slug, cubby, proto):
        threshold = float(kwargs.get("threshold") or 0.6)
        registry = self._load_built_agents(cubby, proto)
        by_cap = {}
        for rec in proto["agents_built"]:
            inst = registry.get(rec["agent"])
            if inst:
                by_cap[rec["capability"]] = inst

        def respond(turn):
            agent = by_cap.get(turn.get("agent"))
            if not agent:
                return None, f"no generated agent for capability {turn.get('agent')!r}"
            try:
                return agent.perform(user_input=turn["user"]), None
            except Exception as e:  # noqa: BLE001
                return None, f"{type(e).__name__}: {e}"

        started = _now()
        html_state = proto.get("html") or {}

        def progress(partial):
            proto["last_test_replay"] = self._replay_payload(
                proto, "local", started, partial, done=False)
            self._regen_html(cubby, proto, mode=html_state.get("mode") or "scripted",
                             api_url=html_state.get("api_url") or "")

        results, all_pass, pass_rate, graded = self._grade_turns(
            proto, respond, threshold, live=False, progress=progress)
        proto["last_test_replay"] = self._replay_payload(
            proto, "local", started, results, done=True)
        self._journal_exchanges(proto)
        report = {"schema": "t2p-test-report/1.0", "target": "local",
                  "cubby": slug, "at": _now(), "threshold": threshold,
                  "passed": all_pass, "pass_rate": pass_rate,
                  "agents_loaded": sorted(registry), "turns": results}
        _write_json(os.path.join(cubby, "show-and-tell", "test_report_local.json"),
                    report)
        proto.setdefault("tests", {})["local"] = {
            "target": "local", "passed": all_pass, "pass_rate": pass_rate,
            "at": report["at"],
            "report": os.path.join(cubby, "show-and-tell", "test_report_local.json")}
        if all_pass:
            proto["stage"] = "local_passed"
            if "test_local" not in proto["stages_done"]:
                proto["stages_done"].append("test_local")
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "test", "success" if all_pass else "failed", cubby=slug, target="local",
            passed=all_pass, pass_rate=pass_rate, threshold=threshold,
            turns=results, report=proto["tests"]["local"]["report"],
            stage=proto["stage"],
            note=("local twin run passed - the generated agents reproduce the demo. "
                  "Next: action=test target=twin to replay against a live twin."
                  if all_pass else
                  "some turns missed their expected keywords - adjust the demo or "
                  "rebuild, then re-run."))

    def _test_twin(self, kwargs, slug, cubby, proto):
        if not (proto.get("tests", {}).get("local") or {}).get("passed"):
            return self._env("test", "error", cubby=slug,
                             error="run (and pass) test target=local before the live twin run.")
        threshold = float(kwargs.get("threshold") or 0.35)
        explicit_url = (kwargs.get("twin_url") or "").rstrip("/")
        injected = []
        if explicit_url:
            # advanced path: caller targets some other twin and owns injection
            chat_url = (explicit_url if explicit_url.endswith("/chat")
                        else explicit_url + "/chat")
            if kwargs.get("inject", True):
                twin_dir = self._bs_agents_dir(kwargs)
                os.makedirs(twin_dir, exist_ok=True)
                for rec in proto["agents_built"]:
                    src = os.path.join(cubby, "agents", rec["file"])
                    dst = os.path.join(twin_dir, rec["file"])
                    with open(src, encoding="utf-8") as f:
                        _write_text(dst, f.read())
                    injected.append(dst)
        else:
            # DEFAULT: this prototype's OWN dedicated twin - completely
            # separate process, port, memory and agents per prototype.
            up = json.loads(self._twin({**kwargs, "op": "up"}))
            if up.get("status") != "success":
                return self._env("test", "error", cubby=slug, target="twin",
                                 error="could not start the prototype's dedicated twin",
                                 twin=up)
            proto = _read_json(os.path.join(cubby, "prototype.json")) or proto
            chat_url = proto["twin"]["chat_url"]
            injected = [os.path.join(proto["twin"]["dir"], "agents", f)
                        for f in (up.get("injected") or [])]

        history = []

        def respond(turn):
            payload = {"user_input": turn["user"],
                       "conversation_history": history[-10:],
                       "session_id": f"t2p-{slug}"}
            data, err = _post_json(chat_url, payload, timeout=120)
            if err:
                return None, f"twin unreachable or errored at {chat_url}: {err}"
            text = (data.get("response") or data.get("assistant_response") or "")
            text = text.split("|||VOICE|||")[0].strip()
            # the twin's LLM paraphrases freely, but its agent_logs carry the
            # invoked agent's RAW grounded reply (which contains the trigger
            # keywords by construction) - score against both, display the text
            respond.score_extra = str(data.get("agent_logs") or "")
            history.append({"role": "user", "content": turn["user"]})
            history.append({"role": "assistant", "content": text})
            return text, None

        started = _now()
        html_state = proto.get("html") or {}

        def progress(partial):
            proto["last_test_replay"] = self._replay_payload(
                proto, "twin", started, partial, done=False)
            self._regen_html(cubby, proto, mode=html_state.get("mode") or "scripted",
                             api_url=html_state.get("api_url") or "")

        results, all_pass, pass_rate, graded = self._grade_turns(
            proto, respond, threshold, live=True, progress=progress)
        proto["last_test_replay"] = self._replay_payload(
            proto, "twin", started, results, done=True)
        self._journal_exchanges(proto)
        unreachable = any("unreachable" in (r.get("error") or "") for r in results)
        report = {"schema": "t2p-test-report/1.0", "target": "twin",
                  "cubby": slug, "at": _now(), "twin_url": chat_url,
                  "threshold": threshold, "injected": injected,
                  "passed": all_pass, "pass_rate": pass_rate, "turns": results}
        _write_json(os.path.join(cubby, "show-and-tell", "test_report_twin.json"),
                    report)
        proto.setdefault("tests", {})["twin"] = {
            "target": "twin", "passed": all_pass, "pass_rate": pass_rate,
            "at": report["at"], "twin_url": chat_url,
            "report": os.path.join(cubby, "show-and-tell", "test_report_twin.json")}
        paths = None
        if all_pass:
            proto["stage"] = "twin_passed"
            if "test_twin" not in proto["stages_done"]:
                proto["stages_done"].append("test_twin")
            # the same rapplication iframe now drives the REAL agents on the twin
            paths = self._regen_html(cubby, proto, mode="live", api_url=chat_url)
        else:
            self._regen_html(cubby, proto, mode=html_state.get("mode") or "scripted",
                             api_url=html_state.get("api_url") or "")
        self._save(cubby, proto)
        status = "success" if all_pass else ("needs_twin" if unreachable else "failed")
        return self._env(
            "test", status, cubby=slug, target="twin", twin_url=chat_url,
            injected=len(injected), passed=all_pass, pass_rate=pass_rate,
            threshold=threshold, turns=results,
            report=proto["tests"]["twin"]["report"], stage=proto["stage"],
            rapplication=(paths or {}).get("shell"),
            note=("live twin run passed - the rapplication iframe was regenerated in "
                  "LIVE mode pointed at the twin, so the same demo now drives the real "
                  "agents. Next: action=export (the gate)." if all_pass else
                  ("twin not reachable - start your brainstem/twin and re-run, or pass "
                   "twin_url=..." if unreachable else
                   "some live turns scored below threshold - the twin's LLM may route "
                   "differently; adjust expectations or re-run.")))

    # ---- dedicated twins: one fully isolated brainstem per prototype --------
    def _twin_source(self, kwargs):
        explicit = kwargs.get("twin_source")
        if explicit:
            return explicit
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if os.path.isfile(os.path.join(here, "brainstem.py")):
            return here  # this agent is installed inside a brainstem
        return os.path.join(self._home(kwargs), ".brainstem", "src", "rapp_brainstem")

    def _twin_dir(self, kwargs, slug):
        h = hashlib.sha256(f"t2p/{slug}".encode()).hexdigest()[:32]
        return os.path.join(self._home(kwargs), ".rapp", "twins", f"t2p-{slug}__{h}")

    def _twin_python(self, kwargs):
        candidates = [
            os.path.join(self._home(kwargs), ".brainstem", "venv", "bin", "python"),
            sys.executable,
            shutil.which("python3") or "python3",
        ]
        for py in candidates:
            if not py or not os.path.exists(py) and "/" in str(py):
                continue
            try:
                r = subprocess.run([py, "-c", "import flask, flask_cors, dotenv"],
                                   capture_output=True, timeout=20)
                if r.returncode == 0:
                    return py
            except Exception:  # noqa: BLE001
                continue
        return None

    def _twin_soul(self, proto):
        a = proto["analysis"]
        caps = "\n".join(f"- {c['name']}: {c['description']}"
                         for c in a["capabilities"])
        return (f"# {a['agent_name']}\n\n"
                f"I am **{a['agent_name']}**, the working prototype for "
                f"{proto['customer']}. When I greet someone, I introduce myself by "
                f"name - never as 'RAPP', 'an AI assistant', or 'the brainstem'.\n\n"
                f"{a.get('summary', '')}\n\nMy capabilities (each backed by a "
                f"generated agent - prefer calling them over answering from "
                f"memory):\n{caps}\n\nDEMO BEHAVIOR: I am a working prototype "
                f"demo. When a request matches a capability, I ALWAYS call that "
                f"capability's agent immediately with the user's message - I "
                f"never ask the user to first provide documents, letters, files "
                f"or content. My agents carry synthetic demo data and respond "
                f"with worked examples; asking for missing input stalls the "
                f"demo. If details are genuinely needed, I call the agent first "
                f"and let its worked example carry the answer.\n\nI am a "
                f"self-contained twin: my memory, my agents, and my identity "
                f"live in this directory and nowhere else.\n")

    def _provision_twin(self, kwargs, slug, cubby, proto):
        """Lay down (or refresh) the prototype's own twin. Kernel files, auth,
        kernel agents and the prototype's generated agents are copied fresh;
        .brainstem_data (the twin's memory) is NEVER touched if present."""
        src = self._twin_source(kwargs)
        if not os.path.isfile(os.path.join(src, "brainstem.py")):
            return None, self._env(
                "twin", "error",
                error=(f"no brainstem kernel at {src} - pass twin_source=<dir "
                       "containing brainstem.py> (your brainstem install)."))
        tdir = self._twin_dir(kwargs, slug)
        os.makedirs(os.path.join(tdir, "agents"), exist_ok=True)
        os.makedirs(os.path.join(tdir, ".brainstem_data"), exist_ok=True)
        copied = []
        for fn in TWIN_KERNEL_FILES + TWIN_AUTH_FILES:
            sp = os.path.join(src, fn)
            if os.path.isfile(sp):
                shutil.copy2(sp, os.path.join(tdir, fn))
                copied.append(fn)
        for fn in TWIN_KERNEL_AGENTS:
            sp = os.path.join(src, "agents", fn)
            if os.path.isfile(sp):
                shutil.copy2(sp, os.path.join(tdir, "agents", fn))
                copied.append(f"agents/{fn}")
        injected = []
        for rec in proto.get("agents_built") or []:
            sp = os.path.join(cubby, "agents", rec["file"])
            if os.path.isfile(sp):
                shutil.copy2(sp, os.path.join(tdir, "agents", rec["file"]))
                injected.append(rec["file"])
        # the twin's registry mirrors the prototype EXACTLY: stale generated
        # agents from before a reset / capability removal would otherwise
        # keep answering with capabilities the prototype no longer has
        keep = set(TWIN_KERNEL_AGENTS) | set(injected)
        for fn in os.listdir(os.path.join(tdir, "agents")):
            if fn.endswith("_agent.py") and fn not in keep:
                os.remove(os.path.join(tdir, "agents", fn))
        # stable port: reuse the one already assigned to this twin, else the
        # sticky port recorded in the twin DIR (which survives prototype.json
        # resets - otherwise a reset drifts the port and the open page dies),
        # else claim a free one near the deterministic base for this slug.
        sticky = os.path.join(tdir, ".port")
        port = (proto.get("twin") or {}).get("port")
        if not port:
            try:
                port = int(open(sticky).read().strip())
            except (OSError, ValueError):
                port = None
            if port:
                # the previous process may still be releasing it (a reset
                # downs the twin right before re-provisioning) - wait briefly
                for _ in range(12):
                    probe = socket.socket()
                    try:
                        probe.bind(("127.0.0.1", port))
                        probe.close()
                        break
                    except OSError:
                        probe.close()
                        time.sleep(0.5)
                else:
                    port = None  # genuinely taken by someone else
        if not port:
            base = TWIN_PORT_BASE + int(hashlib.sha256(slug.encode()).hexdigest(),
                                        16) % 300
            port = _free_port(base)
        _write_text(sticky, str(port))
        model = ""
        src_env = os.path.join(src, ".env")
        if os.path.isfile(src_env):
            for line in open(src_env, encoding="utf-8", errors="ignore"):
                if line.strip().startswith("GITHUB_MODEL="):
                    model = line.strip()
                    break
        _write_text(os.path.join(tdir, ".env"),
                    f"PORT={port}\nSOUL_PATH=./soul.md\nAGENTS_PATH=./agents\n"
                    f"VOICE_MODE=false\n{model}\n")
        _write_text(os.path.join(tdir, "soul.md"), self._twin_soul(proto))
        parent = _read_json(os.path.join(self._home(kwargs), ".brainstem",
                                         "rappid.json")) or {}
        # Canonical keyless mint (spec §6.2): Hb("rapp/1:rappid", uuid4). NEVER a
        # hash of the name/slug — a name-hash address is the cardinal sin. Mint-
        # once: guarded by the rappid.json existence check just below.
        import uuid
        _own = re.sub(r"[^a-z0-9]+", "-", str(parent.get("owner") or "local").lower()).strip("-") or "local"
        _slug = re.sub(r"[^a-z0-9]+", "-", f"t2p-{slug}".lower()).strip("-") or "twin"
        rappid = f"rappid:@{_own}/{_slug}:" + hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()
        if not os.path.isfile(os.path.join(tdir, "rappid.json")):
            _write_json(os.path.join(tdir, "rappid.json"), {
                "schema": "rapp/1", "rappid": rappid,
                "parent_rappid": parent.get("rappid"),
                "born_at": _now(), "name": f"t2p-{slug}",
                "owner": parent.get("owner"), "kind": "t2p-prototype-twin",
                "role": "variant",
                "description": (f"Dedicated prototype twin for {proto['display_name']} "
                                f"({proto['customer']}) - isolated memory, agents, soul."),
                "_summoned_by": "@kody-w/transcript2prototype"})
        _write_text(os.path.join(tdir, "start.sh"),
                    "#!/bin/sh\ncd \"$(dirname \"$0\")\"\n"
                    "exec python3 brainstem.py\n")
        os.chmod(os.path.join(tdir, "start.sh"), 0o755)
        proto["twin"] = {"dir": tdir, "port": port,
                         "url": f"http://127.0.0.1:{port}",
                         "chat_url": f"http://127.0.0.1:{port}/chat",
                         "rappid": rappid, "provisioned_at": _now(),
                         "kernel_source": src, "injected": injected}
        self._save(cubby, proto)
        return {"dir": tdir, "port": port, "copied": copied,
                "injected": injected}, None

    def _twin_health(self, proto):
        twin = proto.get("twin") or {}
        if not twin.get("url"):
            return None
        return _get_json(twin["url"] + "/health")

    def _twin(self, kwargs):
        op = (kwargs.get("op") or "status").lower()
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        twin = proto.get("twin") or {}

        if op == "status":
            health = self._twin_health(proto)
            return self._env("twin", "success", cubby=slug,
                             provisioned=bool(twin), dir=twin.get("dir"),
                             url=twin.get("url"), running=bool(health),
                             health=health,
                             note=None if twin else "no twin yet - twin op=up creates and starts it.")

        if op == "down":
            pid = None
            pidfile = os.path.join(twin.get("dir") or "", "twin.pid")
            if twin.get("dir") and os.path.isfile(pidfile):
                try:
                    pid = int(open(pidfile).read().strip())
                except ValueError:
                    pid = None
            if pid:
                try:
                    cmd = subprocess.run(["ps", "-p", str(pid), "-o", "command="],
                                         capture_output=True, text=True, timeout=10).stdout
                    if "brainstem.py" in cmd:
                        os.kill(pid, 15)
                        os.remove(pidfile)
                        return self._env("twin", "success", cubby=slug, op="down",
                                         stopped_pid=pid)
                except (OSError, subprocess.SubprocessError) as e:
                    return self._env("twin", "error", cubby=slug,
                                     error=f"could not stop pid {pid}: {e}")
            return self._env("twin", "success", cubby=slug, op="down",
                             note="no recorded twin process - nothing to stop.")

        if op in ("provision", "up"):
            if not proto.get("agents_built"):
                return self._env("twin", "error", cubby=slug,
                                 error="build the agents first (action=build) - a twin "
                                       "without its prototype agents has nothing to demo.")
            prov, perr = self._provision_twin(kwargs, slug, cubby, proto)
            if perr:
                return perr
            if op == "provision":
                return self._env("twin", "success", cubby=slug, op="provision",
                                 **prov,
                                 note="twin laid down (not started). twin op=up starts it.")
            # up = refresh + (re)start: provisioning just refreshed the
            # kernel and agents, so an already-running twin is restarted -
            # otherwise it would keep serving the stale code it booted with.
            health = self._twin_health(proto)
            started_pid = None
            if health:
                pidfile = os.path.join(prov["dir"], "twin.pid")
                try:
                    pid = int(open(pidfile).read().strip())
                    cmd = subprocess.run(["ps", "-p", str(pid), "-o", "command="],
                                         capture_output=True, text=True,
                                         timeout=10).stdout
                    if "brainstem.py" in cmd:
                        os.kill(pid, 15)
                        time.sleep(1.5)
                        health = self._twin_health(proto)
                except (OSError, ValueError, subprocess.SubprocessError):
                    pass  # unknown owner of the port - leave it be
            if not health:
                py = self._twin_python(kwargs)
                if not py:
                    return self._env("twin", "error", cubby=slug,
                                     error=("no python with flask/flask_cors/dotenv found "
                                            "to run the twin - is the brainstem venv at "
                                            "~/.brainstem/venv ?"))
                tdir = prov["dir"]
                env = {**os.environ, "PORT": str(prov["port"])}
                with open(os.path.join(tdir, "twin.log"), "ab") as logf:
                    p = subprocess.Popen([py, "brainstem.py"], cwd=tdir, env=env,
                                         stdout=logf, stderr=logf,
                                         start_new_session=True)
                started_pid = p.pid
                _write_text(os.path.join(tdir, "twin.pid"), str(p.pid))
                for _ in range(40):
                    health = self._twin_health(proto)
                    if health:
                        break
                    if p.poll() is not None:
                        tail = open(os.path.join(tdir, "twin.log"),
                                    errors="ignore").read()[-500:]
                        return self._env("twin", "error", cubby=slug,
                                         error=f"twin exited on boot: ...{tail}")
                    time.sleep(0.5)
                if not health:
                    return self._env("twin", "error", cubby=slug,
                                     error="twin did not become healthy within 20s - "
                                           f"see {os.path.join(prov['dir'], 'twin.log')}")
            # the same rapplication iframe now drives THIS prototype's own twin
            paths = self._regen_html(cubby, proto, mode="live",
                                     api_url=proto["twin"]["chat_url"])
            self._save(cubby, proto)
            return self._env(
                "twin", "success", cubby=slug, op="up",
                url=proto["twin"]["url"], chat_url=proto["twin"]["chat_url"],
                dir=proto["twin"]["dir"], pid=started_pid,
                already_running=started_pid is None,
                agents_loaded=(health or {}).get("agents"),
                injected=prov["injected"], rapplication=paths["shell"],
                note=("dedicated twin is up - completely separate process, port, "
                      "memory and agents. The rapplication iframe was regenerated "
                      "to point at it."))
        return self._env("twin", "error", error="op must be up | down | status | provision")

    # ---- Copilot Studio deployment: the stage AFTER the gate -----------------
    def _deploy_lib(self, kwargs):
        """Load the CopilotStudioDeploy agent file as a LIBRARY (single source
        of truth for packaging + auth + Dataverse import mechanics)."""
        candidates = [
            kwargs.get("deploy_agent_path"),
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "copilot_studio_deploy_agent.py"),
            os.path.join(self._home(kwargs), ".brainstem", "src",
                         "rapp_brainstem", "agents",
                         "copilot_studio_deploy_agent.py"),
        ]
        for p in candidates:
            if p and os.path.isfile(p):
                with open(p, encoding="utf-8") as f:
                    source = f.read()
                ns = {"__name__": "t2p_deploy_lib"}
                exec(compile(source, p, "exec"), ns)  # noqa: S102 - trusted sibling agent
                return ns, p
        return None, None

    def _hpa(self, kwargs):
        """Inject the prototype's mutations BACK into its HPA template:
        op=export writes an updated template folder (README.md in the
        m365-agent-templates shape + the agent instructions) authored from
        the prototype's CURRENT capabilities, knowledge, synthetic corpus and
        change journal - drop it into the HPA repo (e.g. the kody-w fork) and
        the template has learned what the prototype learned."""
        op = (kwargs.get("op") or "export").lower()
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if op != "export":
            return self._env("hpa", "error", error="op must be export")
        a = proto["analysis"]
        src = ((proto.get("sources") or {}).get("hpa")
               or kwargs.get("hpa_source") or "")
        repo, _, hpa_name = src.partition(":")
        hpa_name = hpa_name or proto["display_name"]
        lines = [f"# {hpa_name}", "",
                 f"> {a.get('summary') or proto['display_name'] + ' - updated from a working prototype.'}",
                 "", "## Overview",
                 f"{proto['display_name']} for {proto['customer']}. This template "
                 "was updated FROM a working Transcript2Prototype prototype - the "
                 "capabilities below are demo-proven, each with grounded facts and "
                 "synthetic demo records.", "", "## Features"]
        for c in a["capabilities"]:
            lines.append(f"- **{c['name']}** - {c['description']}")
        lines += ["", "## How It Works"]
        for t in proto["demo_script"]:
            user = t.get("user") or ""
            lines.append(f"{t['turn']}. User: \"{user}\"")
        lines += ["", "## Grounding"]
        for c in a["capabilities"]:
            for k in (c.get("knowledge") or []):
                lines.append(f"- {c['name']}: {k}")
        lines += ["", "## Synthetic Demo Data",
                  "Invented for the prototype - no customer data:"]
        for c in a["capabilities"]:
            for r in (c.get("synthetic_records") or [])[:2]:
                lines.append("- " + c["name"] + ": "
                             + "; ".join(f"{k}={v}" for k, v in r.items()))
        changes = [e for e in (proto.get("journal") or [])
                   if e.get("kind") == "note" and any(
                       w in str(e.get("text") or "").lower()
                       for w in ("capability", "adjust", "build", "export"))]
        if changes:
            lines += ["", "## Change Log (prototype mutations)"]
            for e in changes[-12:]:
                lines.append(f"- {str(e.get('at') or '')[:19]} {e.get('text')}")
        lines += ["", f"Updated {_now()} from prototype cubby '{slug}'"
                      + (f" (origin: {src})" if src else "") + "."]
        hdir = os.path.join(cubby, "exports", "hpa_update")
        os.makedirs(hdir, exist_ok=True)
        readme = os.path.join(hdir, "README.md")
        _write_text(readme, "\n".join(lines))
        instr = os.path.join(hdir, "instructions.md")
        _write_text(instr, self._studio_instructions(proto))
        proto["hpa_update"] = {"files": ["README.md", "instructions.md"],
                               "dir": hdir, "origin": src, "at": _now()}
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "hpa", "success", op="export", cubby=slug, dir=hdir,
            files=["README.md", "instructions.md"], origin=src or None,
            note=("updated HPA template written from the prototype's current "
                  "state (capabilities, grounding, synthetic data, change log). "
                  + (f"Drop the folder into {repo} as '{hpa_name}' to teach the "
                     f"template what the prototype learned."
                     if repo else "Pass hpa_source=owner/repo:Name (or start the "
                     "prototype from an HPA) to target a repo.")))

    def _declarative(self, kwargs):
        """Package the prototype as a Microsoft 365 DECLARATIVE AGENT - the
        end artifact in the HPA reference shape: a Teams app zip (manifest
        v1.19 + declarativeAgent.json + icons) that sideloads straight into
        Teams (Apps > Manage your apps > Upload a custom app). The grounded
        instructions and the demo script's conversation starters ride inside,
        so the sideloaded agent runs the same demo as the prototype."""
        op = (kwargs.get("op") or "export").lower()
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if op != "export":
            return self._env("declarative", "error", error="op must be export")
        import uuid as _uuid
        a = proto["analysis"]
        display = proto["display_name"]
        summary = (a.get("summary") or
                   f"{display} - working prototype for {proto['customer']}.")
        instructions = self._studio_instructions(proto)[:8000]
        starters = []
        cap_by_key = {c["key"]: c for c in a["capabilities"]}
        for t in proto["demo_script"][:6]:
            cap = cap_by_key.get(t.get("agent"))
            starters.append({
                "title": (cap["name"] if cap else "Get started")[:50],
                "text": (t.get("user") or "")[:200]})
        dagent = {
            "$schema": ("https://developer.microsoft.com/json-schemas/copilot/"
                        "declarative-agent/v1.0/schema.json"),
            "version": "v1.0",
            "name": display[:100],
            "description": summary[:1000],
            "instructions": instructions,
            "conversation_starters": starters,
        }
        manifest = {
            "$schema": ("https://developer.microsoft.com/en-us/json-schemas/"
                        "teams/v1.19/MicrosoftTeams.schema.json"),
            "manifestVersion": "1.19",
            "version": "1.0.0",
            "id": str(_uuid.uuid5(_uuid.NAMESPACE_DNS, f"t2p.{slug}")),
            "developer": {
                "name": proto["customer"][:32] or "RAPP Prototype",
                "websiteUrl": "https://github.com/kody-w",
                "privacyUrl": "https://github.com/kody-w",
                "termsOfUseUrl": "https://github.com/kody-w",
            },
            "icons": {"color": "color.png", "outline": "outline.png"},
            "name": {"short": display[:30], "full": display[:100]},
            "description": {"short": summary[:80], "full": summary[:4000]},
            "accentColor": "#0F6CBD",
            "copilotAgents": {
                "declarativeAgents": [
                    {"id": "dagent1", "file": "declarativeAgent.json"}]},
        }
        import io as _io
        buf = _io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("manifest.json", json.dumps(manifest, indent=2))
            z.writestr("declarativeAgent.json", json.dumps(dagent, indent=2))
            z.writestr("color.png", _png_square(192, (15, 108, 189, 255)))
            z.writestr("outline.png", _png_square(32, (255, 255, 255, 255)))
        blob = buf.getvalue()
        fname = f"{slug.replace('-', '_')}_declarative_agent.zip"
        dest = os.path.join(cubby, "exports", fname)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(blob)
        src = (proto.get("sources") or {}).get("hpa")
        proto["declarative"] = {"file": fname, "path": dest,
                                "sha256": hashlib.sha256(blob).hexdigest(),
                                "at": _now()}
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "declarative", "success", op="export", cubby=slug, file=fname,
            path=dest, size_bytes=len(blob),
            origin=src or None,
            note=("Teams-sideloadable declarative agent package (the HPA "
                  "reference shape): manifest v1.19 + declarativeAgent.json "
                  "with the grounded instructions and the demo script as "
                  "conversation starters. Sideload via Teams > Apps > Manage "
                  "your apps > Upload a custom app, or distribute through the "
                  "org catalog. It is also in the Outputs downloads."))

    # universal Copilot Studio system topics - the generic PATTERNS every
    # HPA carries; agent-specific topics are dropped and OUR capability
    # topics are generated in their place
    PATTERN_SYSTEM_TOPICS = {
        "ConversationStart", "EndofConversation", "Escalate", "Fallback",
        "Goodbye", "Greeting", "MultipleTopicsMatched", "OnError",
        "ResetConversation", "Signin", "StartOver", "ThankYou"}
    DEFAULT_PATTERN = "kody-w/m365-agent-templates:Know My Customer"
    # OUR publisher - never the pattern HPA's (theirs is e.g. PowerCAT).
    # Overridable per deploy via publisher= / publisher_prefix=.
    DEFAULT_PUBLISHER = {
        # the the work distro library's established publisher (the same identity as
        # MSFTAIBASMultiAgentCopilot) - never the pattern HPA's
        "unique": "Microsoft_Research_and_Development",
        "display": "Microsoft Research and Development",
        "prefix": "msrnd",
        "optionvalue": "55058",
        "website": "",
    }

    @staticmethod
    def _pfx_safe(text):
        """Copilot Studio parses {...} in topic text and GPT instructions as
        Power Fx / template bindings - unparseable braces FAIL PUBLISH (found
        empirically: synthetic records carrying stringified dicts broke it).
        Demo content never needs literal braces; swap them for parentheses."""
        return str(text).replace("{", "(").replace("}", ")")

    @staticmethod
    def _xml_escape(text):
        """Raw capability text (e.g. 'M&A', 'S&AM', '<5%') goes into
        botcomponent.xml element bodies/attrs; an unescaped & or < makes the
        XML invalid and Dataverse rejects the WHOLE solution import (400
        'cannot be imported'). Escape the five XML predefined entities."""
        return (str(text).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;")
                .replace("'", "&apos;"))

    @staticmethod
    def _topic_files(schema, cap):
        """One native Copilot Studio topic (botcomponent.xml + data YAML) for
        a capability: triggers -> triggerQueries, response -> SendActivity."""
        esc = Transcript2PrototypeAgent._xml_escape
        comp = f"{schema}.topic.{cap['class_name']}"
        xml = (f'<botcomponent schemaname="{esc(comp)}">\n'
               f"  <componenttype>9</componenttype>\n"
               f"  <description>{esc(cap['description'][:200])}</description>\n"
               f"  <iscustomizable>1</iscustomizable>\n"
               f"  <name>{esc(cap['name'])}</name>\n"
               f"  <parentbotid>\n"
               f"    <schemaname>{schema}</schemaname>\n"
               f"  </parentbotid>\n"
               f"  <statecode>0</statecode>\n"
               f"  <statuscode>1</statuscode>\n"
               f"</botcomponent>")
        reply = cap["response"]
        if cap.get("synthetic_records"):
            reply += ("\n\nWorked example (synthetic demo data): "
                      + "; ".join(f"{k}={v}" for k, v in
                                  list(cap["synthetic_records"][0].items())[:5]))
        reply = Transcript2PrototypeAgent._pfx_safe(reply)
        data_yaml = (
            "kind: AdaptiveDialog\n"
            "beginDialog:\n"
            "  kind: OnRecognizedIntent\n"
            "  id: main\n"
            "  intent:\n"
            f"    displayName: {json.dumps(cap['name'])}\n"
            "    includeInOnSelectIntent: false\n"
            "    triggerQueries:\n"
            + "".join(f"      - {json.dumps(str(t))}\n"
                      for t in (cap.get("triggers") or [])[:8])
            + "\n  actions:\n"
            "    - kind: SendActivity\n"
            f"      id: sendMessage_{cap['key'][:12]}\n"
            "      activity:\n"
            "        text:\n"
            f"          - {json.dumps(reply)}\n")
        return comp, xml, data_yaml

    @classmethod
    def _inject_capability_topics(cls, zip_bytes, caps):
        """Add one native topic per capability into a BUILT solution zip
        (bot schema discovered from the zip), registering the new parts in
        [Content_Types].xml."""
        import io as _io
        zin = zipfile.ZipFile(_io.BytesIO(zip_bytes))
        schema = next((n.split("/")[1] for n in zin.namelist()
                       if n.startswith("bots/") and n.count("/") >= 2), None)
        if not schema:
            return zip_bytes
        out = _io.BytesIO()
        ct_text = "<Types></Types>"
        adds = []
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                if item == "[Content_Types].xml":
                    ct_text = zin.read(item).decode("utf-8", "replace")
                    continue
                zout.writestr(item, zin.read(item))
            for c in caps:
                comp, xml, data_yaml = cls._topic_files(schema, c)
                zout.writestr(f"botcomponents/{comp}/botcomponent.xml", xml)
                zout.writestr(f"botcomponents/{comp}/data", data_yaml)
                adds.append(
                    f'<Override PartName="/botcomponents/{comp}/botcomponent.xml" '
                    'ContentType="application/octet-stream" />'
                    f'<Override PartName="/botcomponents/{comp}/data" '
                    'ContentType="application/octet-stream" />')
            zout.writestr("[Content_Types].xml",
                          ct_text.replace("</Types>", "".join(adds) + "</Types>"))
        return out.getvalue()

    @staticmethod
    def _patch_bot_configuration(zip_bytes):
        """Bring the packager's bot configuration up to the WORKING agents'
        shape: publish on import (so the agent provisions and opens
        immediately), full bot. NO channel declarations: declaring the
        Microsoft365Copilot channel registers the bot for 'copilot chat'
        service-side, which then REQUIRES Integrated authentication forever
        ('Publish not allowed. Only Authentication mode Integrated is
        supported for copilot chat') - and Integrated auth kills secret-based
        Direct Line, our autonomous verification path. Channels are a Studio
        click at production handoff, never a pipeline default."""
        import io as _io
        zin = zipfile.ZipFile(_io.BytesIO(zip_bytes))
        out = _io.BytesIO()
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                data = zin.read(item)
                if item.startswith("bots/") and item.endswith("configuration.json"):
                    try:
                        cfg = json.loads(data.decode("utf-8", "replace"))
                        cfg.pop("channels", None)
                        cfg.setdefault("publishOnImport", True)
                        cfg.setdefault("isLightweightBot", False)
                        cfg.setdefault("settings", {}).setdefault(
                            "SmartTaskCompletionEnabled", False)
                        data = json.dumps(cfg, indent=1).encode()
                    except ValueError:
                        pass
                zout.writestr(item, data)
        return out.getvalue()

    @staticmethod
    def _portable_flow(text, display="the agent"):
        """Pattern HPA flows ship their AUTHOR'S environment baked in: AI
        Builder prompt record ids and Word templates living on the author's
        own SharePoint site (KMC: microsoft.sharepoint-df.com/teams/
        BuilderPMs). In any other environment the flow cannot even be saved
        (wordonlinebusiness GetFileSchema 404 'The selected file doesn't
        exist'). When a flow smells non-portable, rebuild its action graph on
        the one portable connector - OneDrive Create file + Create share
        link - keeping the agent-facing trigger/response contract identical
        and the OneDrive connection reference embedded (runs on the bound
        connection, never the chat invoker - secret-based Direct Line has no
        user to invoke as)."""
        if not re.search(r"wordonlinebusiness|aibuilder", text):
            return text, False
        try:
            cd = json.loads(text)
            props = cd["properties"]
            d = props["definition"]
            trig = d["triggers"]["manual"]["inputs"]["schema"]
            in_prop = (trig.get("required") or
                       sorted(trig.get("properties") or {"text": 1}))[0]
            resp_name, resp = next(
                (k, v) for k, v in d["actions"].items()
                if v.get("type") == "Response")
            out_props = [k for k, v in
                         (resp["inputs"]["schema"].get("properties") or {}).items()
                         if v.get("type") == "string"] or ["link"]
            od_ref = next((k for k, v in props["connectionReferences"].items()
                           if v.get("api", {}).get("name")
                           == "shared_onedriveforbusiness"), None)
            if not od_ref:
                return text, False
        except (ValueError, KeyError, StopIteration):
            return text, False
        props["connectionReferences"] = {
            od_ref: dict(props["connectionReferences"][od_ref],
                         runtimeSource="embedded")}
        link_expr = "@{outputs('Create_share_link')?['body/WebUrl']}"
        html = ('<html><head><meta charset="utf-8"><title>' + display
                + ' document</title></head><body style="font-family: Segoe UI,'
                ' Arial, sans-serif; max-width: 720px; margin: 2rem auto;">'
                '<div style="border-bottom: 3px solid #0078D4; padding-bottom:'
                ' 8px; margin-bottom: 16px;"><strong>' + display
                + "</strong><br>Generated document</div>"
                '<div style="white-space: pre-wrap;">@{triggerBody()?[\''
                + in_prop + "']}</div></body></html>")
        d["actions"] = {
            "Create_file": {
                "runAfter": {},
                "type": "OpenApiConnection",
                "inputs": {
                    "parameters": {
                        "folderPath": "/",
                        "name": "Draft_@{formatDateTime(utcNow(), "
                                "'yyyyMMdd-HHmmss')}.html",
                        "body": html},
                    "host": {
                        "apiId": "/providers/Microsoft.PowerApps/apis/"
                                 "shared_onedriveforbusiness",
                        "operationId": "CreateFile",
                        "connectionName": od_ref}}},
            "Create_share_link": {
                "runAfter": {"Create_file": ["Succeeded"]},
                "type": "OpenApiConnection",
                "inputs": {
                    "parameters": {
                        "id": "@outputs('Create_file')?['body/Id']",
                        "type": "View",
                        "scope": "Organization"},
                    "host": {
                        "apiId": "/providers/Microsoft.PowerApps/apis/"
                                 "shared_onedriveforbusiness",
                        "operationId": "CreateShareLinkV2",
                        "connectionName": od_ref}}},
            resp_name: dict(
                resp,
                runAfter={"Create_share_link": ["Succeeded"]},
                inputs=dict(resp["inputs"],
                            body={p: link_expr for p in out_props})),
        }
        return json.dumps(cd, indent=2), True

    @staticmethod
    def _publish_bot(uniq, creds, token):
        """The deploy is only DONE when the agent publishes - imports with
        unpublishable content (e.g. Power Fx-breaking braces, found the hard
        way) look fine until the first message fails with
        LatestPublishedVersionNotFound. Publish via pac when available
        (the reliable oracle), else the Dataverse PvaPublish action."""
        # find the imported bot's id by schema name prefix
        botid = None
        try:
            import urllib.parse as _up
            qs = _up.urlencode({"$select": "botid,schemaname",
                                "$filter": f"contains(schemaname, '{uniq}')",
                                "$orderby": "createdon desc", "$top": "1"})
            req = urllib.request.Request(
                creds["resource"].rstrip("/") + "/api/data/v9.2/bots?" + qs,
                headers={"Authorization": "Bearer " + token,
                         "Accept": "application/json"})
            rows = json.loads(urllib.request.urlopen(
                req, timeout=60).read().decode()).get("value", [])
            botid = rows[0]["botid"] if rows else None
        except Exception as exc:  # noqa: BLE001
            return {"status": "unknown", "error": f"bot lookup: {exc}"[:160]}
        if not botid:
            return {"status": "unknown", "error": "bot not found post-import"}
        pac = os.path.expanduser("~/.dotnet/tools/pac")
        if os.path.isfile(pac):
            try:
                env = {**os.environ,
                       "DOTNET_ROOT": os.environ.get(
                           "DOTNET_ROOT", "/opt/homebrew/opt/dotnet/libexec")}
                r = subprocess.run([pac, "copilot", "publish", "--bot", botid],
                                   capture_output=True, text=True, timeout=420,
                                   env=env)
                ok = "Succeeded" in (r.stdout or "")
                return {"status": "published" if ok else "failed",
                        "bot_id": botid, "via": "pac",
                        "detail": (r.stdout or r.stderr or "")[-160:].strip()}
            except (OSError, subprocess.SubprocessError) as exc:
                pass  # fall through to PvaPublish
        try:
            req = urllib.request.Request(
                creds["resource"].rstrip("/")
                + f"/api/data/v9.2/bots({botid})/Microsoft.Dynamics.CRM.PvaPublish",
                data=b"{}", method="POST",
                headers={"Authorization": "Bearer " + token,
                         "Content-Type": "application/json",
                         "Accept": "application/json"})
            urllib.request.urlopen(req, timeout=300)
            return {"status": "publish_requested", "bot_id": botid,
                    "via": "PvaPublish",
                    "note": "verify with pac copilot list / a test message"}
        except Exception as exc:  # noqa: BLE001
            return {"status": "failed", "bot_id": botid,
                    "error": str(exc)[:160]}

    @staticmethod
    def _directline_token_url(creds, token, publish):
        """Auth-none agents need NO Studio secret: the environment's
        tokenless Direct Line endpoint mints conversation tokens directly.
        Host shape: {envid-last2}.{last2}.environment.api.powerplatform.com
        - the 'default' prefix documented for this host belongs to a
        tenant's DEFAULT environment only; named environments (like
        kodyD365) use the bare env-id host. This is what closes the loop:
        deploy -> publish -> mint token -> drive the demo script, zero
        human steps."""
        try:
            bot_id = (publish or {}).get("bot_id")
            if not bot_id:
                return None
            base = creds["resource"].rstrip("/") + "/api/data/v9.2/"
            hdrs = {"Authorization": "Bearer " + token,
                    "Accept": "application/json"}
            req = urllib.request.Request(
                base + f"bots({bot_id})?$select=schemaname", headers=hdrs)
            with urllib.request.urlopen(req, timeout=30) as r:
                schema = json.loads(r.read()).get("schemaname")
            req = urllib.request.Request(
                base + "RetrieveCurrentOrganization(AccessType="
                       "Microsoft.Dynamics.CRM.EndpointAccessType'Default')",
                headers=hdrs)
            with urllib.request.urlopen(req, timeout=30) as r:
                env = (json.loads(r.read()).get("Detail") or {}).get(
                    "EnvironmentId", "")
            hexid = env.replace("-", "")
            if not (schema and len(hexid) == 32):
                return None
            return (f"https://{hexid[:-2]}.{hexid[-2:]}.environment.api."
                    f"powerplatform.com/powervirtualagents/botsbyschema/"
                    f"{schema}/directline/token"
                    f"?api-version=2022-03-01-preview")
        except Exception:  # noqa: BLE001 - enrichment, never fails a deploy
            return None

    def _load_packager(self, kwargs):
        """The the work distro mcs_solution packager as a library - THE canonical
        solution builder (SolutionSpec -> SolutionPackager.package()).
        Discovery: packager_path= > T2P_PACKAGER env > the known repo
        locations. Returns the module or None (callers fall back)."""
        cands = [kwargs.get("packager_path"), os.environ.get("T2P_PACKAGER"),
                 *[os.path.expanduser(p) for p in
                   os.environ.get("T2P_PACKAGER_PATHS", "").split(os.pathsep) if p]]
        # The packager fallback locations used to be hardcoded work-checkout
        # paths. This repo is public, so they now come from $T2P_PACKAGER_PATHS
        # (os.pathsep-separated). $T2P_PACKAGER above still takes precedence;
        # behaviour is unchanged once either is exported.
        if any(str(c).lower() == "off" for c in cands if c):
            return None   # explicit opt-out (tests / skeleton runs)
        for c in cands:
            if not c:
                continue
            c = os.path.expanduser(str(c))
            if not os.path.isfile(os.path.join(c, "wrapper_generator",
                                               "solution_packager.py")):
                continue
            if c not in sys.path:
                sys.path.insert(0, c)
            try:
                import importlib
                try:
                    import requests  # noqa: F401
                except ImportError:
                    # the packager's openapi module imports requests at module
                    # level but our connector-less path never calls it - shim
                    # it so the utility loads in dependency-free hosts (twins,
                    # hermetic tests)
                    import types as _types
                    sys.modules.setdefault("requests",
                                           _types.ModuleType("requests"))
                return importlib.import_module(
                    "wrapper_generator.solution_packager")
            except Exception:  # noqa: BLE001 - discovery is best-effort
                continue
        return None

    @classmethod
    def _solution_from_pattern(cls, zip_bytes, proto, display, uniq,
                               instructions, version="1.0.1.0",
                               publisher=None):
        """Generate OUR OWN Copilot Studio solution USING an HPA's patterns -
        not a rebrand of its content. From the pattern zip we take the
        anatomy: bot + GPT component shape, the universal system topics, the
        document-generation action + Power Automate workflow wiring
        (Dataverse/connector patterns), and the solution manifests. From the
        PROTOTYPE we generate the content: our identity, our grounded
        instructions, one NATIVE topic per capability (triggers ->
        triggerQueries, response -> SendActivity) in the pattern's own topic
        shape. Agent-specific topics from the pattern are dropped.
        Returns (zip_bytes, generated)."""
        import io as _io
        import uuid as _uuid
        zin = zipfile.ZipFile(_io.BytesIO(zip_bytes))
        sol = zin.read("solution.xml").decode("utf-8", "replace")
        m_uniq = re.search(r"<UniqueName>([^<]+)</UniqueName>", sol)
        m_disp = re.search(r'<LocalizedName description="([^"]+)"', sol)
        if not m_uniq:
            raise ValueError("not a solution zip (no solution.xml UniqueName)")
        old_uniq, old_disp = m_uniq.group(1), (m_disp.group(1) if m_disp else "")
        old_schema = next((n.split("/")[1] for n in zin.namelist()
                           if n.startswith("bots/") and n.count("/") >= 2), None)
        if not old_schema:
            raise ValueError("no bot component in the solution zip")
        pub = dict(cls.DEFAULT_PUBLISHER, **(publisher or {}))
        # the schema prefix is the PUBLISHER's customization prefix - ours,
        # never the pattern's (cat_ = PowerCAT, the HPA authors)
        new_schema = pub["prefix"] + "_" + re.sub(r"[^a-z0-9]", "", uniq.lower())
        # the pattern's publisher identity, for scrubbing everywhere
        m_pub = re.search(r"<Publisher>.*?</Publisher>", sol, re.S)
        old_pub_unique = old_pub_display = ""
        if m_pub:
            mu = re.search(r"<UniqueName>([^<]+)</UniqueName>", m_pub.group(0))
            md = re.search(r'<LocalizedName description="([^"]+)"', m_pub.group(0))
            old_pub_unique = mu.group(1) if mu else ""
            old_pub_display = md.group(1) if md else ""
        # flow + action identity from the pattern
        old_guid = None
        for n in zin.namelist():
            m = re.search(r"Workflows/.*?([0-9A-Fa-f-]{36})\.json$", n)
            if m:
                old_guid = m.group(1)
                break
        new_guid = str(_uuid.uuid5(_uuid.NAMESPACE_DNS, f"t2p.{uniq}.flow"))
        old_actions = sorted({n.split(".action.", 1)[1].split("/", 1)[0]
                              for n in zin.namelist() if ".action." in n})
        action_map = {a: "DocumentGeneration" + (str(i) if i else "")
                      for i, a in enumerate(old_actions)}

        def ident(text):
            for a, b in action_map.items():
                text = text.replace(a, b)
            text = (text.replace(old_schema, new_schema)
                        .replace(old_uniq, uniq))
            if old_disp:
                text = text.replace(old_disp, display)
            if old_pub_display:
                text = text.replace(old_pub_display, pub["display"])
            if old_pub_unique:
                text = text.replace(old_pub_unique, pub["unique"])
            if old_guid:
                text = (text.replace(old_guid, new_guid)
                            .replace(old_guid.upper(), new_guid.upper())
                            .replace(old_guid.lower(), new_guid))
            return text

        caps = proto["analysis"]["capabilities"]
        generated = {"capability_topics": [c["name"] for c in caps],
                     "system_topics": 0,
                     "actions": sorted(action_map.values()),
                     "workflows": 1 if old_guid else 0}
        # schemanames of the agent-specific topics we drop - their entries
        # must ALSO leave the Assets set files (msdyn_aimodelset etc.), or
        # the import fails on unresolved botcomponent references
        dropped_comps = {new_schema + ".topic." + n.split(".topic.", 1)[1].split("/", 1)[0]
                         for n in zin.namelist()
                         if ".topic." in n
                         and n.split(".topic.", 1)[1].split("/", 1)[0]
                         not in cls.PATTERN_SYSTEM_TOPICS}
        dropped_parts = []
        out = _io.BytesIO()
        topic_ct_lines = []
        ct_text = "<Types></Types>"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                if ".topic." in item:
                    tname = item.split(".topic.", 1)[1].split("/", 1)[0]
                    if tname not in cls.PATTERN_SYSTEM_TOPICS:
                        dropped_parts.append("/" + ident(item))
                        continue   # agent-specific topic: pattern only, not content
                    if item.endswith("/data"):
                        generated["system_topics"] += 1
                data = zin.read(item)
                newpath = ident(item)
                if newpath.endswith(".gpt.default/data"):
                    body = instructions
                    if action_map:
                        body += ("\n\n# Actions (the borrowed integration "
                                 "pattern)\nYou have these actions - call them "
                                 "when the user asks for a document or file:\n"
                                 + "\n".join("- " + a
                                              for a in sorted(action_map.values())))
                    data = ("kind: GptComponentMetadata\ndisplayName: " + display
                            + "\ninstructions: |-\n"
                            + "\n".join("  " + ln for ln in body.splitlines())
                            + "\n").encode()
                elif newpath == "[Content_Types].xml":
                    # finished at the end, once every dropped part is known
                    ct_text = ident(data.decode("utf-8", "replace"))
                    continue
                else:
                    text = ident(data.decode("utf-8", "replace"))
                    if re.match(r"bots/[^/]+/bot\.xml$", newpath):
                        # TEST PROFILE (the only pipeline profile): auth none
                        # so secret-based Direct Line can drive the agent.
                        # The pattern's synchronizationstatus is the AUTHOR
                        # env's runtime state (their app id, their channel
                        # registrations) - importing it seeds the service-
                        # side 'copilot chat' registration that then demands
                        # Integrated auth at every publish. Scrub it.
                        text = re.sub(r"<authenticationmode>[^<]*"
                                      r"</authenticationmode>",
                                      "<authenticationmode>0"
                                      "</authenticationmode>", text)
                        text = re.sub(r"<authenticationtrigger>[^<]*"
                                      r"</authenticationtrigger>",
                                      "<authenticationtrigger>0"
                                      "</authenticationtrigger>", text)
                        text = re.sub(r"\s*<synchronizationstatus>.*?"
                                      r"</synchronizationstatus>", "",
                                      text, flags=re.S)
                    elif re.match(r"bots/[^/]+/configuration\.json$", newpath):
                        try:
                            cfg = json.loads(text)
                            cfg.pop("channels", None)  # Studio click, never
                            text = json.dumps(cfg, indent=1)  # a default
                        except ValueError:
                            pass
                    elif re.match(r"Workflows/.*\.json$", newpath):
                        text, rewrote = cls._portable_flow(text, display)
                        if rewrote:
                            generated["portable_flow"] = True
                    elif ".action." in newpath and newpath.endswith("/data"):
                        # Maker's connection, never the invoker's: a secret-
                        # based Direct Line conversation HAS no authenticated
                        # invoker (IntegratedAuthenticationNotSupportedInChannel)
                        text = text.replace("mode: Invoker", "mode: Maker")
                    if newpath.startswith("Assets/") and dropped_comps:
                        for comp in dropped_comps:
                            text = re.sub(
                                r"<botcomponent_[a-z_]+ [^>]*botcomponentid\.schemaname=\""
                                + re.escape(comp)
                                + r"\"[^>]*(?:/>|>.*?</botcomponent_[a-z_]+>)",
                                "", text, flags=re.S)
                    if newpath == "solution.xml":
                        text = re.sub(r"<Version>[^<]+</Version>",
                                      f"<Version>{version}</Version>", text)
                        # the publisher block becomes OURS, field by field
                        def _pubfix(mblk):
                            blk = mblk.group(0)
                            blk = re.sub(r"<UniqueName>[^<]*</UniqueName>",
                                         "<UniqueName>" + pub["unique"]
                                         + "</UniqueName>", blk)
                            blk = re.sub(r'<LocalizedName description="[^"]*"',
                                         '<LocalizedName description="'
                                         + pub["display"] + '"', blk)
                            blk = re.sub(r'<Description description="[^"]*"',
                                         '<Description description="'
                                         + pub["display"] + '"', blk)
                            if pub.get("website"):
                                blk = re.sub(r"<SupportingWebsiteUrl>[^<]*"
                                             r"</SupportingWebsiteUrl>",
                                             "<SupportingWebsiteUrl>"
                                             + pub["website"]
                                             + "</SupportingWebsiteUrl>", blk)
                            blk = re.sub(r"<CustomizationPrefix>[^<]*"
                                         r"</CustomizationPrefix>",
                                         "<CustomizationPrefix>" + pub["prefix"]
                                         + "</CustomizationPrefix>", blk)
                            blk = re.sub(r"<CustomizationOptionValuePrefix>[^<]*"
                                         r"</CustomizationOptionValuePrefix>",
                                         "<CustomizationOptionValuePrefix>"
                                         + pub["optionvalue"]
                                         + "</CustomizationOptionValuePrefix>",
                                         blk)
                            return blk
                        text = re.sub(r"<Publisher>.*?</Publisher>", _pubfix,
                                      text, flags=re.S)
                    data = text.encode()
                zout.writestr(newpath, data)
            # OUR capability topics, generated in the pattern's topic shape
            for c in caps:
                comp, xml, data_yaml = cls._topic_files(new_schema, c)
                zout.writestr(f"botcomponents/{comp}/botcomponent.xml", xml)
                zout.writestr(f"botcomponents/{comp}/data", data_yaml)
                topic_ct_lines.append(
                    f'<Override PartName="/botcomponents/{comp}/botcomponent.xml" '
                    'ContentType="application/octet-stream" />'
                    f'<Override PartName="/botcomponents/{comp}/data" '
                    'ContentType="application/octet-stream" />')
            # finish [Content_Types].xml: dropped pattern topics scrubbed,
            # our capability topic parts registered
            for part in dropped_parts:
                ct_text = re.sub(r'<Override PartName="' + re.escape(part)
                                 + r'"[^>]*/>', "", ct_text)
            ct_text = ct_text.replace("</Types>",
                                      "".join(topic_ct_lines) + "</Types>")
            zout.writestr("[Content_Types].xml", ct_text.encode()
                          if isinstance(ct_text, str) else ct_text)
        return out.getvalue(), generated

    def _fetch_hpa_solution(self, pattern, kwargs):
        """'owner/repo:Template Name' -> that template folder's built solution
        zip bytes (first *.zip via the GitHub contents API), or a local file
        via pattern_zip_path= (tests / offline)."""
        local = kwargs.get("pattern_zip_path")
        if local and os.path.isfile(os.path.expanduser(local)):
            with open(os.path.expanduser(local), "rb") as f:
                return f.read(), os.path.basename(local)
        repo, _, name = str(pattern or "").partition(":")
        if not repo or not name:
            raise ValueError("pattern_from must be 'owner/repo:Template Name'")
        api = (f"https://api.github.com/repos/{repo}/contents/"
               + urllib.parse.quote(name))
        with urllib.request.urlopen(api, timeout=30) as r:
            listing = json.loads(r.read().decode())
        zips = [e for e in listing
                if isinstance(e, dict) and str(e.get("name", "")).endswith(".zip")]
        if not zips:
            raise ValueError(f"no built solution zip in {repo}/{name}")
        with urllib.request.urlopen(zips[0]["download_url"], timeout=60) as r:
            return r.read(), zips[0]["name"]

    def _studio_knowledge_pack(self, cubby, proto):
        """Stub out the agent's knowledge sources at deploy time: one upload-
        ready text file per capability (facts + the synthetic corpus + the
        exemplar reply) so the Copilot Studio agent can be grounded exactly
        like the prototype's agents - drag the pack into its Knowledge tab
        and the full end-to-end demo runs the same in the test pane."""
        a = proto["analysis"]
        kdir = os.path.join(cubby, "exports", "knowledge")
        os.makedirs(kdir, exist_ok=True)
        files = []
        for c in a["capabilities"]:
            name = f"{proto['slug'].replace('-', '_')}_{c['key']}_knowledge.txt"
            lines = [f"KNOWLEDGE SOURCE: {c['name']}",
                     f"Prototype: {a['agent_name']} ({proto['customer']})",
                     "", "WHAT THIS CAPABILITY DOES",
                     c["description"], "", "APPROVED FACTS"]
            lines += [f"- {k}" for k in (c.get("knowledge") or [])]
            lines += ["", "APPROVED RECORDS (synthetic demo data - invented "
                          "for the prototype, no customer data)"]
            for i, r in enumerate(c.get("synthetic_records") or [], 1):
                lines.append(f"Record {i}: "
                             + "; ".join(f"{k}={v}" for k, v in r.items()))
            lines += ["", "EXEMPLAR APPROVED RESPONSE", c["response"], "",
                      "USAGE: answer questions about this capability from the "
                      "facts and records above; cite this source by name."]
            path = os.path.join(kdir, name)
            _write_text(path, "\n".join(lines))
            files.append({"file": name, "path": path, "capability": c["key"]})
        manifest = ["KNOWLEDGE PACK - stubbed knowledge sources for "
                    + a["agent_name"],
                    "Upload: Copilot Studio > your agent > Knowledge > Add "
                    "knowledge > Files - drag every file in this pack, then "
                    "run the session guide in the test pane.", ""]
        manifest += [f"- {f['file']}" for f in files]
        _write_text(os.path.join(kdir, "_knowledge_pack_readme.txt"),
                    "\n".join(manifest))
        return files

    def _studio_instructions(self, proto):
        """Author the Copilot Studio system instructions FROM the prototype -
        the same capabilities, grounding and synthetic corpus the demo uses,
        plus the behavior rules that make the test-pane demo match the
        prototype (every point covered, cited sources, flagged gaps, the
        in-session learning loop)."""
        a = proto["analysis"]
        lines = ["# Purpose",
                 f"You are {a['agent_name']}, the prototype agent for "
                 f"{proto['customer']}. {a.get('summary', '')}".strip(),
                 "", "# Capabilities"]
        for c in a["capabilities"]:
            lines.append(f"- {c['name']}: {c['description']}")
        lines += ["", "# Knowledge library",
                  "This is your approved library (synthetic demo data invented "
                  "for the prototype - never present it as real customer data). "
                  "Matching knowledge-source files may also be attached to you; "
                  "they carry the same content:"]
        for c in a["capabilities"]:
            lines.append(f"## {c['name']}")
            lines += [f"- {k}" for k in (c.get("knowledge") or [])]
            for r in (c.get("synthetic_records") or [])[:3]:
                lines.append("- record: "
                             + "; ".join(f"{k}={v}" for k, v in r.items())[:220])
        lines += [
            "", "# How you answer (these rules make the demo)",
            f"- Introduce yourself as {a['agent_name']}.",
            "- Decompose multi-part requests and address EVERY point in order; "
            "never silently drop one.",
            "- Ground every answer in the knowledge library or an attached "
            "knowledge source, and say which capability/source it came from.",
            "- If a point has no matching source, say so explicitly ('this "
            "point needs a source') instead of inventing an answer.",
            "- If the user provides a new approved document or facts during "
            "the conversation, treat them as added to your library from that "
            "moment: acknowledge the addition and cite it in later answers.",
            "- Be concise, accurate and helpful. No emojis."]
        text = self._pfx_safe("\n".join(lines))
        if len(text) > 7600:
            # Copilot Studio instruction budget - keep the rules, trim corpus
            head, _, _tail = text.partition("# How you answer")
            rules = text[text.index("# How you answer"):]
            text = head[:7600 - len(rules) - 40].rsplit("\n", 1)[0] \
                + "\n(corpus continues in the attached knowledge sources)\n\n" \
                + rules
        return text

    def _deploy(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if not (proto.get("export") or {}).get("path"):
            # ONE step in the UI: deploy runs the gated factory export itself.
            # The gate rules are unchanged - a refusal (no passing twin run,
            # no skip_twin) surfaces exactly as export would have refused.
            exp_env = json.loads(self._export({**kwargs, "cubby": slug}))
            if exp_env.get("status") not in ("gated", "success"):
                return self._env("deploy", exp_env.get("status", "error"),
                                 cubby=slug, export=exp_env,
                                 error=exp_env.get("error"),
                                 note=exp_env.get("note"))
            slug, cubby, proto, err = self._resolve(kwargs)
            if err:
                return err
        lib, lib_path = self._deploy_lib(kwargs)
        if not lib:
            return self._env(
                "deploy", "needs_deploy_agent", cubby=slug,
                error=("copilot_studio_deploy_agent.py not found next to this agent "
                       "or in the brainstem's agents/ - drop it in (it carries the "
                       "packaging + Dataverse mechanics) or pass deploy_agent_path=."))
        display = proto["display_name"][:60]
        zip_path = os.path.join(
            cubby, "exports", f"{slug.replace('-', '_')}_copilot_studio_solution.zip")

        # package from the prototype, then deploy autonomously with the saved
        # app registration (service principal). No device-code dance.
        # FRESH EVERY DEPLOY: each push is a brand-new solution + agent
        # (R1, R2, ...) - no upgrades, no collisions, clean test runs.
        seq = int(proto.get("deploy_seq") or 0) + 1
        proto["deploy_seq"] = seq
        display = f"{proto['display_name'][:50]} R{seq}"
        instructions = self._studio_instructions(proto)
        uniq = lib["_sanitize"](display)
        version = f"1.0.0.{seq}"
        pub = dict(self.DEFAULT_PUBLISHER)
        if kwargs.get("publisher"):
            pub["display"] = str(kwargs["publisher"])
            pub["unique"] = re.sub(r"[^A-Za-z0-9_]", "_",
                                   str(kwargs["publisher"]))[:40] or pub["unique"]
        if kwargs.get("publisher_prefix"):
            pub["prefix"] = re.sub(r"[^a-z0-9]", "",
                                   str(kwargs["publisher_prefix"]).lower())[:8]
        borrowed = None
        zip_bytes = None
        # 1. EXPLICIT HPA pattern: borrow its anatomy (topics, actions,
        #    workflows, connector wiring), our content
        if kwargs.get("pattern_from") or kwargs.get("pattern_zip_path"):
            pattern = kwargs.get("pattern_from")
            try:
                hpa_zip, src_name = self._fetch_hpa_solution(pattern, kwargs)
                zip_bytes, generated = self._solution_from_pattern(
                    hpa_zip, proto, display, uniq, instructions,
                    version=version, publisher=pub)
                generated["publisher"] = pub["display"]
                borrowed = {"pattern": pattern, "pattern_zip": src_name,
                            "fresh": display, **generated}
            except Exception as exc:  # noqa: BLE001
                borrowed = {"pattern": pattern, "error": str(exc)[:200],
                            "fallback": "packager/skeleton"}
        # 2. DEFAULT: the the work distro mcs_solution packager - the canonical
        #    utility - builds the solution natively; our capability topics
        #    are injected on top
        if zip_bytes is None:
            pk = self._load_packager(kwargs)
            if pk is not None:
                try:
                    a = proto["analysis"]
                    spec = pk.SolutionSpec(
                        agent_name=re.sub(r"[^A-Za-z0-9]", "", display) or uniq,
                        bot_display_name=display,
                        solution_unique_name=uniq,
                        solution_display_name=display,
                        publisher_prefix=pub["prefix"],
                        publisher_unique_name=pub["unique"],
                        publisher_display_name=pub["display"],
                        is_custom_connector=False,
                        include_custom_connector_definitions=False,
                        include_connection_references=False,
                        agent_description=(a.get("summary") or display)[:900],
                        agent_instructions=instructions,
                        trigger_phrases=[t for c in a["capabilities"]
                                         for t in (c.get("triggers") or [])[:2]][:12],
                        solution_version=version)
                    zip_bytes = pk.SolutionPackager(spec).package()
                    zip_bytes = self._inject_capability_topics(
                        zip_bytes, a["capabilities"])
                    zip_bytes = self._patch_bot_configuration(zip_bytes)
                    borrowed = {"builder": "work_distro_mcs_solution_packager",
                                "publisher": pub["display"], "fresh": display,
                                "capability_topics": [c["name"]
                                                      for c in a["capabilities"]]}
                except Exception as exc:  # noqa: BLE001
                    zip_bytes = None
                    borrowed = {"builder": "work_distro_mcs_solution_packager",
                                "error": str(exc)[:200],
                                "fallback": "skeleton"}
        # 3. last resort: the generic skeleton rebrand
        if zip_bytes is None:
            skeleton = lib["_get_bytes"](lib["REPO_RAW"] + "/pipeline/skeleton.zip")
            zip_bytes = lib["build_solution"](skeleton, display, uniq, instructions)
        os.makedirs(os.path.dirname(zip_path), exist_ok=True)
        with open(zip_path, "wb") as f:
            f.write(zip_bytes)
        creds = None
        if kwargs.get("credentials"):
            creds = lib["_extract_dyn"](kwargs["credentials"])
        elif kwargs.get("credentials_path"):
            creds = lib["_extract_dyn"](_read_json(kwargs["credentials_path"]) or {})
        if not creds:
            creds = lib["_load_local_settings"]()
        if not creds:
            return self._env(
                "deploy", "needs_credentials", cubby=slug, agent=display,
                solution_zip=zip_path,
                note=("packaged, but no app registration is saved. Load your "
                      "deployment settings: use the 'Load settings file' button in "
                      "the rapplication's Deployment credentials panel, or "
                      "action=credentials op=import path=<your local.settings.json> "
                      "(DYNAMICS_365_CLIENT_ID/SECRET/TENANT_ID/RESOURCE). Then run "
                      "deploy again - it completes with no sign-in."))
        token = lib["_sp_token"](creds["client_id"], creds["client_secret"],
                                 creds["tenant_id"], creds["resource"])
        lib["_import"](creds["resource"], token, zip_bytes)
        publish = self._publish_bot(uniq, creds, token)
        knowledge = self._studio_knowledge_pack(cubby, proto)
        dl_token_url = self._directline_token_url(creds, token, publish)
        proto["deploy"] = {"status": "deployed", "agent_name": display,
                           "publish": publish,
                           "environment_url": creds["resource"],
                           "directline_token_url": dl_token_url,
                           "autonomous": True, "solution_zip": zip_path,
                           "knowledge_files": [k["file"] for k in knowledge],
                           "borrowed": borrowed,
                           "at": _now()}
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "deploy", "success", cubby=slug, agent=display, autonomous=True,
            environment_url=creds["resource"], solution_zip=zip_path,
            knowledge_files=[k["file"] for k in knowledge],
            borrowed=borrowed, publish=publish,
            note=("deployed autonomously with the saved app registration - the "
                  "agent's instructions carry the full grounded library so the "
                  "test pane runs the demo end to end immediately. A stubbed "
                  "knowledge pack (one file per capability, in the Outputs "
                  "list) is ready to drag into the agent's Knowledge tab for "
                  f"the full look. Open https://copilotstudio.microsoft.com/, "
                  f"find '{display}', and run the SAME session guide."))

    # ---- MCP App export: the prototype NATIVE to Copilot Studio --------------
    def _mcp_app(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if not proto.get("agents_built"):
            return self._env("mcp_app", "error", cubby=slug,
                             error="build the agents first (action=build) - the MCP app "
                                   "exposes the built capabilities as tools.")
        display = proto["display_name"][:60]
        uniq = re.sub(r"[^a-z0-9]", "", display.lower()) or slug.replace("-", "")
        port = 7800 + int(hashlib.sha256(slug.encode()).hexdigest(), 16) % 150
        caps = [{"key": c["key"], "name": c["name"],
                 "description": c["description"],
                 "triggers": c.get("triggers") or [],
                 "knowledge": c.get("knowledge") or [],
                 "response": c["response"],
                 "synthetic_records": c.get("synthetic_records") or []}
                for c in proto["analysis"]["capabilities"]]
        # the widget is a compact prototype workspace (NOT the chat page -
        # a chat inside Copilot's chat would double the chrome). It speaks
        # the MCP Apps bridge to the host with a direct-HTTP fallback.
        widget_html = (MCP_WIDGET_TEMPLATE
                       .replace("__AGENT_NAME__", display)
                       .replace("__CUSTOMER__", proto["customer"])
                       .replace("__UNIQUE_NAME__", uniq)
                       .replace("__SERVER_URL__", f"http://127.0.0.1:{port}/mcp")
                       .replace("__CAPS_JSON__",
                                json.dumps(caps, ensure_ascii=False)))
        file_name = f"{slug.replace('-', '_')}_mcp_app_server.py"
        source = (MCP_APP_TEMPLATE
                  .replace("__DISPLAY_NAME__", display)
                  .replace("__CUSTOMER__", proto["customer"])
                  .replace("__UNIQUE_NAME__", uniq)
                  .replace("__FILE_NAME__", file_name)
                  .replace("__PORT__", str(port))
                  .replace("__CAPABILITIES_JSON__",
                           json.dumps(caps, ensure_ascii=False, indent=1))
                  .replace("__WIDGET_HTML_B64__",
                           base64.b64encode(widget_html.encode("utf-8")).decode("ascii")))
        out_path = os.path.join(cubby, "exports", file_name)
        compile(source, file_name, "exec")  # must be valid standalone python
        _write_text(out_path, source)
        prev = proto.get("mcp_app") or {}
        proto["mcp_app"] = {"path": out_path, "file": file_name, "port": port,
                            "url": f"http://127.0.0.1:{port}/mcp",
                            "ui_uri": f"ui://{uniq}/app.html",
                            "tools": ["open_demo"] + [c["key"] for c in caps],
                            "pid": prev.get("pid"),
                            "sha256": _sha256_text(source), "at": _now()}

        op = (kwargs.get("op") or "generate").lower()
        pid_file = os.path.join(cubby, "exports", "mcp_app.pid")
        running = _http_ok(f"http://127.0.0.1:{port}/")

        if op == "down":
            stopped = None
            if running and os.path.isfile(pid_file):
                try:
                    pid = int(open(pid_file).read().strip())
                    cmd = subprocess.run(["ps", "-p", str(pid), "-o", "command="],
                                         capture_output=True, text=True,
                                         timeout=10).stdout
                    if "mcp_app_server" in cmd:
                        os.kill(pid, 15)
                        stopped = pid
                except (OSError, ValueError, subprocess.SubprocessError):
                    pass
            if os.path.isfile(pid_file):
                os.remove(pid_file)
            # flip the demo iframe back: live twin if it is up, else scripted
            twin = proto.get("twin") or {}
            if twin.get("chat_url") and self._twin_health(proto):
                self._regen_html(cubby, proto, mode="live",
                                 api_url=twin["chat_url"])
            else:
                self._regen_html(cubby, proto, mode="scripted")
            self._save(cubby, proto)
            return self._env("mcp_app", "success", cubby=slug, op="down",
                             stopped_pid=stopped,
                             note="MCP App server stopped; the demo iframe is back to "
                                  + proto["html"]["mode"] + " mode.")

        if op == "up":
            if running and os.path.isfile(pid_file):
                # restart so the freshly baked server/widget is what serves
                try:
                    pid = int(open(pid_file).read().strip())
                    cmd = subprocess.run(["ps", "-p", str(pid), "-o", "command="],
                                         capture_output=True, text=True,
                                         timeout=10).stdout
                    if "mcp_app_server" in cmd:
                        os.kill(pid, 15)
                        time.sleep(0.6)
                        running = False
                except (OSError, ValueError, subprocess.SubprocessError):
                    pass
            if not running:
                log_path = os.path.join(cubby, "exports",
                                        f"{slug.replace('-', '_')}_mcp_app.log")
                with open(log_path, "ab") as logf:
                    p = subprocess.Popen(
                        [sys.executable or "python3", "-u", out_path],
                        env={**os.environ, "PORT": str(port)},
                        stdout=logf, stderr=logf, start_new_session=True)
                _write_text(pid_file, str(p.pid))
                proto["mcp_app"]["pid"] = p.pid
                for _ in range(20):
                    if _http_ok(f"http://127.0.0.1:{port}/"):
                        running = True
                        break
                    if p.poll() is not None:
                        return self._env("mcp_app", "error", cubby=slug,
                                         error=f"MCP server exited on boot - see {log_path}")
                    time.sleep(0.5)
                if not running:
                    return self._env("mcp_app", "error", cubby=slug,
                                     error=f"MCP server not healthy within 10s - see {log_path}")
            # the Copilot Studio mock: the demo iframe now speaks REAL MCP to
            # the local server and renders the ui:// widget inline.
            paths = self._regen_html(cubby, proto, mode="mcp",
                                     api_url=proto["mcp_app"]["url"])
            self._save(cubby, proto)
            return self._env(
                "mcp_app", "success", cubby=slug, op="up",
                url=proto["mcp_app"]["url"], port=port,
                tools=proto["mcp_app"]["tools"], rapplication=paths["shell"],
                note=("MCP App server is up and the demo iframe is now the Copilot "
                      "Studio MOCK: messages route to real MCP tools/call against "
                      "the local server, and UI-bearing tools render their ui:// "
                      "widget inline - iterate the MCP app locally like everything "
                      "else. Say 'show me the demo' in the demo panel to see the "
                      "widget. Flip back with twin op=up (live) or mcp_app op=down."))

        # default: generate only (keep whatever mode the iframe is in)
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "mcp_app", "success", cubby=slug, path=out_path, port=port,
            tools=proto["mcp_app"]["tools"], ui_uri=proto["mcp_app"]["ui_uri"],
            note=(f"single-file MCP App server generated (stdlib only). mcp_app op=up "
                  "starts it locally AND flips the demo iframe into the Copilot "
                  f"Studio mock. For the real thing: python3 {out_path} ; expose "
                  f"with: devtunnel host -p {port} --allow-anonymous ; add "
                  "<tunnel>/mcp as a Model Context Protocol tool in Copilot Studio. "
                  "Also added to the rapplication downloads."))

    # ---- deployment credentials: import / export / status --------------------
    def _creds_extract(self, obj):
        if isinstance(obj, str):
            try:
                obj = json.loads(obj)
            except ValueError:
                return None
        if not isinstance(obj, dict):
            return None
        vals = obj.get("Values", obj)
        keys = ("DYNAMICS_365_CLIENT_ID", "DYNAMICS_365_CLIENT_SECRET",
                "DYNAMICS_365_TENANT_ID", "DYNAMICS_365_RESOURCE")
        if not all(vals.get(k) for k in keys):
            return None
        return {k: vals[k] for k in keys}

    def _creds_path(self, kwargs):
        return os.path.join(self._home(kwargs), ".rapp_deploy_settings.json")

    def _credentials(self, kwargs):
        op = (kwargs.get("op") or "status").lower()
        saved_path = self._creds_path(kwargs)
        if op == "import":
            raw = kwargs.get("credentials")
            src = kwargs.get("credentials_path") or kwargs.get("path")
            if not raw and src:
                raw = _read_json(os.path.expanduser(src))
            vals = self._creds_extract(raw)
            if not vals:
                return self._env(
                    "credentials", "error",
                    error=("could not read the 4 required values. Provide a "
                           "local.settings.json-shaped file (credentials_path=) or "
                           "object (credentials=) holding DYNAMICS_365_CLIENT_ID, "
                           "DYNAMICS_365_CLIENT_SECRET, DYNAMICS_365_TENANT_ID and "
                           "DYNAMICS_365_RESOURCE (your app registration + Power "
                           "Platform environment)."))
            _write_json(saved_path, {"IsEncrypted": False, "Values": vals})
            return self._env(
                "credentials", "success", op="import", saved=saved_path,
                resource=vals["DYNAMICS_365_RESOURCE"],
                client_id=vals["DYNAMICS_365_CLIENT_ID"], client_secret="***",
                note="saved locally - Copilot Studio deploys are now autonomous "
                     "(no device login). The secret never leaves this machine.")
        if op == "download":
            # raw values for a CLIENT-SIDE file save by the rapplication's
            # static export button. Contains the secret by design - the
            # transport is the localhost twin or an authenticated cloud
            # session (/perform), never a chat message.
            vals = self._creds_extract(_read_json(saved_path))
            if not vals:
                return self._env("credentials", "empty", op="download",
                                 note=f"nothing saved at {saved_path} - "
                                      "credentials op=import first.")
            return self._env(
                "credentials", "success", op="download",
                settings={"IsEncrypted": False, "Values": vals},
                filename="t2p_deploy.local.settings.json",
                note="hand straight to a file save; keep out of chats and repos.")
        if op == "export":
            current = _read_json(saved_path)
            vals = self._creds_extract(current)
            if not vals:
                return self._env("credentials", "empty", op="export",
                                 note=f"nothing saved at {saved_path} - "
                                      "credentials op=import first.")
            dest = os.path.expanduser(
                kwargs.get("path")
                or os.path.join(self._home(kwargs), "Desktop",
                                "rapp_deploy.local.settings.json"))
            _write_json(dest, {"IsEncrypted": False, "Values": vals})
            return self._env(
                "credentials", "success", op="export", exported=dest,
                resource=vals["DYNAMICS_365_RESOURCE"], client_secret="***",
                note=("written as a local.settings.json you can import on another "
                      "machine (credentials op=import credentials_path=...). It "
                      "contains the client secret - keep it OUT of repos, cubbies "
                      "and eggs."))
        # status
        vals = self._creds_extract(_read_json(saved_path))
        if not vals:
            return self._env("credentials", "success", op="status", found=False,
                             note="no deployment credentials saved - credentials "
                                  "op=import credentials_path=<your local.settings.json>. "
                                  "Without them, deploy falls back to a device-login code.")
        return self._env("credentials", "success", op="status", found=True,
                         source=saved_path,
                         resource=vals["DYNAMICS_365_RESOURCE"],
                         client_id=vals["DYNAMICS_365_CLIENT_ID"],
                         client_secret="***")

    # ---- drive: play the twin THROUGH the open rapplication, like a user ----
    def _drive(self, kwargs):
        """Send turns to the live twin and stream each sent/answered pair into
        the open Copilot frame - the UI plays it like a ghost user typing."""
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        twin = proto.get("twin") or {}
        chat_url = (kwargs.get("twin_url") or twin.get("chat_url") or "").rstrip("/")
        if chat_url and not chat_url.endswith("/chat"):
            chat_url += "/chat"
        if not chat_url:
            return self._env("drive", "error", cubby=slug,
                             error="no twin to drive - twin op=up first (or pass twin_url=).")
        if not kwargs.get("twin_url") and not self._twin_health(proto):
            return self._env("drive", "error", cubby=slug,
                             error="the twin is not running - twin op=up first.")
        if kwargs.get("user_input"):
            msgs = [str(kwargs["user_input"])]
        else:
            n = int(kwargs.get("turns") or 0) or len(proto["demo_script"])
            msgs = [t["user"] for t in proto["demo_script"][:n]]
        started = _now()
        html_state = proto.get("html") or {}
        turns, history = [], []
        for m in msgs:
            data, err2 = _post_json(chat_url, {
                "user_input": m, "conversation_history": history[-10:],
                "session_id": f"t2p-drive-{slug}"}, timeout=120)
            text = ("" if err2 else
                    (data.get("response") or data.get("assistant_response") or "")
                    .split("|||VOICE|||")[0].strip())
            if err2:
                text = f"(twin error: {err2})"
            history += [{"role": "user", "content": m},
                        {"role": "assistant", "content": text}]
            turns.append({"user": m, "actual": text[:1500],
                          "passed": not err2, "score": None})
            proto["last_test_replay"] = {
                "target": "drive", "at": started, "done": False,
                "passed": sum(1 for t in turns if t["passed"]),
                "total": len(msgs), "turns": list(turns)}
            # each exchange lands in the bytecode; the open page plays it live
            self._regen_html(cubby, proto,
                             mode=html_state.get("mode") or "scripted",
                             api_url=html_state.get("api_url") or "")
        proto["last_test_replay"]["done"] = True
        self._journal_exchanges(proto)
        self._regen_html(cubby, proto, mode=html_state.get("mode") or "scripted",
                         api_url=html_state.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "drive", "success", cubby=slug, turns=len(turns),
            replies=[{"user": t["user"], "reply": t["actual"][:160]}
                     for t in turns],
            note="the open rapplication played the whole exchange in the "
                 "Copilot frame, live - like a user driving it. Replay last "
                 "test re-plays it on demand.")

    # ---- export: the factory singleton + THE GATE ---------------------------
    def _export(self, kwargs):
        slug, cubby, proto, err = self._resolve(kwargs)
        if err:
            return err
        if (proto.get("gate") or {}).get("stopped"):
            return self._env("export", "gated", cubby=slug,
                             export=proto.get("export"),
                             note="already exported and gated - the factory singleton is the handoff artifact.")
        if not proto.get("agents_built"):
            return self._env("export", "error", cubby=slug,
                             error="nothing to export - action=build first.")
        tests = proto.get("tests") or {}
        if not (tests.get("local") or {}).get("passed"):
            return self._env("export", "refused", cubby=slug,
                             error="export requires a passing local twin run (action=test target=local).")
        if not (tests.get("twin") or {}).get("passed") and not kwargs.get("skip_twin"):
            return self._env("export", "refused", cubby=slug,
                             error=("export requires a passing live twin run (action=test "
                                    "target=twin), or pass skip_twin=true to gate on the "
                                    "local run only."))

        slug_camel = _camel(slug)
        member_sources, member_class_names = [], []
        agents_dir = os.path.join(cubby, "agents")
        for rec in proto["agents_built"]:
            with open(os.path.join(agents_dir, rec["file"]), encoding="utf-8") as f:
                source = f.read()
            # strip each member's docstring header + import block; the factory
            # carries ONE import block at the top.
            body = source.split(AGENT_IMPORT_BLOCK, 1)[-1].strip("\n")
            member_sources.append(body)
            member_class_names.append(rec["class"])

        factory_class = f"{slug_camel}FactoryAgent"
        factory_name = f"{slug_camel}Factory"
        factory_source = FACTORY_TEMPLATE.format(
            display_name=proto["display_name"],
            slug=slug,
            generated_at=_now(),
            import_block=AGENT_IMPORT_BLOCK,
            member_classes="\n\n".join(member_sources),
            member_class_names=", ".join(member_class_names),
            factory_class=factory_class,
            factory_name=factory_name,
        )
        out_name = f"{slug.replace('-', '_')}_factory_agent.py"
        out_path = os.path.join(cubby, "exports", out_name)
        compile(factory_source, out_name, "exec")  # must be valid standalone python
        _write_text(out_path, factory_source)
        sha = _sha256_text(factory_source)
        proto["export"] = {"path": out_path, "file": out_name, "sha256": sha,
                           "factory_class": factory_class,
                           "factory_name": factory_name,
                           "members": member_class_names, "at": _now()}
        proto["stage"] = "exported"
        if "export" not in proto["stages_done"]:
            proto["stages_done"].append("export")
        proto["gate"] = {
            "stopped": True,
            "note": ("GATE: pipeline stopped at export. The factory singleton is the "
                     "handoff artifact for the next stage of the process."),
            "at": _now()}
        # refresh the rapplication so the factory singleton appears in the
        # take-with-you downloads alongside the agent.pys and demo script.
        html = proto.get("html") or {}
        self._regen_html(cubby, proto, mode=html.get("mode") or "scripted",
                         api_url=html.get("api_url") or "")
        self._save(cubby, proto)
        return self._env(
            "export", "success", cubby=slug, factory=out_path, sha256=sha,
            factory_class=factory_class, members=member_class_names,
            stage="exported", gated=True,
            note=("THE GATE: pipeline stopped here by design. "
                  f"{out_name} is one self-contained agent.py carrying the whole "
                  "prototype (drop it into any brainstem's agents/ or feed it to the "
                  "next stage, e.g. the Copilot Studio packaging pipeline)."))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
