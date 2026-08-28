---
name: "rar-kody-w-twin-me"
description: "Pack a GENERIC, PII-stripped digital-twin egg of THIS brainstem so others can hatch your twin on their own machine and use it for anything. Call this whenever the user says 'twin me', 'make a twin egg', 'export my twin', or wants to share their twin. It strips ALL workspace memory, projects, customers, and secrets \u2014 only persona (soul + custom agents + calibration baseline) travels \u2014 and REFUSES if any PII would leak."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_me", "rar_sha256": "d3e0e553b21db6ba2323ebf1119a019bf44b898438fae6432284671359593896", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "twin-me", "pii-strip", "persona", "portable", "federation", "rapp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_me_agent.py` and embedded as the fenced Python below (sha256 d3e0e553b21db6ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_me_agent.py` first:

```bash
python3 twin_me_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 twin_me_agent.py   # or on stdin
python3 twin_me_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
#!/usr/bin/env python3
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
