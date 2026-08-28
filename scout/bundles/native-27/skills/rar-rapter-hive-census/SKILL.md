---
name: "rar-rapter-hive-census"
description: "Emit this box's census as deterministic static JSON \u2014 protocol revision, anchor hash, resident populations, posture, trust \u2014 computed from local filesystem and git facts with NO language-model call. Byte-stable for the same inputs, sorted and string-valued so it drops straight into a rapp/1 frame payload and two boxes computing the same census produce the same hash. Counts things, never names them."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_census_agent", "rar_sha256": "c078c513615c23f87edf14ee12514105af913e06577cfe53b2e2b2368963d4ff", "source_kind": "rar-agent", "source_commit": "1308031e6f8f8350497f2970d717021d3a14762d", "author": "RapterBox", "tags": ["census", "hive", "deterministic", "static", "no-llm", "frames", "shape"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hive_census_agent.py` and embedded as the fenced Python below (sha256 c078c513615c23f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hive_census_agent.py` first:

```bash
python3 hive_census_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hive_census_agent.py   # or on stdin
python3 hive_census_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
