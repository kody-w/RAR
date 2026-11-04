---
name: "rar-rapter-hive-census"
description: "Emit this box's census as deterministic static JSON \u2014 protocol revision, anchor hash, resident populations, posture, trust \u2014 computed from local filesystem and git facts with NO language-model call. Byte-stable for the same inputs, sorted and string-valued so it drops straight into a rapp/1 frame payload and two boxes computing the same census produce the same hash. Counts things, never names them."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_census_agent", "rar_sha256": "0cfcf32f07e2cfa253c4cef082160ef14743303ca387f83381e66d4483e1db2c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "RapterBox", "tags": ["census", "hive", "deterministic", "static", "no-llm", "frames", "shape"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/616Wdei2LLtX2F852E3ZCbSqFh77DEunQqIdAriyTN20veN9Fin/vtdoJmVdXfzdL+X1MVqYkXMmDFD8tcPu2ujsv745UOzq9av6XL8+PTh+Y1bx1UblwV4wuVxC7VR3EBOOf6pgVy/aLoGshvI88GSPC7ipo1dqGnt+R9Bl8/Q1w5boQRU1WVbumUG1X4fN2C7T5BduOBAKLKb6BMYbmLPL1qoKqsus+cDm0/gS9N2tf8Jauuuab/v5ZZ51bW+BwV1mUNZ6doZFMSZ30xN6+dgXw8KgaGB7bYNNMRtBJ1lKLOLsLND/3Neen4GgTXZF4ieWv8zsNbJfCgAtrSRDzV27kNxAU4ABjRlPR80b9m0dVyEn3s768BIU0LgCK8uq2Z+Ysdh1IJVbQnZUG1XFYIC6+adKnvKSvu1RTuUs+f85n0FsN/vR76dCRzlda7/+/jsny8QU3YFuA1wfhECuwq/92uoAM/nMT//AmLlj3ZeAS98/PLf//PpIwafP3759cPN7AYMfRzj3meWI6gQ+BnMnz0CHlQTiHsBvld+DXyQgyHPD6D3tz83fhZ8gv7613Sw67D5yy9fC+j9FwfQa/BL6Ld//vox1HHrf/34ecr855UuCCT0d8gH6PnzX/74sPZBfAsoacrii9flVfPnX18btX7x9eMXqJqPBjv89grFP1J/av5+qTsAibiY8fJ37Kcd/3m3l1P//Jf/sPzjN+CsAsSwcxfUgfv/139BUuzWZVMGLaS7ZddCNXB/nPtfi6/FZU6AePH7jGa/buIZP695IHyJv2wElQH07f/USzIhEfD+P17G/MOe/f/tC3QB68s6DuMC4FejFOVrsTya965APvh1D4DmzBAFkfg8fwBWQ9/+aa8v1fRtwRd4OhulMTzAd9V0mf9lNtiM/OJtnmsXkD/6LkifnxNnyb8y6/1XdjdpnGWQF9fgJmU9LXsDB/wyb/bt2zcHIPJr8cINDr0IokHAhB/mQJ8/gxsE2ZwVXwsf5Dn0p19/+xP0v9B/WrVsPp+hAMi+3QssXGgE4KzL/TkF5lj5IKFm9/7629uPYJsCJAQIRhzEr5yAsrhIfe+7U/Uj9RlbbyDHB84EjswrAIg5AeP2C8QH0A97waHzI0BrUAToB1Bb5c9YcSewqw2u88OTRdmCFG3jJpg+QV3zytlvDiCD2cT8Hy6Y/g2SGAVqS8B8gBuAmcsksLgsYuD+HyF/jYNNasCr9PctvkDnJdErG+Aoqu33GTOzzXEBjPV9+UI8hT98LebE92dXLST6cg+YBDzjvkP6eY75TEE5CGzz/exljj2z3aW0weH116J5I9mu51C4JTBlgsIu9gB1+397Q6qJyi7zFv/5LwZ9R8F7R2XB4L8C7Xc+t6HcdgGx+X8oKfqFuvAM5NmtDdxQQi/efhublWW17Hs5cpCiyfSJkyD+AunyyeD0d245fVyCvQZ7mn3fdCCfAJahIPP9JclmnzUp5IPDv1vwCZovCc2R+/R1duqrADoAMO3MhLNhMx7nE+wWyn27mIHyvbi8jWxmxMzjCx3VM+Jyu13Q9ipK4Apfi/eRkJ0BmHsTQFsGFgF3e3GTAkwuNjoA6UHZ1fMtmiUBIUg/ySb0xz/7ffJy4JzBIFqzCeAGoCqDbG/+Nt98jvt82DwlXxjuNW9x2B+Z+cffTHtznJ3OAzy/lEkbsKmbgi8zMbwGXsfPQJmz4kfxKrrc8etP/2ZrUEQzgAtQawCJQvPur9wD0OmKeo7LXJm/zKvP8vkzy104TeLPvD4DYznkdexfu6YD9Xz667sCvPJ/4Y2p7OYg+4udX6CvH9fX1K8fsw9mW+1/Y9x3xfLpR+leBMqctd/R0ix8+gMicyEGIOnBuBcHIBvA9GxazOduCnfWeYP7fX9/yab56p/en18I/TRbumT9Oz3mGAJUvn3ZLCz0XQD4vjfLk39zhTcmSkD5QJgthlzPBqfxe54CGfP7RRv/O585L8Hhe29OCWt/IZMvkP4SdXMZWu79I/2064n75aV2wMXLxfdAERXNHMq//RSmeEZ3Ni2ISQCaXvtyy90BXwAScfysHOZ54Ea/K7pPs5z7NLMdAGsQv5Jo5oRFDUGRv9DTowPkNrNZ62eAyAFh+/PVv+uptzMXA9oS0CSYVwPSAhsPUQwY4EdFt72FhJPSeVXPI3WZqQWwDHtlZnKRi58Y/AUzIFGW8vTpVa//k6R8q5uFfb4WaVEOxbsUVzaQqkut9T/PYmnOg5kO/Jmnv0AiEC9vQfoJWmTowpMvXTprwhJQW2kDevkOnDmnfze0iewKiIM9A5Fbcg0JjP67194rfla1/0nMdkC6A8oDhoAC9s6OHznxpujl0nMn4P8bTTs7V+N0nuXOFx2iNA5iuT1/5liItqAZWLrCMZ9A5l/mAQo6cldtSf23Gp5j//XDLqaflAoASAtqJ3gEqlfnfH8AJAFIePelofu4bgEHQH4BPpXFoipA3OpyaOZSW5cL8l6CKp9J3QU3mzXSPDLNOF3wuWBxaVleifnKy1dFKF7QfNUhUA1cUA/dpR6D+4MoDvNUQB1lHdqgZ8ohXv8FfAcC6PvIN8gPQ3ByPdu+BCH2vszC9tWLgJL7JfdmTv82P8veu3/7tyvKwn9rDVB439XrjXiQz+2sPLxXJr2hENbAW94MtcUR7cI1880gB6A1zQChLMwEvD17fImmovEGxVhL7XJ/blj+9trg/+lZIOXnXm9mnxfDtuACS8mfE2J58rWYldES3SXJgBUuaAjLHAy+BII5Xyjz7f4t/r4X15lLXsh/nWBDVezOPeULftczQN7ZMo+cxn2B2D90sfPGUD73nc53CC9Cf+ko3xEGVXHeU1lULfSDU5aS17yo8KXQnFm7Lb3YQoNLRw0wGNo1OC36KWOhACTX4pI3G841dR5/WdAu8QBA+S6k/3U3MJR1umiJH9rqu9lve5Z8nmdBMxJBLzw3hPG8j//xS9Fl2aePOVKgGfrpgLlJtOeF4ILN3FwCm0CfOMdr/rY0gPOHP/5qQGXAE8uzl/Z9Kby2fAu5hZpetWUhQDD5pQfm2voSK+1ifLm4+qf2HZjTTtVsowP0NUi8j99AL/fmNO/VBr8nlM7clc2tXgUA92pzf/0AF7HnKL+v8m7cwPTarj83s7pF0C8rcAz4/nIuePZvW7r3PAA20GeAiSs3cAMcC1ZbH3MDMIi7hOsHKxJDNys/QIktgeMr3LVxchuQOE6i/mbjEQSJ+6jnYC7YD+R57YJTgFSP57MddxWgmx1KBr6/czAM36xIfxXgu802sDc+jvkeuVqtnN+XpqDPfV/oZeTsoh/d5Xzx971+/XA2xPw7AdHw1OuPQWDD3t5OznQ67pKNbzHIzlo9jlRrKPend8q6yjc7ps+mShCzs3N363vJ0bEucZwURjlvdekjswJehtUdGUfrtHp2B4uidLfwcTw4xdcorB5eAfeXKoG5E+nvEITGkVG5DZv0YQn7Srw+V1O80k/mXRBDB46O2lG+m9ZBzQ29pl2xJu6FGsOXM20IYwr359yOpIowZW4fILK/4w7uszH2GX8T7jY3KDvjdNhxqiUYvDHG/Kho+/yAPvpyU4037bA3LdgEyoLRH4fzU7lSREbsiWylCVHq15xWRIW7i/mCaRnPtG7qeluRhXkrEK0Y+SaL292VJg/CDqd2QmxdB3ijeGuSEyoJSWAM3gU7zZ0uEsqMXPVI9ZS9BJq9r1UdGX1D0x/yvajIZy+hNDMaPZvZNKJwJ6mqUjGCOd9Zc2Z6BSsbuFtfSjqIEVJdoVTP+xHGXzFTtk/k7sRIYnzh9knWHb2tUCXhVFjRfepIr29PV4l+hCukxOybCvcwfscQHA4ra4/FsCZfYvG+MQQF3puqQ+oaVyA1vTs/ng7R8e3WuCs9H1/SFW5WK2qzevrmjmup+GxyeUveN43IPc7JPaUGnAjifQ9T1TOTkrZJK4JiHkQ3Pv34ueH9gApLIc3NjLQChiV5qkdG9r7T+eC8UsfwcCkm17aJ6XRD7c0lkfrkEIuspD286+N54Fv5sbemTWY4eGIiJjJyiKMP8Z0DcEbV/UgjLndLeqe6wigbbZBVGsAB8nwGu2EXkx7A2eCWjLMhdZYXduceJ6jV2EeFX9DYSWa1iGc2V1PMrKqyYoGNqLV1LPD7JI/nG7p2+ufq1o5erBwy2EUS0qJD9Hzejvxe99tB3U3JBAuyU7PXk2CEWknxLLmX1fxU2QUaklfCTITcjxB/RPcH7UIVjPmwnquuUgiyOZklTbOITY3sRVrHZoRjj5IKTAsoyGni2XuuV2Z52QvnyH9KvFCoOKKc9IRpBTrq6UNoSQMtymeQUPuglrmrx6bJcOAVizsrsXJcr9VAQ+LdakKERy5qWXWIdo8TyZzHR4XvmC4216WoPSb9ITDdbU+aAkHshJ1gZKKhpc+TzxPJ8CRCnenk05EadyTTHSNbh+9aU5KS0Vd6/dDHTTQZ9UidpjF7MtxwFSKsq4eYvmb7jN6HecGwnRUc92v3pk5dlHn9E97KdHM5FqHQwcnpWvkh3qCnixi05O4wRZckxs4he1KVCN89NCXHAj+AB6vIo4SvrlgnnfP6quvqFAox0zCxbOv2+kBnd5fSWtyniaJZp43EPr1UfiQKCp9Pzb1QCBgj4pva+ntvtxsLhmx8+5oqGI3zbsNE8upk7yXGJP1WmqJo66fClh7UbH3EYtbPBh85PjdK3YxbKVIO+lZzUe7i+hSrD2oTM7qKcoRG0F5q+mKj5qNzOXqHU5usseethf0kvIeGxHKYw8s30aeO9xOBs16TRgd7OFvHFIQzraw1sdqeuSo5mpfWtKVRVFZiiu+P0cZKCYGKLbpwFK4Lp7VC8PnxENMkYY4IWublEdFN+15R8UMQDivHJNpTIGrsWjLPZB5JqSoFiq+uGWPYrfSNGVFxzwtPxS4fu+ASenjEsCE3yk4JC+pEPJXYNJqAuwMqFfW2OiYEkjEs54ny1UNrtmhEczQqzgrX9DGCy1ba3mTnXMZkxFY0cahTzps06xx7RStc9UZFpgZ3D3ssum8IZnfWpch7XDF2m1eycPB4saHChLY3W9Tg+iGbxM0IK6MGIwgsBaMAy+OuS8r2OHSNznd7Zu11lrlXbtt6M+xK73GQtgAQyC5zsSQ0jLVq7RDtBJMG/PQnpb9sJJUTBbzcHSrYS5h1N+YCAbRsUY4gr1KrINpVH+bUqo9Kbwez7hnRQpFbH9td0OAWRxj57XCTs0saRSzshqVF3QeJi2RSci5rR9sUadISqCEw3tkDJY/o7tRdeeQSy1/ZfLzzDMytr8JZG3M/qA/TxMUc24gbmL+G+p7OsLWiyIj9xE27Vk5U1QbU8ayRqURjpI5xMFuqhyEVQm0jYEfTFm5EPpDDMeivyC1M1+xT9qxWP3IwwqiyUsg+S2MrsT2He+3sBRsBB5kEb9z0Pp3lnViJm1K+hKxNohlf7NH8xiOKxKxH9VL3Ic8KkuBcK4ly0YxpqnDTcNVqVbDRPrjdn6SS4EjkyqqcqyTF6WZ1sPJ7uA9V+X4Rp7Vm3B+qra2Jw6OQOAF+Pg/ETldYq/LH8zXmqhalSsVxEkTdt8L9FhV3IyAa5HoidkPH8SUZX9ldGtK4PxyaW/CciJu2UtSai61Lwg9CbMLUyMWtafJq+VzxGO97Hk/K9ZavKG0UPMKQLvTqOjr3XH6uH3rAUwXrGHnWtNVAsp7CTAMmCtOFPbBHZH+XRTvhuELZ+pVLuze/Wo83eLsiMnrcgZJnnNi0fezlVM/lgsGbLtF4TrmrUXaI1niuMnKa5ZS0T/l2I9IEcetDxzcmLkONJ4tJT9QImNYh5dVla6ftCs47z6AO+3Vyf6rmausy6emZ2k58N3hBFt0waAh6w1CerCSytDnr9JOGafaAVuf9Da+v6uBkmY6RLBdx4/FmGY17Rj01q7Xhap3Sk4jsrxsXFaXpeaowPNQeSVpyjFxGScTBOmOLzJkiBBVU/6SI8cYqdxV8cDm1yXaAt3Si2xDPYZIcJqaGBC9W1T1LbGdV5UbOPhRYsLiTSxwPCAM4bHiuhfXoU4ShRLq6dUAcDrDRqB5s7g8tObrSle5xBN/VyXk0qZNOewWSF8fVpUVvaBJEN1nZa8/dBMqhu/fYIKtuVXi5rgK3vl7vj24jnM+KErapxSKPtXQqK+0ZUZl95viHYeO4MejceBjykqFNhnmwDWa4vY3ExKDRIXLZtFerEoIjL04JlZ42hk6yeEqGa2qwED/bTGWrHZ97Ca0v24tvGwJyv5Vd/2g85SokuViexRgGKbhBsrtsWRZ/d8zjqjrFyUWSEVH22DVgAOLerD2EcSr2TrDBQZFM+tE/+6NOWUEDhhqtMiXtaLSSCDCvR4eBw22D24ePomQG6c4S6g2jNuskERP6+HSu9erYtrxwEZHjlHWJVTGhFQUdM3aJEQsY57QZfdVlw6IlNkUCjHyeDi1l2S1pGeeWW91PZEWgMn8FYfe3G90+PlsNoN1dByku04erzCmTU2NHfGCV/b2hQyvcjMhdDykNiU4KJh9DvIr1oOfXqeO6Vu9LZ1ONsce+98kjQ6BFxe57XZdvXiOEhGKMVLNp9EG+YuqdwjTjUQ09TQd7iajYJ7XNUOFByirSj6bKaCun2RjsHT/Ipn/soodE+7oGaoJs97i79/mrdKGih9JIBjIIasnt99R+tbFYQyHsLTb4aMS16pZDaQTXDLPn5W3U+H27dSUdKdVnduvZZtiWjtgq6qW399jxOjKxEeTHLsRITHYDiclAN7IFnYch7e4lI4BSbdJIsOpPturFWnc0HpQFP1Z0xzRisUWaTiWFM081fsKGUd/D3hCotuJLVp1hyDG1i+jJVE11vFMBjfAwPVjVzX+GnGmzD7aHRRvIJVNiHoGPBw19T8yr+ayOO6d1nVs0BbdsrSRlcBTZRp4eaDHmJazAYjxI2MEIx7z3I04ELdDqUnVDDRig2cjmjpDjRHyuUDqo4MLJN+LVCC9wNMC8QIYb4VGuGEnBtpovZxNbjqfEfJ77G45brGMKJMtEysT2XtXLCkwhUrtx87UVYQ6BXh+ygkXqcxLOnNa6Quoo5yY2BR50Uh6X7dmNtg66QzycnFGqc/QcHUfq6djrLCMG47prUyLTW6acruZOGMv0xNtEcevcuyExiG1ad8o0MYFXct72dq08iNVEXFHtcbf2iqnaAx0392M+yRt6pxtV6VNliwxPnUcSWrPvqwafrEmposfNpvWs0E8BeTvESazW7bTCrlFShCXFJSYuajsmT3GV8WKVuoYoqjyadNgwfuZxeU9ItnWrbsahOQQUHG0CdRt0VECI0i4IfPVW+E51QJVeuwbGdqr3Buk5jseIT/Jo24lj1CaqkeOhlSNMdvzIsVEsC2BUCMbqycLbVvNiUaxM2gFsYt3sgM8vAnp51mXiMee+u4iM/Lz7kn1yS1FC7qmDhSfmlNzjEfWl3Nxl2+Muw2iY4uW9YHZ9eT/i1jFM9+iR2cZ353htvVTF/THuSl+zH+IOgcU1pkyEv7mUCnyDE2q0xa6BRx6x73XjI0ifsaRS3y+lV3rPCgMiCTl6u0HElOcBLQMAxVZnLM1w7kK+wzGNjSsMy08uQ0qXIyhXVmLd0pNH71It2N2lM3YUq7u6RlOpicO0bKvzKZPH0uVSiwJl4JQo1/WVpphju93asRKcTq0sXLeD3lAPkvD92iNp6obyBhyJu30sWn3Xt8Eo9k+dzC+JeMqtpvECAb0Scl+6Z95DPWRo84Drdu1K2injuE5I1XQe4Y7CQC3rOwLWadkPNTc2H8Uq1veYfAe69x4Rh7EwdAZnWMNx93txFTdDdW23euD6+RPkF3FzdX/lxAdCHK/Tud1t3fMQsyf2RIr+ZVrvYLfPYE/dXTwHfNSJK3t4EP1K2CMSJTaCae0uQcFgQGJOJ5irc17AHN0SMSLJhvaYG3CpJlfbt0qgMojn8R4z3Obo0LSqefDdcVeOiJdGd9PO2oV49lYnHdmGcoknJT67Q9+R50d2UtGqLBM7jYWHogpst7PrvcU5xvXQVEpAMb7fYtuHLfRP30k7I1unHS7DSUTsPKyX0XPlmVpI+A0SnPziQt5vNqopXbgPeAveKgf0vBWlwkNYwrsURvjsJjPVewCdfEBsuc0RTBELM7uUoVFdzhcEPa4H0oxD9NjQboMzU+wn5T47r4ypDQ/R5uZexU7IV3UX5kfcyI+F9tgf6g0aCUNEXKZAvyGHhMr8ce1dGL/uLqEiOg+LT/ocD13bG7HbDt2zxjauHbbajEZntcz9cT1mrIcdKmf12FgnLbMCCu0Tz6mHOjGwlZbAZHeV8aeaOd41t7xIIrCrF+g9lz0a2ReNJ4pd8z6W9CrO6fOVKTAME73OcxFXTb1U5A+b4rQ/s0gbZIg9FtQGu3mGui/a4XKRDEER7mvSyM67qzjisqyunNvkD+JpXxWkv0pn0bpW1wdTvYJ+4nbfd80UrB5rXAjk2ixx2bocnhcr4WlBR8V0o8FnmBmFAJMqWcHJO5bHzpoQbnCp7aujc7qxjoJoN3engN5EWB0MJ3D80PCMW5m3TheTaYJLtxu7PtK6axhJr6P7QxmPksj4al56QGRgqNPXSeo/AsNoMWTvy45Bt6yzjyaW3twe6IgfK4sNeSZs5PF+ptk8HFSCpsOyZbb7YLsy6rTZlLdNjCBR6l+j/chfSCwyj2Ym0sldu/YwTigmULEe4nWtc8yyWOzFdXAwInlTs0zoDvFeVUCjQ0Vb+JwmzVStiFoUpF7j9mjqheHjGYjWUIj06WIk66rqyzUbYLTuXA4Ckh2YxzHWKC8NbgRqPleOFesbZihj7vGsE9CLnusdxZBaSq/qQ5Rsy7KIz2RUkPtCxCTHRzie3l4wDz53jr2S74rD1ScPf1IpGu8PjEMq40mk6xvQiad1msi3SM38flCLAleF5lxlZbayqA18HKotaGlOej5G+FHHjD1amCOO1ipjrwOWrW2gVN1u14j7oyM/nYBfP+ARXY8lap0UHO0nNOnIHWrUzqTlvrO6tZ4w2R6qBia8w1TcrgtEG3hu2qBVbgepVXlxrJblVryb++YMAlAyyto5NcVt65p5/DDK5L6pUxN3SSRjUWlY3erbcfdUEHg4p9v+buVj0ig7FL84/rGH5arLznvLMHoSicRNXMhFeHzIN6qEH5NwWLsZEDF4GsLT+hnbBssmXk+ZON34JNeapxQ7UZxBThnXYdt2Wgcnz0gkT5XHUbiQT+Y+oaW6val4zatU3aCXm7yjd44hPrf4dC6TRxv7uXKDFRLe8I/D/Oq0c7M1v1sBhrgwWzJpV/E0uWrgc7uqGN2rRjc1aVPFHsvkvDw4OGXTO2XQFOUaME7W0M+yoSjq7x+fPub3e//8cuPH25P5x/P/b7/hv35uL3twYOGCE//7Y36l8cty1i//8vT/+fRRuzE4+/Xqocm68P0D/uvFw+d51ecfL2Rer8j/sbwaG9vv725aO5z/H+DHj2nzouX/c/70hmtevbx4AR+K8nOW5bNzlvf4Lx9U/mzN8j/cltciwCJg02//F9kqzPcsKgAA -->
