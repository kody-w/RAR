"""Pocket Brainstem's Python side: runs real Brainstem agents inside the iPhone app.

The Swift app owns the model, the chat and the screens. This module owns everything that
has to be Python so that agents run unchanged:

  * loads rapp_brainstem/agents/*_agent.py with the same shims brainstem.py registers
    (agents.basic_agent, openrappter.agents.basic_agent, utils.azure_file_storage -> local_storage)
  * runs an agent's perform(**kwargs) and collects system_context() from agents that have one
  * thaws and freezes brainfreeze-layout snapshots (.snapshot.tar.gz)
  * previews, installs, packs and removes agent cards (see agentcard_core.py)

Swift talks to it through one function, handle(request_json) -> response_json, always from
the same thread. Every response has "ok": true/false. Nothing here uses the network; agents
may, if their own code does.

Layout under HOME (the app's Documents/brainstem folder, visible in the Files app):

    rapp_brainstem/            the Brainstem: soul.md, agents/, local_storage.py, .brainstem_data/ (memory)
    rapp_brainstem/agents/.cards.json   where each card-installed agent came from
    .hatch/chat.json           the conversation (written by Swift, read by freeze)
    backups/                   automatic freezes taken before a thaw replaces the Brainstem
"""
import ast
import base64
import datetime as _dt
import hashlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tarfile
import time
import traceback
import types
from pathlib import Path

import agentcard_core as cards

HOST_VERSION = "0.1.0"
HOME = None            # Path, set by init
_agents = {}           # name -> instance
_files = {}            # name -> file path
_quarantined = {}      # file -> reason
_shims_done = False

# Never frozen into a snapshot, never shared: sign-in files and keys stay on this phone.
_NEVER_TRAVEL = (".env", ".copilot_token", ".copilot_session", ".brainstem_secret", ".brainstem_book.json")
_SKIP_DIRS = ("__pycache__", ".git")
_NOT_MODULES = {"agents", "utils", "openrappter", "local_storage", "basic_agent"}

_FALLBACK_BASIC_AGENT = '''\
class BasicAgent:
    """Stand-in BasicAgent (the Brainstem's own agents/basic_agent.py is used when present)."""

    def __init__(self, name=None, metadata=None):
        if name is not None:
            self.name = name
        elif not hasattr(self, "name"):
            self.name = "BasicAgent"
        if metadata is not None:
            self.metadata = metadata
        elif not hasattr(self, "metadata"):
            self.metadata = {"name": self.name, "description": "",
                             "parameters": {"type": "object", "properties": {}, "required": []}}

    def perform(self, **kwargs):
        return "Not implemented."

    def system_context(self):
        return None

    def to_tool(self):
        return {"type": "function", "function": {
            "name": self.name,
            "description": self.metadata.get("description", ""),
            "parameters": self.metadata.get("parameters", {"type": "object", "properties": {}})}}
'''

_FALLBACK_LOCAL_STORAGE = '''\
"""Stand-in local storage written by Pocket Brainstem on a phone that has never been thawed.
Same interface and layout as the Brainstem's own local_storage.py (which replaces this on thaw):
  .brainstem_data/shared_memories/memory.json    shared memories
  .brainstem_data/memory/{guid}/user_memory.json per-user memories"""
import json, os, threading

_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".brainstem_data")
_lock = threading.RLock()


def _safe(*parts):
    base = os.path.abspath(_DATA_DIR)
    target = os.path.abspath(os.path.join(base, *[str(p) for p in parts]))
    if os.path.commonpath([base, target]) != base:
        raise ValueError("path escapes data directory")
    return target


class AzureFileStorageManager:
    def __init__(self, share_name=None, **kwargs):
        self.storage_root = ""
        self.default_file_name = "memory.json"
        self.current_guid = None

    def set_memory_context(self, user_guid=None):
        g = str(user_guid).strip() if user_guid else ""
        self.current_guid = g if g and os.sep not in g and g not in (".", "..") else None
        return True

    def _file_path(self):
        if self.current_guid:
            return _safe("memory", self.current_guid, "user_memory.json")
        return _safe("shared_memories", self.default_file_name)

    def read_json(self, file_path=None):
        p = _safe(file_path) if file_path else self._file_path()
        try:
            with open(p, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            return {}

    def write_json(self, data, file_path=None):
        p = _safe(file_path) if file_path else self._file_path()
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with _lock:
            tmp = p + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            os.replace(tmp, p)
        return True

    def update_json(self, update_fn, file_path=None):
        with _lock:
            data = update_fn(self.read_json(file_path))
            self.write_json(data, file_path)
            return data

    def read_file(self, file_path):
        try:
            with open(_safe(file_path), encoding="utf-8") as f:
                return f.read()
        except OSError:
            return None

    def write_file(self, file_path, content):
        p = _safe(file_path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    def list_files(self, directory=""):
        try:
            return sorted(os.listdir(_safe(directory)))
        except OSError:
            return []

    def delete_file(self, file_path):
        try:
            os.remove(_safe(file_path))
            return True
        except OSError:
            return False

    def file_exists(self, file_path):
        return os.path.exists(_safe(file_path))
'''

_FALLBACK_SOUL = "You are a helpful AI assistant running as a Brainstem on the user's iPhone."


# ── plumbing ─────────────────────────────────────────────────────────────────

def _bs() -> Path:
    return HOME / "rapp_brainstem"


def _agents_dir() -> Path:
    return _bs() / "agents"


def _now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def _sha_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _read_json(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def _write_json(p: Path, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, p)


def _ensure_skeleton():
    """A brand-new phone has no Brainstem yet: make the smallest one that works."""
    ad = _agents_dir()
    ad.mkdir(parents=True, exist_ok=True)
    if not (ad / "basic_agent.py").exists():
        (ad / "basic_agent.py").write_text(_FALLBACK_BASIC_AGENT, encoding="utf-8")
    if not (_bs() / "local_storage.py").exists():
        (_bs() / "local_storage.py").write_text(_FALLBACK_LOCAL_STORAGE, encoding="utf-8")
    # The stock agents every Brainstem starts with (both memory agents + Hacker News, from RAR), laid down
    # once on a new phone; removing one later sticks, because the marker says the stock was already offered.
    stock = Path(__file__).resolve().parent / "stock"
    mark = ad / ".stock_seeded"
    if stock.is_dir() and not mark.exists():
        for f in sorted(stock.glob("*_agent.py")):
            if not (ad / f.name).exists():
                (ad / f.name).write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        mark.write_text("seeded\n", encoding="utf-8")
    if not (_bs() / "soul.md").exists():
        (_bs() / "soul.md").write_text(_FALLBACK_SOUL + "\n", encoding="utf-8")


# ── agent loading (mirrors brainstem.py's loader and shims) ───────────────────

def _lib_root() -> Path:
    return HOME / "lib"


def _lib_dir(agent_file: str) -> Path:
    """Each agent's carried files live in their own folder, so removing the agent removes them."""
    return _lib_root() / Path(agent_file).stem


def _lib_paths():
    root = _lib_root()
    if root.is_dir():
        for d in sorted(root.iterdir()):
            if d.is_dir() and str(d) not in sys.path:
                sys.path.append(str(d))


def _unpack_files(card: dict, dest: Path):
    """Write a card's carried files into dest: wheels unzipped (pure Python, already checked), .py files copied."""
    import zipfile
    dest.mkdir(parents=True, exist_ok=True)
    for f in card.get("files") or []:
        data = base64.b64decode(f["b64"])
        name = f["path"].split("/", 1)[1]
        if name.endswith(".whl"):
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                for m in z.namelist():
                    if m.startswith("/") or ".." in m.split("/"):
                        raise ValueError(f"{name} has an unsafe entry {m}")
                z.extractall(dest)
        else:
            (dest / name).write_bytes(data)


def _forget_modules_under(folder: Path):
    """Drop cached modules loaded from a folder, so the next import reads them from where they live now."""
    root = str(folder)
    for k, m in list(sys.modules.items()):
        f = getattr(m, "__file__", None) or ""
        if f.startswith(root):
            sys.modules.pop(k, None)


def _register_shims():
    global _shims_done
    bs, ad = str(_bs()), str(_agents_dir())
    for p in (ad, bs):
        if p not in sys.path:
            sys.path.insert(0, p)
    if _shims_done:
        return
    spec = importlib.util.spec_from_file_location("pocket_basic_agent", _agents_dir() / "basic_agent.py")
    ba = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ba)

    def mod(name, path=None, **attrs):
        m = sys.modules.get(name) or types.ModuleType(name)
        if path is not None:
            m.__path__ = [path]
        for k, v in attrs.items():
            setattr(m, k, v)
        sys.modules[name] = m
        return m

    ba_mod = mod("agents.basic_agent", BasicAgent=ba.BasicAgent)
    mod("agents", ad, basic_agent=ba_mod)
    or_agents = mod("openrappter.agents", ad, basic_agent=ba_mod)
    mod("openrappter", bs, agents=or_agents)
    sys.modules["openrappter.agents.basic_agent"] = ba_mod

    if (_bs() / "local_storage.py").exists():
        spec = importlib.util.spec_from_file_location("local_storage", _bs() / "local_storage.py")
        ls = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ls)
        sys.modules["local_storage"] = ls
        afs = mod("utils.azure_file_storage", AzureFileStorageManager=ls.AzureFileStorageManager)
        # The grail's newer agents ask a factory for storage; on the phone it is always local storage.
        sf = mod("utils.storage_factory", get_storage_manager=lambda *a, **k: ls.AzureFileStorageManager(*a, **k))
        mod("utils", bs, azure_file_storage=afs, storage_factory=sf)
    _shims_done = True


def _reset_shims():
    """After a thaw the Brainstem folder is new, so its basic_agent/local_storage must be reloaded."""
    global _shims_done
    for name in ("agents", "agents.basic_agent", "openrappter", "openrappter.agents",
                 "openrappter.agents.basic_agent", "utils", "utils.azure_file_storage", "utils.storage_factory", "local_storage"):
        sys.modules.pop(name, None)
    _shims_done = False


def _validate(instance):
    name = getattr(instance, "name", None)
    if not isinstance(name, str) or not cards.NAME_RE.match(name or ""):
        return f"name {name!r} is not tool-safe"
    md = getattr(instance, "metadata", None)
    if not isinstance(md, dict):
        return "metadata is not a dict"
    params = md.get("parameters")
    if params is not None and (not isinstance(params, dict) or params.get("type") != "object"):
        return "metadata['parameters'] must be a JSON schema object"
    return None


def _load_file(path: Path) -> dict:
    """{name: instance} from one agent file. Raises on import errors (caller quarantines)."""
    _register_shims()
    _lib_paths()
    mod_name = f"pocket_agent_{path.stem}_{int(time.time() * 1000)}"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    found = {}
    for attr in dir(mod):
        cls = getattr(mod, attr)
        if (isinstance(cls, type) and cls.__module__ == mod.__name__ and hasattr(cls, "perform")
                and attr not in ("BasicAgent", "object") and not attr.startswith("_")):
            inst = cls()
            reason = _validate(inst)
            if reason:
                raise ValueError(f"{attr}: {reason}")
            if inst.name in found:
                raise ValueError(f"two agents named {inst.name!r} in one file")
            found[inst.name] = inst
    return found


def _why(e: Exception) -> str:
    if isinstance(e, ModuleNotFoundError):
        return f"needs the module {e.name!r}, which this app does not bundle (there is no pip on iOS)"
    return f"{type(e).__name__}: {e}"


def _reload_agents():
    global _agents, _files, _quarantined
    agents, files, quarantined = {}, {}, {}
    for path in sorted(_agents_dir().glob("*_agent.py")):
        if path.name == "basic_agent.py":
            continue
        try:
            for name, inst in _load_file(path).items():
                if name in agents:
                    quarantined[path.name] = f"duplicate agent name {name!r}"
                    continue
                agents[name], files[name] = inst, path
        except Exception as e:  # one bad cartridge never takes the rest down
            quarantined[path.name] = _why(e)
    _agents, _files, _quarantined = agents, files, quarantined


def _tool_of(inst) -> dict:
    try:
        return inst.to_tool()
    except Exception:
        md = inst.metadata
        return {"type": "function", "function": {"name": inst.name, "description": md.get("description", ""),
                                                 "parameters": md.get("parameters", {"type": "object", "properties": {}})}}


# ── operations ───────────────────────────────────────────────────────────────

def op_init(req):
    global HOME
    HOME = Path(req["home"]).expanduser().resolve()
    HOME.mkdir(parents=True, exist_ok=True)
    _ensure_skeleton()
    _reset_shims()
    _reload_agents()
    return op_status(req)


def op_status(req):
    version = (_bs() / "VERSION").read_text().strip() if (_bs() / "VERSION").exists() else None
    return {"home": str(HOME), "host_version": HOST_VERSION, "python": sys.version.split()[0],
            "brainstem_version": version, "agents": sorted(_agents),
            "quarantined": _quarantined, "has_soul": (_bs() / "soul.md").exists()}


def op_tools(req):
    return {"tools": [_tool_of(_agents[n]) for n in sorted(_agents)],
            "sources": {n: ("card" if _files[n].name in _read_json(_agents_dir() / ".cards.json", {}) else "brainstem")
                        for n in _agents},
            "quarantined": _quarantined}


def op_system_context(req):
    soul_p = _bs() / "soul.md"
    soul = soul_p.read_text(encoding="utf-8").strip() if soul_p.exists() else _FALLBACK_SOUL
    parts = []
    for name in sorted(_agents):
        fn = getattr(_agents[name], "system_context", None)
        if callable(fn):
            try:
                ctx = fn()
                if ctx:
                    parts.append(str(ctx).strip())
            except Exception as e:
                parts.append(f"[{name} could not add its context: {_why(e)}]")
    return {"soul": soul, "context": "\n\n".join(parts)}


def op_run(req):
    name, args = req["name"], req.get("arguments") or {}
    if isinstance(args, str):
        args = json.loads(args) if args.strip() else {}
    inst = _agents.get(name)
    if inst is None:
        return {"ok": False, "error": f"no agent named {name!r}", "output": f"Error: no agent named {name}."}
    started = time.time()
    try:
        out = inst.perform(**args)
    except Exception as e:
        tb = traceback.format_exc(limit=3)
        return {"ok": True, "failed": True, "output": f"Error: {name} failed: {_why(e)}", "traceback": tb}
    if not isinstance(out, str):
        try:
            out = json.dumps(out, ensure_ascii=False, default=str)
        except Exception:
            out = str(out)
    return {"output": out, "ms": int((time.time() - started) * 1000)}


# ── snapshots ────────────────────────────────────────────────────────────────

def _bundle_map(bundle):
    """{relative path: sha256} from a bundle.json, or None if the format isn't one we recognise."""
    files = bundle.get("files") if isinstance(bundle, dict) else None
    if isinstance(files, dict):
        out = {}
        for k, v in files.items():
            sha = v.get("sha256") if isinstance(v, dict) else v
            if not isinstance(sha, str):
                return None
            out[k] = sha
        return out
    if isinstance(files, list):
        try:
            return {e["path"]: e["sha256"] for e in files}
        except (KeyError, TypeError):
            return None
    return None


def _check_bundle(stage: Path):
    if not (stage / "bundle.json").is_file():
        return "no list in this snapshot (frozen before bundle.json)"
    listed = _bundle_map(_read_json(stage / "bundle.json", None))
    if listed is None:
        return "bundle.json is in a format this app doesn't read, so files were not checked"
    for rel, sha in listed.items():
        p = stage / rel
        if not p.is_file():
            p = stage / "rapp_brainstem" / rel
        if not p.is_file():
            raise ValueError(f"{rel} is listed but missing")
        if _sha_file(p) != sha:
            raise ValueError(f"{rel} does not match its fingerprint")
    listed_names = {Path(r).name for r in listed}
    for p in (stage / "rapp_brainstem").rglob("*_agent.py"):
        if p.name not in listed_names:
            raise ValueError(f"{p.relative_to(stage)} is an agent the list doesn't mention")
    return "every file matches the snapshot's list"


def _safe_members(tar):
    for m in tar.getmembers():
        n = m.name
        if (n.startswith("/") or ".." in Path(n).parts or m.issym() or m.islnk() or m.isdev()
                or not (n in ("state.json", "bundle.json", "bundle.sig", "bundle.signer", "sidecars")
                        or n.startswith(("rapp_brainstem", "sidecars/")))):
            raise ValueError(f"snapshot has an unsafe entry: {n}")
    return tar.getmembers()


def op_thaw(req):
    snap = Path(req["path"])
    if not snap.is_file():
        return {"ok": False, "error": f"no snapshot at {snap}"}
    stage = HOME / ".thaw"
    shutil.rmtree(stage, ignore_errors=True)
    stage.mkdir()
    try:
        with tarfile.open(snap, "r:gz") as tar:
            members = _safe_members(tar)
            tar.extractall(stage, members=members, filter="data") if sys.version_info >= (3, 12) \
                else tar.extractall(stage, members=members)
        if not (stage / "state.json").is_file() or not (stage / "rapp_brainstem").is_dir():
            raise ValueError("this isn't a Brainstem snapshot (no state.json or rapp_brainstem/)")
        checked = _check_bundle(stage)
    except (tarfile.TarError, ValueError, OSError) as e:
        shutil.rmtree(stage, ignore_errors=True)
        return {"ok": False, "error": f"refusing to wake it: {e}"}

    backup = None
    if _bs().exists() and req.get("backup", True):
        bdir = HOME / "backups"
        bdir.mkdir(exist_ok=True)
        backup = str(bdir / f"before-thaw-{time.strftime('%Y%m%d-%H%M%S')}.snapshot.tar.gz")
        op_freeze({"path": backup})
    shutil.rmtree(_bs(), ignore_errors=True)
    (stage / "rapp_brainstem").rename(_bs())
    _ensure_skeleton()

    state = _read_json(stage / "state.json", {})
    history = [{"role": m["role"], "content": m.get("content") or ""}
               for m in state.get("history", []) if m.get("role") in ("user", "assistant")]
    sha = _sha_file(snap)
    _write_json(HOME / ".hatch" / "chat.json", {
        "session_id": state.get("session_id") or "pocket-" + time.strftime("%Y%m%d%H%M%S", time.gmtime()),
        "turns": history, "thawed_from": {"snapshot_sha256": sha}})
    signed = ("signed by " + (stage / "bundle.signer").read_text().strip() + " (signature not checked here)"
              if (stage / "bundle.sig").is_file() else "unsigned")
    shutil.rmtree(stage, ignore_errors=True)
    _reset_shims()
    _reload_agents()
    return {"frozen": state.get("created"), "brainstem": (state.get("brainstem") or {}).get("version"),
            "messages_restored": len(history), "checked": checked, "signature": signed,
            "snapshot_sha256": sha, "settings_the_agents_may_need": state.get("settings_needed", []),
            "agents": sorted(_agents), "quarantined": _quarantined, "backup": backup}


def _travels(rel: Path) -> bool:
    if any(part in _SKIP_DIRS for part in rel.parts):
        return False
    name = rel.name
    return not (name.startswith(_NEVER_TRAVEL) or name.endswith((".pyc", ".tmp", ".key", ".pem")))


def op_freeze(req):
    out = Path(req.get("path") or HOME / f"pocket-{time.strftime('%Y%m%d-%H%M%S')}.snapshot.tar.gz")
    chat = _read_json(HOME / ".hatch" / "chat.json", {"turns": []})
    history = [t for t in chat.get("turns", []) if t.get("role") in ("user", "assistant")]
    files = sorted(p for p in _bs().rglob("*") if p.is_file() and _travels(p.relative_to(_bs())))
    listing = {str(Path("rapp_brainstem") / p.relative_to(_bs())): _sha_file(p) for p in files}
    version = (_bs() / "VERSION").read_text().strip() if (_bs() / "VERSION").exists() else None
    state = {"created": _now(), "session_id": chat.get("session_id"), "history": history,
             "model": req.get("model") or chat.get("model") or "pocket-brainstem",
             "brainstem": {"version": version, "host": f"pocket-brainstem {HOST_VERSION}"},
             "settings_needed": []}
    if chat.get("thawed_from"):
        state["parent"] = chat["thawed_from"]
    bundle = {"schema": "pocket-brainstem-bundle/1", "files": listing}

    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.name + ".tmp")
    with tarfile.open(tmp, "w:gz") as tar:
        for name, data in (("state.json", state), ("bundle.json", bundle)):
            raw = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
            info = tarfile.TarInfo(name)
            info.size, info.mtime, info.mode = len(raw), int(time.time()), 0o644
            tar.addfile(info, io.BytesIO(raw))
        for p in files:
            tar.add(p, arcname=str(Path("rapp_brainstem") / p.relative_to(_bs())), recursive=False)
    os.replace(tmp, out)
    return {"path": str(out), "messages": len(history), "files": len(files), "bytes": out.stat().st_size,
            "sha256": _sha_file(out), "parent": state.get("parent")}


# ── agent cards ──────────────────────────────────────────────────────────────

def _imports(source: str) -> set:
    names = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.add(node.module.split(".")[0])
    return names


def _requires(source: str) -> list:
    std = getattr(sys, "stdlib_module_names", set())
    return sorted(n for n in _imports(source) if n not in std and n not in _NOT_MODULES)


def _permissions(source: str) -> list:
    imp, perms = _imports(source), []
    if imp & {"requests", "urllib", "urllib3", "http", "socket", "httpx", "aiohttp", "ssl"}:
        perms.append("network")
    if "azure_file_storage" in source or "local_storage" in source:
        perms.append("memory")
    if imp & {"subprocess", "ctypes", "multiprocessing"}:
        perms.append("system")
    if "open(" in source or imp & {"shutil", "pathlib"}:
        perms.append("files")
    return perms


def _missing(mods) -> list:
    out = []
    for m in mods:
        try:
            if importlib.util.find_spec(m) is None:
                out.append(m)
        except (ImportError, ValueError):
            out.append(m)
    return out


def op_card_preview(req):
    """What the review screen needs before the person decides. Runs none of the card's code."""
    try:
        card = cards.parse(req["card"])
    except cards.CardError as e:
        return {"ok": False, "error": str(e)}
    probs = cards.problems(card)
    if probs:
        return {"ok": False, "error": "; ".join(probs), "problems": probs}
    try:
        detected_requires, detected_perms = _requires(card["source"]), _permissions(card["source"])
    except SyntaxError as e:
        return {"ok": False, "error": f"the source isn't valid Python: {e}"}
    dest = _agents_dir() / card["file"]
    existing = None
    if dest.exists():
        existing = "same" if _sha_file(dest) == card["sha256"] else "different"
    clash = next((n for n, p in _files.items() if n == card["name"] and p.name != card["file"]), None)
    carried = [{"path": f["path"], "sha256": f["sha256"], "bytes": len(base64.b64decode(f["b64"]))} for f in card.get("files") or []]
    return {"card": {k: v for k, v in card.items() if k not in ("source", "files")}, "source": card["source"],
            "carried_files": carried,
            "lines": card["source"].count("\n") + 1,
            "declared_permissions": card.get("permissions", []), "detected_permissions": detected_perms,
            "declared_requires": card.get("requires", []), "detected_requires": detected_requires,
            "missing_modules": _missing(sorted(set(detected_requires) | set(card.get("requires", [])))),
            "existing_file": existing, "name_clash_with_file": _files[clash].name if clash else None,
            "signature_python": cards.verify_signature(card)}


def op_card_install(req):
    """Install a card the person reviewed and approved. Loads it on its own first; nothing is
    written unless it loads cleanly and its agent's name matches the card."""
    card = cards.parse(req["card"])
    probs = cards.problems(card)
    if probs:
        return {"ok": False, "error": "; ".join(probs)}
    dest = _agents_dir() / card["file"]
    if dest.exists() and _sha_file(dest) != card["sha256"] and not req.get("replace"):
        return {"ok": False, "error": f"{card['file']} is already installed with different code", "needs_replace": True}
    trial = HOME / ".card_trial" / card["file"]
    trial.parent.mkdir(parents=True, exist_ok=True)
    trial.write_text(card["source"], encoding="utf-8")
    trial_lib = HOME / ".card_trial_lib" / Path(card["file"]).stem
    try:
        if card.get("files"):
            shutil.rmtree(trial_lib, ignore_errors=True)
            _unpack_files(card, trial_lib)
            sys.path.insert(0, str(trial_lib))
        found = _load_file(trial)
    except Exception as e:
        shutil.rmtree(trial_lib.parent, ignore_errors=True)
        return {"ok": False, "error": f"it didn't load here: {_why(e)}"}
    finally:
        shutil.rmtree(trial.parent, ignore_errors=True)
        if str(trial_lib) in sys.path:
            sys.path.remove(str(trial_lib))
        _forget_modules_under(trial_lib)
    if card["name"] not in found:
        shutil.rmtree(trial_lib.parent, ignore_errors=True)
        return {"ok": False, "error": f"the card says {card['name']!r} but the code defines {sorted(found)}"}
    lib = _lib_dir(card["file"])
    if lib.exists():
        (HOME / ".trash").mkdir(exist_ok=True)
        shutil.move(str(lib), HOME / ".trash" / f"{int(time.time())}-lib-{lib.name}")
    if card.get("files"):
        lib.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(trial_lib), lib)
    shutil.rmtree(trial_lib.parent, ignore_errors=True)
    dest.write_text(card["source"], encoding="utf-8")
    ledger_p = _agents_dir() / ".cards.json"
    ledger = _read_json(ledger_p, {})
    ledger[card["file"]] = {"name": card["name"], "version": card["version"], "author": card.get("author"),
                            "sha256": card["sha256"], "signer": card.get("signer"),
                            "files": [f["path"] for f in card.get("files") or []],
                            "signer_trusted": bool(req.get("signer_trusted")), "installed": _now()}
    _write_json(ledger_p, ledger)
    _reload_agents()
    if card["name"] not in _agents:
        return {"ok": False, "error": f"installed, but it was quarantined: {_quarantined.get(card['file'])}"}
    return {"installed": card["name"], "file": card["file"], "tool": _tool_of(_agents[card["name"]])}


def op_card_from_file(req):
    """A file the person chose (an agent.py or an .agentcard): hand back a card, ready for preview and install."""
    fname, text = str(req.get("filename") or ""), str(req.get("text") or "")
    want = str(req.get("sha256") or "").strip().lower()
    if want and hashlib.sha256(text.encode("utf-8")).hexdigest() != want:
        return {"ok": False, "error": "the file does not match the fingerprint its library lists, so it was not installed"}
    if fname.endswith(".agentcard") or text.lstrip().startswith("{"):
        return {"card": text}
    if not fname.endswith(".py"):
        return {"ok": False, "error": "choose an agent .py file or an .agentcard"}
    tmp = HOME / ".incoming"
    tmp.mkdir(parents=True, exist_ok=True)
    path = tmp / Path(fname).name
    path.write_text(text, encoding="utf-8")
    try:
        card = pack_file(path, author="you")
    except Exception as e:
        return {"ok": False, "error": f"that file isn't an agent this Brainstem can load: {_why(e)}"}
    finally:
        path.unlink(missing_ok=True)
    return {"card": cards.to_json(card)}


def op_card_pack(req):
    """Make a card from an installed agent, so the phone can trade it onward."""
    name = req["name"]
    if name not in _files:
        return {"ok": False, "error": f"no agent named {name!r}"}
    return {"card": pack_file(_files[name], author=req.get("author"), version=req.get("version"),
                              loaded=_agents[name])}


def pack_file(path: Path, author=None, version=None, loaded=None, name=None) -> dict:
    """A card for one agent file. Loads the agent (it's your own code) to read its metadata."""
    path = Path(path)
    source = path.read_text(encoding="utf-8")
    if loaded is None:
        found = _load_file(path)
        if name:
            loaded = found[name]
        elif len(found) == 1:
            loaded = next(iter(found.values()))
        else:
            raise ValueError(f"{path.name} defines {sorted(found)}; pick one with name=")
    md = loaded.metadata
    return {"schema": cards.SCHEMA, "name": loaded.name, "file": path.name,
            "version": version or str(md.get("version") or getattr(loaded, "version", None) or "1.0.0"),
            "author": author or "", "description": md.get("description", ""),
            "parameters": md.get("parameters", {"type": "object", "properties": {}}),
            "requires": _requires(source), "permissions": _permissions(source),
            "source": source, "sha256": cards.source_sha256(source)}


def op_card_remove(req):
    name = req["name"]
    if name not in _files:
        return {"ok": False, "error": f"no agent named {name!r}"}
    path = _files[name]
    trash = HOME / ".trash"
    trash.mkdir(exist_ok=True)
    shutil.move(str(path), trash / f"{int(time.time())}-{path.name}")
    lib = _lib_dir(path.name)
    if lib.exists():
        if str(lib) in sys.path:
            sys.path.remove(str(lib))
        _forget_modules_under(lib)
        shutil.move(str(lib), trash / f"{int(time.time())}-lib-{lib.name}")
    ledger_p = _agents_dir() / ".cards.json"
    ledger = _read_json(ledger_p, {})
    ledger.pop(path.name, None)
    _write_json(ledger_p, ledger)
    _reload_agents()
    return {"removed": name, "moved_to": str(trash)}


def op_reload(req):
    _reset_shims()
    _reload_agents()
    return op_status(req)


_OPS = {"card_from_file": op_card_from_file, "init": op_init, "status": op_status, "tools": op_tools, "system_context": op_system_context,
        "run": op_run, "thaw": op_thaw, "freeze": op_freeze, "card_preview": op_card_preview,
        "card_install": op_card_install, "card_pack": op_card_pack, "card_remove": op_card_remove,
        "reload": op_reload}


def handle(request_json: str) -> str:
    """The one door Swift uses. Never raises: errors come back as {"ok": false, "error": ...}."""
    try:
        req = json.loads(request_json)
        op = _OPS.get(req.get("op"))
        if op is None:
            resp = {"ok": False, "error": f"unknown op {req.get('op')!r}"}
        elif HOME is None and req.get("op") != "init":
            resp = {"ok": False, "error": "call init first"}
        else:
            resp = op(req)
            resp.setdefault("ok", True)
    except Exception as e:
        resp = {"ok": False, "error": _why(e), "traceback": traceback.format_exc(limit=4)}
    return json.dumps(resp, ensure_ascii=False, default=str)
