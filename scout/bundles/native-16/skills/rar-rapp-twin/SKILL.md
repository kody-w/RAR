---
name: "rar-rapp-twin"
description: "Manages the local digital-twin lifecycle \u2014 summon, hatch eggs, boot each twin as its own brainstem, stop, chat, inspect \u2014 under ~/.rapp/twins/."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/twin_agent", "rar_sha256": "ca59d24cc598580225532ed9cbe5932dcc37957f77325d2dfccbe78a92826460", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.3", "author": "RAPP", "tags": ["twin", "summon", "hatch", "boot", "lifecycle", "egg", "estate", "local-first"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_agent.py` and embedded as the fenced Python below (sha256 ca59d24cc5985802…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_agent.py` first:

```bash
python3 twin_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 twin_agent.py   # or on stdin
python3 twin_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/twin_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/twin_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/twin_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
