---
name: "rar-kody-w-twin-me"
description: "Pack a GENERIC, PII-stripped digital-twin egg of THIS brainstem so others can hatch your twin on their own machine and use it for anything. Call this whenever the user says 'twin me', 'make a twin egg', 'export my twin', or wants to share their twin. It strips ALL workspace memory, projects, customers, and secrets \u2014 only persona (soul + custom agents + calibration baseline) travels \u2014 and REFUSES if any PII would leak."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_me", "rar_sha256": "821f3c97589ab2bd5ab346d36a2458621f39d568f205b9391893308099efabed", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "twin-me", "pii-strip", "persona", "portable", "federation", "rapp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/twin_me`. The original RAPP
agent is preserved byte-for-byte in `twin_me_agent.py` and in the RCI capsule.

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

@kody-w/twin_me  —  "twin me"

Pack a GENERIC, PII-stripped digital-twin egg of the current brainstem, hatchable
on anyone else's locally-running brainstem.

Drop this one file into a brainstem's agents/ folder, restart, and the LLM gets a
`TwinMe` tool. Say "twin me" and it emits a portable `.egg` cartridge that carries
ONLY your persona — your soul.md voice, your custom capability agents, the standard
memory pair, and a calibration baseline — with EVERY trace of your workspace data
left behind:

  EXCLUDED wholesale (never enters the egg):
    .brainstem_data/  (the memory corpus — facts, customers, projects)
    conversations/  ·  private/  ·  soul_history/  ·  _versions/
    secrets: .lineage_key · .copilot_token · .copilot_session · .env · voice.zip

  CONTENT-SCANNED (the persona files that DO travel):
    soul.md  ·  rappid.json  ·  agents/*.py

A content PII gate (emails / phones / SSNs / GitHub tokens / secret assignments,
with the canonical allowlist) runs over every file that would travel. If anything
trips, `twin me` REFUSES and tells you exactly where — it never ships a leak
(refusal-is-a-feature, CONSTITUTION Art. XLIV / L). The result is a generic snapshot
of *who you are* that wakes up on another device with NO access to *what you've
worked on*.

The egg is `brainstem-egg/2.1` (repo/ layout) and also declares `scale: twin`, so the
shipped `@kody-w/twin_egg_hatcher` and `@rapp/egg_hatcher` hatch it unchanged into
`~/.rapp/twins/<hash>/`.

CLI:
    python twin_me_agent.py twin-me                  # full generic twin egg of ./ (or $SOUL_PATH dir)
    python twin_me_agent.py twin-me --flavor basic   # persona only (no custom agents)
    python twin_me_agent.py audit                    # scan + report, write nothing
    python twin_me_agent.py hatch --egg twin.egg     # materialize into ~/.rapp/twins/<hash>/

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "twin_me/pack = build the egg; audit = scan + report only; hatch = materialize a received egg; status = list local eggs/twins.",
      "enum": [
        "twin_me",
        "pack",
        "audit",
        "hatch",
        "status"
      ],
      "type": "string"
    },
    "display_name": {
      "description": "Optional display name for the twin.",
      "type": "string"
    },
    "dry_run": {
      "description": "Scan and report without writing the egg.",
      "type": "boolean"
    },
    "egg": {
      "description": "For action=hatch: path to a .egg to materialize.",
      "type": "string"
    },
    "flavor": {
      "description": "basic = persona only (soul + memory agents); full = + your custom agents. Default full.",
      "enum": [
        "basic",
        "full"
      ],
      "type": "string"
    },
    "redact": {
      "description": "If true, auto-redact any PII found instead of refusing. Default false.",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_me_agent.py` and embedded as the fenced Python below (sha256 821f3c97589ab2bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_me_agent.py` first:

```bash
python3 twin_me_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 twin_me_agent.py   # or on stdin
python3 twin_me_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
#!/usr/bin/env python3
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/twin_me_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/twin_me_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/twin_me/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
@kody-w/twin_me  —  "twin me"

Pack a GENERIC, PII-stripped digital-twin egg of the current brainstem, hatchable
on anyone else's locally-running brainstem.

Drop this one file into a brainstem's agents/ folder, restart, and the LLM gets a
`TwinMe` tool. Say "twin me" and it emits a portable `.egg` cartridge that carries
ONLY your persona — your soul.md voice, your custom capability agents, the standard
memory pair, and a calibration baseline — with EVERY trace of your workspace data
left behind:

  EXCLUDED wholesale (never enters the egg):
    .brainstem_data/  (the memory corpus — facts, customers, projects)
    conversations/  ·  private/  ·  soul_history/  ·  _versions/
    secrets: .lineage_key · .copilot_token · .copilot_session · .env · voice.zip

  CONTENT-SCANNED (the persona files that DO travel):
    soul.md  ·  rappid.json  ·  agents/*.py

A content PII gate (emails / phones / SSNs / GitHub tokens / secret assignments,
with the canonical allowlist) runs over every file that would travel. If anything
trips, `twin me` REFUSES and tells you exactly where — it never ships a leak
(refusal-is-a-feature, CONSTITUTION Art. XLIV / L). The result is a generic snapshot
of *who you are* that wakes up on another device with NO access to *what you've
worked on*.

The egg is `brainstem-egg/2.1` (repo/ layout) and also declares `scale: twin`, so the
shipped `@kody-w/twin_egg_hatcher` and `@rapp/egg_hatcher` hatch it unchanged into
`~/.rapp/twins/<hash>/`.

CLI:
    python twin_me_agent.py twin-me                  # full generic twin egg of ./ (or $SOUL_PATH dir)
    python twin_me_agent.py twin-me --flavor basic   # persona only (no custom agents)
    python twin_me_agent.py audit                    # scan + report, write nothing
    python twin_me_agent.py hatch --egg twin.egg     # materialize into ~/.rapp/twins/<hash>/
"""
from __future__ import annotations

import os
import re
import io
import sys
import json
import time
import zipfile
import hashlib
import argparse
import base64
from datetime import datetime, timezone
from pathlib import Path

# BasicAgent resolves in a brainstem (agents.basic_agent), standalone (basic_agent),
# or falls back to a minimal shim for tests / RAR.
try:
    from agents.basic_agent import BasicAgent  # in-brainstem
except Exception:
    try:
        from basic_agent import BasicAgent  # alongside basic_agent.py
    except Exception:
        class BasicAgent:  # minimal fallback
            def __init__(self, name=None, metadata=None):
                if name is not None:
                    self.name = name
                if metadata is not None:
                    self.metadata = metadata

            def perform(self, **kwargs):
                return "Not implemented."

            def to_tool(self):
                return {"type": "function", "function": {
                    "name": getattr(self, "name", "BasicAgent"),
                    "description": getattr(self, "metadata", {}).get("description", ""),
                    "parameters": getattr(self, "metadata", {}).get("parameters", {})}}


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/twin_me",
    "version": "1.0.3",
    "display_name": "TwinMe",
    "description": (
        "Packs a PII-stripped .egg of the current brainstem's persona, custom agents, and calibration baseline, refusing if its content scan finds leaks."),
    "author": "Kody Wildfeuer",
    "tags": ["twin", "egg", "twin-me", "pii-strip", "persona", "portable", "federation", "rapp"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": "twin me",
}

PACKER = "@kody-w/twin_me"
EGG_SCHEMA = "brainstem-egg/2.1"
EGG_SCALE = "twin"
ORIGIN_RAPPID = "rappid:@kody-w/rapp:9a8f0a4b5a710e20f4d819a0f37d2a4c9f113b5e78fb3c29e70b54fff48a38f9"

# ── what NEVER travels ────────────────────────────────────────────────────────
EXCLUDE_DIR_NAMES = {
    ".git", "__pycache__", ".pytest_cache", "venv", ".venv", "node_modules",
    ".brainstem_data", "soul_history", "private", "conversations", "_versions",
}
EXCLUDE_FILE_NAMES = {
    ".lineage_key", ".copilot_token", ".copilot_session", ".env", ".env.local",
    "voice.zip", ".DS_Store", "Thumbs.db",
}
EXCLUDE_SUFFIXES = (".pyc", ".pyo", ".lock", ".tmp")
# Infra kernel agents the host already ships — not persona, don't travel.
KERNEL_INFRA_AGENTS = {"learn_new_agent.py", "swarm_factory_agent.py", "hacker_news_agent.py"}
# Generic, PII-free kernel files we DO ship so a booted twin can import + remember.
ALWAYS_SHIP_AGENTS = {"basic_agent.py", "context_memory_agent.py", "manage_memory_agent.py"}

# ── PII gate (vendored from kody-w/rapp-egg-hub/scripts/pii_gate.py) ───────────
ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(
    r"(?<!\d)(?:\+1[\s.\-]?)?(?:\(\d{3}\)\s?|\d{3}[\s.\-])\d{3}[\s.\-]\d{4}(?!\d)")
SSN_RE = re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")
GH_TOKEN_RE = re.compile(r"\bgh[opsur]_[A-Za-z0-9]{20,}\b")
GH_PAT_RE = re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")
AWS_KEY_RE = re.compile(r"\bAKIA[0-9A-Z]{16}\b")
SECRET_ASSIGN_RE = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|passwd|client[_-]?secret|access[_-]?key)\b"
    r"\s*[:=]\s*['\"]?([^\s'\"]{8,})['\"]?")
_SECRET_PLACEHOLDERS = {
    "none", "null", "placeholder", "changeme", "your_key_here", "yourtokenhere",
    "xxx", "xxxx", "...", "example", "redacted", "true", "false", "undefined",
}


def _email_allowed(addr: str) -> bool:
    a = addr.lower()
    if a.startswith("noreply@") or a.startswith("git@github.com"):
        return True
    for frag in ("@rapp", "@microsoft.com", "@example.com", "@example.org",
                 "@users.noreply.github.com"):
        if frag in a:
            return True
    if re.match(r"^[0-9a-f]{16,64}@github\.com$", a):  # rappid anchor
        return True
    return False


def _mask(s: str) -> str:
    s = s.strip()
    if len(s) <= 6:
        return (s[:1] or "?") + "***"
    return s[:3] + "***" + s[-2:]


def scan_text(text: str, location: str) -> list:
    """Return [(location, kind, masked_value), ...] of PII / secret findings."""
    findings = []
    iso_spans = [m.span() for m in ISO_DATE_RE.finditer(text)]

    def _in_iso(span):
        return any(a <= span[0] and span[1] <= b for a, b in iso_spans)

    for m in EMAIL_RE.finditer(text):
        if not _email_allowed(m.group(0)):
            findings.append((location, "email", _mask(m.group(0))))
    for m in PHONE_RE.finditer(text):
        findings.append((location, "phone", _mask(m.group(0))))
    for m in SSN_RE.finditer(text):
        if not _in_iso(m.span()):
            findings.append((location, "ssn", _mask(m.group(0))))
    for rex, kind in ((GH_TOKEN_RE, "github-token"), (GH_PAT_RE, "github-pat"),
                      (AWS_KEY_RE, "aws-key")):
        for m in rex.finditer(text):
            findings.append((location, kind, _mask(m.group(0))))
    for m in SECRET_ASSIGN_RE.finditer(text):
        val = m.group(2)
        low = val.lower()
        if low in _SECRET_PLACEHOLDERS or val.startswith("${") or val.startswith("<"):
            continue
        findings.append((location, "secret:" + m.group(1).lower().replace("-", "_"), _mask(val)))
    return findings


# ── helpers ───────────────────────────────────────────────────────────────────
def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _read_text(p: Path):
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        try:
            return p.read_bytes().decode("utf-8", "replace")
        except Exception:
            return None


def _slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (name or "twin").lower()).strip("-")
    return s or "twin"


def _hash_from_rappid(rappid: str) -> str:
    """Workspace hash from a rappid, across all three rappid grammars. Verbatim, never minted."""
    if not rappid:
        return hashlib.sha256(b"anon").hexdigest()[:32]
    m = re.match(r"^rappid:@[^:]+:([0-9a-fA-F]{16,})$", rappid)  # consolidated
    if m:
        return m.group(1)
    m = re.search(r":([0-9a-fA-F]{32})(?:@|$)", rappid)  # v2-long
    if m:
        return m.group(1)
    cleaned = re.sub(r"[^0-9a-zA-Z]", "", rappid)
    return cleaned[:32] if cleaned else hashlib.sha256(rappid.encode()).hexdigest()[:32]


def _resolve_workspace(kwargs) -> Path:
    ws = kwargs.get("_workspace_dir") or kwargs.get("workspace")
    if ws:
        return Path(ws).expanduser().resolve()
    soul = os.environ.get("SOUL_PATH")
    if soul and Path(soul).exists():
        return Path(soul).expanduser().resolve().parent
    here = Path(__file__).resolve()
    if here.parent.name == "agents":
        return here.parent.parent
    return Path.cwd().resolve()


def _agents_dir(ws: Path) -> Path:
    env = os.environ.get("AGENTS_PATH")
    if env and Path(env).exists():
        return Path(env).expanduser().resolve()
    return ws / "agents"


def _load_rappid(ws: Path, kwargs) -> dict:
    # When a workspace is explicitly chosen (--workspace / test hook), its own
    # rappid.json wins. Otherwise the running organism identity (~/.brainstem) does.
    explicit_ws = bool(kwargs.get("_workspace_dir") or kwargs.get("workspace"))
    home_id = Path.home() / ".brainstem" / "rappid.json"
    candidates = [ws / "rappid.json", home_id] if explicit_ws else [home_id, ws / "rappid.json"]
    src = kwargs.get("_rappid_path")
    if src:
        candidates.insert(0, Path(src).expanduser())
    for c in candidates:
        try:
            if c.exists():
                return json.loads(c.read_text(encoding="utf-8"))
        except Exception:
            continue
    owner = (os.environ.get("GITHUB_USER") or os.environ.get("USER") or "operator").lower()
    owner = re.sub(r"[^a-z0-9]+", "-", owner).strip("-") or "operator"
    # Keyless mint (spec §6.2): Hb("rapp/1:rappid", uuid4) — never a hash of the
    # name (a name-hash address is the cardinal sin the spec exists to end).
    import uuid
    h = hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()
    return {
        "schema": "rapp/1",
        "rappid": f"rappid:@{owner}/twin:{h}",
        "parent_rappid": ORIGIN_RAPPID,
        "kind": "personal",
        "name": "twin",
        "owner": owner,
        "minted_at": _now(),
        "notes": "Generic twin identity minted by @kody-w/twin_me (no prior rappid found).",
        "_minted_generic": True,
    }


_RAPPID_KEEP_KEYS = (
    "schema", "rappid", "parent_rappid", "kind", "name", "display_name",
    "namespace", "owner", "repo", "host", "born_at", "minted_at",
)


def _sanitize_rappid(rappid_json: dict) -> dict:
    out = {k: rappid_json[k] for k in _RAPPID_KEEP_KEYS if k in rappid_json}
    out.setdefault("schema", "rapp/1")
    return out


def _brainstem_version(ws: Path) -> str:
    for cand in (ws / "VERSION", ws.parent / "VERSION",
                 Path(__file__).resolve().parents[2] / "rapp_brainstem" / "VERSION"):
        try:
            if cand.exists():
                return cand.read_text(encoding="utf-8").strip()
        except Exception:
            continue
    return "unknown"


class TwinMeRefusal(Exception):
    def __init__(self, report: dict):
        super().__init__(report.get("error", "refused"))
        self.report = report


# ── pack ────────────────────────────────────────────────────────────────────
def pack_twin(kwargs) -> dict:
    flavor = (kwargs.get("flavor") or "full").lower()
    if flavor not in ("basic", "full"):
        flavor = "full"
    dry_run = bool(kwargs.get("dry_run"))
    redact = bool(kwargs.get("redact"))

    ws = _resolve_workspace(kwargs)
    rappid_json_raw = _load_rappid(ws, kwargs)
    rappid = rappid_json_raw.get("rappid", "")
    name = rappid_json_raw.get("name") or _slugify(rappid_json_raw.get("display_name") or "twin")
    display_name = kwargs.get("display_name") or rappid_json_raw.get("display_name") or name
    owner = rappid_json_raw.get("owner") or (os.environ.get("GITHUB_USER") or "").lower()

    soul_path = Path(os.environ.get("SOUL_PATH") or (ws / "soul.md"))
    soul = _read_text(soul_path) if soul_path.exists() else None
    if not soul:
        return {"ok": False, "error": f"No soul.md found (looked at {soul_path}). "
                "A twin needs a persona — author soul.md first."}

    # ── select persona files that will travel ──────────────────────────
    travel: dict[str, str] = {}
    travel["repo/soul.md"] = soul
    travel["repo/rappid.json"] = json.dumps(_sanitize_rappid(rappid_json_raw), indent=2) + "\n"

    agents_dir = _agents_dir(ws)
    shipped_agents, excluded_agents = [], []
    if agents_dir.is_dir():
        for p in sorted(agents_dir.glob("*.py")):
            fn = p.name
            if fn in KERNEL_INFRA_AGENTS:
                excluded_agents.append(fn)
                continue
            is_kernel = fn in ALWAYS_SHIP_AGENTS
            if flavor == "basic" and not is_kernel:
                excluded_agents.append(fn)
                continue
            txt = _read_text(p)
            if txt is None:
                continue
            travel[f"repo/agents/{fn}"] = txt
            shipped_agents.append(fn)

    # ── PII gate over everything that will travel ──────────────────────
    findings = []
    for arc, text in list(travel.items()):
        findings.extend(scan_text(text, arc))
    redactions = []
    if findings:
        if redact and not dry_run:
            for arc, _text in list(travel.items()):
                t = travel[arc]
                for _loc, kind, masked in [f for f in findings if f[0] == arc]:
                    redactions.append({"file": arc, "kind": kind, "masked": masked})
                # redact by re-scanning and replacing concrete matches
                t = _redact_text(t)
                travel[arc] = t
            findings = []  # cleaned
        elif not dry_run:
            raise TwinMeRefusal({
                "ok": False,
                "refused": True,
                "error": "PII gate tripped — refusing to pack a leaky twin.",
                "findings": [{"file": f[0], "kind": f[1], "masked": f[2]} for f in findings],
                "remedy": ("Clean these from the persona files (soul.md / rappid.json / your "
                           "agents) and re-run, or pass redact=true to auto-redact. The egg "
                           "was NOT written."),
            })

    # ── calibration baseline + human manifest ──────────────────────────
    soul_sha = hashlib.sha256(travel["repo/soul.md"].encode("utf-8")).hexdigest()
    baseline = {
        "schema": "rapp-twin-baseline/1.0",
        "rappid": rappid,
        "flavor": flavor,
        "soul_sha256": soul_sha,
        "shipped_agents": shipped_agents,
        "packed_at": _now(),
        "packed_by": PACKER,
        "note": ("Baseline fingerprint of this twin at pack time. A hatched twin can compare "
                 "its running soul/agents against this to detect drift ('not at baseline') and "
                 "report back to the source twin over rapp-twin-chat/1.0."),
    }
    travel["repo/baseline.json"] = json.dumps(baseline, indent=2) + "\n"
    travel["repo/MANIFEST.md"] = _human_manifest(display_name, flavor, rappid, shipped_agents)

    # ── count what was stripped (for transparency) ─────────────────────
    stripped = _count_stripped(ws)
    stripped["agents_excluded"] = excluded_agents

    manifest = {
        "schema": EGG_SCHEMA,
        "type": "twin",
        "scale": EGG_SCALE,
        "rapp_egg_version": "2.0",
        "flavor": flavor,
        "generic": True,
        "pii_stripped": True,
        "bundled_repo": True,
        "bundled_state": False,
        "exported_at": _now(),
        "exported_by": PACKER,
        "source": {
            "rappid": rappid,
            "parent_rappid": rappid_json_raw.get("parent_rappid") or ORIGIN_RAPPID,
            "name": name,
        },
        "brainstem": {"version": _brainstem_version(ws)},
        "repo_file_count": len(travel),
        "soul_sha256": soul_sha,
        "stripped": stripped,
        "redactions": redactions,
        "implements": ["CONSTITUTION Art. XLIV (refusal-is-a-feature)",
                       "rapp-egg-hub SPEC §12 (no PII / secrets)"],
    }

    # ── build the egg ──────────────────────────────────────────────────
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("manifest.json", json.dumps(manifest, indent=2) + "\n")
        for arc, text in sorted(travel.items()):
            z.writestr(arc, text)
    blob = buf.getvalue()
    sha = hashlib.sha256(blob).hexdigest()

    plan = {
        "ok": True,
        "action": "audit" if dry_run else "twin_me",
        "flavor": flavor,
        "rappid": rappid,
        "display_name": display_name,
        "would_ship": sorted(travel.keys()),
        "stripped": stripped,
        "pii_findings": [{"file": f[0], "kind": f[1], "masked": f[2]} for f in findings],
        "egg_sha256": sha,
        "egg_size_bytes": len(blob),
    }
    if dry_run:
        plan["note"] = "Dry run / audit — nothing written. Persona is clean and ready to pack." \
            if not findings else "Dry run — PII findings above would cause a real pack to refuse."
        return plan

    # ── write egg + sidecar + html ─────────────────────────────────────
    out = kwargs.get("out")
    if out:
        egg_path = Path(out).expanduser().resolve()
    else:
        egg_path = Path.home() / ".rapp" / "eggs" / f"{_slugify(name)}-{flavor}-generic.egg"
    egg_path.parent.mkdir(parents=True, exist_ok=True)
    egg_path.write_bytes(blob)

    sidecar = _build_sidecar(slug=_slugify(name), rappid=rappid, name=name,
                             display_name=display_name, owner=owner,
                             kind=rappid_json_raw.get("kind") or "personal",
                             flavor=flavor, sha=sha, size=len(blob),
                             parent_rappid=rappid_json_raw.get("parent_rappid") or ORIGIN_RAPPID,
                             parent_repo=rappid_json_raw.get("repo"))
    sidecar_path = egg_path.with_suffix(".json")
    sidecar_path.write_text(json.dumps(sidecar, indent=2) + "\n", encoding="utf-8")

    html_path = egg_path.with_suffix(".html")
    html_path.write_text(_build_html(display_name, flavor, rappid, blob, sha), encoding="utf-8")

    return {
        "ok": True,
        "action": "twin_me",
        "flavor": flavor,
        "rappid": rappid,
        "display_name": display_name,
        "egg_path": str(egg_path),
        "egg_sha256": sha,
        "egg_size_bytes": len(blob),
        "sidecar_path": str(sidecar_path),
        "html_path": str(html_path),
        "shipped": sorted(travel.keys()),
        "stripped": stripped,
        "pii_stripped": True,
        "next": [
            "Share the .egg (AirDrop / link / USB).",
            f"On another brainstem: HatchTwinEgg(action='hatch', egg='{egg_path.name}')",
            "Or: python twin_egg_hatcher_agent.py hatch --egg <file>",
            "Then: Twin(action='boot', rappid_uuid='<rappid>') and Twin(action='chat', ...).",
        ],
    }


def _redact_text(text: str) -> str:
    out = text
    for rex in (EMAIL_RE,):
        out = rex.sub(lambda m: "[REDACTED-EMAIL]" if not _email_allowed(m.group(0)) else m.group(0), out)
    out = PHONE_RE.sub("[REDACTED-PHONE]", out)
    out = SSN_RE.sub("[REDACTED-SSN]", out)
    out = GH_TOKEN_RE.sub("[REDACTED-TOKEN]", out)
    out = GH_PAT_RE.sub("[REDACTED-TOKEN]", out)
    out = AWS_KEY_RE.sub("[REDACTED-KEY]", out)

    def _sec(m):
        val = m.group(2)
        if val.lower() in _SECRET_PLACEHOLDERS or val.startswith("${") or val.startswith("<"):
            return m.group(0)
        return m.group(0).replace(val, "[REDACTED-SECRET]")
    out = SECRET_ASSIGN_RE.sub(_sec, out)
    return out


def _count_stripped(ws: Path) -> dict:
    memory_files = conversation_files = secret_files = 0
    data_dirs = [ws / ".brainstem_data", ws / "utils" / ".brainstem_data"]
    for d in data_dirs:
        if d.is_dir():
            for p in d.rglob("*"):
                if p.is_file():
                    if "conversation" in str(p).lower():
                        conversation_files += 1
                    elif p.suffix == ".json":
                        memory_files += 1
    for fn in EXCLUDE_FILE_NAMES:
        if (ws / fn).exists():
            secret_files += 1
    return {"memory_files": memory_files, "conversation_files": conversation_files,
            "secret_files": secret_files}


def _human_manifest(display_name, flavor, rappid, agents) -> str:
    lines = [
        f"# {display_name} — generic twin ({flavor})",
        "",
        "This is a **generic, PII-stripped** digital twin. It carries persona only:",
        "soul.md (voice + working style), a calibration baseline, and the agents listed",
        "below. It has **no access** to the source workspace's memory, projects,",
        "customers, or secrets — those were stripped at pack time.",
        "",
        f"- rappid: `{rappid}`",
        f"- flavor: {flavor}",
        f"- packed_by: {PACKER}",
        "",
        "## Agents shipped",
    ]
    lines += [f"- {a}" for a in (agents or ["(persona only)"])]
    lines += [
        "",
        "## Hatch",
        "```",
        "HatchTwinEgg(action='hatch', egg='<this>.egg')",
        "Twin(action='boot', rappid_uuid='<rappid>')",
        "Twin(action='chat', rappid_uuid='<rappid>', message='hello')",
        "```",
        "",
    ]
    return "\n".join(lines)


def _build_sidecar(*, slug, rappid, name, display_name, owner, kind, flavor, sha, size,
                   parent_rappid, parent_repo) -> dict:
    sc = {
        "schema": "rapp-egg-hub-entry/2.0",
        "slug": slug,
        "rappid": rappid,
        "name": name,
        "display_name": display_name,
        "kind": kind,
        "description": (f"Generic, PII-stripped digital twin of {display_name} ({flavor} flavor). "
                        "Persona, voice, and custom agents only — no memory, projects, customers, "
                        "or secrets travel. Packed by @kody-w/twin_me; hatch on any local brainstem."),
        "tags": ["twin", "generic", "pii-stripped", "persona", "portable", flavor],
        "egg_schema": EGG_SCHEMA,
        "size_bytes": size,
        "sha256": sha,
        "packed_by": ("@" + owner) if owner else PACKER,
        "packed_at": _now(),
        "egg_path": f"eggs/{slug}.egg",
        "raw_url": f"https://raw.githubusercontent.com/kody-w/rapp-egg-hub/main/eggs/{slug}.egg",
        "lineage": {"parent_rappid": parent_rappid, "parent_repo": parent_repo},
        "pii_stripped": True,
        "generic": True,
        "flavor": flavor,
    }
    if owner:
        sc["github"] = f"https://github.com/{owner}"
    return sc


def _build_html(display_name, flavor, rappid, blob, sha) -> str:
    b64 = base64.b64encode(blob).decode("ascii")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{display_name} — generic twin</title>
<style>
 body{{margin:0;background:#0d1117;color:#e6edf3;font:16px/1.6 -apple-system,Segoe UI,sans-serif;display:flex;min-height:100vh;align-items:center;justify-content:center}}
 .card{{max-width:560px;padding:32px;border:1px solid #30363d;border-radius:16px;background:#161b22}}
 h1{{margin:0 0 4px;font-size:22px}} .k{{color:#8b949e;font-size:13px;word-break:break-all}}
 .b{{display:inline-block;margin:6px 6px 0 0;padding:2px 10px;border-radius:999px;background:#1f6feb22;color:#58a6ff;font-size:12px}}
 a.dl{{display:inline-block;margin-top:20px;padding:12px 18px;border-radius:10px;background:#238636;color:#fff;text-decoration:none;font-weight:600}}
 p{{color:#c9d1d9}}
</style></head><body><div class="card">
<h1>🧬 {display_name}</h1>
<div><span class="b">generic twin</span><span class="b">{flavor}</span><span class="b">PII-stripped</span></div>
<p>A generic snapshot of a person's persona — voice, working style, custom agents.
No memory, projects, customers, or secrets travel. Hatch it on your own locally-running
brainstem to summon this twin for assistance.</p>
<div class="k">rappid: {rappid}</div>
<div class="k">sha256: {sha}</div>
<a class="dl" href="data:application/octet-stream;base64,{b64}" download="{_slugify(display_name)}.egg">⬇ Download .egg</a>
<p class="k" style="margin-top:18px">Hatch: <code>HatchTwinEgg(action='hatch', egg='&lt;file&gt;.egg')</code></p>
</div></body></html>
"""


# ── hatch (self-contained; mirrors @kody-w/twin_egg_hatcher) ────────────────────
def hatch(kwargs) -> dict:
    egg = kwargs.get("egg") or kwargs.get("egg_path")
    if not egg:
        return {"ok": False, "error": "hatch requires egg=<path to .egg>"}
    egg_path = Path(egg).expanduser().resolve()
    if not egg_path.exists():
        return {"ok": False, "error": f"egg not found: {egg_path}"}
    blob = egg_path.read_bytes()
    z = zipfile.ZipFile(io.BytesIO(blob))
    names = set(z.namelist())
    manifest = {}
    for cand in ("manifest.json", "repo/manifest.json"):
        if cand in names:
            try:
                manifest = json.loads(z.read(cand).decode("utf-8"))
            except Exception:
                manifest = {}
            break

    # repo/ prefix per brainstem-egg/2.1, with flat fallback
    prefix = "repo/" if any(n.startswith("repo/") for n in names) else ""
    rappid_arc = prefix + "rappid.json"
    if rappid_arc not in names:
        return {"ok": False, "error": "egg has no rappid.json — not a twin egg"}
    rappid_json = json.loads(z.read(rappid_arc).decode("utf-8"))
    rappid = rappid_json.get("rappid", "")
    h = _hash_from_rappid(rappid)

    dest_root = kwargs.get("_dest_root") or (Path.home() / ".rapp" / "twins")
    dest = Path(dest_root).expanduser() / h
    already = (dest / "rappid.json").exists()
    (dest / "agents").mkdir(parents=True, exist_ok=True)
    (dest / ".brainstem_data").mkdir(parents=True, exist_ok=True)

    written = []
    for n in names:
        if prefix and not n.startswith(prefix):
            continue
        rel = n[len(prefix):] if prefix else n
        if not rel or rel.endswith("/") or rel == "manifest.json":
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(z.read(n))
        written.append(rel)

    receipt = {
        "schema": "rapp-hatch-receipt/1.0",
        "hatched_by": PACKER,
        "rappid": rappid,
        "manifest": manifest,
        "hatched_at": _now(),
        "workspace": str(dest),
        "files": sorted(written),
        "re_hatched": already,
        "generic": bool(manifest.get("generic")),
        "pii_stripped": bool(manifest.get("pii_stripped")),
    }
    (dest / "HATCH_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    return {
        "ok": True,
        "action": "hatch",
        "rappid": rappid,
        "workspace": str(dest),
        "files_written": sorted(written),
        "re_hatched": already,
        "next": [f"Twin(action='boot', rappid_uuid='{rappid}')",
                 f"Twin(action='chat', rappid_uuid='{rappid}', message='hello')"],
    }


def status(kwargs) -> dict:
    eggs_dir = Path(kwargs.get("_eggs_dir") or (Path.home() / ".rapp" / "eggs"))
    twins_dir = Path(kwargs.get("_dest_root") or (Path.home() / ".rapp" / "twins"))
    eggs = sorted(p.name for p in eggs_dir.glob("*.egg")) if eggs_dir.is_dir() else []
    twins = sorted(p.name for p in twins_dir.iterdir() if p.is_dir()) if twins_dir.is_dir() else []
    return {"ok": True, "action": "status", "packer": PACKER, "egg_schema": EGG_SCHEMA,
            "local_eggs": eggs, "hatched_twins": twins}


# ── agent ─────────────────────────────────────────────────────────────────────
class TwinMeAgent(BasicAgent):
    def __init__(self):
        self.name = "TwinMe"
        self.metadata = {
            "name": self.name,
            "description": (
                "Pack a GENERIC, PII-stripped digital-twin egg of THIS brainstem so others can "
                "hatch your twin on their own machine and use it for anything. Call this whenever "
                "the user says 'twin me', 'make a twin egg', 'export my twin', or wants to share "
                "their twin. It strips ALL workspace memory, projects, customers, and secrets — "
                "only persona (soul + custom agents + calibration baseline) travels — and REFUSES "
                "if any PII would leak."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["twin_me", "pack", "audit", "hatch", "status"],
                               "description": "twin_me/pack = build the egg; audit = scan + report only; "
                                              "hatch = materialize a received egg; status = list local eggs/twins."},
                    "flavor": {"type": "string", "enum": ["basic", "full"],
                               "description": "basic = persona only (soul + memory agents); "
                                              "full = + your custom agents. Default full."},
                    "display_name": {"type": "string", "description": "Optional display name for the twin."},
                    "egg": {"type": "string", "description": "For action=hatch: path to a .egg to materialize."},
                    "redact": {"type": "boolean",
                               "description": "If true, auto-redact any PII found instead of refusing. Default false."},
                    "dry_run": {"type": "boolean", "description": "Scan and report without writing the egg."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "twin_me").lower().replace("-", "_")
        try:
            if action in ("twin_me", "pack"):
                return json.dumps(pack_twin(kwargs), indent=2)
            if action == "audit":
                kwargs = dict(kwargs)
                kwargs["dry_run"] = True
                return json.dumps(pack_twin(kwargs), indent=2)
            if action == "hatch":
                return json.dumps(hatch(kwargs), indent=2)
            if action == "status":
                return json.dumps(status(kwargs), indent=2)
            return json.dumps({"ok": False, "error": f"unknown action '{action}'",
                               "actions": ["twin_me", "audit", "hatch", "status"]}, indent=2)
        except TwinMeRefusal as r:
            return json.dumps(r.report, indent=2)
        except Exception as e:  # never crash the brainstem turn
            return json.dumps({"ok": False, "error": str(e), "action": action}, indent=2)


# ── CLI ───────────────────────────────────────────────────────────────────────
def _main(argv=None):
    ap = argparse.ArgumentParser(prog="twin_me", description="Pack/audit/hatch a generic PII-stripped twin egg.")
    sub = ap.add_subparsers(dest="cmd")
    for cmd in ("twin-me", "pack", "audit"):
        sp = sub.add_parser(cmd)
        sp.add_argument("--flavor", choices=["basic", "full"], default="full")
        sp.add_argument("--workspace", default=None)
        sp.add_argument("--out", default=None)
        sp.add_argument("--display-name", default=None)
        sp.add_argument("--redact", action="store_true")
    hp = sub.add_parser("hatch")
    hp.add_argument("--egg", required=True)
    hp.add_argument("--dest", default=None)
    sub.add_parser("status")
    args = ap.parse_args(argv)

    agent = TwinMeAgent()
    if args.cmd in ("twin-me", "pack", "audit"):
        out = agent.perform(action="audit" if args.cmd == "audit" else "twin_me",
                            flavor=args.flavor, workspace=args.workspace, out=args.out,
                            display_name=args.display_name, redact=args.redact)
    elif args.cmd == "hatch":
        out = agent.perform(action="hatch", egg=args.egg, _dest_root=args.dest)
    elif args.cmd == "status":
        out = agent.perform(action="status")
    else:
        ap.print_help()
        return 0
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7W8CbOryJIm+Fdkt9rs5Ssyk33LmjfWgEAgdgQCVFmWySpA7KvQm5rfPqFzTuZbu7rbZubYtXskiPDw8HD//Pt0L/rzt2iZi2789tM3tUv3g1/WaZ4t2fjt+29pNiVj2c9l14LbVpQ8DtHhJBqiowjfHyxF+WGawf0+Sw9peS/nqP5h3sr2kN3vhy4/uLJyOcRjVLbTnDWHqTt0c5GN0yGJ2kMRzUlx2LtlPHzM6doDuFmOh25rD02UFGWbHaI2PSxTdijnQ96N4O0+g+v3Hw9CVNdgfDkdtiJrszUb37PfY8fDFO3T4Q8fRpvsD98f/tBED2Dq8Jtr70vZs+/G+dDsH1fBFWB9i9p5OszdYSqiMfvy5n37x4MyHz52Oh04TTts3fiY+ijJgP2mG/fvD/3YVVkyT98fkmWauwZs8vsP56csGTNg9ecFQ1ACbLLeDz2427XR4bupW+oD9DXlEN2z9/rgfVSXIGrvqB/iaMpqEIk/HuYxWrP6d0tv444oeRfxcijzd2Te5wFcW+r0UGfR40dwftkzavo6m7799O//8f23Erz+9tOfvyV1NIFL31ywNT3j3suCsXXU3sHFHkQYnPb334CXIOQNuJRm+eHr3XfAm/z7w7/+62OLxvv0x59+bg9fP1Hy4fCfDt993vvxns3f/fzt8/LP3/74jvDP397h/KXJwPsf627Lxu/++OOY9TWIJRj7w8/fvgdjfgF3/2J3Hve/WuX9897u52LgPL/7K5vvyeBYHmD+3015/4BzWMb2UIHY/5guTT999x77y3v2l8t//B5YTEE4/oT98X+05J/+BBaJlrScf/72Txb5NASikJbJ/JvZ/9Gwf//5Wzruv4wLiM9/gDnuuGT/v/r9UXP/1O9/XORj7P/uAtMczcv0v7jC5+D/6RL/OPHPP3/rwCH/dJCiesrep56NYze+r+Q/f1vaR/vGkC+//vDnzxf/+QeQIP/o1t/9/Jaw7z0c/v3vcuvr2L//SyS//6s9/8d//tMtZM8k6+fDZ7E5Wb5MUX2IpsP40/9sm+O7NABK/VdmxY9f730Ck9lPh8O/HD7RMBmjqfjAxL8A8HuB/xexBQj4XfbH7w9/KeqfvoL81zv/9p8AacB64/IZSAAg//IvB71Mxm7q8vlwSbplPoCcn0sQV+CP+0Zx8Oft6/j2fSrjOvsa9wWs7w2ChvLrf3+AFvXDBn8dy68/HlwwqxtB82lBWB3Osn5uP4D0bbEfM9APVtCd4n3OfgAA9sP7xRs2fv2y8MvH4B/7/dcPRC0/mtDBERSAwv201NmPbxd90GO+HHq3ruyZJQuwU3cAqg95CRD2e+D61NVr9tmUpkcJ+lNajsB30CA+bIMt//Q29uuvvwJUL35uP6EWP3z22AkGA3535/DDD8D7vC7vxfxzmyVFBxL5P/9w+L8O/9WsD+PvNSyA8F8BBR6eL6ZxAEW2NB8d5iMbovQjoH/+z68YAjMtSBsQ/jIvs8/JoPE8svS3gF5k7geMpA5xBgIJgti8cxM0Y9CcQYPMD7/7e/hM2wm03KKb5kOa9dk7OxLQbEHd/Nz+Hsm2A30VNLopBz303effq/76e8L+koDhvx50wQJduavfrRm4+TEITO7aEoT/9+NufycAf5gO/G8mfjwYH+XQR2PUF6AmPtfIo89zeXOKr+nAeARqZ/u5fffJ7B2qjxb8GR4wCEQm+TrSH95nfki6pgEHO/229seYaAbp5nYRWHz8uZ2+cvfNJ8DEDriyH+5LmUZtkv3bV0pNxUfTfsfvi8Z8nUL6dSofOfh3qX/4jQh8NdXDG6Q+j/5/k6V9hHMZx3cYfg/995/8LAKV+HP73kC7d4CPAQKSgfB+JH69//B2750Bv0/78PQ4dv1nGbynfITqK7y/jwM2PukODHhdnWbjR/3M0Rvs3rXy9knTdBDSdxqBtP6Ez18/8uDHwyXa/3rbn6U7H7Km/Mi6d/a9PT/8+iPY468gWUYQgPSefeTf++0IUvzn1jS08JOB/kbJvmL6ce3Nzn5s0sPalQkAwo9rX1QNYEMUl3U571/b+P7DY7CBNo1GUDGfvBBkXTl+bij6p6zut/W2ci4O4lV0wjfNA7wSHMvHen9hmmk0gzjUGUDQOAMcOP3AksNBDATNO4pHwIM7gEMR2PV3nx0A+PXm2m/HQBR+Y0Q//qW63ibhw+G794gvh5Nu7JffOea7Sv6W0v7Gc78aUdK1b7z+2BQ4SjAPQWL6AIaVKyiEv7ryDuYvICXeVfdXl3/5gPv35E+DX3T5p8OP7/CA2P7yyPbfRv+YdH1Zd/Mvc/cAePz3V6dsepv6/XrWrr+9/jjCH19l/xkzwTRc0XB/uAicYYDQfUTgtxT4gPPPRDmaX6z7t+D9lhK/+w9ApS/TH9/98y8XvzL7Xz8A+eeWe4dpflfXm6DfQVwO32VNVAIuDx96gOXZ+8XlYrx/ncpZXuLDxw7f7z8DApr7VN7bD/gGHOYjXf4GBQ+gHLutBvH94xszQOV9ZMAH3HwU4Md+PsXB55Y+IPs3PfVz+yFuvv9siyAZfv1dW3xUY1YDZ0FCgs4HUgJIGCC6xt+zF1TeZ8ZNxVshRR/y4+f2u/GT7PxQTj9EP+QZYEkjqCMQ/IuruJ6rgKbEjaB3BJpyBVvV/vjViTLQdz/6d/Q77E4t6MZFB3oHqIx/Ban+4Q1A1X/92hlQeNNh6Q8fUPWhMkHbWcGpf9aWYQKmkmTTh7wD88EUYOAPKwC3d4kBZOzaf/3xk418lMt7+b80oh/AFRj7Ef318N27t8GHOgLTQaw/SrsGwjbNgKoCnh9+ncBxACL2DuSv3781L3AGNILiE4D/lsEAs7984Gw2fvKPX//7O6Pgv7n+KZRBkJcWAHJ7z9IPOAWg+H/DP34Mf9ua4P+jAKzi/4R//diGoClfOfvJFw5/z3c+Lvzw7iN///Mvh3wB5OW30P91q/gRPnwHWuZ/u5ie9ovFufK7H/7xf22dH37I62gFswH4AbPvdX4ruQ9V/F3b/a0S/p/Y/SDj/4zC/wugRoCkQYff2PM2lqDm3lnxker/ldHPWP/wPu9P5f9+8Wm0AYU7lgDEX1/t7J9G/y2kQdaBxv/tpxaE8ftvbdRkv4vtt64GTKTJ3tD81uIAUEEU5jL7ePfJpt+v/vaTly8/4bfwAzoxXso6/Q3Y/+0rEn/6221/BPXfvjb0p7/xPnpTkax88+KP+Z8CBgx648cXqQU3ps+dfXyO0C7Nt5/+/Tc/PnaRPMCvj6XB749lwO9PU9/+4/tv896/t/1mHu39rQnScgI6f//lMx5/v0Pz40X05swfww7vYR+f+by3+XEU3/6Z0U/5/I/2Lu9YfLDuz2i8UeDNtd658GYsX8H7K6MxYBZZ1L6tghv/aFF6c8WP8/nTx25/At39DcNvXvORJuDVX0X5n7r7WQH/aPuzJP70dwXx9fHQV2v+Kop/+6zOP4Ebf81IPu/+eDhmefRGz/egvz65jxXA+/f1f3o8Y5aC3f2ja6BLACkHcDta5u6Hz1G/f9qUd8uHaPpdT3xA/scHdL878paR/yzMH2sOC+DT6efHU18DuvjNMN4ugTyYPz+C+vM3UDHRm6981cyXJgTDx2j8YXrTaBj9EQHLgPef5Qzu/R1l/ro7FRGQMeA2g6E5nrA0ybBRjMUpGcU4QaU4FWEEyVDvu2xKUkyOIWTM4izKsDiOMAjLgr3FwG2Q7+AIkuyXtxIo3yvGCZKjFBiZZxkbYxhOIUyGADsUnUdUhmNZyiCAJfxl6gNQua9tfLr9DszvwvUDFD538+dvMUWAkTIxKdznjwBDKIvhcbxrwd2koZJrMtM+T+I5bee5aR3c7+N5vEZaMN+SajiPOnf3HNu525zFScMFvT1RfAnl1zox5OIzL3yCzldma19H2qu9LhCqs3nDyJuCBkh5tmcUo9MFpaWMZm/jUZ8Ykbjcwx26bP6V8SbXITG6a2A4X+Ath0WIRXEasR03Ievuylyn/R4ge+lzK3EKBJ14II+ndHqUz8QDp6Kl+e2UO7g4dZ2brYNpDremNccRzbejBNdO0iezrp0uvg3rd4tMirWQJHVREEG8eqx4sQNTIuJhHNPEe1zkjkiPstbzDqk4OSlqY8xMtuU7XM2clAUXGo+NhPjiHPHncQ/XIxLJontmVvUGHWt1W+1SJoa82ihKfihPlRil5Cjc91FHNCLO45aijVt1VgSyUR7PWutVhBOrXSDb4mI56zQ9S+QGN86We1aXmK/Z2oYWLlovkOJji3XtxebDWZJ3USXqouHgQNuxvJReoskULTJn2NnAWucJt1jIl84lKl0uHl+EZiL1rvMjb7/8hHwqUHa9230vy0R9M0GGbhDBZjytFZsnoXL5oq7WSONSnZUtMTLmqolZTPKtSA5OQJOXIL3EeunK3AkptW16NrYvNeBkC/ycWLGsh54q8ayXZYtytGye1Xz3shY2y0UrTC+4MzmFfWUTMz0fSS8+h9JE2uaZbs1oboszqmuLMvYSdj9u6bZ4pRscOwLppjt2KcT58RLPZ9y6765eOIsivOqGkWN8YaEz+pTvuHo7U8dzcDajc7odIYaPPHQUSV1bZxiG1tZmiGo2e8XDlBXG43VbC0Kw7Cq1+pWbGpIRzGBhUnrE85wVXRqOcQhvHCecpEnZtvvDU4iKvNZY2io9ctESDtoVLisuctB2wrWYvexJq8ejkJH2QtQE+hKCUr2UFEzZgnSuz/t1jJ8mifm+1t7XsDN2a7vVWqzHPNbR7Or4TkH44oOT+Rd01rdHbCwFY95v95xU87sBBPUlM+/DvC+1DavdJXHQItAMdbLPlXTe2Ibdaszjbu6RgWzLPtZbo/t7/Hqx6/F+fMVPvnOkrD+1O1vGBXR+nR4Yp7IqvbvKilQNEtzdSlUoVd2ucIVw0g682HXNDHTapUVwEGVVlbZrnxXyjj880eTs5bzoykM5V0HCZ6K8wBi+wjwqPTbPLe2ZDyWsxtoS3lzn7tmXzPfQ+9W0jZNlPpHCqGg4XI7HHcaD8UzsthkO/aq8XorL8Ue9uAjCEGSynNnj2Vv3KV54USB978ybSLM/XwDEIvfIQzmvdzco809u3+4+Q0tn+fG68HagRkK0x5C5wqLEVRDIc69CCqJ9hux2pq4Dy8SiYgwKm7jVOUQGeRM5jLNXNgkaSYpJZemq+wwLCsszt2ZlGl66aDvDI+ptLTQVMtjSiZTqma5HAsaPHUw7O4sdN4bXXJtdo0LJ3WaF9QUvzdzS60hBAC4lgtpWD219MdWJUrzyBa9K+1po03oI6ZZO50A86c9oabnUaZWF9xUOqeGqosy7DdO7WVa5NkXCmTha1sl2MLlH6mRXo+OAsHTc3S83XYlEl0sf3Ro++ExiHwvNo5GXV5bkM0Uz6dLG70N047aiRs7mjpAUdMSKMqB7LZbOsATRrC93NFLhD2Lna97xb0Iw6SPH7GyjN/peqPgRPVtWxyV3TLqfyCeCP1i9RqQQ3teZz/fhGPYtH9z5RH7iq4wzBN6ytCpHr60wYYutYNnbLmloVI+yIvWSDGVb0fdyj8rjdpbWx6S5PUdYGR9xja2cLRy97UKCHPOkPCl7dOFqbxeZypz0E+RsdFI24s4J0tG957HNH8cQEjZ6kU5cRwXnPOOoJ/JCTctubfjMZkcrZN9DbpWtFJhiKgJ2P2lRg5+y7VG6p5PAO1UzcY/75JhCK9ecPD4Y+RGeEwY1JcpTV6uS5CbAyrEi2WqzkUHbW5mospt9Toxjcwx6zkgrim8eAjpFMzMd9SMKEJXgDZ1IAt7q9YYiqbLzrXv5InfYGuAMUymeQ92QfTV0SnGoLufyiAPUFGDshULcU7lTLNk3Mgmf7lneufKmZfdrwcq0CuoZNAV7A56TJronNCiMuzOVx7hLWOclDxz0GBRl0e8ldgLtCKkiAw7OF5OuzFovmPZ1JZ87Fjkhz8JYSYrMiD+a0q3M8L6wVo1U9VpCpZkovLpNd12Dx9S40IaRwfpQw07UQvUVuoWNXUNt4rw8tCakgWhhr7LvomBXzAlLH+Uun92K1yrmop9Eo8SfZwLJrIF0YBTmLrTIOjf+fsWHaIHvk22qqA0RJWgOprHXUf68PWayvfhXm/HvN+var06r4j3lxJWuJePN4XqES5BNuO3PAj0WoF738kxORzs0V92O+3aT8Z0rHgUo94xRH2PfisLsNlkxD4I0hxfKkDjsdgpE+tE9eZq9J0EBP15yvxpxxnhkm10d1cSG3RKeJXxzLvzxtOnLPHY3MfZHv+Rw0UmShpF48x7vd2eRaW24c96Lz+7jI5Hts7ml1MUJhbJxKHpDSDZDHHfosOR4QcbR8KenoaBt23upZ89YO17uLPY0UIO9ST12qvVjfz+OlpS8FhyGYU5TzBN0E5KKv9lR82wkVX2eNUlJdvb8bFokGDr6LOcRvVJp149FeBlvXZ9IdXIe0hZ2KJViox6ccqpyAaqXpepyshlD0rrEtinK9chTsn7e+Sd6KdG8ujSdCo/XNDt6Y37h1GGinQKzEIHP5lcKjQFAovU6zFYPHakwNkSPLZBtIiXh3pvH4NzJpbDvs9JGPLpm/WTeI9UmjHwWpH0GpTNzCgQVecGeIFsThwGKJ4pcLuWiJBP2kF3n4olLdxLyzLXD84lDVdi6DGGXXmn3Jp0YREVOlm3f5cjZDF7FlUcShc5pjDrGvGRBIba+onZ7wDXWpmRPnXVkka695kY5j+tWNPPLLkJlLAOukiEP1S95uVelmYrHDdng2kcFRxh5mnsgViaoppoOBffY2MqyO0c8eQZnaCuLnqJjTziZ89KKyaoZwaPbi+Rq5MhMSqNNVlapQnbq/PBycj0hdCd5U1LpFmgq2T7voSS6WVNBYVoNsjFKhCyYa0p3U86yxNFxr12vWTg0XmHW1Az8AdG+8bQ3+SLhoc5qQu6lKQXhOMTmUFlh2As+x2SjBXtnMrlMpIBKBfYrO7rQeS2wCDWWGCHywoOw9h69X+bFvPId07pUGvsbLOLMPLUILB/3/OZCGd5A51lGoBZBbtaduFm9R6XusvJK5j7FBll7xGphHaJOVaXR8DmnadAi8RvLTa8kPrHIcBEv0EqXEa8dtdxhcvumFpQV9FJME9XpwvN5Lz+6+NJSeSF228P1dDR7nkYsCNOHK8V5Xr7Cwr4cjfGuEKNja3BkscVon7DbnXOuT/syrZLYKBruJoQAy+2jOMrwxSnF6/p67dU2RiYjOLdpJU0rFxLbb7oNWgNQVG3J7+I1cYvY9OCHFpDwpWoEKNHWPn9gD7+UzdvZ1fzx4Tw8qMA5BCkfm7gJdFQg6lPA/IG43srSQLBb7OCh3aU0D9MQEa34AthwRPOpcJlMRhUnxjHIEGgtuyIUhG6sZ1XfV1TZuY0YdGwHYMoGnNmPxt0KmdBcAhvBfEYPxAYteN6fZeMII8VF1PnJ2Hn/OnbuAEkv8/nSXuY4yRYEQ5x7pG4rlB4D6RpfNcTTK21rctwePMXh1SUd0cctwy1kBGV1RwvW03xSeEJ3bq8tdDH5/ekzd3nzCzi2JTjF8PR1g+FuzNmdxSsrJyBdPRtciOt3famb15Q/n/CRQqLOglnUh2GEKEZPbscbjEgjfNNy+Ekd4VtswahlwTthWnCqyzi6rIzVVD1KAQ4G44s24zFLZEaXtKeJABp8SYFw0ReIxDeCseYHAZFzdU5ZfGWMh1Ty1GK1IUzOMGtX7DVJU6jjGwLHxFw3XAfxRQ0/dXoEFBDajBjUoTAMxMuaWL55gw13BtRjeppwoA66VhvgQicgtyZD5h1e+3tbF0YerTM9sTLcsXSOgSqx1gpeiDOqZKeeTeOKbnkkpTTgkgwvtIPk9LjBXlfFXf7EqK0UScYWbluDwuE51zX91ufScDQCyrntR1gI9tuTV51zCqRqWsEdOgu3jh6hxmDgU0iaTAKfHChHTDh/uE/2BcsB22v5wFQTh6DptlZrmMcyTi44v9M4LhWsbnN6e7tvviXLgXmulFNQS5GXOTRxRIXWtpRxRZBgqQJQnhB3xTO5JkvfD6gSBiAynybAEhXPuJ9fymO8XOOp6i7PY8sCHC05uXPqQVNo8jjbE7G06NPT28tR1/dTyN+aIJXgatmq291LR9ueGJqPyFHBOeuybIIVxB29yHzeXLCTTJPI4nfwVS8Fh0Z9nZNioBsduM+5nKMBjg5a3djXNtJVatSZO2vAVoc0Prk0SMfRYJGeIF6t8eo3/5y+SHnS6yXKOdYYAadoeyQ0h/SqyNKpE9yEdtztJMJC9iAiDnaccbECCvFGiy0tHJYmTlsax5hKRYwWRLwaJ8D8jtaIH3tWBOUIv5JXsl7vMazidqM98OVR38JRZFbxFc/lbbczAz3OZJkfx6uRKFumnPQLnwBBmidJdhI6xjI8iTkmMOUzlvv0HsPpSKvcnMAcwz956aQPoZGb1ZNUxfSJtxZ8o4ilJq1WMdWqlM5HOadawiDUeGK5i8OWTSjs97UKxWstFw6LmHZa1Cp8V5q8tVSdYV1LQiRhhMIMbi+0I/avQKw1o628k74N95Gk93s4hECvgXSQn8nNgO77RX2lXH7SnnsW9v4lRk4odx6ZBDkNdzF8As5pWPNJVZqL5ipDKDmdC3v6qYsTiEpvWb0TPolFO+D+Nm5LXuGjiLrZKMJRrtz7EoosqH+fTT4SWMfoSCGABaqa9J1Ks/Mg5XaZT1eGee0kH5J6UGmFGBhPLRCVV9Ae2bo+89ceqRJ7FBBZHF1rKwJe0+1kvncLU23DZtnmUdj4h3Y5L80lXht2eQY3wDuIDCiFBFKMwE3nxOPMK885TrBodKOhnNLRtmpzHO+z7QTTeaDx7kDjWYKBpHyF+6WPN5dyJfgkqDKy8mvq+ojcnklRKxdkz1/8LfMm+8ZF8qV/RYhMXe8DhbxOgxnDDHGZ/XB7UOE1rh1G5dmxpwEjpoMcqyf/8RQuWsjVo6QQ2PIkJw+2Tb7zDZrL4gZkjpu4hIxIvDcqWny5+6dwKpYIo7WITPkkF1Rs1W5nrdy6Pbm58mzhJ2p+FZsKIyj03CvMfnFFJUji6Vi7j3pVljJ9TG5QYRJa7qRvJR4T9KSE7FPQgrZSHJ1OgOv9qI3CfoO8dEU4Hsn3/hQ+HknDh11JDJBNXdXOjiXaR23+vuqS3DF9KyfG1eqTRhP4U/6KnOi0N4F1U01bSvlbQj4Zob6U5MWf5ps0vVouKmyiTfYToy+tlXqlLGZTPAeCX0n70wMa4eo/HHFttyDGX0/suVGnSyObOv64OU2y8zhw1Tfjc74kop97momezbV1QZXxiHSNUIyGpUudDTs9+PXelnDng2TOnoV4SamCb17JXR0b2fJD81ZNhl/gDZGH6iuu1hyu5/k1+iSEQM8CXyx9e9T3U0eggdopJ6g7SiLe2K+7hlNDKRaCl19kX1SdJ0arK2mYyKO0XX+LrbArQpJ5UO5dbRgYudOLf6NN/qrsNS3kS/O6F6h8ig1iMRjf9DxiZe63IeGOuLKwFFNoYt6VkdmK1/ujOcur428Z31clVQJa4crTUbSYiR+EcIgMe7YaWe7OR4FumNyf0/7EPmPeLNe+Db3AYZ8nlpVnYl1RSBQ5TYiiIS6N0rIFvcTJo4vf0eB2mjrhRc5JwV+R4RhUciGvWhPvop/NWpE3V9dxnj2VnWZ1GybxZhn7Sa+vNR2o/VIkoZI6L5Tgq7aHG+857u3IKVq3NXs7EGecyi7hs6nnx8uzaSZzJPmx3V/yJFz24SRgEBQYdug1z8vLOCLyFMLFHWCDl+K300UMdSsWfeRpLEqx73H9Ulf9/NLv9zLQ7P6hcrILtMdxsiZx6h836nLhdsOlpyPtxzjNbmWl9TezTyFJ6AUG5pzCijl2ESnoVBiF81ibU1jo7rQXfIWmg5/R/UgUdwRjQsK9pp37imK9Wo3Jm2EYSAvWeoGmg4WuSpFDZylcdn5c6eZmxfE8eYNfeN2SCtYtGvoQFwA5vQsY4g/GrVUucnrO6Ac5e5W2Dhx/NaTorvUmryyWn7LtCEM6JsvwZjn4umYpPkpJdzmj6B0XKuOySjmVTyc2PA2Y1gNty0rQEVaHZ/mKr3wovPgX6bkMe4GsNcMXT9tuC+2GdwoBajlFlvp5IiJAsejneeeySZM5z4Wv5xeH6CH8intMQ0RI7LyI3rvjmdOw0PDUYZeO9jI+o0YKeROHrkavvVxTeK5cX7xs1O846/G0Uy8/4XdR07i7t4qDPdGN4wf2wocv2X/e5NKQ2JrDjBCoNUR7ltO5BJT8tg+0aRkTPl5GR6OmzG8IolO67CmHuTnFapfku2UjGp+7QTYxav1k70QJj6x8ayNPLmwzQ1v39sD4EpcyffQ8hnjGe+44UdEnW4S/nJRYx1C06iE6+xdeN+8Y0Y2eUkbkhp0Yg6BnJeyPknn24EQv2hklLc+rhz3ML54a2z5gITJmKH1YUol9BCFlTIZ4OZro6ezpSrFVf0pMWsOUdSqHDfCh7lkC7dyfu9a5dbKF50I5NWXe9sxleU2PJJ62NOPNqy+g/lIZts5N3FmqThuXDQsnUSPPLahxs2tUZKSbMJYtVZGObh1vl/HOtiTNcBSOszQl8PSV7E9kELgjLZkv9DQzT8O2z37CqEt5CQCjDa9PjrjgDEYNqW1ZY3uHV/KMUuzlegsUEyKqSU2II9FeZJbcFuo2LNLZnhsXSkj1pvTP7RnspGK+VHRxqFdO1vVwOWcnEUDBuhcWjy2uueU5e8/K+7W5rah7TiT3Vcj6/shOpBYN971/ikGpjqG7+XuA6ydzPz8sZ2AYA7lQ9c6pknlsekGdY7fqWK7Pt6hJA6unbpEkL1cQHEvswnvTjLtwDcfX5YHWc4pL7dkI+XPnLktfPeI2bYZqdC5xlJ+Mt65xoqtn3KImvs9dahBGPY7XuHih8PmuG8OE9GOEnZ7EEyYNuF+dkh2j6Src+TEfbwopaUl8OStXv8E7HDtvCG8ZQR2Uy8WTbwMZ4zvsxug1HCzncdqljlhu3mRsox+RxR1FSOo4qoH9cDtqT6B7MWqh310IsaaEV3JSt+ph3YhQf5jAeXI7LS8f869X5SbuvaAH6P2hvnrQdglqXy1u23VI7czzedOsR3+qNGSEuQeuJmoujvqO15fpkjV5k3niXYVbU2Xavq5vkP2ojrZABDWkzbcO00hbwHZ50ur8fKIN6GFcFL5LTmfzWslRvxyjJ+LU9i32zfosASIV8LpOUjFp5ne9l0r2yBCaELiIy/R9JAedw6IXzbjsNpp5d6MC8hgNoRK1bBYWxcIwFXBglo+XxlkyHh3XYmivVUjhxkYioDRORSk/X08bCR+XnFRHqe6V20wOD2STjOkECrHUfFcnrHDN6BndMmQR9sEERT0mpnRNOD96wHKcQZ4QyGqtVuaAPgEaXR1ldYLhitSndjqhN7T32qPK7JlX5JCFndGxG21PSZDGCk/dVgfSSTuN05CUCP96XcaXVcjU3Zio/tRWS3hNrl24nqPrDSjBjho4+1aHR/+pymKKIUEkHtkFkYbrnQ4KNLGansH2UcofpuBGqx1DL+iWLMoRriJl2+v7wNfdaZzHFxQuJEUH8Nzz830V7mp0f3lEhmRiQdxqeDwPYv6AKoF7ia4VOtT7n3+I57PjLvldVp6QEEpZdqvxrtNafL6UbJjskwIykkB5sRsvA8mwrRqYLTWRJ2sUO+XJDSoyTDqeMLdZSbsJPYJMzs6+2pQ9RVZGn5up56vR0fTK2xVLK+z41J19fabPnT1vzzrNJqU/c0v4ch8U6mbPpg0VdW5G54VVQ7rY25NlCzQoAYbFUiasBFKxEenPiqUWtMs5bJ0asbjJj0fqF8rD3rNz5AMFUMp9WIwFSLxUfT78yGHzKZFfLu/AZpxp2/neY5BFAQs6F61yL+Xotc4ppDV4TMVaTr+kosZaiNIrgTe229Vw0Yg2B+1o6GGABfzjlPMyRaK3lFOJEZsjfjsNrxK50pdZq3kRvaqap87yi9PLwj/CN+nSC4I5e1enjX03JANoIbzuWp2ls3mJWHIOCyJnOYI7KfCDBdwPZ5rsEjgkUVHqBghEy3mvZ0Tn50p/da7k6sr9gWEi2QiIrSdcovYq15mYkxOGYW+ZLjxt1MZekdQpKWEtTlnpXINsbJwYnfik8lhQW1Xd+j26EBeLDFSikqdVNlzngQ+aRT2kmE2DfRedowaUGGtYC5FT4xoZABZf9CzmeudYgTGlVPMgdVwrKUpBU8G4KdutpRbFMhBHCKr+DDBAdT2s3mvslS/QxuIurN+7GGNv8wVHw9Ut3CMzetRFNlcqDBnA52dsTfPsWgkKaNKPoV0w6voaotihJymLb/klurpjopNYejFXnCLnsW6zAJUek8FNcmiiJ91g9hCi5speuXmQjUjud32STk4PqiXs4xlOVk6MSHr0E2r2X/gyqhQfldkLNRySwp6GJZ1I9VqFZXVm3E7zTJe+Urdxxi6IPUGoelZU0eibZpigOX/6tGakNqwyRlc5vBMW1HRaIkUumMhvLWKB/S4zUlCJVFMorEo8U5mGb1mpwdDNX+IOZKTd5BkaZhdqpo6Mq6o2jhtbDtXjA/E3ZuoThevYACg7w4L83U+pa0mb93yCXSkCNHZKAf8T5gVosVnblIJd8nwIrZSgd18pr09GDYJAe1LpI7zVqYMbsexOaKMNy1CdUW1Ji8KvKqeqhRj8rcknA8OuVHFqQ9gZtSEjxr2ornvazKcH4WvYsMI8Sb8KZZh292px0bS1iO5B8qsP6Yjre3l/kfv5NZySW3wyz1QbpdhzFEuc6aP0uBwrSDXYwTSegUEWXskw0E2U1s3ycus5q5pkCCNzB+AaIkHhJVc8UqSpjjTx/d8xFmlrR3koXNkBqJUiWcpzct4HZ0pTHtERTXLJPDnq/UzKTr9snCVmtSvIlujAY1WcvU55OU9imRzGcB6KGRINp/u9Shkn/UIcUZWzCVulvfWWzlr2IKrleWw8TKdyIeH1fpO5CdJdQtGr0CjlboVF6t21d2x4vrJaeVwZSVgAHI5PD2O1E6nv3mkaG3TuydYe7JXhg+sOHyV0LKe+mtErTA44Fg0ryiEMMa0EWuBjr76bZddck2JzpCXVtyMDcDNb2GszC8rgk2Z3ldsazYC7j0zY6mQNOGe6cldLpbxqvK2XKX8Nc0OzN9zkvGuQ9rdKGPjoHMOY3OCVN3Qvm12iu41MkW1OsLMaisou24RkxLJdF0qSZoWC2St6EpwREtrRwXiDf2Lr1M5XVXbaqjas5qpujIDqUIBgNUK53cT2nSHJmO0xj0sZ9aq3K8LkBnt5bI+8FRPahb9Lti8MPmaN+93ZMeJZtcI1snwqgqT+NrSJxq/wzPRcdQG9mSIh2iIosbvXPR0oUVHR9RW/ako03EDjcyNYHHf1hZKzkWlJflnV4RSIiA0zwjCeEaBz6BN2RfK05+4CCh1bBgJ02h7die8ZOmaG7hEihP50ViSguDWB4OllBqiMgT1gZlWQNo2Nd4xVVm2eh26AWhPDnuHir/Iynzo4VVM5dbR2zmjzRp9vYrFcbV1uKy1DZHcJd82PTqbcksSoIWVtVR1iLGV3xQKo95o7Q4ozSotQJN2MxJecErQZwWFUGppf1wrV1iwYMss+MVBVhkfC5DY5TD06o2k8yW1Zzc5Q1LoD3jLnko+uDJJY2fK8eeRju1aNb9gm85zp2Q9IzBxm/zTvKDoGhsbaMbKOyLnFQNwJa9ckk+XjDWWT2TsdjzNu1WlVeHw0IC8nh2wbuaCptRpxk86l2xBM8Vgvmvd0X0Jq9h469FBvT6/7S8AnwzGx00S0gO2Pr9Ps9FB+Y1/UgOt1G4waGfMEfspnXvR5D2VGIk5pZDOhwHEurjFnnZfErcr3NTQ8xdek+qqs10jxpBq7m00Iw+ULtvHbBdbSVEOjNrHMk43ZI5P74m4otxG9cX57RMIywn2osBm/vU/kXndAcp+gmRgFzKXO4aIrs2ucXuKwm7r38NtLcLPma13HCI2e2ZGXATlKWYC1o255UUxNTHCmL7zDoINVbDVcg+ooZHKWOyi7AQaLXF4V/tSCFAnHaWG6a0oRmNZsJDmXcMWKmksnDj6y8A0w6c7NIzhfKae+mDNRswmSdmSs0t3Veq0noHsoj3YQHn5q2yTcbe/6kiIpOUUYUSF4FA7X7liEVd8FeGecU27lXFFLOo68pEFdbHxr2MXdm0QsGQOTDP3UimeNQs6Wqz8L/DkW08RVYqYIL6oLDfxen0flNKBmO27sXHpwAJ9WdLhG/BULO5bXruUD0Xls2Bo8Q+M7vuKOSVcCNA+BXAyeR0781ZwMIJJNf3OI9bEwyss6M8Q4YkmQZYiPQXDaupcBeuLti75N+HVB6RnT+RGRJZ8pp7HOFZCfWnTzejdq4ABxU4V7cC7bG70VO8R1NQfxSgv6eoRanSeKvXGkK4KPECbsdwlN6VbOoAtIvYTsJ/PpzbUU00mkTmnzqpIsCvStNYiQquOMPFLYa0DE2e5UW8Gso5C+JPHUo3AKO5amvrRjP8a98QIYMRr17Rpe7XCP9qfD6IYUnOMEzlWIzRHSc4emMSl7wqBriK/QybVAHh0xKxHxl6A+AxkZ42CNzAxvhZno75u2Nns0kiWm9eA44dy4sAWi6wuU+zh/JXckYI4n89QTTsPoyPWqI/vomM00+dXs0+6YE8jDs7rbMahG1b14cefIw1KJQly3Nw9XoWNEOTmQDoE62Uzow6+TOvQDW54RRsOvJveqWFR+0pn1OncLFp618/xIdF2hCmUVWu1KYDuKZ3OIsclQRPm1jfBudmXt2kGn5Hp3uwFNIKY5L8PA44ZXx9OoBfd4UEUY3XrjXOcoW7tQ2y2QLr9gQeHalF5G/s6MHXEqFau9Z+RZ74ae3prjALqPGetn9D6fC8ZNGNqELmJ1NxBJb8UsJl4PRCZyLl1Lxo2h0UikeTjy56A34sfcJpCz6lxKZEUsernpOLY/PaV8Zfe2eBKZQ5TCIrJPyhB9tpZE3qnYGStaczMXdH4UY1aQDrHz60CtJCJhUhkcX34WYiF3uhaKSWPYyUfnGH9RcX+Uu6OVP8JnbcrgPVe7xzHJtJ05+SxaIVxkPmkzDdJjyz7cp9bn5YYzy/FsMkfFy93bBsiUe/FrBm68VM33rJj4Gp3ilgIQb0q08Oq9VzGa6mlEepg9BUVoaPgwQM2I7tP9tDFWL5ymmtglws0s45kFr+eNLzmKJBKAnHzZngJSCZv5qWbVtmgVnlhWQYDgqEvR2s59BqXB3SIyruj8hLETsTcguZQ8lBTorkxAvVHPeuHQapRiwaQh6NoUpN7SFKU2yNBsbMHfiBTQllZv77lYwbSdPl0JiCNoup4e4ZmeLeh0gtCMup14jRPhgj0ZqykoSeD3fRO37/+5hcBjQt6h9jGExZV6xiQhVlTqnl4XYS11QSOea6Eaea+sxdzhiRZq5cXWVX7ahHBdiweTWDI22X3FQWYLNIeMhsyTLvFrp6Oc726LZbihM4QBR2WABRYeXOAJxe2B027GJJd5QLpFwZLrDDkbeeF5DY7NlYTh15rDjdWsF+lWz7Zg+TkNCVdDG6+YXGe444SYWpbnPIvCetIQyTuZktPeYImZcdkxl+5klgu8Hi9XY7iDsr7SfRDFA4j6KgbZvFWoAQ978jxmtfWQcc2CHmFhZqmINEeNTCqqjYm4i4XXBVt1ZluW5sxq8emyhe2zs0iGfMWB0zWIXnXXQTu7sncvoOYycGOhidWtb5JtgO6CEitXQYXUJuQCyfPL0/32OjPPGCJTDtdPj10VoUy4Nb14JTQtWJlFYPI2hxcTLm/ZoI01km4hP9bKWV4MhpQqr6LdxRIS7zh5JrPS7fz+J6enErxYToHJ7EUUj1iqpmM0DUqHtevxXKr8vnWMQRgQ1EV+pVO1FwKY4WOcpM5Z6PbDWIcpZLH5Tq/lZLds6kAJN7P77BPnRUUTJ85UkU+h7a6vGj4KTinfKHZ9CX5C14LNY3cX+J34QRDdh5y4hVh8H5JaNa5HE0/gptO7TrjjiVsXuRWO/E1WpyNXYefc9xRv9aTe0ujTxROrs6qz2JQsWwKYkatwOyb5PbCMRT3hx5dLlsjnO+vjKFXSaT2FKdoRr+Dos1ERiugkM9rLqaXXMuKs5o5+ZOH4i5twzIQK5uyRiLhJkOVzx7wUKKcLx9MxSVh3mXinJj2NkILKC1XLsdHttJaPrscboAX0cRQ78S6JhsOaySgeoWLn02C+k/Eo50fCruur7PtTl+8+HopIyRMdrEd+nUZzTIfGS0gaSUSjLn3582Us/Ngo4zC5oM+n0kryKcon1ilj/6EY9SOKUZlrc0m9u5k/vU7LvRLznlFmXY4D2LVv3tk+67eWJS/GdrJ4yZ8DgnWg1u/noan0QaVTBBN0Dh+1taPZhL9F5132Xij+oC+2MI5ck1ZIdLurVKDdYidDboGjqq+Wv6vkkvg96gaXDFVhckNDbwRSogE1PGwvz74ep+TiDIF593WOnxTuwjmmaJlDcwUniZVzYL8eqXM7syEsVq0VtRXY/F5mqXXT7C5unfsjdgcgy9BAxq4zTTQ3PGIVZK6qjiYH0eVvAwyIXLXrxWCOgg4BqeFqi2Avfc/M5BkeKlstRHRu0JvWEqTSoH6TR5umsjLZLNm9vza1M2YX1A8x9LymQOevsJXSAFkw/ImPbrpkl0H1iX2+XGICS33DZ1/7GjAbrYXlii4iEB4c9fAlaoHTiIIe8Zi1HMKuLKZGR6liMc3ROZGhAug61F4BdefLLRPthmKO0dk+1ktUQW4qVTHBJurpZgXOADJtm/KxxI590avJPgToSduVvivlIL3Or0taD8JCs7nO8warY9Ri00fEUVh/jMPnMHUigwxa2dY9xHfBqqkQKZ0BIA97/RTny7XrB+UKZ+UVDkt3L+ipU5qHLls08nrB8Xk/zhGSdNoS+Tg131JoUfIEUtibeIcjzH+N/QrXOy633Rakjh+lGB6UY55bzXBE9WxlH/A0klYdZcKjJ3ezx69JJfInPHjcTSDnbmhWGfdUt5lGf21WUXd6jprX3KYHER+yTJcC3wvJvKBAnRvDyTaqSa0Q4CqxT/4JenBqopZGFnCLlnphAEsA6uQWIbeYPC6kwKsQKgz57DBL8iwakWAaybyWLHTklhlfnDtj4G4/O0EfP4djV7UhEAG1KUr0lTOEI1oW2Aw/MWGmcU6wenfDsEpXsWNzrZNnB4Q4Osu6P+Wr35H5PltAOlbtaYn9tORsZGtCBU40EAwEOimkn1ee5p2bDCfTW/kUrrfXA+f2awbUWUucdomBVL4F+qPI1Axn0TXV6RHnkuDusL6rTaynr1gHjQ+mnHV2gR9bbKzKKqWnOoMffLTr+XSL7Vbi2nvq2WPGlVPh6EoZjlk2oe1L2h9O1fQl5kkN60P5+Ej8/Oy8rtZj6C5SzRKSXTfwlkKquKoddT/D03HSe0mt6b24vhCgBNBIraTCWGzvtl58uJN8oHuLm+yDimaU9pVG6t3BT419ZSrUN5doSoGapAnBfZhS8LxdR5518Ov1cST6aN62C0lNQfKEkKOkJKNqZUWbb5LrPfhQsflQhwyg+Hit2+L6rqY5e1GpzQgVoiGruxq7ImIdT+SRvtbrfT+mjTsm6urrcPC43fe5wlX0KkHzuu0610Y1LmDw6Vo6mBQ1ZITn5EkXBgOy+2vxyDzPncYu1h4LzKQhZtguKSzzxJBhbBotF9Wv/Xaro2iLqhN+OcuvRCZE2oa4XOtk9XgdLb+MxLDihdjFaMaG+HoKxKCQ7ITE8zFQGsAsnMyIZD9N2WlmI3e80BoC8VNgmRaahCkmGqQxemXC5hpWe/Gmd3ygtXeOYC+3yYjJ3iGhxkSi14QGTTB5xhn30aJvTw6x7e0uAPbF5zic+yXguE6KUfzF1xx+ovZM2nIaxjasgtGaezyVJJQ4i13yy4b4kPko2AxN4ldC+5D6JIOcqLXmfuopQ+OHPbMwxT0rvJj6nBRp+8J6VwqxR/ZGQBE4hJO4b4yibKx54h2g1JNx0Vuuzmj0dnLNW7HbLh3HQxXf4OKq8keqL+g0Eo8UTcpyZdiPzcnGI+0eDdS4FVX+8lID94ZORRyZKrVjQ3dj4NW1jmiYG+IbBFLpKuWUe4VTHB/b9DHW1OkhPafTKj4GAD9mDSjHLEhuYtdpx+pDzhjOBWu1dZ5dSfIpaTlSTfh4JoNgWyK3XUOCIR+BHCwriGqI1iiZ5IiokbB09Z5C4qDKI+3tvqvO17b3MLhPnSTDaKqoTBlVUDM/auJGwYbyRCFCzjcCukEqlYyD90B3r0+PD7uGpSkPVNQaSjKKGVWry3soDDeTEFOrNgiGt1vqmmY62guosaGBEsLD47o8xHFfnlO27nRpJHsTqwOhGOmLKm9nQ+Q8J2sZ24MrFH9KkPS83PqFGTerMofdUjt2oCtuCDJ/wDG4zgPenJrNPHMc96f3g6BlnX09mvz3T0G/H078/+wZyc/HGbsVLNYm2ftR1DGL0p8+1vrpH1b+j++/jUkJ1v18mHOql/vXw5Gfj3L+8PU0+fve/vkVMe/vVnjOvz1tPUf36bcnlb99Psn7/be/TOrL8vPLUD6/4Oz9sO371df3hbzDkqXZ55d0fDwt2vdvl76+pOLTrR/xb//5/wA1yd4dNE8AAA== -->
