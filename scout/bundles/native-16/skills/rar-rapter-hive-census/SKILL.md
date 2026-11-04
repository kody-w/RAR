---
name: "rar-rapter-hive-census"
description: "Emit this box's census as deterministic static JSON \u2014 protocol revision, anchor hash, resident populations, posture, trust \u2014 computed from local filesystem and git facts with NO language-model call. Byte-stable for the same inputs, sorted and string-valued so it drops straight into a rapp/1 frame payload and two boxes computing the same census produce the same hash. Counts things, never names them."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_census_agent", "rar_sha256": "0cfcf32f07e2cfa253c4cef082160ef14743303ca387f83381e66d4483e1db2c", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "RapterBox", "tags": ["census", "hive", "deterministic", "static", "no-llm", "frames", "shape"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapter/hive_census_agent`. The original RAPP
agent is preserved byte-for-byte in `hive_census_agent.py` and in the RCI capsule.

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

hive_census_agent.py — a machine's census as STATIC data. No model in the loop.

THE PROBLEM IT SOLVES. The obvious way to survey a fleet is to ask each machine, over chat,
to describe itself as JSON. That means a language model spends a turn reformatting facts the
machine already holds on disk. It is bad four ways:

  SLOW               a model turn is seconds to minutes; a file read is microseconds. The
                     timeout budget for a socket and for a model are not the same number,
                     so live peers get reported unreachable.
  NON-DETERMINISTIC  the model *usually* returns the JSON you asked for. "Usually" is not a
                     protocol, and two identical machines can describe themselves differently.
  EXPENSIVE          every peer, every survey, forever — to move numbers that never needed a
                     model to exist.
  UNVERIFIABLE       prose cannot be hashed into agreement. Static bytes can.

THE RULE: frames do the transport; the model is only for judgment. Every field below is a
filesystem, git, or config fact. Nothing here requires intelligence to produce — only to
interpret, which is the reader's job.

WHAT IT PRODUCES. One canonical JSON document, byte-stable for the same inputs, written to a
known local path and re-emitted on demand. Keys sorted, values as strings, no floats — the
canonical shape RFC 8785 JCS requires — so it drops into a rapp/1 frame payload unchanged,
and two machines in the same state produce the same hash.

RESIDENTS ARE DEFINED BY THE SPEC, NOT BY A HEURISTIC. Counting "any directory containing
subdirectories" counts virtual environments, browser profiles and image caches, and yields a
confident number that means nothing. The specification says what an organism IS: an
`organism` egg carries rappid.json and soul.md; a `rapplication` carries rappid.json and one
agent.py. That is the test used here — grounded, and it needs no blocklist to maintain.

PRIVACY. It counts things; it never names them. Populations, not identities. No paths, no
user content, no customer data. What leaves the machine is a shape, not a picture.

RUNS ANYWHERE. Deterministic data must be producible with nothing but a Python interpreter,
so the agent base class is optional garnish — the functions below are the product, and
`python3 hive_census_agent.py` works on a machine with no agent framework at all.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "write": {
      "description": "Also write the census to the local static path so peers can read it without a model call.",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hive_census_agent.py` and embedded as the fenced Python below (sha256 0cfcf32f07e2cfa2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hive_census_agent.py` first:

```bash
python3 hive_census_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hive_census_agent.py   # or on stdin
python3 hive_census_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapter/hive_census_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hive_census_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapter/hive_census_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""hive_census_agent.py — a machine's census as STATIC data. No model in the loop.

THE PROBLEM IT SOLVES. The obvious way to survey a fleet is to ask each machine, over chat,
to describe itself as JSON. That means a language model spends a turn reformatting facts the
machine already holds on disk. It is bad four ways:

  SLOW               a model turn is seconds to minutes; a file read is microseconds. The
                     timeout budget for a socket and for a model are not the same number,
                     so live peers get reported unreachable.
  NON-DETERMINISTIC  the model *usually* returns the JSON you asked for. "Usually" is not a
                     protocol, and two identical machines can describe themselves differently.
  EXPENSIVE          every peer, every survey, forever — to move numbers that never needed a
                     model to exist.
  UNVERIFIABLE       prose cannot be hashed into agreement. Static bytes can.

THE RULE: frames do the transport; the model is only for judgment. Every field below is a
filesystem, git, or config fact. Nothing here requires intelligence to produce — only to
interpret, which is the reader's job.

WHAT IT PRODUCES. One canonical JSON document, byte-stable for the same inputs, written to a
known local path and re-emitted on demand. Keys sorted, values as strings, no floats — the
canonical shape RFC 8785 JCS requires — so it drops into a rapp/1 frame payload unchanged,
and two machines in the same state produce the same hash.

RESIDENTS ARE DEFINED BY THE SPEC, NOT BY A HEURISTIC. Counting "any directory containing
subdirectories" counts virtual environments, browser profiles and image caches, and yields a
confident number that means nothing. The specification says what an organism IS: an
`organism` egg carries rappid.json and soul.md; a `rapplication` carries rappid.json and one
agent.py. That is the test used here — grounded, and it needs no blocklist to maintain.

PRIVACY. It counts things; it never names them. Populations, not identities. No paths, no
user content, no customer data. What leaves the machine is a shape, not a picture.

RUNS ANYWHERE. Deterministic data must be producible with nothing but a Python interpreter,
so the agent base class is optional garnish — the functions below are the product, and
`python3 hive_census_agent.py` works on a machine with no agent framework at all.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapter/hive_census_agent",
    "version": "1.0.0",
    "display_name": "Hive Census",
    "description": (
        "Emit this box's census as deterministic static JSON — protocol revision, anchor "
        "hash, resident populations, posture, trust — computed from local filesystem and "
        "git facts with NO language-model call. Byte-stable for the same inputs, sorted "
        "and string-valued so it drops straight into a rapp/1 frame payload and two boxes "
        "computing the same census produce the same hash. Counts things, never names them."),
    "author": "RapterBox",
    "tags": ["census", "hive", "deterministic", "static", "no-llm", "frames", "shape"],
    "category": "core",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapter/basic_agent"],
}

import glob
import hashlib
import json
import os
import platform
import socket
import subprocess

# The census is DETERMINISTIC DATA and must be producible with nothing but a Python
# interpreter — no brainstem, no agent framework, no model. Hard-importing the base class
# broke exactly that: `python3 hive_census_agent.py` on a peer died on ModuleNotFoundError,
# which would have made the no-LLM path depend on the very stack it was meant to bypass.
# So the agent wrapper is optional garnish; the functions below are the product.
try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:                     # standalone: enough to define the subclass
            def __init__(self, name=None, metadata=None):
                self.name = name or getattr(self, "name", "agent")
                self.metadata = metadata or getattr(self, "metadata", {})

            def system_context(self):
                return None

            def to_tool(self):
                return {"type": "function",
                        "function": {"name": self.name,
                                     "description": self.metadata.get("description", ""),
                                     "parameters": self.metadata.get("parameters", {})}}


CENSUS_PATH = os.path.expanduser(os.getenv("HIVE_CENSUS_PATH", "~/.rapp-census.json"))
ANCHOR_CACHE = os.path.expanduser("~/.rapp-dogg-cache.json")


def _sh(cmd, cwd=None):
    try:
        return subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True,
                              text=True, timeout=20).stdout.strip()
    except Exception:
        return ""


def _populations():
    """Discovered, not enumerated from a fixed list — a new species of resident should be
    visible without editing this file. Counts only; never names."""
    out = {}
    for root in ("~/.brainstem", "~/.rapp", "~/.rappvision", "~/.openrappter"):
        rp = os.path.expanduser(root)
        if not os.path.isdir(rp):
            continue
        for entry in sorted(os.listdir(rp)):
            sub = os.path.join(rp, entry)
            if not os.path.isdir(sub) or entry.startswith("."):
                continue
            try:
                members = [m for m in os.listdir(sub)
                           if os.path.isdir(os.path.join(sub, m)) and not m.startswith(".")]
            except Exception:
                continue
            # A RESIDENT is something with an identity or a mind — not any directory that
            # happens to hold subfolders. The first cut counted venvs, chrome profiles and
            # image caches and reported 296 residents on one box, which is a confident
            # number that means nothing. §9.2 says what an organism IS: an `organism` egg
            # MUST carry rappid.json and soul.md; a `rapplication` MUST carry rappid.json
            # and exactly one agent.py. So that is the test — spec-grounded, not a blocklist
            # I would have to keep extending every time a new kind of junk appears.
            real = [m for m in members if any(
                os.path.exists(os.path.join(sub, m, marker))
                for marker in ("rappid.json", "soul.md", "agent.py", ".rappid.json"))]
            if real:
                out[f"{root.strip('~/.')}_{entry}".replace(".", "_")] = str(len(real))
    return out


def _anchor_state():
    """What canon this box holds — read from the cache the DOGG agent already maintains.
    No network call: the census reports what IS, not what could be fetched."""
    try:
        with open(ANCHOR_CACHE) as f:
            c = json.load(f)
        doc = c.get("doc") or {}
        spec = doc.get("spec") or {}
        return {
            "rev": str(spec.get("revision") or doc.get("rev") or "unknown"),
            "anchor": str(c.get("pin") or "unknown")[:16],
            "spec_sha256": str(spec.get("normative_sha256") or "unknown")[:16],
            "trust": str(c.get("trust") or "unknown"),
        }
    except Exception:
        return {"rev": "unknown", "anchor": "unknown", "spec_sha256": "unknown",
                "trust": "no-anchor-cache"}


def census():
    """Every value a plain fact. Sorted keys, string values, no floats — canonical shape."""
    agents_dir = os.path.expanduser("~/.brainstem/src/rapp_brainstem/agents")
    pops = _populations()
    body = {
        "schema": "rapp/1-census",
        "host": socket.gethostname(),
        "platform": platform.system().lower(),
        **_anchor_state(),
        "populations": pops,
        "residents": str(sum(int(v) for v in pops.values())),
        "agents_installed": str(len(glob.glob(os.path.join(agents_dir, "*_agent.py")))),
        "scheduled_jobs": str(len(glob.glob(
            os.path.expanduser("~/Library/LaunchAgents/*.plist")))),
        "disk_free_gb": str(int(__import__("shutil").disk_usage("/").free / 1e9)),
    }
    # The census names itself by its own content, so a peer can tell "unchanged" from
    # "re-sent" without reading a single field — and two boxes in the same state agree.
    canon = json.dumps({k: v for k, v in body.items() if k != "census_hash"},
                       sort_keys=True, separators=(",", ":"))
    body["census_hash"] = hashlib.sha256(canon.encode()).hexdigest()
    return body


def emit(path=None):
    """Write the census where anything can read it — no server, no model, no auth."""
    p = path or CENSUS_PATH
    doc = census()
    tmp = p + ".tmp"
    with open(tmp, "w") as f:
        json.dump(doc, f, sort_keys=True, indent=2)
        f.write("\n")
    os.replace(tmp, p)                 # atomic: a reader never sees a half-written census
    return doc, p


class HiveCensusAgent(BasicAgent):
    def __init__(self):
        self.name = "hive_census"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "write": {
                        "type": "boolean",
                        "description": ("Also write the census to the local static path so "
                                        "peers can read it without a model call."),
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        if kwargs.get("write"):
            doc, p = emit()
            return json.dumps({"written": p, **doc}, sort_keys=True, indent=2)
        return json.dumps(census(), sort_keys=True, indent=2)


if __name__ == "__main__":
    doc, p = emit()
    print(json.dumps(doc, sort_keys=True, indent=2))
    print(f"\nwritten: {p}")
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
