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
