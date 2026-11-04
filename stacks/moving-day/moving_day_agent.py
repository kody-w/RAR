"""Moving Day: your new computer becomes your old one.

"Pack my Brainstem for moving" writes one move file on this computer. It is a rapp/1 organism egg, laid and verified by
brainfreeze (older .snapshot.tar.gz move files still unpack, as an alias): agents, soul, memory, the picked model, plus the list of packs and private
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
    "version": "1.2.0",
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


SLUG = "my-brainstem"
# Standby (Cover For Me, folded in): a fresh egg every night in a folder your other Mac also sees (iCloud Drive).
STANDBY = os.environ.get("MOVING_DAY_STANDBY_DIR") or os.path.expanduser(
    "~/Library/Mobile Documents/com~apple~CloudDocs/Brainstem Standby")
LABEL = "com.brainstem.moving-day.standby"
AGENTS_DIR = os.environ.get("MOVING_DAY_LAUNCH_AGENTS") or os.path.expanduser("~/Library/LaunchAgents")
SIDE = os.path.join(".brainstem_data", "moving-day.json")  # packs + private topics ride inside the egg as memory


def _owner():
    import re
    o = re.sub(r"[^a-z0-9-]", "", (os.environ.get("USER") or "owner").lower()).strip("-")
    return o or "owner"


def pack_up(root=None, keep_newest=None):
    bf = _brainfreeze()
    md = {"packs": (_json(os.path.join(LAYERS, "packs.json"), {}) or {}).get("packs", []),
          "private_topics": _json(os.path.join(LAYERS, "private-topics.json")),
          "from": os.uname().nodename, "packed": time.strftime("%Y-%m-%d %H:%M")}
    os.makedirs(os.path.join(KERNEL_DIR, ".brainstem_data"), exist_ok=True)
    with open(os.path.join(KERNEL_DIR, SIDE), "w") as f:
        json.dump(md, f, indent=1)
    rid = (_json(os.path.join(KERNEL_DIR, "rappid.json"), {}) or {}).get("rappid")
    out_dir = os.path.join(root or MOVES, time.strftime("%Y%m%d-%H%M%S"))
    laid = bf.lay_egg(KERNEL_DIR, out_dir, owner=None if rid else _owner(), slug=None if rid else SLUG, rappid=rid)
    egg = str(laid["organism"])
    if keep_newest:  # standby keeps only the newest few; older ones are moved to moving-day/old-standby, never deleted
        runs = sorted(d for d in os.listdir(root) if d[:8].isdigit())
        for d in runs[:-keep_newest]:
            os.makedirs(os.path.join(MOVES, "old-standby"), exist_ok=True)
            shutil.move(os.path.join(root, d), os.path.join(MOVES, "old-standby", d))
    size = os.path.getsize(egg) / 1e6
    return (f"Packed. Your move file is {egg} ({size:.1f} MB, {laid['files']} files, a verified rapp/1 egg). It holds your "
            f"agents, soul, memory and model{', and these packs: ' + ', '.join(md['packs']) if md['packs'] else ''}. "
            "Sign-in and secrets are not in it. Carry it to the new computer (AirDrop or a drive), install the Brainstem "
            "there, then say: unpack my move file.")


def _candidates():
    found = []
    for d in (MOVES, STANDBY, os.path.expanduser("~/Downloads"), os.path.expanduser("~/Desktop")):
        if not os.path.isdir(d):
            continue
        for root, _, names in os.walk(d) if d in (MOVES, STANDBY) else [(d, None, os.listdir(d))]:
            found += [os.path.join(root, f) for f in names
                      if f.endswith("--" + SLUG + ".egg") or (f.startswith("brainstem-move-") and f.endswith(".snapshot.tar.gz"))]
    return found


def _latest():
    found = _candidates()
    return max(found, key=os.path.getmtime) if found else None


def _read_move(path):
    """-> {relative path: bytes} for the RESTORE set, or a refusal sentence. Eggs are verified (rapp/1 §9.3);
    an older brainfreeze snapshot (.snapshot.tar.gz) is read as an alias of the egg."""
    keep = lambda rel: rel.split("/")[0] in RESTORE
    if path.endswith(".egg"):
        bf = _brainfreeze()
        blob = open(path, "rb").read()
        ok, step, why = bf.rapp1.verify_egg(blob)
        if not ok:
            return f"{os.path.basename(path)} did not pass the egg check ({step}: {why}); nothing was changed."
        manifest, files = bf.rapp1.read_egg(blob)
        if manifest.get("variant") != "organism":
            return f"{os.path.basename(path)} is a {manifest.get('variant')} egg, not a Brainstem; nothing was changed."
        return {k: v for k, v in files.items() if keep(k)}
    out = {}
    with tarfile.open(path, "r:gz") as tar:
        state = json.load(tar.extractfile("state.json"))
        if state.get("kind") != "brainstem-snapshot":
            return f"{os.path.basename(path)} is not a Brainstem move file; nothing was changed."
        for m in tar.getmembers():
            if not m.name.startswith("rapp_brainstem/") or not m.isfile():
                continue
            out[m.name[len("rapp_brainstem/"):]] = tar.extractfile(m).read()
    md = state.get("moving_day")
    if md:
        out[SIDE] = json.dumps(md).encode()
    return {k: v for k, v in out.items() if keep(k)}


def unpack(path=None):
    path = os.path.expanduser(path) if path else _latest()
    if not path or not os.path.isfile(path):
        return "I could not find a move file. Put it in Downloads or Desktop, or tell me where it is."
    files = _read_move(path)
    if isinstance(files, str):
        return files
    for rel in files:  # refuse anything that would land outside the Brainstem folder
        n = os.path.normpath(rel)
        if n.startswith("..") or os.path.isabs(n):
            return f"{os.path.basename(path)} has an unsafe entry; nothing was changed."
    keep = os.path.join(MOVES, "before-" + time.strftime("%Y%m%d-%H%M%S"))
    os.makedirs(keep, exist_ok=True)
    for top in RESTORE:  # a copy of what is replaced, so the move can be undone by hand
        src = os.path.join(KERNEL_DIR, top)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(keep, top), dirs_exist_ok=True)
        elif os.path.isfile(src):
            shutil.copy2(src, os.path.join(keep, top))
    for rel, b in files.items():
        dest = os.path.join(KERNEL_DIR, os.path.normpath(rel))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(b)
    md = json.loads(files.get(SIDE, b"{}") or b"{}")
    if md.get("private_topics"):
        os.makedirs(LAYERS, exist_ok=True)
        with open(os.path.join(LAYERS, "private-topics.json"), "w") as f:
            json.dump(md["private_topics"], f, indent=1)
    packs = [p for p in md.get("packs", []) if p.replace("-", "").isalnum()]
    note = ""
    sup = os.path.join(LAYERS, "packs.py")
    if packs and os.path.isfile(sup) and not os.environ.get("MOVING_DAY_NO_PACKS"):
        extra = ["--no-restart"] if os.environ.get("MOVING_DAY_NO_RESTART") else []
        log = open(os.path.join(MOVES, "unpack-packs.log"), "a")  # after this reply: same packs, then a restart
        subprocess.Popen([sys.executable, "-c", "import time,subprocess,sys;time.sleep(3);sys.exit(subprocess.call(sys.argv[1:]))",
                          sys.executable, sup, "--kernel", os.path.join(KERNEL_DIR, "brainstem.py"), "--python", sys.executable,
                          "--port", os.environ.get("PORT", "7071"), *extra, *packs],
                         stdout=log, stderr=log, start_new_session=True)
        note = f" I am adding your packs ({', '.join(packs)}) now; your Brainstem restarts by itself in about a minute."
    elif packs:
        note = (f" Your packs were {', '.join(packs)}. Add them back with: "
                f"curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- {' '.join(packs)}")
    return (f"Unpacked {len(files)} files from {os.path.basename(path)} (moved from {md.get('from', 'your old computer')}). "
            f"What was here before is kept in {keep}.{note}")


def standby(on):
    plist = os.path.join(AGENTS_DIR, LABEL + ".plist")
    if not on:
        if os.path.isfile(plist):
            subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}", plist], capture_output=True)
            os.makedirs(MOVES, exist_ok=True)
            shutil.move(plist, os.path.join(MOVES, LABEL + ".plist.off"))
        return "Standby is off. Nothing already saved was removed."
    os.makedirs(STANDBY, exist_ok=True)
    code = (f"import sys,os;sys.path.insert(0,{KERNEL_DIR!r});os.chdir({KERNEL_DIR!r});"
            f"from agents.moving_day_agent import pack_up;print(pack_up({STANDBY!r},3))")
    import plistlib
    os.makedirs(AGENTS_DIR, exist_ok=True)
    with open(plist, "wb") as f:
        plistlib.dump({"Label": LABEL, "ProgramArguments": [sys.executable, "-c", code],
                       "StartCalendarInterval": {"Hour": 3, "Minute": 30},
                       "StandardOutPath": os.path.join(MOVES, "standby.log"), "StandardErrorPath": os.path.join(MOVES, "standby.log"),
                       "EnvironmentVariables": {k: os.environ[k] for k in ("GRAIL_LAYERS_HOME", "MOVING_DAY_DIR", "MOVING_DAY_STANDBY_DIR") if k in os.environ}}, f)
    if not os.environ.get("MOVING_DAY_NO_LAUNCHD"):
        subprocess.run(["launchctl", "bootstrap", f"gui/{os.getuid()}", plist], capture_output=True)
    first = pack_up(STANDBY, 3)
    return ("Standby is on. Every night at 3:30 I lay a fresh copy in iCloud Drive (Brainstem Standby), keeping the newest "
            "three. If this Mac is ever lost or broken, install the Brainstem on another Mac signed in to the same iCloud "
            "and say: take over. " + first.split(". ")[0] + ".")


class MovingDayAgent(BasicAgent):
    def __init__(self):
        self.name = "MovingDay"
        self.metadata = {
            "name": self.name,
            "description": ("Moves this Brainstem to a new computer. action=pack writes one move file (agents, soul, memory, "
                            "model, packs; never sign-in or secrets). action=unpack, on the new computer, restores it and "
                            "re-adds the same packs. action=list shows move files here. standby_on keeps a fresh copy every night in "
                            "iCloud Drive so another Mac can cover; take_over, on the other Mac, unpacks the newest one."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["pack", "unpack", "list", "standby_on", "standby_off", "take_over"]},
                "path": {"type": "string", "description": "the move file to unpack (default: newest in moving-day, Downloads or Desktop)"},
            }, "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            a = kwargs.get("action")
            if a == "pack":
                return pack_up()
            if a in ("unpack", "take_over"):
                return unpack(kwargs.get("path"))
            if a in ("standby_on", "standby_off"):
                return standby(a == "standby_on")
            found = sorted(_candidates(), key=os.path.getmtime)
            return "Move files here: " + (", ".join(found) if found else "none yet. Say: pack my Brainstem for moving.")
        except Exception as e:
            return f"Moving Day could not finish ({e}). Nothing on this computer was removed."
