---
name: "rar-kody-w-transcript2prototype"
description: "Turns a business transcript into a working prototype \u2014 demo script, injected M365 demo iframe, generated agents, twin test runs, factory export."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/transcript2prototype", "rar_sha256": "8a6a12130be0fdac137a316a07076b917304e15242b8b81c609efcb1c6a4a3d1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.4", "author": "Kody Wildfeuer", "tags": ["rapplication", "pipeline", "prototype", "demo", "cubby", "factory", "twin", "m365"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `transcript2prototype_agent.py` and embedded as the fenced Python below (sha256 8a6a12130be0fdac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `transcript2prototype_agent.py` first:

```bash
python3 transcript2prototype_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 transcript2prototype_agent.py   # or on stdin
python3 transcript2prototype_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/transcript2prototype_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/transcript2prototype_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/transcript2prototype/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
