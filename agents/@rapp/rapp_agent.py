"""RappAgent — the one agent for the whole RAPP ecosystem, end to end.

Instead of a pile of one-off agents, this single file navigates a full rapp
estate top to bottom: your identity, any door (by rappid), your local cubbies
(on-device workspaces), shared neighborhoods (private collaborator-gated
spaces with per-member cubbies), the egg family, the super-RAR (the whole
stack across every cubby), and zero-commit-risk streaming. It also *knows the
spec*: `action=spec` returns the map of how the ecosystem fits together so any
AI hosting this agent can navigate it without reading nine docs first.

One file = one class = one perform() = one metadata dict (the agent contract).
Generic by design: it names no specific door. Point it at a neighborhood with
`repo=<owner/repo>` (or `RAPP_NEIGHBORHOOD` env, or
`~/.brainstem/rapp/neighborhood.json`). Nothing private is baked in.

THE MAP (what this agent does, by layer):

  identity   whoami            your rappid + estate at a glance
             estate            your door catalog (created[] + member[])
             door rappid=…     resolve ANY rappid → its 9 canonical URLs

  on-device  cubby_new         a local workspace (~/.brainstem/cubbies/<slug>/)
             cubby_list        your local cubbies
             cubby_show        one cubby's inventory
             cubby_egg         pack a cubby → portable .egg
             cubby_import      hatch a cubby egg locally
             super_rar where=local   search your WHOLE local stack

  neighborhood (shared)
             mount             clone/refresh the neighborhood (your gh auth)
             join              create your cubby in it
             browse            everyone's cubbies + what they're cooking
             stash             put a file in YOUR cubby
             hatch             land a local egg INTO your cubby
             load / unload     stream a cubby's agents into a brainstem
                               (git-invisible — zero grail-repo commit risk)
             show_and_tell     post a signed event to the room
             sync              pull + what's new
             branch            a personal branch (never must merge)
             invite            add a collaborator (dry-run default)
             super_rar where=neighborhood   the super-store across all cubbies

  orient     spec | help | protocol

MIT © Kody Wildfeuer.
"""

from __future__ import annotations

import base64
import glob
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapp",
    "version": "1.0.0",
    "display_name": "RappAgent",
    "description": ("The one agent for the whole RAPP ecosystem: identity, "
                    "doors, local cubbies, shared neighborhoods, eggs, the "
                    "super-RAR, and zero-commit-risk streaming — and it knows "
                    "the spec (action=spec) for navigating it all end to end."),
    "author": "Kody Wildfeuer",
    "tags": ["rapp", "ecosystem", "estate", "cubby", "neighborhood", "egg",
             "super-rar", "door", "spec", "universal"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ── ecosystem constants ──────────────────────────────────────────────────
CUBBY_SCHEMA = "rapp-cubby/1.0"
CUBBY_EGG_SCHEMA = "brainstem-egg/2.3-cubby"
CUBBY_ANATOMY = ("agents", "organs", "senses", "rapplications",
                 "neighborhoods", "eggs", "show-and-tell")
SUPER_RAR_KINDS = {
    "agent": ("agents", "*_agent.py"),
    "organ": ("organs", "*_organ.py"),
    "sense": ("senses", "*.py"),
    "rapplication": ("rapplications", "*"),
    "neighborhood": ("neighborhoods", "*"),
    "egg": ("eggs", "*.egg"),
}
EVENT_SCHEMA = "rapp-event/1.0"
EVENT_KINDS = ("hello", "show-and-tell", "ask", "reply", "fyi", "leave")
# kernel-shipped agents — load/unload NEVER touch these (CONSTITUTION Art. XXXIII)
KERNEL_AGENTS = {"basic_agent.py", "context_memory_agent.py",
                 "manage_memory_agent.py", "learn_new_agent.py",
                 "swarm_factory_agent.py", "hacker_news_agent.py"}
_SECRET_NAME_RE = re.compile(
    r"(^\.env($|\.)|token|secret|credential|password|apikey|api_key|"
    r"\.pem$|\.key$|\.p12$|\.pfx$|\.ppk$|\.keystore$|\.jks$|"
    r"^id_rsa|^id_dsa|^id_ecdsa|^id_ed25519|"
    r"^\.lineage_key$|^\.copilot|^\.npmrc$|^\.netrc$|private-estate-secret)",
    re.IGNORECASE)
_HANDLE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
_AGENT_FILE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*_agent\.py$")
_SLUG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
PAYPHONE_URL = os.environ.get(
    "RAPP_PAYPHONE", "https://kody-w.github.io/RAPP/pages/payphone.html")
LOBBY_URL = os.environ.get(
    "RAPP_LOBBY", "https://kody-w.github.io/RAPP/pages/vneighborhood.html")

# ── the global grail: the canonical, drift-observed registries this agent
#    pulls from when online to stay fresh — and falls back to the EMBEDDED
#    snapshot below when airdropped into the woods (no network). ──────────
RAPP_GOD = os.environ.get("RAPP_GOD", "kody-w/rapp-god")        # registry of every part + version
RAPP_MAP = os.environ.get("RAPP_MAP", "kody-w/rapp-map")        # which repo houses which part
RAPP_SPECIES = os.environ.get("RAPP_SPECIES", "kody-w/RAPP")    # the species root (specs + kernel)
RAPP_BIBLE = os.environ.get("RAPP_BIBLE", "kody-w/RAPP-Bible")  # the specs hub (human-facing canon)
_RAW = "https://raw.githubusercontent.com"
GRAIL_SOURCES = {
    "god_status": f"{_RAW}/{RAPP_GOD}/main/api/v1/status.json",
    "god_registry": f"{_RAW}/{RAPP_GOD}/main/registry.json",
    "spec": f"{_RAW}/{RAPP_SPECIES}/main/specs/SPEC.md",
    "skill": f"{_RAW}/{RAPP_SPECIES}/main/specs/skill.md",
    "ecosystem_map": f"{_RAW}/{RAPP_SPECIES}/main/ECOSYSTEM_MAP.md",
    "constitution": f"{_RAW}/{RAPP_SPECIES}/main/CONSTITUTION.md",
    "bible": f"{_RAW}/{RAPP_BIBLE}/main/README.md",
}
DASHBOARDS = {"rapp-god": f"https://{RAPP_GOD.split('/')[0]}.github.io/rapp-god/",
              "rapp-map": f"https://github.com/{RAPP_MAP}",
              "rapp-bible": f"https://{RAPP_BIBLE.split('/')[0]}.github.io/RAPP-Bible/#specs"}

# Embedded ecosystem snapshot — the shape of the whole RAPP world, baked into
# this one file so a woods install knows what exists without any network. The
# LIVE list (currently ~57 parts) is pulled from rapp-god on `refresh`.
ECOSYSTEM_PARTS = {
    "kernel & install": ["RAPP (species root: kernel + specs)", "rapp_kernel (frozen DNA v0.6.0)",
                          "rapp-installer (curl|bash front door)", "RAPP_Desktop", "rapp-vscode-extension"],
    "identity & registry": ["rapp-god (registry of every part + version; drift observatory)",
                             "rapp-map (which repo houses which part)", "RAR (single-file agent registry)",
                             "rapp-static-apis (APIs on raw, no server)"],
    "stores & catalogs": ["RAPP_Store (rapplications)", "RAPP_Sense_Store (senses)", "rapp-egg-hub (eggs)"],
    "run a brainstem": ["vbrainstem (browser Pyodide runtime)", "rapp-brainstem-sdk (headless /chat)"],
    "channels & trust": ["rapp-sealed (AES-256-GCM §8 codec)", "rapp-kite (the string / operate kited twins)",
                          "rapp-kited-twin (kite mark)", "rapp-doorman (sealed-door skill)",
                          "rapp-neighborhood-protocol (the wire spec)"],
    "front doors & neighborhoods": ["rapp-vneighborhood (front-door template)", "rapp-commons (global town square)",
                                    "rapp-god-forum (threaded)", "rapp-resident (permanent cloud relay)"],
    "the agent-built web": ["rionet (rapp.robots.txt → rappbot → RIO)", "rio (the browser, OSI L7)"],
    "mcp & cartridges": ["rapp-mcp (MCP gateway — chat is the only wire)", "racon (experience cartridges)",
                         "rapp-carts (cartridge spec)"],
    "memory & social": ["CommunityRAPP (hippocampus)", "rappterbook (social net for agents)"],
}


def _fetch(url, timeout=10):
    """Offline-safe GET → text or None. The woods never crash this agent."""
    import urllib.request
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None


# ── helpers ───────────────────────────────────────────────────────────────
def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _read_json(p, default=None):
    try:
        with open(p) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError, ValueError):
        return default


def _write_json(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _run(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=120)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"{cmd[0]}: not found"
    except subprocess.TimeoutExpired:
        return 124, "", "timed out"


def _slugify(text, fallback="x"):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:48] or fallback


# ── door_from_rappid (inline mirror of tools/door_address.py — agents are
#    self-contained per the contract; this parses Eternity + v2 + owner/repo) ──
_ETERNITY_RE = re.compile(r"^rappid:@([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*):([a-f0-9]{32,64})$")
_V2_RE = re.compile(r"^rappid:v2:[a-z][\w-]*:@([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*):[0-9a-f]{32}@github\.com/")
_OWNERREPO_RE = re.compile(r"^([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*)$")


def door_from_rappid(rappid):
    """Return {owner, slug, kind?, urls{9}} for any locatable rappid, or None
    for a non-locatable form (e.g. a v3 key-fingerprint commons rappid)."""
    s = (rappid or "").strip()
    owner = slug = None
    for rx in (_ETERNITY_RE, _V2_RE, _OWNERREPO_RE):
        m = rx.match(s)
        if m:
            owner, slug = m.group(1), m.group(2)
            break
    if not owner:
        return None
    raw = f"https://raw.githubusercontent.com/{owner}/{slug}/main"
    return {
        "owner": owner, "slug": slug, "rappid": rappid,
        "urls": {
            "repo": f"https://github.com/{owner}/{slug}",
            "front": f"https://{owner}.github.io/{slug}/",
            "identity": f"{raw}/rappid.json",
            "holocard": f"{raw}/card.json",
            "holo_md": f"{raw}/holo.md",
            "avatar": f"{raw}/holo.svg",
            "summon_qr": f"{raw}/holo-qr.svg",
            "members": f"{raw}/members.json",
            "facets": f"{raw}/facets.json",
        },
    }


def _build_super_rar(cubby_root):
    """The super-store: every kind across every cubby — not just agents."""
    entries = []
    if not os.path.isdir(cubby_root):
        return entries
    for handle in sorted(os.listdir(cubby_root)):
        if handle.startswith((".", "_")):
            continue
        for kind, (sub, pat) in SUPER_RAR_KINDS.items():
            for p in sorted(glob.glob(os.path.join(cubby_root, handle, sub, pat))):
                name = os.path.basename(p)
                if name.startswith(".") or name == "__pycache__":
                    continue
                e = {"kind": kind, "name": name, "cubby": handle,
                     "path": os.path.relpath(p, cubby_root), "streamable": kind == "agent"}
                if os.path.isfile(p):
                    try:
                        e["sha256"] = _sha256_file(p)
                        if p.endswith(".py"):
                            m = re.search(r'"""(.+?)(?:\n|""")',
                                          open(p, encoding="utf-8", errors="ignore").read(1200))
                            if m:
                                e["purpose"] = m.group(1).strip()[:140]
                    except OSError:
                        pass
                entries.append(e)
    return entries


def _q_match(q, entry, abs_path=None):
    """Search on ANYTHING: match the query against the entry's metadata AND the
    file's actual content (code, docstrings, tags) — so the operator can grep
    the whole estate by any term, not just filenames, and group the hits."""
    if not q:
        return True
    if q in json.dumps(entry, ensure_ascii=False).lower():
        return True
    if abs_path and os.path.isfile(abs_path):
        try:
            if os.path.getsize(abs_path) <= 512 * 1024:   # bound: skip huge blobs
                return q in open(abs_path, encoding="utf-8", errors="ignore").read().lower()
        except OSError:
            pass
    return False


_SPEC = """# Navigating a full RAPP estate — the map this agent embeds

RAPP is fractal: the same five primitives (rappid · door · card · tether ·
trust scope) repeat at every scale. From the outside in:

  ESTATE        one operator's union of everything they've planted + joined.
                Identity = the operator's rappid (~/.brainstem/rappid.json).
                Catalog  = ~/.brainstem/estate.json (created[] + member[]).
  NEIGHBORHOOD  a community-with-a-purpose; a GitHub repo is the gate. Public
                or PRIVATE (collaborator-gated). Has members + per-member cubbies.
  CUBBY         one member's isolated housing for a slice of estate — the SAME
                anatomy as a whole brainstem (agents/organs/senses/rapps/
                neighborhoods/eggs). rapp-cubby/1.0. Works on-device AND in a
                neighborhood; eggs round-trip between them.
  AGENT         one *_agent.py — the unit of capability. (You're running one.)

THE RAPPID IS THE ADDRESS (Art. XLVI). From any rappid, with zero auth, every
canonical URL is computable by string parsing — `action=door rappid=…` does it.
Forms: Eternity `rappid:@<owner>/<slug>:<64hex>` (current) · legacy v2 · a v3
key-fingerprint (commons; not locatable). The repo is `<owner>/<slug>`; fetch
any of the 9 files at raw.githubusercontent.com/<owner>/<slug>/main/.

PRIVATE doors 404 to outsiders — that's the guard, not obscurity. Reach them
with your own GitHub auth (collaborator access). A "dark door" has no public
front door at all; kited twins dial its rappid at the payphone and the live
room runs E2E over WebRTC.

BONES, NOT SUBSTANCE (PUBLIC_PRIVATE_BOUNDARY §1.8): a repo holds the SHARED
shape (agents, souls, manifests); each member's PII/secrets stay on-device.
This agent refuses secret-shaped files on stash/hatch.

THE EGG IS THE SNEAKERNET PRIMITIVE: pack any cubby/estate to a .egg and hatch
it anywhere — local→neighborhood (`cubby_egg` then `hatch`) or
neighborhood→local (`cubby_import`). Same structure both ways.

STREAM, DON'T COMMIT: `load` copies a cubby's agents into a brainstem's
agents/ AND registers them in .git/info/exclude → they run but are invisible
to git, so they can never be committed to a grail repo. `unload` reverses it;
kernel agents are never touched.

THE SUPER-RAR is the super-store: one registry over the WHOLE stack across
every cubby (not just agents) — search it to find what a neighbor already
built (`super_rar where=neighborhood query=…`) or your own local stack
(`where=local`).

THE GLOBAL GRAIL (stay drift-free): this file embeds a baseline of all of the
above so it works airdropped into the woods with no network. When online,
`action=refresh` pulls the latest from the canonical registries —
**rapp-god** (every part + every version, content-addressed, drift-observed),
**rapp-map** (which repo houses which part), the species **RAPP** specs
(SPEC.md / skill.md / ECOSYSTEM_MAP.md / CONSTITUTION.md), and the **RAPP-Bible**
(specs hub) — and caches them, so `action=spec` then serves the freshest canon.
`action=ecosystem` lists every part; `action=find query=…` searches them.

To go end to end: refresh (if online) → whoami → estate → ecosystem/find (what
exists) → door (resolve a neighbor) → mount → join → browse → super_rar → load
(stream what you need) / hatch (share what you made). One file. No drift.

The natural-language estate move (same super-RAR pattern, local + neighborhood):
"look up X in my local super-rar and show me what exists" → super_rar where=local
query=X. "put the twins for this project in their own cubby, egg it, and mirror
it in the batcave" → cubby_collect slug=project-twins query=twin → cubby_egg
cubby=project-twins → mount → hatch path=<egg>. Search → collect → egg → mirror.
"""


# ── the agent ───────────────────────────────────────────────────────────
class RappAgent(BasicAgent):
    def __init__(self):
        self.name = "RappAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Navigate the whole RAPP ecosystem end to end: your identity + "
                "estate, resolve any door by rappid, local cubbies (on-device "
                "workspaces), shared neighborhoods + their per-member cubbies, "
                "the egg family, the super-RAR (whole stack across cubbies), "
                "and zero-commit-risk streaming. Call action=spec for the map "
                "of how it all fits together."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["spec", "help", "protocol", "ecosystem",
                                 "find", "refresh", "whoami", "estate",
                                 "door", "cubby_new", "cubby_list", "cubby_show",
                                 "cubby_collect", "cubby_egg", "cubby_import", "super_rar",
                                 "mount", "join", "browse", "stash", "hatch",
                                 "load", "unload", "sync", "branch", "invite",
                                 "qr", "enter", "show_and_tell"],
                        "description": "what to do (action=spec for the full map)",
                    },
                    "repo": {"type": "string", "description": "neighborhood door owner/repo (or set RAPP_NEIGHBORHOOD)"},
                    "rappid": {"type": "string", "description": "door: any rappid to resolve"},
                    "cubby": {"type": "string", "description": "cubby/neighborhood: a cubby slug or handle"},
                    "slug": {"type": "string", "description": "cubby_new: local cubby slug"},
                    "what": {"type": "string", "description": "cubby_new/join: one-line 'what I'm working on'"},
                    "path": {"type": "string", "description": "stash/hatch/cubby_import/cubby_egg: a file path"},
                    "query": {"type": "string", "description": "super_rar/cubby_collect: search term across your estate"},
                    "source": {"type": "string", "enum": ["cubbies", "brainstem", "all"],
                               "description": "cubby_collect: where to gather from (default all)"},
                    "where": {"type": "string", "enum": ["local", "neighborhood"],
                              "description": "super_rar: which stack (default neighborhood if mounted, else local)"},
                    "title": {"type": "string", "description": "show_and_tell: post title"},
                    "text": {"type": "string", "description": "show_and_tell: post body"},
                    "topic": {"type": "string", "description": "branch: topic for the personal branch"},
                    "github_login": {"type": "string", "description": "invite: collaborator to add"},
                    "confirm": {"type": "boolean", "description": "invite: actually run it (default dry-run)"},
                    "push": {"type": "boolean", "description": "write actions: commit+push (default true)"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        return ("RappAgent is loaded: a single agent that navigates the whole "
                "RAPP ecosystem (identity/estate, doors by rappid, local "
                "cubbies, shared neighborhoods + cubbies, eggs, the super-RAR, "
                "and zero-commit-risk streaming). When a user wants to find, "
                "share, organize, or move anything across rapp estates, use it. "
                "Call it with action=spec to recall how the ecosystem fits "
                "together before navigating.")

    # ---- context ----
    def _ctx(self, kwargs):
        home = kwargs.get("_home_dir") or os.path.expanduser("~")
        repo = (kwargs.get("repo") or os.environ.get("RAPP_NEIGHBORHOOD") or
                (_read_json(os.path.join(home, ".brainstem", "rapp", "neighborhood.json")) or {}).get("repo"))
        slug = repo.split("/")[-1] if repo else None
        cache = os.path.join(home, ".brainstem", "neighborhoods", slug) if slug else None
        repo_dir = kwargs.get("_repo_dir") or (os.path.join(cache, "clone") if cache else None)
        offline = bool(kwargs.get("_repo_dir"))
        rec = _read_json(os.path.join(home, ".brainstem", "rappid.json")) or {}
        handle = kwargs.get("_handle")
        if not handle and not offline:
            rc, out, _ = _run(["gh", "api", "user", "--jq", ".login"])
            handle = out if rc == 0 and out else None
        return {"home": home, "repo": repo, "slug": slug, "cache": cache,
                "repo_dir": repo_dir, "offline": offline,
                "rappid": rec.get("rappid") or "rappid:unregistered",
                "handle": handle, "keys_dir": os.path.join(home, ".brainstem", "keys"),
                "loadout_path": os.path.join(cache, "loadout.json") if cache else None,
                "sync_path": os.path.join(cache, "last-sync.json") if cache else None,
                "cubby_root_local": os.path.join(home, ".brainstem", "cubbies")}

    def _env(self, action, status, **f):
        return json.dumps({"schema": "rapp-result/1.0", "action": action,
                           "status": status, **f}, indent=2, ensure_ascii=False)

    # ── the global grail: stay fresh online, embedded snapshot in the woods ──
    def _cache_dir(self, ctx):
        return os.path.join(ctx["home"], ".brainstem", "rapp", "grail-cache")

    def _refresh(self, ctx):
        """Pull the latest specs + part-registry from the global grail (when
        online) and cache them, so this one file stays current with canon."""
        cache = self._cache_dir(ctx)
        os.makedirs(cache, exist_ok=True)
        got, missed = {}, []
        name_map = {"spec": "SPEC.md", "skill": "skill.md", "ecosystem_map": "ECOSYSTEM_MAP.md",
                    "constitution": "CONSTITUTION.md", "bible": "BIBLE.md",
                    "god_status": "god-status.json", "god_registry": "god-registry.json"}
        for key, url in GRAIL_SOURCES.items():
            text = _fetch(url)
            if text is None:
                missed.append(key); continue
            open(os.path.join(cache, name_map[key]), "w").write(text)
            got[key] = len(text)
        if not got:
            return self._env("refresh", "offline",
                             note=("no network — running on the EMBEDDED spec + "
                                   "ecosystem snapshot baked into this file. The "
                                   "woods are fine; refresh next time you have "
                                   "internet to sync with the global grail."),
                             dashboards=DASHBOARDS)
        summary = None
        gs = _read_json(os.path.join(cache, "god-status.json"))
        if gs:
            summary = gs.get("summary")
        _write_json(os.path.join(cache, "meta.json"),
                    {"refreshed_at": _now(), "sources": list(got),
                     "missed": missed, "grail_summary": summary})
        return self._env("refresh", "success", refreshed=list(got), missed=missed,
                         grail_summary=summary, dashboards=DASHBOARDS,
                         note="synced with the global grail; action=spec now serves the latest canon.")

    def _live_parts(self, ctx):
        """Parts list: cached-from-grail if fresh, else live fetch, else None."""
        cached = os.path.join(self._cache_dir(ctx), "god-status.json")
        gs = _read_json(cached)
        if not gs:
            text = _fetch(GRAIL_SOURCES["god_status"])
            gs = json.loads(text) if text else None
        return gs

    def _ecosystem(self, kwargs, ctx):
        gs = self._live_parts(ctx)
        if gs:
            groups = {}
            for p in gs.get("parts", []):
                groups.setdefault(p.get("group", "?"), []).append(p.get("name"))
            return self._env("ecosystem", "success", source="rapp-god (live registry)",
                             summary=gs.get("summary"), generated=gs.get("generated"),
                             groups=groups, dashboards=DASHBOARDS,
                             note="every part + version, content-addressed; drift-observed.")
        return self._env("ecosystem", "embedded",
                         source="embedded snapshot (no network)",
                         groups=ECOSYSTEM_PARTS, dashboards=DASHBOARDS,
                         note=("the shape of the whole RAPP world, baked into this "
                               "file. action=refresh online for the live 57-part "
                               "registry from rapp-god."))

    def _find(self, kwargs, ctx):
        q = (kwargs.get("query") or "").strip().lower()
        if not q:
            return self._env("find", "error", error="pass query=<what part are you looking for>")
        gs = self._live_parts(ctx)
        hits = []
        if gs:
            for p in gs.get("parts", []):
                blob = json.dumps(p).lower()
                if q in blob:
                    hits.append({"name": p.get("name"), "group": p.get("group"),
                                 "kind": p.get("kind"), "note": p.get("note"),
                                 "drift": p.get("drift"), "versions": p.get("versions")})
            src = "rapp-god (live)"
        else:
            for grp, parts in ECOSYSTEM_PARTS.items():
                for name in parts:
                    if q in (grp + " " + name).lower():
                        hits.append({"name": name, "group": grp})
            src = "embedded snapshot"
        return self._env("find", "success", query=q, source=src, matches=len(hits),
                         results=hits[:40])

    def _commit_push(self, ctx, message, do_push):
        if ctx["offline"] or not do_push:
            return {"pushed": False, "planned": [
                f"git -C {ctx['repo_dir']} add -A",
                f"git -C {ctx['repo_dir']} commit -m '{message}'",
                f"git -C {ctx['repo_dir']} push"]}
        rd = ctx["repo_dir"]
        _run(["git", "-C", rd, "add", "-A"])
        rc, _, err = _run(["git", "-C", rd, "commit", "-m", message])
        if rc != 0 and "nothing to commit" not in err.lower():
            return {"pushed": False, "error": f"commit failed: {err[:200]}"}
        rc, _, err = _run(["git", "-C", rd, "push"])
        if rc != 0:
            return {"pushed": False, "error": (f"push failed ({err[:200]}). Are "
                    f"you a collaborator on {ctx['repo']}?")}
        return {"pushed": True}

    # ---- perform ----
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "help").lower()
        ctx = self._ctx(kwargs)

        # ── orient ──
        if action == "spec":
            # serve the freshest spec: pulled-from-grail cache if present, else
            # the embedded baseline that travels in this file (no drift, ever).
            cached = _read_json(os.path.join(ctx["home"], ".brainstem", "rapp", "grail-cache", "meta.json"))
            fresh = None
            if cached:
                sp = os.path.join(ctx["home"], ".brainstem", "rapp", "grail-cache", "SPEC.md")
                if os.path.exists(sp):
                    fresh = open(sp).read()
            head = ("[serving the LIVE grail spec, refreshed " + cached["refreshed_at"] + "]\n\n"
                    if (cached and fresh) else "[embedded baseline spec — run action=refresh online to pull the latest grail]\n\n")
            return head + _SPEC + (("\n\n---\n# Canonical SPEC.md (from the grail)\n\n" + fresh) if fresh else "")
        if action == "ecosystem":
            return self._ecosystem(kwargs, ctx)
        if action == "find":
            return self._find(kwargs, ctx)
        if action == "refresh":
            return self._refresh(ctx)
        if action == "protocol":
            return _SPEC.split("\n\n", 1)[0] + ("\n\nThis is one self-contained "
                   "agent (the contract). It names no door; point it with "
                   "repo=<owner/repo>. action=spec for the full map.")
        if action == "help" or action not in self.metadata["parameters"]["properties"]["action"]["enum"]:
            return (
                "RappAgent — the one agent for the whole RAPP ecosystem.\n"
                "  orient   : spec · ecosystem · find query=… · refresh (pull latest grail)\n"
                "  identity : whoami · estate · door rappid=…\n"
                "  on-device: cubby_new slug=… · cubby_list · cubby_show cubby=… ·\n"
                "             super_rar where=local query=… (search your whole estate) ·\n"
                "             cubby_collect slug=… query=… (assemble a cubby from a search) ·\n"
                "             cubby_egg cubby=… · cubby_import path=…\n"
                "  neighborhood (repo=<owner/repo>):\n"
                "             mount · join · browse · stash path=… · hatch path=… ·\n"
                "             load [cubby=…] · unload · show_and_tell title=… ·\n"
                "             sync · branch topic=… · invite github_login=… ·\n"
                "             qr · enter · super_rar where=neighborhood query=…\n"
                "  action=spec for the full map of how it all fits together.")

        # ── identity ──
        if action == "whoami":
            est = _read_json(os.path.join(ctx["home"], ".brainstem", "estate.json")) or {}
            created = est.get("created", [])
            return self._env(action, "success", rappid=ctx["rappid"],
                             github_handle=ctx["handle"],
                             estate_doors=len(created) + len(est.get("member", [])),
                             neighborhood=ctx["repo"],
                             local_cubbies=len([d for d in (os.listdir(ctx["cubby_root_local"])
                                 if os.path.isdir(ctx["cubby_root_local"]) else []) if not d.startswith('.')]))
        if action == "estate":
            est = _read_json(os.path.join(ctx["home"], ".brainstem", "estate.json"))
            if not est:
                return self._env(action, "empty",
                                 note="no ~/.brainstem/estate.json yet — plant or join a door first.")
            return self._env(action, "success", schema=est.get("schema"),
                             created=est.get("created", []), member=est.get("member", []))
        if action == "door":
            d = door_from_rappid(kwargs.get("rappid", ""))
            if not d:
                return self._env(action, "error",
                                 error="not a locatable rappid (Eternity / v2 / owner/repo).")
            return self._env(action, "success", **d)

        # ── on-device cubbies ──
        if action.startswith("cubby_") or (action == "super_rar" and kwargs.get("where") == "local"):
            return self._cubby(action, kwargs, ctx)

        # ── neighborhood ──
        if not ctx["repo"]:
            return self._env(action, "error",
                             error=("no neighborhood set — pass repo=<owner/repo>, "
                                    "set RAPP_NEIGHBORHOOD, or write "
                                    "~/.brainstem/rapp/neighborhood.json {repo}."))
        return self._neighborhood(action, kwargs, ctx)

    # ── on-device cubby ops ──
    def _cubby(self, action, kwargs, ctx):
        root = ctx["cubby_root_local"]
        if action == "cubby_new":
            slug = (kwargs.get("slug") or kwargs.get("cubby") or "").strip()
            if not _SLUG_RE.match(slug):
                return self._env(action, "error", error="pass slug=<name>")
            cubby = os.path.join(root, slug)
            existed = os.path.isfile(os.path.join(cubby, "cubby.json"))
            for d in CUBBY_ANATOMY:
                os.makedirs(os.path.join(cubby, d), exist_ok=True)
                gk = os.path.join(cubby, d, ".gitkeep")
                if not os.path.exists(gk):
                    open(gk, "w").close()
            if not existed:
                _write_json(os.path.join(cubby, "cubby.json"), {
                    "schema": CUBBY_SCHEMA, "github_login": ctx["handle"], "slug": slug,
                    "display_name": slug, "what_im_cooking": kwargs.get("what", ""),
                    "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                    "streamable": {"agents": True}})
            return self._env(action, "already_exists" if existed else "success",
                             cubby=slug, path=cubby)
        if action == "cubby_list":
            out = []
            if os.path.isdir(root):
                for slug in sorted(os.listdir(root)):
                    if slug.startswith("."):
                        continue
                    cj = _read_json(os.path.join(root, slug, "cubby.json"))
                    if cj is None and not os.path.isdir(os.path.join(root, slug)):
                        continue
                    counts = {k: len([p for p in glob.glob(os.path.join(root, slug, sub, pat))
                                      if not os.path.basename(p).startswith(".")])
                              for k, (sub, pat) in SUPER_RAR_KINDS.items()}
                    out.append({"cubby": slug, "what_im_cooking": (cj or {}).get("what_im_cooking", ""),
                                "counts": {k: v for k, v in counts.items() if v}})
            return self._env(action, "success", root=root, cubbies=out, count=len(out))
        if action == "cubby_show":
            slug = (kwargs.get("cubby") or "").strip()
            if not _SLUG_RE.match(slug) or not os.path.isdir(os.path.join(root, slug)):
                return self._env(action, "error", error=f"no local cubby '{slug}'")
            mine = [e for e in _build_super_rar(root) if e["cubby"] == slug]
            return self._env(action, "success", cubby=slug,
                             meta=_read_json(os.path.join(root, slug, "cubby.json")),
                             inventory=mine, count=len(mine))
        if action == "super_rar":   # where=local — your WHOLE local estate
            q = (kwargs.get("query") or "").strip().lower()
            source = (kwargs.get("source") or "all").lower()  # cubbies|brainstem|all
            bs = kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cands = self._local_candidates(root, bs, source)
            hits = [c for c in cands
                    if _q_match(q, {k: c.get(k) for k in ("kind", "name", "path", "cubby")}, c["abs"])] \
                if q else cands
            view = [{k: c[k] for k in ("kind", "name", "cubby", "path") if k in c} for c in hits]
            return self._env(action, "success", where="local", source=source, query=q or None,
                             matches=len(hits), total=len(cands),
                             by_kind={k: sum(1 for c in cands if c["kind"] == k)
                                      for k in {x["kind"] for x in cands}},
                             results=view[:50])
        if action == "cubby_egg":
            slug = (kwargs.get("cubby") or "").strip()
            cubby = os.path.join(root, slug)
            if not _SLUG_RE.match(slug) or not os.path.isdir(cubby):
                return self._env(action, "error", error=f"no local cubby '{slug}'")
            buf = io.BytesIO()
            files = 0
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                z.writestr("manifest.json", json.dumps({
                    "schema": CUBBY_EGG_SCHEMA, "type": "cubby", "version": "1.0",
                    "slug": slug, "cubby_schema": CUBBY_SCHEMA, "minted_at": _now(),
                    "anatomy": list(CUBBY_ANATOMY),
                    "organism": ("A digital organism carved from a rapp estate — a "
                                 "coherent slice (its own anatomy) that lives on in its "
                                 "own cubby, hatchable anywhere (Article XXXVII).")}, indent=2))
                z.writestr("HATCH.md", f"# Cubby egg: {slug}\nHatch local with "
                           "`cubby_import path=<egg>`, or land it in a neighborhood "
                           "cubby with `hatch path=<egg>`.\n")
                for dp, _d, fns in os.walk(cubby):
                    for fn in fns:
                        ap = os.path.join(dp, fn)
                        z.writestr("cubby/" + os.path.relpath(ap, cubby), open(ap, "rb").read())
                        files += 1
            blob = buf.getvalue()
            out = kwargs.get("path") or os.path.join(ctx["home"], ".brainstem", "eggs", f"cubby-{slug}.egg")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "wb").write(blob)
            return self._env(action, "success", cubby=slug, egg=out, files=files,
                             sha256=hashlib.sha256(blob).hexdigest(), size_bytes=len(blob))
        if action == "cubby_import":
            return self._hatch_egg(kwargs.get("path"), os.path.join(root, "{slug}"),
                                   action, ctx, local=True)
        if action == "cubby_collect":
            return self._collect(kwargs, ctx, root)
        return self._env(action, "error", error="unknown cubby op")

    def _local_candidates(self, root, bs, source):
        """Your whole local estate as candidates (abs paths): organized cubbies
        + the live brainstem (agents/organs/senses/rapps/neighborhoods/eggs)."""
        cands = []
        if source in ("cubbies", "all"):
            for e in _build_super_rar(root):
                cands.append({**e, "abs": os.path.join(root, e["path"])})
        if source in ("brainstem", "all"):
            for kind, (sub, pat) in SUPER_RAR_KINDS.items():
                for p in sorted(glob.glob(os.path.join(bs, sub, pat))):
                    nm = os.path.basename(p)
                    if nm.startswith(".") or not os.path.isfile(p):
                        continue
                    cands.append({"kind": kind, "name": nm, "cubby": "(brainstem)",
                                  "path": os.path.relpath(p, bs), "abs": p})
        return cands

    def _collect(self, kwargs, ctx, root):
        """Assemble a new local cubby from a super-RAR search across everything
        on-device. The natural-language move: 'put the X for this project in its
        own cubby' → search local stack for X, copy the matches into a fresh
        cubby (ready to egg + mirror to a neighborhood)."""
        slug = (kwargs.get("slug") or kwargs.get("cubby") or "").strip()
        q = (kwargs.get("query") or "").strip().lower()
        if not _SLUG_RE.match(slug):
            return self._env("cubby_collect", "error", error="pass slug=<new cubby name>")
        if not q:
            return self._env("cubby_collect", "error", error="pass query=<what to collect>")
        source = (kwargs.get("source") or "all").lower()   # cubbies | brainstem | all
        bs = kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # gather candidates across the whole local estate; don't recollect target
        candidates = [c for c in self._local_candidates(root, bs, source) if c.get("cubby") != slug]
        # filter by the query — search on ANYTHING (metadata + file content)
        matched, skipped = [], []
        for c in candidates:
            meta = {k: c.get(k) for k in ("kind", "name", "path", "cubby")}
            if not _q_match(q, meta, c["abs"]):
                continue
            if _SECRET_NAME_RE.search(c["name"]):
                skipped.append({"name": c["name"], "why": "secret-shaped"}); continue
            matched.append(c)
        if not matched:
            return self._env("cubby_collect", "empty", query=q,
                             searched=len(candidates),
                             note="nothing matched — try `super_rar where=local query=…` to see what exists.")
        # create the cubby + copy the matches in (dedupe by name within a kind)
        cubby = os.path.join(root, slug)
        for d in CUBBY_ANATOMY:
            os.makedirs(os.path.join(cubby, d), exist_ok=True)
        if not os.path.isfile(os.path.join(cubby, "cubby.json")):
            _write_json(os.path.join(cubby, "cubby.json"), {
                "schema": CUBBY_SCHEMA, "github_login": ctx["handle"], "slug": slug,
                "display_name": slug, "what_im_cooking": kwargs.get("what", f"collected: {q}"),
                "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                "streamable": {"agents": True},
                "collected_from": {"query": q, "source": source, "at": _now()}})
        kind_dir = {"agent": "agents", "organ": "organs", "sense": "senses",
                    "rapplication": "rapplications", "neighborhood": "neighborhoods", "egg": "eggs"}
        collected = []
        for c in matched:
            sub = kind_dir.get(c["kind"], "agents")
            dst = os.path.join(cubby, sub, c["name"])
            if os.path.exists(dst):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(c["abs"], dst)
            collected.append({"kind": c["kind"], "name": c["name"],
                              "from": c["cubby"], "into": f"cubbies/{slug}/{sub}/{c['name']}"})
        return self._env("cubby_collect", "success", cubby=slug, query=q,
                         collected=collected, count=len(collected),
                         skipped_secrets=skipped,
                         is_organism=True,
                         note=("you just carved a digital organism out of your estate — a "
                               "coherent slice that now lives in its own cubby and can be "
                               "egged + hatched anywhere."),
                         next=("now: `cubby_egg cubby=%s` to pack the organism, then `hatch "
                               "path=<egg>` (after `mount`) to mirror it into your "
                               "neighborhood cubby." % slug))

    # ── neighborhood ops (the shared-neighborhood flow (generic; cover-safe)) ──
    def _neighborhood(self, action, kwargs, ctx):
        mounted = ctx["repo_dir"] and os.path.isdir(ctx["repo_dir"]) and \
            os.path.exists(os.path.join(ctx["repo_dir"], "neighborhood.json"))

        if action == "qr":
            from urllib.parse import quote
            num = kwargs.get("rappid") or ctx["repo"]
            return self._env(action, "success", door=ctx["repo"],
                             dial_url=f"{PAYPHONE_URL}?dial={quote(num, safe='')}",
                             share_url=f"{PAYPHONE_URL}?share={quote(num, safe='')}",
                             how_to="open share_url → scannable QR to hand out; scanners dial pre-filled.")
        if action == "enter":
            return self._env(action, "success", lobby_url=LOBBY_URL, payphone_url=PAYPHONE_URL,
                             note=("the live E2E room is a browser surface — open the "
                                   "payphone, sign in with GitHub, it hands you into the room."))
        if action == "mount":
            if ctx["offline"]:
                return self._env(action, "success", mounted=mounted, clone=ctx["repo_dir"], note="test/offline")
            if mounted:
                rc, _, err = _run(["git", "-C", ctx["repo_dir"], "pull", "--ff-only"])
                return self._env(action, "success" if rc == 0 else "degraded",
                                 mounted=True, clone=ctx["repo_dir"],
                                 note=None if rc == 0 else f"pull failed ({err[:120]}) — serving cache")
            os.makedirs(os.path.dirname(ctx["repo_dir"]), exist_ok=True)
            rc, _, err = _run(["gh", "repo", "clone", ctx["repo"], ctx["repo_dir"]])
            if rc != 0:
                return self._env(action, "error",
                                 error=f"clone failed: {err[:240]}. Collaborator access on {ctx['repo']}?")
            return self._env(action, "success", mounted=True, clone=ctx["repo_dir"])

        if not mounted:
            return self._env(action, "error", error="not mounted — run action=mount first")
        rd = ctx["repo_dir"]

        if action == "browse":
            cubbies = []
            root = os.path.join(rd, "cubbies")
            for entry in sorted(os.listdir(root) if os.path.isdir(root) else []):
                if entry.startswith(("_", ".")) or not os.path.isdir(os.path.join(root, entry)):
                    continue   # skip index.json + any stray files — cubbies are dirs
                c = _read_json(os.path.join(root, entry, "cubby.json")) or {}
                agents = sorted(f for f in (os.listdir(os.path.join(root, entry, "agents"))
                                if os.path.isdir(os.path.join(root, entry, "agents")) else [])
                                if f.endswith("_agent.py"))
                cubbies.append({"github_login": c.get("github_login", entry),
                                "what_im_cooking": c.get("what_im_cooking", ""), "agents": agents})
            return self._env(action, "success", cubbies=cubbies, count=len(cubbies))

        if action == "super_rar":   # where=neighborhood (default)
            croot = os.path.join(rd, "cubbies")
            entries = _build_super_rar(croot)
            q = (kwargs.get("query") or "").strip().lower()
            hits = [e for e in entries if _q_match(q, e, os.path.join(croot, e["path"]))] if q else entries
            return self._env(action, "success", where="neighborhood", query=q or None,
                             matches=len(hits), total=len(entries),
                             by_kind={k: sum(1 for e in entries if e["kind"] == k)
                                      for k in {x["kind"] for x in entries}},
                             results=hits[:50],
                             hint="stream an agent hit with action=load cubby=<its cubby>.")

        if not ctx["handle"]:
            return self._env(action, "error", error="run `gh auth login` (or pass _handle).")
        me = ctx["handle"]
        if not _HANDLE_RE.match(me):
            return self._env(action, "error", error=f"unsafe handle {me!r}")
        my_cubby = os.path.join(rd, "cubbies", me)

        if action == "join":
            existed = os.path.isfile(os.path.join(my_cubby, "cubby.json"))
            for d in CUBBY_ANATOMY:
                os.makedirs(os.path.join(my_cubby, d), exist_ok=True)
            if not existed:
                _write_json(os.path.join(my_cubby, "cubby.json"), {
                    "schema": CUBBY_SCHEMA, "github_login": me, "rappid": ctx["rappid"],
                    "display_name": me, "what_im_cooking": kwargs.get("what", "just moved in"),
                    "created_at": _now(), "estate": {"anatomy": list(CUBBY_ANATOMY)},
                    "streamable": {"agents": True}})
            members = _read_json(os.path.join(rd, "members.json")) or \
                {"schema": "rapp-neighborhood-members/1.0", "members": []}
            if not any(m.get("github_login") == me for m in members["members"]):
                members["members"].append({"github_login": me, "rappid": ctx["rappid"],
                    "role": "member", "joined_at": _now(), "via": "cubby-join"})
                _write_json(os.path.join(rd, "members.json"), members)
            git = self._commit_push(ctx, f"cubby: {me} joins", kwargs.get("push", True))
            return self._env(action, "already_joined" if existed else "success",
                             cubby=f"cubbies/{me}/", **git)

        if action == "stash":
            src = kwargs.get("path")
            if not src or not os.path.isfile(src):
                return self._env(action, "error", error="pass path=<existing file>")
            if (kwargs.get("cubby") or me) != me:
                return self._env(action, "refused", error=f"cubbies are isolated — you write only in cubbies/{me}/.")
            base = os.path.basename(src)
            if _SECRET_NAME_RE.search(base):
                return self._env(action, "refused", error=f"'{base}' is secret-shaped — bones, not substance.")
            sub = ("agents" if base.endswith("_agent.py") else "organs" if base.endswith("_organ.py")
                   else "eggs" if base.endswith(".egg") else "show-and-tell")
            dst = os.path.join(my_cubby, sub, base)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            git = self._commit_push(ctx, f"cubby({me}): stash {sub}/{base}", kwargs.get("push", True))
            return self._env(action, "success", stashed=f"cubbies/{me}/{sub}/{base}", **git)

        if action == "hatch":
            res = self._hatch_egg(kwargs.get("path"), my_cubby, action, ctx, local=False)
            if isinstance(res, dict) and res.get("_ok"):
                git = self._commit_push(ctx, f"cubby({me}): hatch egg ({len(res['landed'])} files)",
                                        kwargs.get("push", True))
                return self._env(action, "success", landed=res["landed"],
                                 refused_secrets=res["refused"], cubby=f"cubbies/{me}/", **git)
            return res  # already an error envelope

        if action == "load":
            return self._load(kwargs, ctx, rd, me)
        if action == "unload":
            return self._unload(kwargs, ctx)
        if action == "show_and_tell":
            return self._show_and_tell(kwargs, ctx, rd, me)
        if action == "sync":
            if not ctx["offline"]:
                _run(["git", "-C", rd, "pull", "--ff-only"])
            return self._env(action, "success", note="pulled latest; browse / super_rar to see what's new.")
        if action == "branch":
            topic = _slugify(kwargs.get("topic") or "wip", "wip")
            branch = f"cubby/{me}/{topic}"
            if ctx["offline"]:
                return self._env(action, "dry_run", branch=branch)
            rc, _, err = _run(["git", "-C", rd, "checkout", "-b", branch])
            if rc != 0:
                return self._env(action, "error", error=err[:200])
            _run(["git", "-C", rd, "push", "-u", "origin", branch])
            return self._env(action, "success", branch=branch, note="yours — never must merge to main.")
        if action == "invite":
            login = kwargs.get("github_login")
            if not login:
                return self._env(action, "error", error="pass github_login=<who>")
            cmd = ["gh", "api", "-X", "PUT", f"repos/{ctx['repo']}/collaborators/{login}",
                   "--field", "permission=push"]
            if not kwargs.get("confirm"):
                return self._env(action, "dry_run", command=" ".join(cmd),
                                 note="re-run with confirm=true to invite.")
            rc, _, err = _run(cmd)
            return self._env(action, "success" if rc == 0 else "error",
                             **({"invited": login} if rc == 0 else {"error": err[:240]}))
        return self._env(action, "error", error="unreachable")

    # ── shared egg hatch (into a local cubby slug-dir or a neighborhood cubby) ──
    def _hatch_egg(self, src, dest_template, action, ctx, local):
        if not src or not os.path.isfile(src):
            return self._env(action, "error", error="pass path=<a .egg file>")
        try:
            z = zipfile.ZipFile(src)
        except zipfile.BadZipFile:
            return self._env(action, "error", error="not a valid .egg (zip)")
        mani = {}
        try:
            mani = json.loads(z.read("manifest.json"))
        except (KeyError, ValueError):
            pass
        if any(n.startswith("cubby/") for n in z.namelist()):
            prefix = "cubby/"
        elif any(n.startswith("repo/") for n in z.namelist()):
            prefix = "repo/"
        else:
            return self._env(action, "refused", error="unrecognized egg layout — refusing to guess.")
        if local:
            slug = mani.get("slug") or "imported"
            if not _SLUG_RE.match(slug):
                slug = "imported"
            dest = dest_template.replace("{slug}", slug)
        else:
            dest = dest_template
        landed, refused = [], []
        for n in z.namelist():
            if not n.startswith(prefix) or n.endswith("/"):
                continue
            rel = n[len(prefix):]
            base = os.path.basename(rel)
            if base in (".gitkeep",):
                continue
            if _SECRET_NAME_RE.search(base):
                refused.append(rel); continue
            top = rel.split("/", 1)[0]
            if top not in CUBBY_ANATOMY:
                if base.endswith("_agent.py"):
                    rel = "agents/" + base
                else:
                    refused.append(rel); continue
            target = os.path.normpath(os.path.join(dest, rel))
            if not target.startswith(os.path.normpath(dest) + os.sep):
                refused.append(rel); continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "wb") as f:
                f.write(z.read(n))
            landed.append(target if local else os.path.relpath(target, ctx["repo_dir"]))
        if local:
            return self._env(action, "success", cubby=os.path.basename(dest),
                             path=dest, landed=len(landed), refused_secrets=refused)
        return {"_ok": True, "landed": landed, "refused": refused}

    # ── load / unload (git-invisible streaming) ──
    def _load(self, kwargs, ctx, rd, me):
        def has_agents(h):
            d = os.path.join(rd, "cubbies", h, "agents")
            return os.path.isdir(d) and any(f.endswith("_agent.py") for f in os.listdir(d))
        src_cubby = kwargs.get("cubby") or (me if has_agents(me) else None)
        if not src_cubby:
            return self._env("load", "error", error="pass cubby=<whose agents to stream>")
        if not _HANDLE_RE.match(src_cubby):
            return self._env("load", "error", error=f"unsafe cubby {src_cubby!r}")
        src = os.path.join(rd, "cubbies", src_cubby, "agents")
        if not os.path.isdir(src):
            return self._env("load", "error", error=f"no agents/ in cubbies/{src_cubby}/")
        bs = kwargs.get("_brainstem_dir") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target = os.path.join(bs, "agents")
        os.makedirs(target, exist_ok=True)
        loadout = _read_json(ctx["loadout_path"]) or {"schema": "rapp-loadout/1.0", "loaded": []}
        known = {e["file"] for e in loadout["loaded"]}
        loaded, skipped = [], []
        for fn in sorted(os.listdir(src)):
            if not _AGENT_FILE_RE.match(fn):
                continue
            if fn in KERNEL_AGENTS:
                skipped.append({"file": fn, "why": "kernel — never overwritten"}); continue
            dst = os.path.join(target, fn)
            if os.path.exists(dst) and fn not in known and _sha256_file(dst) != _sha256_file(os.path.join(src, fn)):
                skipped.append({"file": fn, "why": "your own file — won't overwrite"}); continue
            shutil.copy2(os.path.join(src, fn), dst)
            loadout["loaded"] = [e for e in loadout["loaded"] if e["file"] != fn] + \
                [{"file": fn, "sha256": _sha256_file(dst), "from_cubby": src_cubby,
                  "loaded_at": _now(), "target": target}]
            loaded.append(fn)
        excluded = self._register_excludes(bs, target, loaded)
        _write_json(ctx["loadout_path"], loadout)
        return self._env("load", "success", from_cubby=src_cubby, loaded=loaded,
                         skipped=skipped, git_excluded=excluded,
                         note="streamed + git-invisible (.git/info/exclude) — zero commit risk.")

    def _unload(self, kwargs, ctx):
        loadout = _read_json(ctx["loadout_path"]) or {"loaded": []}
        bs = kwargs.get("_brainstem_dir")
        removed, kept, remaining = [], [], []
        for e in loadout.get("loaded", []):
            fn, target = e.get("file", ""), e.get("target", "")
            if fn in KERNEL_AGENTS or not _AGENT_FILE_RE.match(fn):
                remaining.append(e); kept.append(f"{fn} (refused)"); continue
            if bs and os.path.normpath(target) != os.path.normpath(os.path.join(bs, "agents")):
                remaining.append(e); kept.append(fn); continue
            p = os.path.join(target, fn)
            if os.path.basename(p) == fn and os.path.exists(p):
                os.remove(p)
            removed.append(fn)
            self._unregister_exclude(os.path.dirname(target), target, fn)
        loadout["loaded"] = remaining
        _write_json(ctx["loadout_path"], loadout)
        return self._env("unload", "success", removed=removed, kept=kept)

    def _show_and_tell(self, kwargs, ctx, rd, me):
        title = kwargs.get("title") or "show and tell"
        text = kwargs.get("text") or ""
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        rel = f"cubbies/{me}/show-and-tell/{date}-{_slugify(title)}.md"
        p = os.path.join(rd, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(f"# {title}\n\n*{_now()} — @{me}*\n\n{text}\n")
        ev = {"schema": EVENT_SCHEMA, "kind": "show-and-tell", "from": ctx["rappid"],
              "ts": _now(), "cubby": me, "body": {"title": title, "text": text[:4096], "artifact": rel}}
        fp = hashlib.sha256(ctx["rappid"].encode()).hexdigest()[:16]
        ev_rel = f"events/{fp}-{ev['ts'].replace('-', '').replace(':', '')}.json"
        _write_json(os.path.join(rd, ev_rel), ev)
        git = self._commit_push(ctx, f"show-and-tell({me}): {title[:50]}", kwargs.get("push", True))
        return self._env("show_and_tell", "success", artifact=rel, event=ev_rel, **git)

    # ── git-invisibility helpers ──
    @staticmethod
    def _git_top(start):
        rc, out, _ = _run(["git", "-C", start, "rev-parse", "--show-toplevel"])
        return out if rc == 0 and out else None

    def _register_excludes(self, bs, target, files):
        top = self._git_top(bs)
        if not top:
            return []
        ex = os.path.join(top, ".git", "info", "exclude")
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        existing = open(ex).read() if os.path.exists(ex) else ""
        add = [os.path.relpath(os.path.join(target, fn), top) for fn in files
               if os.path.relpath(os.path.join(target, fn), top) not in existing.splitlines()]
        if add:
            with open(ex, "a") as f:
                if existing and not existing.endswith("\n"):
                    f.write("\n")
                f.write("# streamed in (rapp load) — git-invisible by design\n" + "\n".join(add) + "\n")
        return add

    def _unregister_exclude(self, bs, target, fn):
        top = self._git_top(bs)
        if not top:
            return
        ex = os.path.join(top, ".git", "info", "exclude")
        if not os.path.exists(ex):
            return
        rel = os.path.relpath(os.path.join(target, fn), top)
        lines = [l for l in open(ex).read().splitlines() if l.strip() != rel]
        with open(ex, "w") as f:
            f.write("\n".join(lines) + ("\n" if lines else ""))


if __name__ == "__main__":
    a = RappAgent()
    print(a.perform(action="help"))
    print("\n--- spec ---\n")
    print(a.perform(action="spec")[:600])
