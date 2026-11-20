---
name: "rar-kody-w-replay"
description: "Make a shared chat file run on this Brainstem: 'load' fetches the exact agent versions the file points to (checked by fingerprint) so they are usable from the next message; 'unload' removes them again; 'status' lists them."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/replay_agent", "rar_sha256": "337b4b6d960fbe4a96a89547311f090d1b621befec25974c588779075654d974", "source_kind": "rar-agent", "source_commit": "58a7c49b68d8b93db5f30657f0a6a5afdcc087c3", "version": "0.1.0", "author": "kody-w", "tags": ["replay", "chat-file", "pointer", "hotload", "share"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/replay_agent`. The original RAPP
agent is preserved byte-for-byte in `replay_agent.py` and in the RCI capsule.

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

Replay: make a shared chat file run here. A room or chat file carries pointers (catalog guid + fingerprint per agent
file) instead of copies of agents. Dropped into any Brainstem's agents/ folder, this one file fetches each pointed version
from the catalog, checks its fingerprint, and hot loads it; 'unload' removes exactly what it loaded. The kernel is untouched.
Lessons paid by others: npm/PyPI lockfiles (install by exact hash, never 'latest'); Docker pulls by digest; and the xz
backdoor (2024): never run a fetched file whose fingerprint was not checked first.
Catalogs, tried in order: REPLAY_CATALOG (this device's, a folder or https base; layout <guid>/<first 8 of sha256>.py), then the
public RAR version store (REPLAY_PUBLIC; layout versions/@publisher/<slug>/<first 12 of sha256>.py).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "load",
        "unload",
        "status"
      ],
      "type": "string"
    },
    "file": {
      "description": "For load: full path of the chat or room file.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `replay_agent.py` and embedded as the fenced Python below (sha256 337b4b6d960fbe4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `replay_agent.py` first:

```bash
python3 replay_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 replay_agent.py   # or on stdin
python3 replay_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
