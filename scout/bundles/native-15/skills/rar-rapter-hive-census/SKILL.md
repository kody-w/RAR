---
name: "rar-rapter-hive-census"
description: "Emit this box's census as deterministic static JSON \u2014 protocol revision, anchor hash, resident populations, posture, trust \u2014 computed from local filesystem and git facts with NO language-model call. Byte-stable for the same inputs, sorted and string-valued so it drops straight into a rapp/1 frame payload and two boxes computing the same census produce the same hash. Counts things, never names them."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_census_agent", "rar_sha256": "c078c513615c23f87edf14ee12514105af913e06577cfe53b2e2b2368963d4ff", "source_kind": "rar-agent", "source_commit": "1308031e6f8f8350497f2970d717021d3a14762d", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "hive_census_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapter/hive-census:05ef7a9d5b6d9fab4ec5e61742e4f6ce084965951a1a35858f7d1dd09a57b540", "kind": "skill"}, "author": "RapterBox", "tags": ["census", "hive", "deterministic", "static", "no-llm", "frames", "shape"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapter/hive_census_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `hive_census_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
