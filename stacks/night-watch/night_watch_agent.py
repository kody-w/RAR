"""Night Watch: your Brainstem looks after the computer it lives on, and tells you only when something needs you.

Each chat turn it runs a few cheap checks (at most every 10 minutes): free disk space, whether the Brainstem had to
fall back to plain grail, whether its own services answer, last night's drills. A new problem is told once, in one
sentence; nothing is said while all is well. "check my computer" lists everything; "fix it" does only safe fixes
(restarting the Brainstem's own helper services), never deletes anything.
"""
import json
import os
import shutil
import subprocess
import time
import urllib.request

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/night_watch_agent",
    "version": "1.0.0",
    "display_name": "Night Watch",
    "description": "Your Brainstem looks after its own computer: disk space, its own services and drills; tells you once, in one sentence, only when something needs you.",
    "author": "kody-w",
    "tags": ["health", "maintenance", "self-care", "estate"],
    "category": "operations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

HOME = os.environ.get("GRAIL_LAYERS_HOME") or os.path.expanduser("~/.brainstem/layers")
STATE = os.path.join(HOME, "night-watch.json")
EVERY = 600
SERVICES = {  # helper services the Brainstem may run beside it: url, launchd label
    "journal": ("http://127.0.0.1:7074/health", "com.airaptr.brainstem-journal"),
}


def _json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def _up(url):
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return r.status == 200
    except Exception:
        return False


def _plist(label):
    return os.path.exists(os.path.expanduser(f"~/Library/LaunchAgents/{label}.plist"))


def checks():
    found = []
    du = shutil.disk_usage(os.path.expanduser("~"))
    free = du.free / du.total
    if free < 0.10:
        found.append(("disk", f"your disk is {100 - free * 100:.0f}% full ({du.free / 1e9:.0f} GB left)"))
    boot = _json(os.path.join(HOME, "last-boot.json")) or {}
    if boot.get("fallback"):
        found.append(("fallback", f"the Brainstem started as plain grail because {boot.get('why', 'a layer failed')}"))
    for name, (url, label) in SERVICES.items():
        if _plist(label) and not _up(url):
            found.append((f"service:{name}", f"the {name} service is not answering"))
    for drill in ("chaos", "succession"):
        r = _json(os.path.join(HOME, drill, "latest.json"))
        if r and r.get("survived") is not None and r.get("survived") != r.get("total"):
            found.append((f"drill:{drill}", f"last night's {drill} drill passed {r.get('survived')} of {r.get('total')}"))
    return found


class NightWatchAgent(BasicAgent):
    def __init__(self):
        self.name = "NightWatch"
        self.metadata = {
            "name": self.name,
            "description": ("Looks after this computer for the owner: disk space, the Brainstem's own services and "
                            "drills. Use for 'check my computer', 'is everything ok', 'fix it'."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["check", "fix"]}}, "required": ["action"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _state(self):
        return _json(STATE) or {"told": [], "at": 0, "found": []}

    def _save(self, st):
        os.makedirs(HOME, exist_ok=True)
        with open(STATE + ".tmp", "w") as f:
            json.dump(st, f)
        os.replace(STATE + ".tmp", STATE)

    def system_context(self):
        try:
            st = self._state()
            if time.time() - st.get("at", 0) > EVERY:
                st["found"], st["at"] = checks(), time.time()
            keys = [k for k, _ in st["found"]]
            st["told"] = [k for k in st.get("told", []) if k in keys]  # a fixed problem may be told again if it returns
            new = [(k, s) for k, s in st["found"] if k not in st["told"]]
            st["told"] += [k for k, _ in new]
            self._save(st)
            if not new:
                return None
            return ("<night_watch>Before answering, tell the owner in ONE plain sentence, once: " +
                    "; ".join(s for _, s in new) + ". Offer to fix it if NightWatch can (services only).</night_watch>")
        except Exception:
            return None

    def perform(self, action="check", **_):
        found = checks()
        st = self._state(); st["found"], st["at"] = found, time.time(); self._save(st)
        if action == "fix":
            done = []
            for name, (url, label) in SERVICES.items():
                if _plist(label) and not _up(url):
                    subprocess.run(["launchctl", "kickstart", "-k", f"gui/{os.getuid()}/{label}"], capture_output=True)
                    time.sleep(2)
                    done.append(f"restarted the {name} service ({'answering now' if _up(url) else 'still not answering'})")
            rest = [s for k, s in found if not k.startswith("service:")]
            return ("; ".join(done) or "Nothing I can fix safely.") + (" Still needs you: " + "; ".join(rest) if rest else "")
        if not found:
            du = shutil.disk_usage(os.path.expanduser("~"))
            return f"All good: {du.free / 1e9:.0f} GB free, the Brainstem started normally, its services answer."
        return "Needs attention: " + "; ".join(s for _, s in found) + "."
