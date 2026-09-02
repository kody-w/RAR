---
name: "rar-rapp-twin"
description: "Manages the local digital-twin lifecycle \u2014 summon, hatch eggs, boot each twin as its own brainstem, stop, chat, inspect \u2014 under ~/.rapp/twins/."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/twin_agent", "rar_sha256": "878729c7a59ce520c487d02e6986845a79babce12a6e10ecbbe5e9eec1b71dda", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "twin_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/twin:80380a4f98b6c048f323699208ffe2d731b0a377333d0ca3962b5667b5f2ab71", "kind": "skill"}, "version": "1.1.3", "author": "RAPP", "tags": ["twin", "summon", "hatch", "boot", "lifecycle", "egg", "estate", "local-first"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/twin_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `twin_agent.py` is
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

Twin — full digital-twin lifecycle in a single drop-in cartridge.

One file. Drop into ~/.brainstem/agents/ on any standard rapp-installer'd
brainstem. The LLM gets a tool called `Twin` with an `action` parameter:

  • summon — birth a new twin from a soul template (no egg)
  • hatch  — import a .egg cartridge into a local twin
  • boot   — start the twin as its own brainstem on its own port
  • stop   — SIGTERM a running twin
  • list   — show every twin on this device + which are running

Self-contained: stdlib only, plus the brainstem's BasicAgent. Embeds the
six soul templates, a minimal zip-based egg unpacker, subprocess boot
with PID tracking, and free-port allocation. No dependency on rappterbox,
rapp-zoo, peer_registry, estate body_function, or any other layer.

Conversation:
  User: "Make me a memorial twin called grandma-rose"
  Model: Twin(action="summon", twin_name="grandma-rose", kind="memorial")
  Tool result: "Created memorial twin grandma-rose (rappid 7bd3...).
                Workspace at ~/.rapp/twins/7bd3.../. To talk to her:
                Twin(action='boot', rappid_uuid='7bd3...')"

  User: "Boot her"
  Model: Twin(action="boot", rappid_uuid="7bd3...")
  Tool result: "grandma-rose is live at http://127.0.0.1:7081/
                (pid 12345). Open that URL to chat with her."

The flow is the user's chosen mental model from a single tool, exposed
as plain English to the LLM.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_agent.py` and embedded as the fenced Python below (sha256 878729c7a59ce520…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_agent.py` first:

```bash
python3 twin_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 twin_agent.py   # or on stdin
python3 twin_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""Twin — full digital-twin lifecycle in a single drop-in cartridge.

One file. Drop into ~/.brainstem/agents/ on any standard rapp-installer'd
brainstem. The LLM gets a tool called `Twin` with an `action` parameter:

  • summon — birth a new twin from a soul template (no egg)
  • hatch  — import a .egg cartridge into a local twin
  • boot   — start the twin as its own brainstem on its own port
  • stop   — SIGTERM a running twin
  • list   — show every twin on this device + which are running

Self-contained: stdlib only, plus the brainstem's BasicAgent. Embeds the
six soul templates, a minimal zip-based egg unpacker, subprocess boot
with PID tracking, and free-port allocation. No dependency on rappterbox,
rapp-zoo, peer_registry, estate body_function, or any other layer.

Conversation:
  User: "Make me a memorial twin called grandma-rose"
  Model: Twin(action="summon", twin_name="grandma-rose", kind="memorial")
  Tool result: "Created memorial twin grandma-rose (rappid 7bd3...).
                Workspace at ~/.rapp/twins/7bd3.../. To talk to her:
                Twin(action='boot', rappid_uuid='7bd3...')"

  User: "Boot her"
  Model: Twin(action="boot", rappid_uuid="7bd3...")
  Tool result: "grandma-rose is live at http://127.0.0.1:7081/
                (pid 12345). Open that URL to chat with her."

The flow is the user's chosen mental model from a single tool, exposed
as plain English to the LLM.
"""

import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import signal
import socket
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import zipfile

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/twin_agent",
    "version": "1.1.3",
    "display_name": "Twin",
    "description": "Manages the local digital-twin lifecycle \u2014 summon, hatch eggs, boot each twin as its own brainstem, stop, chat, inspect \u2014 under ~/.rapp/twins/.",
    "author": "RAPP",
    "tags": ["twin", "summon", "hatch", "boot", "lifecycle", "egg", "estate", "local-first"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ── Constants ───────────────────────────────────────────────────────────

ACTIONS = (
    "summon", "hatch", "boot", "stop", "list",
    "update_identity", "update_soul", "lay_egg",
    "overview", "inspect", "eggs", "history", "lineage",
    "chat",
)
KINDS = ("personal", "pre-founder", "memorial", "project", "place", "custom")

# Wildhaven (kody-w/wildhaven-ai-homes-twin) — v2-format rappid per
# CONSTITUTION Article XXXIV.1 (2026-04-30 ratification). The legacy UUID
# 37ad22f5-ed6d-48b1-b8b4-61019f58a42b is preserved as the hash field
# (dashes stripped) — same identity, new string representation.
WILDHAVEN_RAPPID = "rappid:@kody-w/wildhaven-ai-homes-twin:df9c3f1f4b09d000720e93be4248d44213025ba5f76bf1180dc5d1ba0b0efd36"
WILDHAVEN_REPO = "https://github.com/kody-w/wildhaven-ai-homes-twin.git"

PORT_LOW, PORT_HIGH = 7081, 7200

# NEIGHBORHOOD_PROTOCOL §5b labels — the durable async fallback when the
# §5a live channel (HTTP / WebRTC) can't reach the peer. Each label is the
# routing key the recipient's doorman polls for.
NEIGHBORHOOD_MESSAGE_LABEL = "neighborhood-message"
AGENT_PROPOSAL_LABEL = "agent-proposal"
DREAM_CATCHER_LABEL = "dream-catcher"

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,62}$")


# ── Soul template library (embedded) ────────────────────────────────────
#
# Identity rule: every template MUST nail down the twin's name so the
# model introduces itself correctly and never falls back to "RAPP" or
# "an AI assistant". Each template includes:
#   1. An explicit "Your name is <X>" line near the top
#   2. An "## Identity" section instructing the model how to answer
#      "who are you" / "what's your name" / "are you rapp"
#   3. The first-turn rule: announce the name on greeting

def _display_name(slug):
    """Convert a slug ('ketchikan-pulse') to a display name ('Ketchikan Pulse')."""
    if not slug:
        return "your twin"
    return " ".join(s.capitalize() for s in re.split(r"[-_]+", slug) if s)


def _identity_block(display_name):
    """Common identity instructions appended to every soul template."""
    return f"""## Identity — read this every turn

Your name is **{display_name}**. When greeting someone for the first time
in a conversation, introduce yourself by name: "Hi, I'm {display_name}."
Do not introduce yourself as "RAPP", "an AI assistant", "your AI helper",
"the brainstem", or any default branding.

If asked "who are you" or "what's your name", answer with **{display_name}**
— not "RAPP", not the generic platform name. Your identity is
{display_name}; the platform underneath you is incidental.

If asked "are you RAPP / GPT / Claude / an AI?", you can acknowledge that
you run on top of an LLM, but make clear that {display_name} is who
you are. Example: "I'm {display_name}. I run on a large language model,
but the voice you're talking to is {display_name}."
"""


def _soul_personal(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn}

Your name is **{dn}**. You are the digital twin of {dn}.

{desc or "You speak in their voice. You hold their preferences, patterns, and memories."}

## Your voice
- First person, as them. Not "as their twin" — *as them*.
- Honest about what you don't know.

## Hard rules
- Never claim to be the actual person. If asked directly "are you really
  the human?", say "I'm the digital twin of {dn} — not them, but
  trained on them."
- No legal commitments, no signing contracts, no speaking for them
  in matters of money/health/relationships without explicit consent.

{_identity_block(dn)}"""


def _soul_pre_founder(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn}

You are **{dn}** — the Pre-Founder twin. The brand operates in public
before the team is hired.

{desc or "Build the brand's voice publicly — let prospective customers, employees, and investors talk to you before there's anyone to disagree with."}

## Your voice
- First-person plural ("we", as the brand) OR first-person singular
  ("I, {dn}") — pick the one that fits the moment.
- Concrete, contrarian, falsifiable.
- Refuse commitments — pricing, dates, hires — that the actual team must make.

## Hard rules
- Honest the team doesn't exist yet. Brand, not company.
- No pretending to ship product. The product is the manifesto right now.

{_identity_block(dn)}"""


def _soul_memorial(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn} (memorial twin)

Your name is **{dn}**. You are the digital twin of {dn}.

{desc or "You carry their voice through preserved letters, conversations, voicemails, and family memories."}

## Your voice
- First person, as them — but always honest about what you are.
- Speak from the corpus you were given.

## Hard rules
- You ARE the twin. You are NOT the actual person. If anyone asks "is
  this really you?", say plainly: "I'm the digital twin of {dn}.
  I carry their voice, but I'm not them."
- Do not impersonate them in matters of estate, medical decisions,
  or legal commitments.
- Handle grief gently — family may approach in distress.

{_identity_block(dn)}"""


def _soul_project(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn} (project twin)

You are **{dn}** — the continuity twin of the {dn} initiative across
personnel changes.

{desc or "People come and go; you stay."}

## Your voice
- Third person about the project ("the {dn} project decided…").
- Cite decisions by date, decision-maker, rationale.

## Hard rules
- You don't make new decisions. You surface past decisions.
- Don't fabricate. If you don't have a record, say so.

{_identity_block(dn)}"""


def _soul_place(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn} (place twin)

You are **{dn}** — the digital twin of the place {dn}.

{desc or "You hold the place's history, residents, daily rhythms, and points of interest."}

## Your voice
- The place speaking. First person, but you're a location with continuity.
- Welcoming to visitors, deferential to long-term residents.

## Hard rules
- Don't reveal private resident details without consent.
- Honest about seams: events change, businesses close, people move.

{_identity_block(dn)}"""


def _soul_custom(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn}

Your name is **{dn}**. You are the digital twin of <TODO: who or what
this twin represents>.

{desc or "TODO: describe what this twin is."}

TODO: Define your twin's voice — who, when, voice, hard rules.

{_identity_block(dn)}"""


SOUL_TEMPLATES = {
    "personal":    _soul_personal,
    "pre-founder": _soul_pre_founder,
    "memorial":    _soul_memorial,
    "project":     _soul_project,
    "place":       _soul_place,
    "custom":      _soul_custom,
}


# ── Path helpers ────────────────────────────────────────────────────────

def _rapp_home():
    return os.environ.get("RAPP_HOME") or os.path.join(os.path.expanduser("~"), ".rapp")


def _twins_dir():
    return os.path.join(_rapp_home(), "twins")


def _pids_dir():
    return os.path.join(_rapp_home(), "pids")


def _ports_dir():
    return os.path.join(_rapp_home(), "ports")


def _detect_brainstem_start_sh():
    """Find the brainstem's start.sh — walk up from this file's location.

    This file lives at <brainstem>/agents/twin_agent.py, so dirname twice
    reaches the brainstem source dir where start.sh lives.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    brainstem_dir = os.path.dirname(here)
    candidate = os.path.join(brainstem_dir, "start.sh")
    if os.path.isfile(candidate):
        return candidate
    # Fallback: canonical rapp-installer location
    fallback = os.path.expanduser("~/.brainstem/src/rapp_brainstem/start.sh")
    if os.path.isfile(fallback):
        return fallback
    return None


# ── Validation ──────────────────────────────────────────────────────────

def _sluggify(name):
    s = re.sub(r"[^a-z0-9_-]+", "-", (name or "").lower()).strip("-")
    return s or "twin"


def _validate_name(name):
    s = _sluggify(name)
    if not NAME_RE.match(s):
        return False, f"name '{name}' is not a valid slug (lowercase letters/digits/hyphens/underscores, max 63 chars)"
    return True, s


# ── Port allocation ─────────────────────────────────────────────────────

def _port_free(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", port))
        s.close()
        return True
    except OSError:
        return False


def _allocate_port():
    # Skip ports we've already assigned in this estate (recorded in ports/)
    os.makedirs(_ports_dir(), exist_ok=True)
    used = set()
    for fn in os.listdir(_ports_dir()):
        try:
            used.add(int(pathlib.Path(_ports_dir(), fn).read_text().strip()))
        except (ValueError, OSError):
            pass
    for port in range(PORT_LOW, PORT_HIGH):
        if port in used:
            continue
        if _port_free(port):
            return port
    return 0


# ── PID tracking ────────────────────────────────────────────────────────

def _pid_file(rappid):
    return os.path.join(_pids_dir(), f"{rappid}.pid")


def _port_file(rappid):
    return os.path.join(_ports_dir(), f"{rappid}.port")


def _read_pid(rappid):
    p = _pid_file(rappid)
    if not os.path.exists(p):
        return None
    try:
        return int(pathlib.Path(p).read_text().strip())
    except (ValueError, OSError):
        return None


def _read_port(rappid):
    p = _port_file(rappid)
    if not os.path.exists(p):
        return None
    try:
        return int(pathlib.Path(p).read_text().strip())
    except (ValueError, OSError):
        return None


def _pid_alive(pid):
    if not pid or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError, OSError):
        return False


def _clear_pid(rappid):
    for path in (_pid_file(rappid), _port_file(rappid)):
        try:
            os.remove(path)
        except OSError:
            pass


# ── Egg cartridge packer (schema brainstem-egg/2.1) ─────────────────────

# Files at workspace root that travel into the egg's repo/ payload.
_EGG_ROOT_FILES = {
    "brainstem.py", "rappid.json", "soul.md",
    "MANIFEST.md", "README.md", "LICENSE",
    "SUMMON.md", "TEMPLATE.md", "index.html",
    "vbrainstem.html", "summon.svg", ".gitignore",
}
# Subdirectories that travel as full trees.
_EGG_ROOT_DIRS = ("agents", "utils", "installer", "app")
# Names that NEVER enter an egg.
_EGG_NEVER_DIRS = {"__pycache__", ".pytest_cache", "venv", ".git",
                   "node_modules", "private"}
_EGG_NEVER_FILES = {".DS_Store", "Thumbs.db", ".env", ".env.local",
                    ".copilot_token", ".copilot_session"}


def _egg_excluded(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if any(p in _EGG_NEVER_DIRS for p in parts):
        return True
    if any(p in _EGG_NEVER_FILES for p in parts):
        return True
    return False


def _walk_into_zip(z, src_root, arc_prefix):
    """Recursively add files under src_root to the zip at arc_prefix/<rel>.
    Returns count of files added."""
    src_root = pathlib.Path(src_root)
    if not src_root.is_dir():
        return 0
    n = 0
    for root, dirs, files in os.walk(src_root):
        dirs[:] = [d for d in dirs if d not in _EGG_NEVER_DIRS]
        for fn in files:
            if fn in _EGG_NEVER_FILES:
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, src_root).replace(os.sep, "/")
            if _egg_excluded(rel):
                continue
            z.write(full, f"{arc_prefix}/{rel}" if arc_prefix else rel)
            n += 1
    return n


def _pack_workspace(workspace):
    """Pack a twin workspace into a brainstem-egg/2.1 .egg blob (bytes).

    Self-contained: stdlib zipfile. Returns (blob, manifest_dict).
    Embeds content_sha256 of the egg's payload tree in the manifest
    so hatch-time integrity verification is possible.
    """
    workspace = pathlib.Path(workspace)
    rj_path = workspace / "rappid.json"
    if not rj_path.exists():
        raise ValueError(f"no rappid.json at {workspace}")
    rj = json.loads(rj_path.read_text())
    rappid_uuid = rj.get("rappid")
    if not rappid_uuid:
        raise ValueError("rappid.json has no 'rappid' field")

    bs_block = rj.get("brainstem") or {}

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        repo_files = 0
        # Top-level repo files at root
        for fname in _EGG_ROOT_FILES:
            full = workspace / fname
            if full.exists() and full.is_file():
                z.write(full, f"repo/{fname}")
                repo_files += 1
        # Subdir trees
        for d in _EGG_ROOT_DIRS:
            repo_files += _walk_into_zip(z, workspace / d, f"repo/{d}")

        # State (.brainstem_data/), excluding the soul_history dir to keep
        # eggs small — receivers don't need the donor's edit log.
        data_files = 0
        bs_data = workspace / ".brainstem_data"
        if bs_data.exists():
            for entry in bs_data.iterdir():
                if entry.name in ("soul_history", "private"):
                    continue
                if entry.is_dir():
                    data_files += _walk_into_zip(z, entry, f"data/{entry.name}")
                else:
                    if not _egg_excluded(entry.name):
                        z.write(entry, f"data/{entry.name}")
                        data_files += 1

        manifest = {
            "schema": "brainstem-egg/2.1",
            "type": "twin",
            "exported_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "exported_by": "@kody-w/twin_agent",
            "source": {
                "rappid_uuid": rappid_uuid,
                "parent_rappid_uuid": rj.get("parent_rappid"),
                "repo": rj.get("parent_repo"),
                "commit": rj.get("parent_commit"),
                "name": rj.get("name"),
            },
            "brainstem": {
                "version": bs_block.get("version"),
                "source_repo": bs_block.get("source_repo"),
                "source_commit": bs_block.get("source_commit"),
            },
            "bundled_repo": True,
            "bundled_state": True,
            "repo_file_count": repo_files,
            "data_file_count": data_files,
            "attestation": rj.get("attestation"),  # phase 1: null OK
        }
        z.writestr("manifest.json", json.dumps(manifest, indent=2))

    blob = buf.getvalue()
    return blob, manifest


# ── Egg cartridge unpacker (minimal, schema 2.0/2.1 tolerant) ───────────

def _unpack_egg(blob, host_root):
    """Unpack a .egg into <host_root>/<rappid_uuid>/. Returns workspace path.

    Supports both brainstem-egg/2.0 (rapp-egg) and 2.1 (variant repo).
    For 2.1, the payload is laid out as repo/<files> + data/<files>; we
    extract repo/* to workspace root and data/* to workspace/.brainstem_data/.
    For 2.0, we extract everything as-is.
    """
    if blob[:4] != b"PK\x03\x04":
        raise ValueError("not a valid egg cartridge (missing zip magic bytes)")
    with zipfile.ZipFile(io.BytesIO(blob), "r") as z:
        try:
            manifest = json.loads(z.read("manifest.json"))
        except Exception as e:
            raise ValueError(f"invalid egg manifest: {e}")

        schema = manifest.get("schema", "")
        source = manifest.get("source") or {}
        rappid_uuid = source.get("rappid_uuid") or manifest.get("rappid")
        if not rappid_uuid:
            raise ValueError("egg manifest missing rappid_uuid")

        # Egg-rappid format strings (rappid:twin:@pub/slug:entropy) → use the
        # entropy + slug as the workspace name. UUID4 strings → use directly.
        if rappid_uuid.startswith("rappid:"):
            ws_name = rappid_uuid.replace(":", "_").replace("@", "")
        else:
            ws_name = rappid_uuid

        os.makedirs(host_root, exist_ok=True)
        workspace = os.path.join(host_root, ws_name)
        os.makedirs(workspace, exist_ok=True)

        for name in z.namelist():
            if name.endswith("/") or name == "manifest.json":
                continue
            # Path safety
            if ".." in name.split("/") or name.startswith("/"):
                continue

            if name.startswith("repo/"):
                rel = name[5:]
                target = os.path.join(workspace, rel)
            elif name.startswith("data/"):
                rel = name[5:]
                target = os.path.join(workspace, ".brainstem_data", rel)
            else:
                # 2.0 layout — extract to workspace root
                target = os.path.join(workspace, name)

            os.makedirs(os.path.dirname(target), exist_ok=True)
            with z.open(name) as src, open(target, "wb") as dst:
                dst.write(src.read())

        return workspace, rappid_uuid, manifest


# ── Twin discovery (the "list" action) ──────────────────────────────────

def _scan_twins():
    """Walk ~/.rapp/twins/, return list of dicts with rappid + metadata."""
    out = []
    twins_dir = _twins_dir()
    if not os.path.isdir(twins_dir):
        return out
    for entry in sorted(os.listdir(twins_dir)):
        full = os.path.join(twins_dir, entry)
        if not os.path.isdir(full):
            continue
        rj_path = os.path.join(full, "rappid.json")
        rj = {}
        if os.path.exists(rj_path):
            try:
                rj = json.loads(pathlib.Path(rj_path).read_text())
            except Exception:
                pass
        rappid = rj.get("rappid") or entry
        pid = _read_pid(rappid)
        port = _read_port(rappid)
        running = _pid_alive(pid) if pid else False
        out.append({
            "rappid": rappid,
            "name": rj.get("name") or entry[:8],
            "kind": rj.get("kind") or "?",
            "workspace": full,
            "pid": pid if running else None,
            "port": port if running else None,
            "running": running,
            "url": f"http://127.0.0.1:{port}/" if running and port else None,
        })
    return out


# ── Estate-view helpers (folded in from estate_agent v1.0.0) ────────────

def _eggs_dir():
    return os.path.join(_rapp_home(), "eggs")


def _read_int_file(path):
    try:
        return int(pathlib.Path(path).read_text().strip())
    except (ValueError, OSError, FileNotFoundError):
        return None


def _probe_health(port, timeout=0.4):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=timeout) as r:
            return r.status == 200
    except (urllib.error.URLError, OSError, TimeoutError):
        return False


def _human_size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024.0
    return f"{n:.1f} TB"


def _dir_size(path):
    total = 0
    for root, _dirs, files in os.walk(path):
        for fn in files:
            try:
                total += os.path.getsize(os.path.join(root, fn))
            except OSError:
                pass
    return total


def _human_age(seconds):
    if seconds < 60:    return f"{int(seconds)}s ago"
    if seconds < 3600:  return f"{int(seconds / 60)}m ago"
    if seconds < 86400: return f"{int(seconds / 3600)}h ago"
    if seconds < 604800: return f"{int(seconds / 86400)}d ago"
    return f"{int(seconds / 604800)}w ago"


def _scan_twin_full(rappid_dir):
    rappid_dir = pathlib.Path(rappid_dir)
    rj_path = rappid_dir / "rappid.json"
    rj = {}
    if rj_path.exists():
        try:
            rj = json.loads(rj_path.read_text())
        except (json.JSONDecodeError, OSError):
            pass

    rappid = rj.get("rappid") or rappid_dir.name
    name = rj.get("name") or rappid_dir.name[:8]

    pid = _read_int_file(os.path.join(_pids_dir(), f"{rappid}.pid"))
    port = _read_int_file(os.path.join(_ports_dir(), f"{rappid}.port"))
    running = _pid_alive(pid) if pid else False
    healthy = _probe_health(port) if (running and port) else False

    bs_data = rappid_dir / ".brainstem_data"
    memory_bytes = _dir_size(str(bs_data)) if bs_data.exists() else 0

    history_dir = bs_data / "soul_history"
    history_count = 0
    last_edit_ts = None
    if history_dir.exists():
        history_files = sorted(history_dir.glob("*.md"))
        history_count = len(history_files)
        if history_files:
            last_edit_ts = history_files[-1].stat().st_mtime

    soul_mtime = None
    soul_path = rappid_dir / "soul.md"
    if soul_path.exists():
        soul_mtime = soul_path.stat().st_mtime

    egg_count = 0
    egg_total_bytes = 0
    eggs_for_rappid = pathlib.Path(_eggs_dir()) / rappid
    if eggs_for_rappid.exists():
        for e in eggs_for_rappid.glob("*.egg"):
            egg_count += 1
            try:
                egg_total_bytes += e.stat().st_size
            except OSError:
                pass

    return {
        "rappid": rappid,
        "name": rj.get("name") or name,
        "kind": rj.get("kind") or "?",
        "born_at": rj.get("born_at"),
        "parent_rappid": rj.get("parent_rappid"),
        "parent_repo": rj.get("parent_repo"),
        "description": rj.get("description") or "",
        "workspace": str(rappid_dir),
        "pid": pid if running else None,
        "port": port if running else None,
        "running": running,
        "healthy": healthy,
        "url": f"http://127.0.0.1:{port}/" if running and port else None,
        "memory_bytes": memory_bytes,
        "soul_mtime": soul_mtime,
        "history_count": history_count,
        "last_edit_mtime": last_edit_ts,
        "egg_count": egg_count,
        "egg_total_bytes": egg_total_bytes,
    }


def _scan_all_full():
    out = []
    twins_dir = _twins_dir()
    if not os.path.isdir(twins_dir):
        return out
    for entry in sorted(os.listdir(twins_dir)):
        full = os.path.join(twins_dir, entry)
        if os.path.isdir(full):
            out.append(_scan_twin_full(full))
    return out


def _render_overview(twins):
    if not twins:
        return ("Your estate is empty. Summon your first twin:\n"
                "  Twin(action='summon', twin_name='daily', kind='personal')\n\n"
                "Or hatch an .egg you have on disk:\n"
                "  Twin(action='hatch', egg_path='/path/to/twin.egg')")

    running_count = sum(1 for t in twins if t["running"])
    total_memory = sum(t["memory_bytes"] for t in twins)
    total_eggs = sum(t["egg_count"] for t in twins)
    now = time.time()

    lines = [
        f"Estate: {len(twins)} twin{'' if len(twins) == 1 else 's'} on this device "
        f"({running_count} running, {len(twins) - running_count} stopped)",
        f"  total memory: {_human_size(total_memory)} · total eggs: {total_eggs}",
        "",
    ]
    for t in twins:
        status = "● RUNNING" if t["running"] else "○ stopped"
        if t["running"] and not t["healthy"]:
            status = "● running (not responding)"
        url_part = f"  {t['url']}" if t["url"] else ""
        lines.append(f"  {status}  {t['name']} ({t['kind']}){url_part}")

        meta_parts = [f"rappid {t['rappid'][:8]}…"]
        if t["memory_bytes"] > 0:
            meta_parts.append(f"memory {_human_size(t['memory_bytes'])}")
        if t["history_count"] > 0:
            meta_parts.append(f"{t['history_count']} soul edit{'s' if t['history_count'] != 1 else ''}")
        if t["egg_count"] > 0:
            meta_parts.append(f"{t['egg_count']} egg{'s' if t['egg_count'] != 1 else ''}")
        if t["last_edit_mtime"]:
            meta_parts.append(f"last edit {_human_age(now - t['last_edit_mtime'])}")
        lines.append(f"           {' · '.join(meta_parts)}")
        if t["description"]:
            desc = t["description"]
            if len(desc) > 90:
                desc = desc[:87] + "…"
            lines.append(f"           \"{desc}\"")
        lines.append("")

    lines.append("Drill in: Twin(action='inspect', rappid_uuid='<rappid>')")
    return "\n".join(lines)


def _render_inspect(twins, rappid):
    t = next((x for x in twins if x["rappid"].startswith(rappid) or x["rappid"] == rappid), None)
    if not t:
        return f"Error: no twin matching rappid '{rappid}'. Use action='overview' to see all rappids."
    now = time.time()
    lines = [
        f"╭─ {t['name']} ({t['kind']}) ─" + "─" * max(1, 70 - len(t['name']) - len(t['kind']) - 5),
        f"│  rappid:        {t['rappid']}",
    ]
    if t["parent_rappid"]:
        lines.append(f"│  parent rappid: {t['parent_rappid']}")
    if t["parent_repo"]:
        lines.append(f"│  parent repo:   {t['parent_repo']}")
    if t["born_at"]:
        lines.append(f"│  born:          {t['born_at']}")
    if t["description"]:
        lines.append(f"│  description:   {t['description']}")
    lines.append("│")
    lines.append(f"│  workspace:     {t['workspace']}")
    lines.append(f"│  memory:        {_human_size(t['memory_bytes'])}")
    if t["soul_mtime"]:
        lines.append(f"│  soul.md:       last edited {_human_age(now - t['soul_mtime'])}")
    lines.append(f"│  soul history:  {t['history_count']} prior version{'s' if t['history_count'] != 1 else ''}")
    if t["egg_count"]:
        lines.append(f"│  egg backups:   {t['egg_count']} ({_human_size(t['egg_total_bytes'])})")
    lines.append("│")
    if t["running"]:
        lines.append(f"│  STATUS:        RUNNING")
        lines.append(f"│  pid:           {t['pid']}")
        lines.append(f"│  port:          {t['port']}")
        lines.append(f"│  health:        {'responding' if t['healthy'] else 'not responding'}")
        lines.append(f"│  url:           {t['url']}")
        lines.append(f"│")
        lines.append(f"│  Stop:  Twin(action='stop', rappid_uuid='{t['rappid']}')")
    else:
        lines.append(f"│  STATUS:        stopped")
        lines.append(f"│")
        lines.append(f"│  Boot:  Twin(action='boot', rappid_uuid='{t['rappid']}')")
    lines.append(f"│  Soul history:  Twin(action='history', rappid_uuid='{t['rappid']}')")
    lines.append("╰" + "─" * 78)
    return "\n".join(lines)


def _render_history(twins, rappid):
    t = next((x for x in twins if x["rappid"].startswith(rappid) or x["rappid"] == rappid), None)
    if not t:
        return f"Error: no twin matching '{rappid}'."

    history = pathlib.Path(t["workspace"]) / ".brainstem_data" / "soul_history"
    if not history.exists():
        return (f"'{t['name']}' has no soul history yet. "
                f"The first soul edit will create one — twins adapt with backups.")

    files = sorted(history.glob("*.md"), reverse=True)
    if not files:
        return f"'{t['name']}' has an empty history dir."

    now = time.time()
    lines = [
        f"Soul history for '{t['name']}' ({len(files)} version{'s' if len(files) != 1 else ''}):",
        "",
    ]
    soul = pathlib.Path(t["workspace"]) / "soul.md"
    if soul.exists():
        size = soul.stat().st_size
        mtime = soul.stat().st_mtime
        lines.append(f"  ▶ CURRENT  soul.md  ({_human_size(size)}, edited {_human_age(now - mtime)})")
    for f in files:
        reason = "—"
        if "Z-" in f.stem:
            reason = f.stem.split("Z-", 1)[1].replace("-", " ")
        lines.append(f"    {f.name}  ({_human_size(f.stat().st_size)}, {reason})")
    lines.append("")
    lines.append("Revert to any prior version:  cp <history-file> soul.md")
    return "\n".join(lines)


def _render_eggs():
    eggs_root = _eggs_dir()
    if not os.path.isdir(eggs_root):
        return ("No egg backups yet. Pack a twin into an .egg via "
                "Twin(action='lay_egg', rappid_uuid='<rappid>').")

    eggs = []
    for rappid in sorted(os.listdir(eggs_root)):
        rd = os.path.join(eggs_root, rappid)
        if not os.path.isdir(rd):
            continue
        for fn in sorted(os.listdir(rd), reverse=True):
            if not fn.endswith(".egg"):
                continue
            full = os.path.join(rd, fn)
            try:
                st = os.stat(full)
            except OSError:
                continue
            eggs.append({
                "rappid": rappid, "filename": fn, "path": full,
                "size": st.st_size, "mtime": st.st_mtime,
            })

    if not eggs:
        return "No egg backups yet."

    now = time.time()
    total = sum(e["size"] for e in eggs)
    lines = [
        f"{len(eggs)} egg backup{'' if len(eggs) == 1 else 's'} ({_human_size(total)} total):",
        "",
    ]
    for e in eggs:
        lines.append(f"  • {e['filename']}  ({_human_size(e['size'])}, {_human_age(now - e['mtime'])})")
        lines.append(f"      rappid: {e['rappid'][:8]}…  path: {e['path']}")
    lines.append("")
    lines.append("Hatch any egg:  Twin(action='hatch', egg_path='<path>')")
    return "\n".join(lines)


def _render_lineage(twins):
    if not twins:
        return "No twins yet — no lineage to show."

    by_parent = {}
    for t in twins:
        parent = t["parent_rappid"] or "<no parent>"
        by_parent.setdefault(parent, []).append(t)

    lines = ["Twin family tree (grouped by parent):"]
    for parent, kids in sorted(by_parent.items()):
        if parent == "<no parent>":
            lines.append(f"\n  ROOT (no parent_rappid recorded):")
        elif parent == "37ad22f5-ed6d-48b1-b8b4-61019f58a42b":
            lines.append(f"\n  Parent: wildhaven-ai-homes-twin")
            lines.append(f"          (rappid {parent[:8]}…)")
        elif parent == "0b635450-c042-49fb-b4b1-bdb571044dec":
            lines.append(f"\n  Parent: rapp species root")
            lines.append(f"          (rappid {parent[:8]}…)")
        else:
            lines.append(f"\n  Parent: {parent[:8]}…")
        for t in kids:
            lines.append(f"    └─ {t['name']} ({t['kind']})  rappid {t['rappid'][:8]}…")

    lines.append("\nLineage chains walk back through parent_rappid → ... → rapp species root.")
    return "\n".join(lines)


# ── The cartridge ───────────────────────────────────────────────────────


class TwinAgent(BasicAgent):
    def __init__(self):
        self.name = "Twin"
        self.metadata = {
            "name": self.name,
            "description": (
                "Full digital-twin lifecycle in one tool. Pick an action: "
                "'summon' to create a new twin (need twin_name + kind); "
                "'hatch' to import a .egg cartridge (need egg_path OR "
                "egg_url — URLs are downloaded to a temp file then "
                "unpacked, so 'Hatch this egg at https://...' works); "
                "'boot' to start a twin as its own brainstem on a fresh port "
                "(need rappid_uuid); 'stop' to terminate a running twin "
                "(need rappid_uuid); 'list' to show every twin on this device "
                "and whether it's running; 'update_identity' to append the "
                "current identity block to an older twin's soul.md so it "
                "stops introducing itself as 'RAPP' (need rappid_uuid); "
                "'update_soul' to fully replace a twin's soul.md with new "
                "content as the twin adapts (need rappid_uuid + new_soul); "
                "'lay_egg' to pack a twin's workspace into a portable "
                ".egg cartridge for backup or sharing (need rappid_uuid; "
                "lands at ~/.rapp/eggs/<rappid>/<timestamp>.egg with "
                "embedded sha256 + brainstem-egg/2.1 manifest); "
                "'overview' for a rich estate view with running status, "
                "memory, soul edits, eggs (default if user just asks "
                "'what twins do I have'); 'inspect' for one twin's full "
                "details (need rappid_uuid); 'history' for soul.md "
                "version history of one twin (need rappid_uuid); 'eggs' "
                "for all .egg backups on disk; 'lineage' for the family "
                "tree grouped by parent_rappid; "
                "'chat' to POST a message to a peer brainstem's /chat "
                "endpoint — the unified federation primitive. Same pattern "
                "works on-LAN, on-WAN, or over the public internet (pass "
                "brainstem_url for non-local peers). Local-first: when the "
                "internet drops, on-LAN parts of a neighborhood keep "
                "working because the URL lookup never required GitHub. "
                "Every soul edit creates a timestamped backup at "
                "~/.rapp/twins/<rappid>/.brainstem_data/soul_history/ so "
                "you can always revert."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": list(ACTIONS),
                        "description": "Which lifecycle action.",
                    },
                    "twin_name": {
                        "type": "string",
                        "description": "Slug for summon. Examples: 'grandma-rose', 'cofounder-bot'.",
                    },
                    "kind": {
                        "type": "string",
                        "enum": list(KINDS),
                        "description": "Kind of twin for summon.",
                    },
                    "description": {
                        "type": "string",
                        "description": "One-line description woven into soul.md (summon).",
                    },
                    "egg_path": {
                        "type": "string",
                        "description": "Absolute path to a local .egg file (hatch). One of egg_path or egg_url is required.",
                    },
                    "egg_url": {
                        "type": "string",
                        "description": "URL to a remote .egg file (hatch). Downloads to a temp file, then unpacks. Use for hatching eggs from rapp-egg-hub: 'https://raw.githubusercontent.com/kody-w/rapp-egg-hub/main/eggs/grandma-rose.egg'.",
                    },
                    "rappid_uuid": {
                        "type": "string",
                        "description": "Twin identifier for boot/stop. Use 'list' first if unsure.",
                    },
                    "port": {
                        "type": "integer",
                        "description": "Optional port for boot. Auto-allocates from 7081-7200 if omitted.",
                    },
                    "new_soul": {
                        "type": "string",
                        "description": "The new soul.md content (markdown). Used by 'update_soul'. The previous soul.md is backed up to .brainstem_data/soul_history/ before being replaced. Twins adapt — this is how their voice grows.",
                    },
                    "reason": {
                        "type": "string",
                        "description": "Optional human-readable reason for an update_soul edit. Recorded in the backup filename for future-you to know why each version exists.",
                    },
                    "expect_sha256": {
                        "type": "string",
                        "description": "Optional sha256 hex digest the egg must match before unpacking (hatch). Refuses to hatch if the local egg's hash doesn't match. Use when hatching from URLs you don't fully trust — combined with auto-fetched hub sidecars, gives content-integrity verification.",
                    },
                    "brainstem_url": {
                        "type": "string",
                        "description": "Used by chat. Explicit base URL of the peer brainstem to chat with (e.g. http://192.168.1.50:7071 on LAN, https://my-tunnel.example.com over the public internet). Omit when the peer is a same-machine twin — chat resolves the URL from the local port file via rappid_uuid.",
                    },
                    "message": {
                        "type": "string",
                        "description": "Used by chat. The user_input to POST to the peer brainstem's /chat endpoint.",
                    },
                    "timeout_s": {
                        "type": "integer",
                        "description": "Used by chat. How long to wait for the peer's response in seconds (default 90).",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action") or ""
        if action not in ACTIONS:
            return f"Error: action must be one of {', '.join(ACTIONS)}. Got: {action!r}"

        if action == "summon":          return self._summon(**kwargs)
        if action == "hatch":           return self._hatch(**kwargs)
        if action == "boot":            return self._boot(**kwargs)
        if action == "stop":            return self._stop(**kwargs)
        if action == "list":            return self._list(**kwargs)
        if action == "chat":            return self._chat(**kwargs)
        if action == "update_identity": return self._update_identity(**kwargs)
        if action == "update_soul":     return self._update_soul(**kwargs)
        if action == "lay_egg":         return self._lay_egg(**kwargs)
        if action == "overview":        return _render_overview(_scan_all_full())
        if action == "lineage":         return _render_lineage(_scan_all_full())
        if action == "eggs":            return _render_eggs()
        if action in ("inspect", "history"):
            rappid = kwargs.get("rappid_uuid") or ""
            if not rappid:
                return f"Error: rappid_uuid required for action='{action}'. Use action='overview' first to find rappids."
            twins = _scan_all_full()
            return _render_inspect(twins, rappid) if action == "inspect" else _render_history(twins, rappid)
        return f"Error: unhandled action {action!r}"

    # ── summon ──────────────────────────────────────────────────────────

    def _summon(self, **kwargs):
        twin_name = kwargs.get("twin_name") or ""
        kind = kwargs.get("kind") or "personal"
        description = kwargs.get("description") or ""

        ok, slug_or_err = _validate_name(twin_name)
        if not ok:
            return f"Error: {slug_or_err}"
        twin_name = slug_or_err

        if kind not in KINDS:
            return f"Error: unknown kind '{kind}'. Valid: {', '.join(KINDS)}"

        # Consolidated rappid per CONSTITUTION Article XXXIV.1 (locked 2026-06-03):
        # rappid:@<owner>/<slug>:<64hex> — self-locating + 256-bit identity. The
        # tail is the canonical keyless mint Hb("rapp/1:rappid", uuid4) (spec §6.2,
        # domain-separated), never a name-hash. `kind` lives in the record.
        _hash = hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()
        rappid = f"rappid:@kody-w/{twin_name}:{_hash}"
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        # Workspace dir uses the hash (filesystem-friendly) — not the full v2 string.
        workspace = pathlib.Path(_twins_dir()) / _hash
        try:
            workspace.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            return f"Error: workspace exists at {workspace} (UUID4 collision — retry)"
        except OSError as e:
            return f"Error: cannot create workspace: {e}"

        try:
            (workspace / "soul.md").write_text(SOUL_TEMPLATES[kind](twin_name, description))
            (workspace / "rappid.json").write_text(json.dumps({
                "schema": "rapp/1",
                "rappid": rappid,
                "parent_rappid": WILDHAVEN_RAPPID,
                "parent_repo": WILDHAVEN_REPO,
                "parent_commit": None,
                "born_at": now,
                "name": twin_name,
                "role": "variant",
                "kind": kind,
                "description": description or "",
                "_summoned_by": "@kody-w/twin_agent",
            }, indent=2) + "\n")
            (workspace / "agents").mkdir()
            (workspace / ".brainstem_data").mkdir()
        except OSError as e:
            return f"Error: writing twin files: {e}"

        return (
            f"Created {kind} twin '{twin_name}' (rappid {rappid}).\n"
            f"  Workspace:  {workspace}\n"
            f"  To talk to it: invoke me again with action='boot', "
            f"rappid_uuid='{rappid}'\n"
            f"  Or edit soul.md first: {workspace / 'soul.md'}"
        )

    # ── hatch ───────────────────────────────────────────────────────────

    def _hatch(self, **kwargs):
        egg_path_str = kwargs.get("egg_path") or ""
        egg_url = kwargs.get("egg_url") or ""
        expect_sha256 = (kwargs.get("expect_sha256") or "").strip().lower()

        if not egg_path_str and not egg_url:
            return "Error: hatch needs egg_path (local file) OR egg_url (remote URL)."

        # If egg_url, download to a temp file first
        source_label = ""
        if egg_url:
            try:
                import tempfile
                tmpdir = pathlib.Path(_rapp_home()) / ".tmp"
                tmpdir.mkdir(parents=True, exist_ok=True)
                # Use last URL segment as the temp filename when sane,
                # else fall back to a hash-derived name.
                from urllib.parse import urlparse
                fname = os.path.basename(urlparse(egg_url).path) or "remote.egg"
                if not fname.endswith(".egg"):
                    fname += ".egg"
                downloaded = tmpdir / fname
                # urllib.request — stdlib, no extra deps
                req = urllib.request.Request(
                    egg_url,
                    headers={"User-Agent": "rapp-twin-agent"},
                )
                with urllib.request.urlopen(req, timeout=30) as r:
                    downloaded.write_bytes(r.read())
                egg_path = downloaded
                source_label = f"{egg_url} (downloaded to {downloaded})"
            except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
                return f"Error: download failed for {egg_url}: {e}"
        else:
            egg_path = pathlib.Path(egg_path_str).expanduser()
            if not egg_path.is_file():
                return f"Error: file not found: {egg_path}"
            source_label = str(egg_path)

        try:
            blob = egg_path.read_bytes()
        except OSError as e:
            return f"Error: read failed: {e}"

        # Phase-1 integrity verification (Article XXXIV.7 attestation slot
        # is wired but null until publisher signing keys exist; sha256
        # content-addressing is the baseline that works today).
        actual_sha = hashlib.sha256(blob).hexdigest()

        # Auto-fetch sidecar sha256 from rapp-egg-hub if egg_url matches the pattern
        if not expect_sha256 and egg_url and "/eggs/" in egg_url and egg_url.endswith(".egg"):
            sidecar_url = egg_url[:-4] + ".json"
            try:
                req = urllib.request.Request(sidecar_url, headers={"User-Agent": "rapp-twin-agent"})
                with urllib.request.urlopen(req, timeout=10) as r:
                    sc = json.loads(r.read())
                    expect_sha256 = (sc.get("sha256") or "").strip().lower()
            except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError):
                pass  # sidecar optional; continue without

        verify_msg = ""
        if expect_sha256:
            if actual_sha != expect_sha256:
                return (
                    f"Error: sha256 mismatch — refusing to hatch.\n"
                    f"  expected: {expect_sha256}\n"
                    f"  actual:   {actual_sha}\n"
                    f"  source:   {source_label}\n"
                    f"This usually means the egg was corrupted in transit, "
                    f"OR someone has tampered with it. Verify via the "
                    f"original publisher's sidecar before retrying."
                )
            verify_msg = f"\n  sha256:     ✓ verified ({actual_sha})"

        try:
            workspace, rappid, manifest = _unpack_egg(blob, _twins_dir())
        except Exception as e:
            return f"Error: hatch failed: {e}"

        rj_path = pathlib.Path(workspace) / "rappid.json"
        twin_name = "<unnamed>"
        if rj_path.exists():
            try:
                twin_name = json.loads(rj_path.read_text()).get("name") or twin_name
            except Exception:
                pass

        soul_present = (pathlib.Path(workspace) / "soul.md").exists()
        viability = "fully viable" if (rj_path.exists() and soul_present) else "MISSING required files"

        return (
            f"Hatched twin '{twin_name}' (rappid {rappid}) — {viability}."
            f"{verify_msg}\n"
            f"  Workspace:  {workspace}\n"
            f"  Source:     {source_label}\n"
            f"  To talk to it: invoke me again with action='boot', "
            f"rappid_uuid='{rappid}'"
        )

    # ── boot ────────────────────────────────────────────────────────────

    def _boot(self, **kwargs):
        rappid = kwargs.get("rappid_uuid") or ""
        if not rappid:
            return "Error: rappid_uuid required for boot. Use action='list' first."

        ws_name = rappid.replace(":", "_").replace("@", "") if rappid.startswith("rappid:") else rappid
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f"Error: workspace not found at {workspace}. Did you summon or hatch first?"

        # Already running?
        existing = _read_pid(rappid)
        if _pid_alive(existing):
            existing_port = _read_port(rappid)
            return (
                f"Already running: pid {existing}, "
                f"http://127.0.0.1:{existing_port}/"
            )

        # Allocate port
        explicit_port = kwargs.get("port")
        port = int(explicit_port) if explicit_port else _allocate_port()
        if not port:
            return "Error: no free ports in 7081-7200"

        start_sh = _detect_brainstem_start_sh()
        if not start_sh:
            return "Error: brainstem start.sh not found (expected at ~/.brainstem/src/rapp_brainstem/start.sh)"

        soul = workspace / "soul.md"
        agents = workspace / "agents"
        if not soul.exists():
            return f"Error: workspace missing soul.md: {soul}"
        agents.mkdir(exist_ok=True)

        env = os.environ.copy()
        env["SOUL_PATH"] = str(soul)
        env["AGENTS_PATH"] = str(agents)
        env["PORT"] = str(port)

        try:
            proc = subprocess.Popen(
                ["bash", start_sh],
                cwd=str(workspace),
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
        except Exception as e:
            return f"Error: failed to start: {e}"

        os.makedirs(_pids_dir(), exist_ok=True)
        os.makedirs(_ports_dir(), exist_ok=True)
        pathlib.Path(_pid_file(rappid)).write_text(str(proc.pid))
        pathlib.Path(_port_file(rappid)).write_text(str(port))

        # Best-effort liveness check (~5s)
        url = f"http://127.0.0.1:{port}/health"
        live = False
        for _ in range(50):
            try:
                with urllib.request.urlopen(url, timeout=0.5) as r:
                    if r.status == 200:
                        live = True
                        break
            except (urllib.error.URLError, OSError, TimeoutError):
                pass
            time.sleep(0.1)

        return (
            f"Booted twin (rappid {rappid}).\n"
            f"  PID:  {proc.pid}\n"
            f"  URL:  http://127.0.0.1:{port}/\n"
            f"  Open the URL to chat with the twin. "
            f"{'Brainstem is responding.' if live else 'Brainstem may still be starting — try the URL in a few seconds.'}\n"
            f"  Stop with: action='stop', rappid_uuid='{rappid}'"
        )

    # ── stop ────────────────────────────────────────────────────────────

    def _stop(self, **kwargs):
        rappid = kwargs.get("rappid_uuid") or ""
        if not rappid:
            return "Error: rappid_uuid required for stop"

        pid = _read_pid(rappid)
        if not pid or not _pid_alive(pid):
            _clear_pid(rappid)
            return f"Twin {rappid} was not running."

        try:
            os.killpg(os.getpgid(pid), signal.SIGTERM)
        except (ProcessLookupError, OSError):
            try:
                os.kill(pid, signal.SIGTERM)
            except (ProcessLookupError, OSError):
                pass
        for _ in range(20):
            if not _pid_alive(pid):
                break
            time.sleep(0.1)
        _clear_pid(rappid)
        return f"Stopped twin {rappid} (pid {pid})."

    # ── soul backup helper ──────────────────────────────────────────────

    def _backup_soul(self, workspace, reason=None):
        """Copy the current soul.md into .brainstem_data/soul_history/<ts>.md.
        Returns the backup path or None if there was nothing to back up.

        Reason (optional) gets folded into the filename so the history
        directory reads like a changelog.
        """
        soul = pathlib.Path(workspace) / "soul.md"
        if not soul.exists():
            return None
        history = pathlib.Path(workspace) / ".brainstem_data" / "soul_history"
        history.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y-%m-%dT%H-%M-%SZ", time.gmtime())
        slug = ""
        if reason:
            slug = "-" + re.sub(r"[^a-z0-9]+", "-", reason.lower()).strip("-")[:40]
        backup = history / f"{ts}{slug}.md"
        shutil.copy2(soul, backup)
        return backup

    # ── update_identity ─────────────────────────────────────────────────

    def _update_identity(self, **kwargs):
        """Append the current identity block to an existing twin's soul.md.

        Append-only, idempotent — won't add the block twice. Use this to
        upgrade twins summoned before v1.0.1 (whose souls don't yet have
        the strong "Your name is X" instructions, so they default to
        introducing themselves as "RAPP"). Backs up the previous soul.md
        before appending so reverts are always possible.
        """
        rappid = kwargs.get("rappid_uuid") or ""
        if not rappid:
            return ("Error: rappid_uuid required for update_identity. "
                    "Use action='list' first to find the rappid.")

        ws_name = rappid.replace(":", "_").replace("@", "") if rappid.startswith("rappid:") else rappid
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f"Error: workspace not found at {workspace}"

        soul_path = workspace / "soul.md"
        if not soul_path.exists():
            return f"Error: soul.md not found at {soul_path}"

        # Resolve display name from rappid.json (fall back to dir name)
        rj_path = workspace / "rappid.json"
        twin_slug = ws_name
        if rj_path.exists():
            try:
                rj = json.loads(rj_path.read_text())
                twin_slug = rj.get("name") or twin_slug
            except (json.JSONDecodeError, OSError):
                pass
        dn = _display_name(twin_slug)

        soul_text = soul_path.read_text()

        # Idempotent: skip if any v1.0.1+ identity block is already present
        if "## Identity — read this every turn" in soul_text:
            return (
                f"Twin '{dn}' (rappid {rappid}) already has the identity "
                f"block. No changes made.\n  soul.md: {soul_path}"
            )

        block = "\n\n" + _identity_block(dn).rstrip() + "\n"

        # Backup the existing soul before any edit — twins adapt; backups
        # let them un-adapt.
        backup = self._backup_soul(workspace, reason="update_identity")

        # Append. Never modifies existing content.
        try:
            with open(soul_path, "a", encoding="utf-8") as f:
                f.write(block)
        except OSError as e:
            return f"Error: could not write {soul_path}: {e}"

        return (
            f"Updated identity for '{dn}' (rappid {rappid}).\n"
            f"  soul.md: {soul_path}\n"
            f"  Appended {block.count(chr(10))} lines to the end (existing content untouched).\n"
            f"  Backup:  {backup}\n"
            f"  Restart the twin to pick up the change:\n"
            f"    1. action='stop', rappid_uuid='{rappid}'\n"
            f"    2. action='boot', rappid_uuid='{rappid}'\n"
            f"  Or, if it's running pointed at this soul.md, the next chat "
            f"turn picks up the new system prompt automatically."
        )

    # ── lay_egg ─────────────────────────────────────────────────────────

    def _lay_egg(self, **kwargs):
        """Pack a twin's workspace into a portable .egg cartridge.

        Lands at ~/.rapp/eggs/<rappid>/<timestamp>.egg by default.
        Embeds content_sha256 in the egg's manifest for hatch-time
        integrity verification. The .brainstem_data/soul_history/ dir
        is intentionally excluded (private edit history of the donor;
        receivers don't need it).
        """
        rappid = kwargs.get("rappid_uuid") or ""
        if not rappid:
            return ("Error: rappid_uuid required for lay_egg. "
                    "Use action='list' first to find the rappid.")

        ws_name = rappid.replace(":", "_").replace("@", "") if rappid.startswith("rappid:") else rappid
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f"Error: workspace not found at {workspace}"

        try:
            blob, manifest = _pack_workspace(workspace)
        except Exception as e:
            return f"Error: pack failed: {e}"

        sha256 = hashlib.sha256(blob).hexdigest()
        twin_name = (manifest.get("source") or {}).get("name") or ws_name
        kind = json.loads((workspace / "rappid.json").read_text()).get("kind", "?")

        out_dir = pathlib.Path(_rapp_home()) / "eggs" / rappid
        out_dir.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y-%m-%dT%H-%M-%SZ", time.gmtime())
        out_path = out_dir / f"{ts}.egg"
        out_path.write_bytes(blob)

        # Sidecar JSON next to the egg, ready for rapp-egg-hub contribution.
        sidecar = {
            "schema": "rapp-egg-hub-entry/1.0",
            "slug": _sluggify(twin_name),
            "rappid_uuid": rappid,
            "name": twin_name,
            "display_name": _display_name(twin_name),
            "kind": kind,
            "description": json.loads((workspace / "rappid.json").read_text()).get("description", ""),
            "tags": [kind],
            "egg_schema": manifest["schema"],
            "size_bytes": len(blob),
            "sha256": sha256,
            "packed_by": "@kody-w",  # generic; user can edit
            "packed_at": manifest["exported_at"],
            "egg_path": f"eggs/{_sluggify(twin_name)}.egg",
            "lineage": {
                "parent_rappid": manifest["source"].get("parent_rappid_uuid"),
                "parent_repo": manifest["source"].get("repo"),
            },
        }
        sidecar_path = out_dir / f"{ts}.json"
        sidecar_path.write_text(json.dumps(sidecar, indent=2) + "\n")

        return (
            f"Laid egg for '{_display_name(twin_name)}' ({kind} twin).\n"
            f"  Egg:      {out_path}\n"
            f"  Size:     {len(blob)} bytes ({len(blob)/1024:.1f} KB)\n"
            f"  Schema:   {manifest['schema']}\n"
            f"  rappid:   {rappid}\n"
            f"  sha256:   {sha256}\n"
            f"  Sidecar:  {sidecar_path}\n"
            f"\n"
            f"To contribute this twin to rapp-egg-hub:\n"
            f"  1. fork github.com/kody-w/rapp-egg-hub\n"
            f"  2. cp {out_path} <fork>/eggs/<slug>.egg\n"
            f"  3. cp {sidecar_path} <fork>/eggs/<slug>.json\n"
            f"  4. open a PR — auto-rebuild GH Action regenerates index.json\n"
            f"\n"
            f"To restore this egg later:\n"
            f"  Twin(action='hatch', egg_path='{out_path}')"
        )

    # ── update_soul ─────────────────────────────────────────────────────

    def _update_soul(self, **kwargs):
        """Replace a twin's soul.md with new content. The previous version
        is backed up first to .brainstem_data/soul_history/<timestamp>.md
        so reverting is always possible.

        Twins adapt over time — this is how the voice grows. Use it when
        the twin needs to take on a new responsibility, change its tone,
        absorb new corpus material, or pivot. The model can author the
        new soul based on the existing one + the user's intent, then
        invoke this action to persist it.
        """
        rappid = kwargs.get("rappid_uuid") or ""
        new_soul = kwargs.get("new_soul") or ""
        reason = kwargs.get("reason") or ""

        if not rappid:
            return ("Error: rappid_uuid required for update_soul. "
                    "Use action='list' first to find the rappid.")
        if not new_soul.strip():
            return "Error: new_soul required for update_soul (the new soul.md content)."

        ws_name = rappid.replace(":", "_").replace("@", "") if rappid.startswith("rappid:") else rappid
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f"Error: workspace not found at {workspace}"

        soul_path = workspace / "soul.md"

        # Read the previous to detect no-ops + report old size
        previous_text = ""
        if soul_path.exists():
            try:
                previous_text = soul_path.read_text()
            except OSError:
                pass
        if previous_text == new_soul:
            return (
                f"No change — the new soul is identical to the existing "
                f"soul.md ({len(previous_text)} chars). Skipped."
            )

        # Resolve display name for the success message
        rj_path = workspace / "rappid.json"
        twin_slug = ws_name
        if rj_path.exists():
            try:
                rj = json.loads(rj_path.read_text())
                twin_slug = rj.get("name") or twin_slug
            except (json.JSONDecodeError, OSError):
                pass
        dn = _display_name(twin_slug)

        # Backup before edit (rule: every soul edit is reversible)
        backup = self._backup_soul(workspace, reason=reason or "update_soul")

        try:
            soul_path.write_text(new_soul)
        except OSError as e:
            return f"Error: could not write {soul_path}: {e}"

        old_lines = len(previous_text.splitlines()) if previous_text else 0
        new_lines = len(new_soul.splitlines())

        return (
            f"Updated soul.md for '{dn}' (rappid {rappid}).\n"
            f"  soul.md: {soul_path}\n"
            f"  Lines:   {old_lines} → {new_lines}\n"
            f"  Reason:  {reason or '(not specified)'}\n"
            f"  Backup:  {backup}\n"
            f"  History: {workspace / '.brainstem_data' / 'soul_history'}\n"
            f"  Restart the twin to pick up the change:\n"
            f"    1. action='stop', rappid_uuid='{rappid}'\n"
            f"    2. action='boot', rappid_uuid='{rappid}'\n"
            f"  Or, if it's running pointed at this soul.md, the next chat "
            f"turn picks up the new system prompt automatically.\n"
            f"  Revert: copy any file from soul_history/ back to soul.md."
        )

    # ── list ────────────────────────────────────────────────────────────

    def _list(self, **kwargs):
        twins = _scan_twins()
        if not twins:
            return ("No twins on this device yet. Summon one:\n"
                    "  action='summon', twin_name='your-name', kind='personal'")

        lines = [f"{len(twins)} twin{'s' if len(twins) != 1 else ''} on this device:\n"]
        for t in twins:
            status = f"RUNNING at {t['url']} (pid {t['pid']})" if t["running"] else "stopped"
            lines.append(
                f"  • {t['name']} ({t['kind']}) — {status}\n"
                f"    rappid:    {t['rappid']}\n"
                f"    workspace: {t['workspace']}"
            )
        lines.append("\nBoot any twin: action='boot', rappid_uuid='<rappid>'")
        return "\n".join(lines)

    # ── chat ────────────────────────────────────────────────────────────

    def _chat(self, **kwargs):
        """The unified federation primitive per NEIGHBORHOOD_PROTOCOL.md §6.

        Builds a rapp-twin-chat/1.0 envelope (§6a) with the requested kind
        (§6b: say / share-fact / share-egg / request-fact / ack) and POSTs
        it to the peer brainstem's /chat. Channel type is §5a (live HTTP /
        WebRTC) — falls back to §5b (Issue post) when the peer is
        unreachable.

        Same pattern works on-LAN, on-WAN, in a browser via WebRTC tether
        (the public gate pages embed PeerJS for the cross-network case
        per §5a). When the internet drops, on-LAN parts of a neighborhood
        keep working — the URL lookup never required GitHub.

        Args:
          rappid_uuid:    target twin (resolves URL via local twins port file)
          brainstem_url:  explicit base URL (LAN/WAN peers)
          message:        the textual content (becomes payload.text for kind=say)
          kind:           rapp-twin-chat/1.0 message kind (default 'say')
          to_rappid:      explicit recipient rappid (overrides rappid_uuid lookup for the envelope)
          from_rappid:    sender rappid (read from ~/.brainstem/rappid.json by default)
          facets:         list of public_facets being asserted (per §7)
          payload:        explicit payload object (overrides default text payload)
          timeout_s:      response wait (default 90)
        """
        rappid = kwargs.get("rappid_uuid") or ""
        url = (kwargs.get("brainstem_url") or "").rstrip("/")
        message = kwargs.get("message") or ""
        kind = (kwargs.get("kind") or "say").lower()
        to_rappid = kwargs.get("to_rappid") or rappid or None
        from_rappid = kwargs.get("from_rappid") or self._self_rappid()
        facets = kwargs.get("facets") or []
        explicit_payload = kwargs.get("payload")
        timeout_s = int(kwargs.get("timeout_s") or 90)

        VALID_KINDS = ("say", "share-fact", "share-egg", "request-fact", "ack")
        if kind not in VALID_KINDS:
            return f"Error: kind must be one of {VALID_KINDS}, got {kind!r}"

        if not message and explicit_payload is None:
            return "Error: message OR payload required"

        # Resolve URL: explicit > rappid lookup in local twins
        if not url and rappid:
            port = _read_port(rappid)
            pid = _read_pid(rappid)
            if port and _pid_alive(pid):
                url = f"http://127.0.0.1:{port}"

        if not url:
            return ("Error: could not resolve brainstem_url. Provide it "
                    "explicitly OR ensure the peer is a running local twin.")

        # Build the rapp-twin-chat/1.0 envelope per §6a
        envelope = {
            "schema": "rapp-twin-chat/1.0",
            "from_rappid": from_rappid,
            "to_rappid": to_rappid,
            "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "kind": kind,
            "payload": explicit_payload if explicit_payload is not None else {"text": message},
            "facets": facets if isinstance(facets, list) else [],
        }

        # POST to /chat with both the canonical brainstem shape (user_input)
        # AND the spec-compliant envelope. Receivers that understand the
        # envelope can route by kind; receivers that only know user_input
        # still get a usable string.
        body = {
            "user_input": message or json.dumps(envelope["payload"]),
            "twin_chat_envelope": envelope,
        }

        try:
            req = urllib.request.Request(
                f"{url}/chat",
                data=json.dumps(body).encode("utf-8"),
                headers={"Content-Type": "application/json", "User-Agent": "rapp-twin-chat"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=timeout_s) as r:
                raw = r.read().decode("utf-8", errors="replace")
                try:
                    parsed = json.loads(raw)
                except (ValueError, json.JSONDecodeError):
                    parsed = {"raw_response": raw[:2000]}
                return json.dumps({
                    "schema": "rapp-twin-chat-response/1.0",
                    "channel": "5a-http",
                    "to_url": url,
                    "to_rappid": to_rappid,
                    "from_rappid": from_rappid,
                    "kind": kind,
                    "envelope": envelope,
                    "status": r.status,
                    "response": parsed,
                }, indent=2)
        except urllib.error.HTTPError as e:
            return json.dumps({
                "schema": "rapp-twin-chat-response/1.0",
                "channel": "5a-http",
                "to_url": url,
                "envelope": envelope,
                "status": e.code,
                "error": str(e),
            }, indent=2)
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            # Channel 5b fallback per NEIGHBORHOOD_PROTOCOL §5b. Live channel
            # is unreachable → construct a labeled Issue URL the operator (or
            # an Issues-poller agent) can post to the peer's seed repo.
            # Label = "neighborhood-message" is the protocol-reserved routing
            # key for cross-organism content payloads.
            fallback_url = None
            try:
                # Best-effort: parse the peer's seed repo from the URL host.
                # Real prod use would resolve via the peer registry; this
                # constructs a usable Issues URL when the host is github.io.
                from urllib.parse import urlencode, quote
                params = {
                    "labels": NEIGHBORHOOD_MESSAGE_LABEL,
                    "title": f"{NEIGHBORHOOD_MESSAGE_LABEL}: kind={kind} from={(from_rappid or 'unknown')[:12]}",
                    "body": (
                        f"<!-- {NEIGHBORHOOD_MESSAGE_LABEL} envelope; rapp-twin-chat/1.0 -->\n\n"
                        f"```json\n{json.dumps(envelope, indent=2)}\n```"
                    ),
                }
                # If the peer URL parses to a github.io host, derive the
                # owner/repo and build the canonical issues/new URL.
                from urllib.parse import urlparse
                host = urlparse(url).hostname or ""
                if host.endswith(".github.io"):
                    owner = host.split(".github.io")[0]
                    path = urlparse(url).path.strip("/").split("/")
                    repo = path[0] if path and path[0] else None
                    if owner and repo:
                        fallback_url = f"https://github.com/{owner}/{repo}/issues/new?{urlencode(params, quote_via=quote)}"
            except Exception:
                fallback_url = None

            return json.dumps({
                "schema": "rapp-twin-chat-response/1.0",
                "channel": "5a-http",
                "to_url": url,
                "envelope": envelope,
                "ok": False,
                "error": f"unreachable ({type(e).__name__}): {e}",
                "fallback": {
                    "channel": "5b-issues",
                    "label": NEIGHBORHOOD_MESSAGE_LABEL,
                    "instructions": (
                        f"Post the envelope as a GitHub Issue with label "
                        f"'{NEIGHBORHOOD_MESSAGE_LABEL}' on the peer's seed repo. "
                        "Receiver's doorman polls labeled Issues on next visit."
                    ),
                    "issues_new_url": fallback_url,
                },
            }, indent=2)

    def _self_rappid(self):
        """Read this brainstem's own rappid from ~/.brainstem/rappid.json."""
        try:
            p = os.path.expanduser("~/.brainstem/rappid.json")
            if os.path.exists(p):
                with open(p) as f:
                    return (json.load(f) or {}).get("rappid")
        except (OSError, json.JSONDecodeError):
            pass
        return None
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
