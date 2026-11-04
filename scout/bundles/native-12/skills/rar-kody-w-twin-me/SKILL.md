---
name: "rar-kody-w-twin-me"
description: "Pack a GENERIC, PII-stripped digital-twin egg of THIS brainstem so others can hatch your twin on their own machine and use it for anything. Call this whenever the user says 'twin me', 'make a twin egg', 'export my twin', or wants to share their twin. It strips ALL workspace memory, projects, customers, and secrets \u2014 only persona (soul + custom agents + calibration baseline) travels \u2014 and REFUSES if any PII would leak."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_me", "rar_sha256": "821f3c97589ab2bd5ab346d36a2458621f39d568f205b9391893308099efabed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "twin-me", "pii-strip", "persona", "portable", "federation", "rapp"]}
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

<!-- rci-capsule:v1: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 -->
