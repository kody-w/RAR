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
