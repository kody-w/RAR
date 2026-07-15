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
    "version": "1.0.1",
    "display_name": "Transcript2Prototype",
    "description": ("Transcript -> demo script -> injected M365 demo iframe -> "
                    "generated agent.pys -> local twin run -> live twin run -> "
                    "factory singleton export (gate). One cubby per prototype."),
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

# speaker labels like "Maria (Ops Lead):" / "Kunal:" at the start of a line -
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

// ── click-through tutorial: the Kunal proposal-generation demo ──
var TOUR = [
  { t: 'Welcome - the proposal generation walkthrough', target: null,
    x: 'This short tour trains you on the whole loop using Kunal\'s use case: start from the Proposal Generation template, have the brainstem make sure it also generates PDF proposals, then build, test, and deploy to Copilot Studio. Next walks you through; "Do this step" runs each step for real; Skip any time.' },
  { t: '1. Start from the template', target: '#tpl-select',
    x: 'Instead of pasting a transcript, pick "Proposal Generation Stack" from this dropdown. The pipeline snaps the prototype to it: capabilities, demo script and agent plan come from the template.',
    payload: ['The user picked the template "proposal_generation_stack" from the library dropdown. Run Transcript2Prototype action=template op=use template_id=proposal_generation_stack right away. Then say what was created and that the tour continues with the feedback step.',
              'Start a prototype from the Proposal Generation Stack template.'] },
  { t: '2. Ask for what is missing - in plain language', target: '#fb-input',
    x: 'Kunal also needs the agent to actually generate PDF proposals. Just ask for it here - the brainstem mutates the prototype: a new capability is added, the demo regenerates and the agents rebuild, live.',
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
                                                     "the AIBAST mcs_solution packager builds "
                                                     "the solution natively (the default).")},
                    "packager_path": {"type": "string",
                                      "description": ("deploy: dir containing wrapper_generator/"
                                                      "solution_packager.py (the AIBAST "
                                                      "utility). Default discovery: T2P_PACKAGER "
                                                      "env, then the known repo locations. "
                                                      "'off' disables it (skeleton fallback).")},
                    "publisher": {"type": "string",
                                  "description": ("deploy: solution publisher display "
                                                  "name (default: Microsoft Research "
                                                  "and Development, the AIBAST library "
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
                "schema": "rapp-rappid/3.0", "rappid": rappid,
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
        # the AIBAST library's established publisher (the same identity as
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
        """The AIBAST mcs_solution packager as a library - THE canonical
        solution builder (SolutionSpec -> SolutionPackager.package()).
        Discovery: packager_path= > T2P_PACKAGER env > the known repo
        locations. Returns the module or None (callers fall back)."""
        cands = [kwargs.get("packager_path"), os.environ.get("T2P_PACKAGER"),
                 os.path.expanduser(
                     "~/MSFTAIBASTRAPP/AIBAST-RAPP/mcs_pipeline/scripts"),
                 os.path.expanduser(
                     "~/MSFTAIBASTRAPP/AIBAST-RAPP/AIBAST_RAPP/scripts")]
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
        # 2. DEFAULT: the AIBAST mcs_solution packager - the canonical
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
                    borrowed = {"builder": "aibast_mcs_solution_packager",
                                "publisher": pub["display"], "fresh": display,
                                "capability_topics": [c["name"]
                                                      for c in a["capabilities"]]}
                except Exception as exc:  # noqa: BLE001
                    zip_bytes = None
                    borrowed = {"builder": "aibast_mcs_solution_packager",
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
