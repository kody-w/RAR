# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/replay_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/replay_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/replay_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Replay: make a shared chat file run here. A room or chat file carries pointers (catalog guid + fingerprint per agent
file) instead of copies of agents. Dropped into any Brainstem's agents/ folder, this one file fetches each pointed version
from the catalog, checks its fingerprint, and hot loads it; 'unload' removes exactly what it loaded. The kernel is untouched.
Lessons paid by others: npm/PyPI lockfiles (install by exact hash, never 'latest'); Docker pulls by digest; and the xz
backdoor (2024): never run a fetched file whose fingerprint was not checked first.
Catalogs, tried in order: REPLAY_CATALOG (this device's, a folder or https base; layout <guid>/<first 8 of sha256>.py), then the
public RAR version store (REPLAY_PUBLIC; layout versions/@publisher/<slug>/<first 12 of sha256>.py)."""
import hashlib, json, os, urllib.request
try:
    from agents.basic_agent import BasicAgent
except Exception:  # standalone use and tests
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/replay_agent",
    "version": "0.1.0",
    "display_name": "Replay",
    "description": "Make a shared chat file run on this Brainstem: loads the exact agent versions the file points to, checked by fingerprint, and unloads them again.",
    "author": "kody-w",
    "tags": ["replay", "chat-file", "pointer", "hotload", "share"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": "Use Replay to load the chat file ~/Downloads/room.json",
}
HERE = os.path.dirname(os.path.abspath(__file__)); LEDGER = os.path.join(HERE, ".replay.json")
CATALOG = os.environ.get("REPLAY_CATALOG", os.path.expanduser("~/.openrappter/rar/by-guid"))


PUBLIC = os.environ.get("REPLAY_PUBLIC", "https://raw.githubusercontent.com/kody-w/RAR/main")   # RAR's append-only version store


def _get(where):
    web = where.startswith("https://") or where.startswith("http://127.0.0.1")   # plain http only for a test server on this Mac
    return urllib.request.urlopen(where, timeout=30).read() if web else open(where, "rb").read()


def _fetch(ref):
    """The bytes a pointer names. Tried in order: this device's catalog (by guid), then the public RAR version store (by
    publisher/slug). Where the bytes come from is not trusted; only the fingerprint is (content addressing, as in Git)."""
    guid, sha, stem = ref.get("guid", ""), ref["sha256"], os.path.basename(ref["file"])[:-3]
    if not (sha.isalnum() and len(sha) == 64 and guid.replace("-", "").isalnum() and stem.replace("_", "").isalnum()):
        raise ValueError("bad pointer")
    tries = [f"{CATALOG.rstrip('/')}/{guid}/{sha[:8]}.py"]
    pub = ref.get("rar", "@kody-w/" + stem)   # "@publisher/slug"; the slug defaults to the file's own name
    if pub.startswith("@") and pub.replace("@", "").replace("/", "").replace("_", "").replace("-", "").isalnum():
        tries.append(f"{PUBLIC}/versions/{pub.split('/')[0]}/{stem}/{sha[:12]}.py")
    for where in tries:
        try: data = _get(where)
        except Exception: continue
        if hashlib.sha256(data).hexdigest() == sha: return data, where
        raise ValueError("fingerprint does not match the pointer")
    raise ValueError("this version is in neither this device's catalog nor the public one")


class ReplayAgent(BasicAgent):
    def __init__(self):
        self.name = "Replay"
        self.metadata = {"name": self.name,
            "description": "Make a shared chat file run on this Brainstem: 'load' fetches the exact agent versions the file points to "
                           "(checked by fingerprint) so they are usable from the next message; 'unload' removes them again; 'status' lists them.",
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "enum": ["load", "unload", "status"]},
                "file": {"type": "string", "description": "For load: full path of the chat or room file."}},
                "required": ["action"]}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, action="status", file="", **kw):
        led = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}
        if action == "status":
            return json.dumps({"loaded_by_replay": sorted(led)})
        if action == "unload":
            gone = []
            for f, sha in list(led.items()):
                p = os.path.join(HERE, f)
                if os.path.exists(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() == sha:
                    os.remove(p); gone.append(f)
                led.pop(f)   # a file the owner changed since is theirs now: left in place
            json.dump(led, open(LEDGER, "w"))
            return json.dumps({"unloaded": gone})
        try:
            d = json.load(open(os.path.expanduser(file)))
        except Exception as e:
            return json.dumps({"loaded": [], "why": f"could not read the chat file: {e}"})
        refs = {}
        for t in d.get("turns", []):
            for r in t.get("pointer") or []:
                refs[r["file"]] = r
        if not refs:
            return json.dumps({"loaded": [], "why": "this chat file carries no pointers (saved before pointers existed)"})
        loaded, kept, refused = [], [], []
        for f, r in sorted(refs.items()):
            p = os.path.join(HERE, os.path.basename(f))
            try:
                data, came = _fetch(r)
            except Exception as e:
                refused.append(f"{f}: {e}"); continue
            if os.path.exists(p) and f not in led:
                same = hashlib.sha256(open(p, "rb").read()).hexdigest() == r["sha256"]
                kept.append(f + (" (already the same version)" if same else " (yours differs; kept yours)")); continue
            open(p, "wb").write(data); led[f] = r["sha256"]; loaded.append(f"{f}@{r['sha256'][:8]}" + (" (public catalog)" if came.startswith("https://") else ""))
        json.dump(led, open(LEDGER, "w"))
        return json.dumps({"loaded": loaded, "kept_owner_files": kept, "refused": refused,
                           "note": "loaded agents are usable from the next message; say 'unload' to remove them"})


if __name__ == "__main__":
    print(ReplayAgent().perform(action="status"))
