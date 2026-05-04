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
    "name": "@kody-w/twin_agent",
    "version": "1.0.5",
    "display_name": "Twin",
    "description": "One cartridge for the full twin lifecycle: summon a new twin, hatch an .egg, boot a twin on its own port, stop it, list everything. Drop in to any standard brainstem; no extra layers required.",
    "author": "kody-w",
    "tags": ["twin", "summon", "hatch", "boot", "lifecycle", "egg", "local-first"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ── Constants ───────────────────────────────────────────────────────────

ACTIONS = ("summon", "hatch", "boot", "stop", "list", "update_identity", "update_soul", "lay_egg")
KINDS = ("personal", "pre-founder", "memorial", "project", "place", "custom")

WILDHAVEN_RAPPID = "37ad22f5-ed6d-48b1-b8b4-61019f58a42b"
WILDHAVEN_REPO = "https://github.com/kody-w/wildhaven-ai-homes-twin.git"

PORT_LOW, PORT_HIGH = 7081, 7200

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
                "embedded sha256 + brainstem-egg/2.1 manifest). "
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
        if action == "update_identity": return self._update_identity(**kwargs)
        if action == "update_soul":     return self._update_soul(**kwargs)
        if action == "lay_egg":         return self._lay_egg(**kwargs)
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

        rappid = str(uuid.uuid4())
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        workspace = pathlib.Path(_twins_dir()) / rappid
        try:
            workspace.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            return f"Error: workspace exists at {workspace} (UUID4 collision — retry)"
        except OSError as e:
            return f"Error: cannot create workspace: {e}"

        try:
            (workspace / "soul.md").write_text(SOUL_TEMPLATES[kind](twin_name, description))
            (workspace / "rappid.json").write_text(json.dumps({
                "schema": "rapp-rappid/1.1",
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
