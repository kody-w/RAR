"""Moving Day: your new computer becomes your old one.

"Pack my Brainstem for moving" writes one move file on this computer. It is a brainfreeze snapshot (the same
format brainfreeze thaws anywhere): agents, soul, memory, the picked model, plus the list of packs and private
topics. Sign-in, secrets, .env values, logs and caches are never inside.
On the new computer, after the one-line install, "unpack my move file" puts those things into the Brainstem that
is already there (the engine on the new computer stays its own, unchanged), keeps a copy of anything it replaces,
and re-adds the same packs by fingerprint. Nothing is uploaded anywhere: you carry the file (AirDrop, a drive).
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import time
import urllib.request

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/moving_day_agent",
    "version": "1.0.0",
    "display_name": "Moving Day",
    "description": "Moves your Brainstem to a new computer: one file with your agents, soul, memory, model and packs (never sign-in or secrets), unpacked on the new computer in one sentence.",
    "author": "kody-w",
    "tags": ["moving", "backup", "estate", "new-computer"],
    "category": "operations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

BASE = os.path.expanduser("~/.brainstem")
LAYERS = os.environ.get("GRAIL_LAYERS_HOME") or os.path.join(BASE, "layers")
MOVES = os.environ.get("MOVING_DAY_DIR") or os.path.join(BASE, "moving-day")
KERNEL_DIR = os.environ.get("MOVING_DAY_KERNEL_DIR") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# brainfreeze, pinned by commit and by the sha256 of every file (public: github.com/kody-w/rapp-brainfreeze)
BF_COMMIT = "3ed8ee710f50a7eb5294562c991003ec0d8d072f"
BF_FILES = {
    "__init__.py": "6fd2b66feb9b3aa79623cba69d1b9c714b0e784b85bcdcef1a0eb4c5d8539c6e",
    "bundle.py": "e8ae56d98aa41de34bf4b81601ca8215d5e5718b51a47d38081c8f3188d26497",
    "lineage.py": "fd68924e9ce2336aafc9191569a180ef9c73a187b594a08c95ea83d4dedaa853",
    "legacy.py": "6ecb4a84a3c01c6e6d78b2d696bbc6fa2bbac486c1eb4885d7520a0c5bb7907a",
    "rapp1.py": "1a04362b02f14c1e37b70c6b4f72d79e92df1cc9c2b5b394e8e1b141fc0b6050",
    "rapp1.vendor.json": "256cae1a6929b9a6dc19a24f0ef929d712f2efecbe7f0131c829318ec92f67f3",
}
RESTORE = ("agents", "soul.md", ".brainstem_data", ".brainstem_model")  # never brainstem.py: the engine stays


def _brainfreeze():
    lib = os.path.join(BASE, "lib", "bf-" + BF_COMMIT[:12])
    pkg = os.path.join(lib, "brainfreeze")
    if not all(os.path.isfile(os.path.join(pkg, f)) for f in BF_FILES):
        os.makedirs(pkg, exist_ok=True)
        for f, sha in BF_FILES.items():
            url = f"https://raw.githubusercontent.com/kody-w/rapp-brainfreeze/{BF_COMMIT}/brainfreeze/{f}"
            b = urllib.request.urlopen(url, timeout=30).read()
            if hashlib.sha256(b).hexdigest() != sha:
                raise RuntimeError(f"brainfreeze {f} did not match its fingerprint; nothing was changed")
            with open(os.path.join(pkg, f), "wb") as out:
                out.write(b)
    if lib not in sys.path:
        sys.path.insert(0, lib)
    import brainfreeze
    return brainfreeze


def _json(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return default


def pack_up():
    bf = _brainfreeze()
    os.makedirs(MOVES, exist_ok=True)
    out = os.path.join(MOVES, time.strftime("brainstem-move-%Y%m%d-%H%M%S.snapshot.tar.gz"))
    md = {"packs": (_json(os.path.join(LAYERS, "packs.json"), {}) or {}).get("packs", []),
          "private_topics": _json(os.path.join(LAYERS, "private-topics.json")),
          "from": os.uname().nodename}
    bf.freeze(KERNEL_DIR, out, extra={"moving_day": md})
    size = os.path.getsize(out) / 1e6
    return (f"Packed. Your move file is {out} ({size:.1f} MB). It holds your agents, soul, memory and model"
            f"{', and these packs: ' + ', '.join(md['packs']) if md['packs'] else ''}. Sign-in and secrets are not in it. "
            "Carry it to the new computer (AirDrop or a drive), install the Brainstem there, then say: unpack my move file.")


def _latest():
    found = []
    for d in (MOVES, os.path.expanduser("~/Downloads"), os.path.expanduser("~/Desktop")):
        if os.path.isdir(d):
            found += [os.path.join(d, f) for f in os.listdir(d) if f.startswith("brainstem-move-") and f.endswith(".snapshot.tar.gz")]
    return max(found, key=os.path.getmtime) if found else None


def unpack(path=None):
    path = os.path.expanduser(path) if path else _latest()
    if not path or not os.path.isfile(path):
        return "I could not find a move file. Put it in Downloads or Desktop, or tell me where it is."
    with tarfile.open(path, "r:gz") as tar:
        state = json.load(tar.extractfile("state.json"))
        if state.get("kind") != "brainstem-snapshot":
            return f"{os.path.basename(path)} is not a Brainstem move file; nothing was changed."
        members = [m for m in tar.getmembers() if m.name.startswith("rapp_brainstem/")]
        for m in members:  # refuse anything that would land outside the Brainstem folder
            rel = os.path.normpath(m.name[len("rapp_brainstem/"):])
            if rel.startswith("..") or os.path.isabs(rel) or m.issym() or m.islnk():
                return f"{os.path.basename(path)} has an unsafe entry; nothing was changed."
        chosen = [m for m in members if m.name[len("rapp_brainstem/"):].split("/")[0] in RESTORE and (m.isfile() or m.isdir())]
        md = state.get("moving_day") or {}
        keep = os.path.join(MOVES, "before-" + time.strftime("%Y%m%d-%H%M%S"))
        os.makedirs(keep, exist_ok=True)
        for top in RESTORE:  # a copy of what is replaced, so the move can be undone by hand
            src = os.path.join(KERNEL_DIR, top)
            if os.path.isdir(src):
                shutil.copytree(src, os.path.join(keep, top), dirs_exist_ok=True)
            elif os.path.isfile(src):
                shutil.copy2(src, os.path.join(keep, top))
        n = 0
        for m in chosen:
            dest = os.path.join(KERNEL_DIR, os.path.normpath(m.name[len("rapp_brainstem/"):]))
            if m.isdir():
                os.makedirs(dest, exist_ok=True); continue
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with tar.extractfile(m) as fsrc, open(dest, "wb") as fdst:
                shutil.copyfileobj(fsrc, fdst)
            n += 1
    if md.get("private_topics"):
        os.makedirs(LAYERS, exist_ok=True)
        with open(os.path.join(LAYERS, "private-topics.json"), "w") as f:
            json.dump(md["private_topics"], f, indent=1)
    packs = [p for p in md.get("packs", []) if p.replace("-", "").isalnum()]
    note = ""
    sup = os.path.join(LAYERS, "packs.py")
    if packs and os.path.isfile(sup) and not os.environ.get("MOVING_DAY_NO_PACKS"):
        log = open(os.path.join(MOVES, "unpack-packs.log"), "a")  # after this reply: same packs, then a restart
        subprocess.Popen([sys.executable, "-c", "import time,subprocess,sys;time.sleep(3);sys.exit(subprocess.call(sys.argv[1:]))",
                          sys.executable, sup, "--kernel", os.path.join(KERNEL_DIR, "brainstem.py"), "--python", sys.executable, *packs],
                         stdout=log, stderr=log, start_new_session=True)
        note = f" I am adding your packs ({', '.join(packs)}) now; your Brainstem restarts by itself in about a minute."
    elif packs:
        note = (f" Your packs were {', '.join(packs)}. Add them back with: "
                f"curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- {' '.join(packs)}")
    return (f"Unpacked {n} files from {os.path.basename(path)} (moved from {md.get('from', 'your old computer')}). "
            f"What was here before is kept in {keep}.{note}")


class MovingDayAgent(BasicAgent):
    def __init__(self):
        self.name = "MovingDay"
        self.metadata = {
            "name": self.name,
            "description": ("Moves this Brainstem to a new computer. action=pack writes one move file (agents, soul, memory, "
                            "model, packs; never sign-in or secrets). action=unpack, on the new computer, restores it and "
                            "re-adds the same packs. action=list shows move files here."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["pack", "unpack", "list"]},
                "path": {"type": "string", "description": "the move file to unpack (default: newest in moving-day, Downloads or Desktop)"},
            }, "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            a = kwargs.get("action")
            if a == "pack":
                return pack_up()
            if a == "unpack":
                return unpack(kwargs.get("path"))
            found = sorted(f for f in os.listdir(MOVES) if f.endswith(".snapshot.tar.gz")) if os.path.isdir(MOVES) else []
            return "Move files here: " + (", ".join(found) if found else "none yet. Say: pack my Brainstem for moving.")
        except Exception as e:
            return f"Moving Day could not finish ({e}). Nothing on this computer was removed."
