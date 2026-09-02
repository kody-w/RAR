---
name: "rar-kody-w-twin-me"
description: "Pack a GENERIC, PII-stripped digital-twin egg of THIS brainstem so others can hatch your twin on their own machine and use it for anything. Call this whenever the user says 'twin me', 'make a twin egg', 'export my twin', or wants to share their twin. It strips ALL workspace memory, projects, customers, and secrets \u2014 only persona (soul + custom agents + calibration baseline) travels \u2014 and REFUSES if any PII would leak."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_me", "rar_sha256": "d3e0e553b21db6ba2323ebf1119a019bf44b898438fae6432284671359593896", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "twin_me_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/twin-me:88f945122d4c5ce8768f04fbcdfa0b93ec287ddb03120fd3199f425c402db2a5", "kind": "skill"}, "version": "1.0.3", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "twin-me", "pii-strip", "persona", "portable", "federation", "rapp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/twin_me`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `twin_me_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
