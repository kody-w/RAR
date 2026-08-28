---
name: "rar-rapp-twin"
description: "Manages the local digital-twin lifecycle \u2014 summon, hatch eggs, boot each twin as its own brainstem, stop, chat, inspect \u2014 under ~/.rapp/twins/."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/twin_agent", "rar_sha256": "878729c7a59ce520c487d02e6986845a79babce12a6e10ecbbe5e9eec1b71dda", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.1.3", "author": "RAPP", "tags": ["twin", "summon", "hatch", "boot", "lifecycle", "egg", "estate", "local-first"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/twin_agent`. The original RAPP
agent is preserved byte-for-byte in `twin_agent.py` and in the RCI capsule.

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
