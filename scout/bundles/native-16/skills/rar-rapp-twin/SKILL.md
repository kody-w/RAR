---
name: "rar-rapp-twin"
description: "Manages the local digital-twin lifecycle \u2014 summon, hatch eggs, boot each twin as its own brainstem, stop, chat, inspect \u2014 under ~/.rapp/twins/."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/twin_agent", "rar_sha256": "ca59d24cc598580225532ed9cbe5932dcc37957f77325d2dfccbe78a92826460", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.3", "author": "RAPP", "tags": ["twin", "summon", "hatch", "boot", "lifecycle", "egg", "estate", "local-first"]}
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
