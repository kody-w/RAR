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
    "version": "1.1.0",
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
# Spend Guard (folded in from the Spend Guard pack idea): Copilot is flat-rate, but premium models draw on a monthly
# allowance. The kernel does not expose that allowance, so this counts premium-model replies in the journal on this
# computer (an estimate) against a monthly limit the owner sets. Local models and the included models never count.
BUDGET = os.path.join(HOME, "spend-guard.json")
JOURNAL = os.path.join(os.environ.get("JOURNAL_STORE") or os.path.expanduser("~/.brainstem/journal"), "frames.jsonl")
INCLUDED = ("gpt-4.1", "gpt-4o", "gpt-4o-mini", "gpt-5-mini")
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


def premium_used(month=None):
    month = month or time.strftime("%Y-%m")
    n = 0
    try:
        with open(JOURNAL) as f:
            for line in f:
                try:
                    fr = json.loads(line)
                except Exception:
                    continue
                m = fr.get("model") or ""
                if str(fr.get("at", "")).startswith(month) and m and not m.startswith("ollama/") and m not in INCLUDED:
                    n += 1
    except OSError:
        return None
    return n


def checks():
    found = []
    limit = (_json(BUDGET) or {}).get("monthly")
    if limit:
        used = premium_used()
        if used is not None and used >= limit:
            found.append(("spend:over", f"you have used about {used} premium replies this month, past your limit of {limit} (only a warning: nothing is blocked)"))
        elif used is not None and used >= 0.8 * limit:
            found.append(("spend:near", f"you have used about {used} of your {limit} premium replies this month (only a warning: nothing is blocked)"))
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
                            "drills, and premium-model use against a monthly limit (Spend Guard). Use for 'check my computer', "
                            "'is everything ok', 'fix it', 'how much have I used', 'warn me past N premium replies'."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["check", "fix", "set_spend_limit", "spend"]},
                "limit": {"type": "integer", "description": "for set_spend_limit: premium replies allowed per month (0 turns it off)"}},
                "required": ["action"]},
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

    def perform(self, action="check", limit=None, **_):
        if action == "set_spend_limit":
            try:
                n = max(0, int(limit or 0))
            except (TypeError, ValueError):
                return "Tell me a whole number of premium replies per month, or 0 to turn the limit off."
            os.makedirs(HOME, exist_ok=True)
            with open(BUDGET, "w") as f:
                json.dump({"monthly": n}, f)
            return (f"Done. I will tell you once at {int(n * 0.8)} and again at {n} premium replies this month."
                    if n else "The spend limit is off.")
        if action == "spend":
            used, n = premium_used(), (_json(BUDGET) or {}).get("monthly")
            if used is None:
                return "I cannot count yet: the journal on this computer has no record of your chats."
            return (f"About {used} premium replies so far this month" + (f", of your limit of {n}." if n else ". No limit is set.") +
                    " This is an estimate from this computer's journal; local models and included models are not counted, and nothing is ever blocked.")
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
        du = shutil.disk_usage(os.path.expanduser("~"))
        keys = {k.split(":")[0] for k, _ in found}
        ok = [x for k, x in (("disk", f"{du.free / 1e9:.0f} GB free"), ("fallback", "the Brainstem started normally"),
                             ("service", "its services answer"), ("drill", "last night's drills passed")) if k not in keys]
        if not found:
            return "All good: " + ", ".join(ok) + "."
        return "Needs attention: " + "; ".join(s for _, s in found) + ". Everything else is fine: " + ", ".join(ok) + "."
