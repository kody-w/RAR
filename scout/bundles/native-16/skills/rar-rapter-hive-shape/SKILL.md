---
name: "rar-rapter-hive-shape"
description: "Look at every cubby in a hive at once and report its SHAPE \u2014 divergence (who disagrees about what the world is), silence (who did not answer, always named), mass (where the population actually lives), and spread (how unlike each other the members are). Private by construction: publishes nothing, writes no frame, and leaves the picture on the operator's machine."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_shape_agent", "rar_sha256": "a1c3e6b99c86bf1a8622779c5900fd17ef4c9b1a9feb93affb436e32fdaa4836", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "RapterBox", "tags": ["hive", "fleet", "shape", "divergence", "drift", "census", "observability", "private"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapter/hive_shape_agent`. The original RAPP
agent is preserved byte-for-byte in `hive_shape_agent.py` and in the RCI capsule.

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

hive_shape_agent.py — see the SHAPE of a fleet, every member at once, privately.

WHY SHAPE AND NOT A DASHBOARD. Counting machines is easy and nearly useless. What you need to
know is the SHAPE: where the mass sits, who has drifted away from everyone else, who has gone
quiet, and whether the thing is one mind or several pretending. A number that says "3 healthy"
hides the failure that actually hurts — a member operating confidently on a different reality
while every individual health check reads green.

Four things, in the order they bite:

    DIVERGENCE  who disagrees with the rest about what the world is — a different protocol
                revision, a different anchor, different canon. One member on a stale
                specification is not a rounding error; it will act confidently on it.
    SILENCE     who did not answer. Named, always, as a row of its own. A fleet of five where
                two are unreachable is NOT a fleet of three — it is a fleet of five with a
                hole in it, and any summary that quietly reports three is lying.
    MASS        where the population actually lives. Averages hide this; one machine holding
                80% of everything is a single point of failure wearing a healthy number.
    SPREAD      how unlike each other the members are. A fleet whose members are each
                slightly different in different ways is drifting apart, even when every
                individual reading looks fine.

STATIC FIRST, MODEL NEVER. It reads each member's static census — plain bytes, no model call,
no authentication dance, and no dependence on any particular transport being open. Asking a
language model to restate facts already on disk is slow, non-deterministic and unverifiable.

PRIVATE BY CONSTRUCTION. This agent PUBLISHES NOTHING. It reads, it composes, it hands the
shape to whoever asked, and it writes no frame, no file, and makes no remote call carrying
what it saw. The capability is generic and safe to hand anyone; the picture belongs to the
operator and stays on the operator's machine.

TEMPLATE. The member list, what is asked of each, and what counts as divergence are inputs,
not constants. Point it at any set of machines. Nothing here knows anything about a
particular fleet.

HONESTY. Unreachable is not absent. Unparseable is not empty. Busy is not dead — a slow
thinker and a refused connection are different facts, and collapsing them loses the only
distinction that tells you whether to go fix something or wait. None of these is ever folded
into a healthy count: unknown must never read as healthy.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "cubbies": {
      "description": "Hosts or IPs to look at. Omit to use the HIVE_PEERS setting, or this machine alone. This agent never scans a network it was not pointed at.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "raw": {
      "description": "Return the composed shape as JSON instead of prose.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hive_shape_agent.py` and embedded as the fenced Python below (sha256 a1c3e6b99c86bf1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hive_shape_agent.py` first:

```bash
python3 hive_shape_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hive_shape_agent.py   # or on stdin
python3 hive_shape_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapter/hive_shape_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hive_shape_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapter/hive_shape_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""hive_shape_agent.py — see the SHAPE of a fleet, every member at once, privately.

WHY SHAPE AND NOT A DASHBOARD. Counting machines is easy and nearly useless. What you need to
know is the SHAPE: where the mass sits, who has drifted away from everyone else, who has gone
quiet, and whether the thing is one mind or several pretending. A number that says "3 healthy"
hides the failure that actually hurts — a member operating confidently on a different reality
while every individual health check reads green.

Four things, in the order they bite:

    DIVERGENCE  who disagrees with the rest about what the world is — a different protocol
                revision, a different anchor, different canon. One member on a stale
                specification is not a rounding error; it will act confidently on it.
    SILENCE     who did not answer. Named, always, as a row of its own. A fleet of five where
                two are unreachable is NOT a fleet of three — it is a fleet of five with a
                hole in it, and any summary that quietly reports three is lying.
    MASS        where the population actually lives. Averages hide this; one machine holding
                80% of everything is a single point of failure wearing a healthy number.
    SPREAD      how unlike each other the members are. A fleet whose members are each
                slightly different in different ways is drifting apart, even when every
                individual reading looks fine.

STATIC FIRST, MODEL NEVER. It reads each member's static census — plain bytes, no model call,
no authentication dance, and no dependence on any particular transport being open. Asking a
language model to restate facts already on disk is slow, non-deterministic and unverifiable.

PRIVATE BY CONSTRUCTION. This agent PUBLISHES NOTHING. It reads, it composes, it hands the
shape to whoever asked, and it writes no frame, no file, and makes no remote call carrying
what it saw. The capability is generic and safe to hand anyone; the picture belongs to the
operator and stays on the operator's machine.

TEMPLATE. The member list, what is asked of each, and what counts as divergence are inputs,
not constants. Point it at any set of machines. Nothing here knows anything about a
particular fleet.

HONESTY. Unreachable is not absent. Unparseable is not empty. Busy is not dead — a slow
thinker and a refused connection are different facts, and collapsing them loses the only
distinction that tells you whether to go fix something or wait. None of these is ever folded
into a healthy count: unknown must never read as healthy.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapter/hive_shape_agent",
    "version": "1.0.0",
    "display_name": "Hive Shape",
    "description": (
        "Look at every cubby in a hive at once and report its SHAPE — divergence (who "
        "disagrees about what the world is), silence (who did not answer, always named), "
        "mass (where the population actually lives), and spread (how unlike each other "
        "the members are). Private by construction: publishes nothing, writes no frame, "
        "and leaves the picture on the operator's machine."),
    "author": "RapterBox",
    "tags": ["hive", "fleet", "shape", "divergence", "drift", "census", "observability",
             "private"],
    "category": "core",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapter/basic_agent"],
}

import concurrent.futures as _cf
import json
import os
import socket
import subprocess
import urllib.error
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


DEFAULT_PORTS = (7071, 7081, 7082, 7077)
# An LLM-backed /chat turn can take far longer than a socket handshake. The first cut used
# one 20s budget for both and reported three LIVE peers as UNREACHABLE — a false negative,
# which is the unknown-vs-unhealthy confusion running in the other direction and just as
# dishonest. So liveness and thinking get separate budgets, and BUSY is its own state.
PROBE_S = int(os.getenv("HIVE_PROBE_TIMEOUT", "6"))     # is anyone home
THINK_S = int(os.getenv("HIVE_TIMEOUT", "120"))         # is anyone answering


def _ask(host, port, prompt, timeout=None):
    """One cubby, one question. Any failure is a NAMED state, never an empty answer."""
    url = f"http://{host}:{port}/chat"
    body = json.dumps({"user_input": prompt}).encode()
    req = urllib.request.Request(url, data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout or THINK_S) as r:
            raw = r.read().decode(errors="ignore")
    except Exception as e:
        # A refused connection and a slow thinker are DIFFERENT facts. Collapsing them
        # loses the only distinction that tells you whether to go fix a box or wait.
        name = type(e).__name__
        blob = f"{name}: {e}".lower()
        if "timed out" in blob or "timeout" in name.lower():
            return {"state": "BUSY", "why": "answered the socket but not in time"}
        return {"state": "UNREACHABLE", "why": name}
    try:
        d = json.loads(raw)
    except Exception:
        return {"state": "UNREADABLE", "why": "response was not JSON"}
    return {"state": "OK", "response": str(d.get("response", ""))[:2000]}


def _discover(hosts=None):
    """Which cubbies to look at. Explicit list wins; otherwise just this machine —
    this agent never scans a network it was not pointed at."""
    if hosts:
        return [h.strip() for h in hosts if str(h).strip()]
    env = os.getenv("HIVE_PEERS")
    if env:
        return [h.strip() for h in env.split(",") if h.strip()]
    return ["127.0.0.1"]


def _probe(host):
    """Find the port a cubby actually answers on. The estate has been bitten by assuming
    a port: a watcher reported 'brainstem unreachable' for four days while the brainstem
    was alive on a different port the whole time."""
    best = {"state": "UNREACHABLE", "why": f"no listener on {DEFAULT_PORTS}"}
    for port in DEFAULT_PORTS:
        # A cheap HTTP touch settles "is anyone home" without spending an LLM turn.
        # ANY status back — even 400 or 404 — proves a server is listening there.
        try:
            req = urllib.request.Request(f"http://{host}:{port}/health")
            with urllib.request.urlopen(req, timeout=PROBE_S) as r:
                if r.status:
                    return port, {"state": "OK"}
        except urllib.error.HTTPError:
            return port, {"state": "OK"}          # it answered; it is home
        except Exception as e:
            if "timed out" in str(e).lower():
                best = {"state": "BUSY", "why": f"port {port} accepted but did not reply"}
            continue
    return None, best


CENSUS_ASK = (
    "Answer as compact JSON only, no prose, no code fence. Keys exactly: "
    '{"rev": <the rapp/1 revision you operate under or "unknown">, '
    '"anchor": <first 12 chars of the spec hash you have, or "unknown">, '
    '"residents": <integer count of AI units you host, 0 if unknown>, '
    '"posture": <your current posture/profile name, or "unknown">, '
    '"trust": <your canon trust state, or "unknown">}'
)


def _parse(resp):
    """Pull the JSON a cubby was asked for. A cubby that answered prose is UNREADABLE —
    we do not guess at what it meant."""
    t = resp.strip()
    if "```" in t:
        t = t.split("```")[1] if len(t.split("```")) > 1 else t
        t = t.lstrip("json").strip()
    i, j = t.find("{"), t.rfind("}")
    if i == -1 or j == -1:
        return None
    try:
        return json.loads(t[i:j + 1])
    except Exception:
        return None



CENSUS_FILE = os.getenv("HIVE_CENSUS_PATH", "~/.rapp-census.json")


def _static_census(host):
    """Read a peer's census as STATIC DATA — no model, no HTTP, no auth dance.

    has so there is no need for an llm call to even serve it each way (dynamic data
    sloshing)". Yes. Every field is already a fact on that box's disk. Spending a language
    model turn to reformat it was the whole reason the first survey was slow, flaky, and
    unverifiable — and why three live peers were reported unreachable.

    This also sidesteps a real blocker found the same day: brainstems refuse LAN HTTP with
    "Invalid Host header. Use localhost, a loopback address, or an explicitly configured
    LAN host." Static bytes do not care what transport carried them, so the census travels
    over whatever already works.
    """
    if host in ("127.0.0.1", "localhost", socket.gethostname()):
        try:
            with open(os.path.expanduser(CENSUS_FILE)) as f:
                return {"state": "OK", "via": "local", **json.load(f)}
        except FileNotFoundError:
            return {"state": "NO-CENSUS", "why": "box has not emitted one yet"}
        except Exception as e:
            return {"state": "UNREADABLE", "why": type(e).__name__}
    try:
        r = subprocess.run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8",
                            host, f"cat {CENSUS_FILE}"],
                           capture_output=True, text=True, timeout=30)
    except Exception as e:
        return {"state": "UNREACHABLE", "why": type(e).__name__}
    if r.returncode != 0:
        err = (r.stderr or "").strip().lower()
        if "no such file" in err:
            return {"state": "NO-CENSUS", "why": "box has not emitted one yet"}
        return {"state": "UNREACHABLE", "why": (r.stderr or "ssh failed").strip()[:60]}
    try:
        return {"state": "OK", "via": "ssh", **json.loads(r.stdout)}
    except Exception:
        return {"state": "UNREADABLE", "why": "census was not valid JSON"}


def survey(hosts=None):
    cubbies = _discover(hosts)
    out = {}

    def one(h):
        # STATIC FIRST. A model turn is the fallback, not the path.
        stat = _static_census(h)
        if stat["state"] == "OK":
            return h, stat
        port, alive = _probe(h)
        if port is None:
            return h, {"state": alive["state"], "why": alive["why"]}
        r = _ask(h, port, CENSUS_ASK)
        if r["state"] != "OK":
            return h, {"state": r["state"], "why": r.get("why", ""), "port": port}
        parsed = _parse(r["response"])
        if parsed is None:
            return h, {"state": "UNREADABLE", "port": port,
                       "why": "answered, but not in the shape asked for"}
        return h, {"state": "OK", "port": port, **parsed}

    with _cf.ThreadPoolExecutor(max_workers=8) as ex:
        for h, rec in ex.map(one, cubbies):
            out[h] = rec
    return out


def shape(survey_result):
    """Compose the four things that actually matter."""
    ok = {h: r for h, r in survey_result.items() if r.get("state") == "OK"}
    missing = {h: r for h, r in survey_result.items() if r.get("state") != "OK"}

    def spread_of(field):
        vals = {}
        for h, r in ok.items():
            vals.setdefault(str(r.get(field, "unknown")), []).append(h)
        return vals

    revs, anchors = spread_of("rev"), spread_of("anchor")
    residents = {h: int(r.get("residents") or 0) for h, r in ok.items()}
    total = sum(residents.values())

    # DIVERGENCE: the majority reading is the hive's reality; anyone else is diverged.
    def odd_ones(vals):
        if len(vals) <= 1:
            return []
        big = max(vals.values(), key=len)
        return [(v, hs) for v, hs in vals.items() if hs is not big]

    return {
        "cubbies": len(survey_result),
        "answered": len(ok),
        "divergence": {"revision": odd_ones(revs), "anchor": odd_ones(anchors)},
        "silence": [{"cubby": h, "state": r.get("state"), "why": r.get("why", "")}
                    for h, r in missing.items()],
        "busy": [h for h, r in missing.items() if r.get("state") == "BUSY"],
        "mass": {"total_residents": total,
                 "by_cubby": dict(sorted(residents.items(), key=lambda kv: -kv[1])),
                 "concentration": (f"{max(residents.values()) * 100 // total}% in one cubby"
                                   if total and residents else "unknown")},
        "spread": {"revisions": {k: len(v) for k, v in revs.items()},
                   "postures": {k: len(v) for k, v in spread_of("posture").items()},
                   "trust": {k: len(v) for k, v in spread_of("trust").items()}},
    }


def render(sh):
    L = [f"HIVE SHAPE — {sh['answered']} of {sh['cubbies']} cubbies answered"]
    d = sh["divergence"]
    if d["revision"] or d["anchor"]:
        L.append("\nDIVERGENCE — members operating on a different reality:")
        for field in ("revision", "anchor"):
            for val, hosts in d[field]:
                L.append(f"  {field}={val}: {', '.join(hosts)}")
    else:
        L.append("\nDIVERGENCE: none — every answering cubby agrees on revision and anchor")
    if sh["silence"]:
        # Named individually and never netted out of the totals above.
        L.append("\nSILENCE — a hole in the hive, not a smaller hive:")
        for s in sh["silence"]:
            L.append(f"  {s['cubby']}: {s['state']} ({s['why']})")
    else:
        L.append("\nSILENCE: none")
    m = sh["mass"]
    L.append(f"\nMASS — {m['total_residents']} residents, {m['concentration']}")
    for h, n in list(m["by_cubby"].items())[:8]:
        L.append(f"  {h}: {n}")
    sp = sh["spread"]
    L.append("\nSPREAD — how unlike each other the members are:")
    for k, v in sp.items():
        L.append(f"  {k}: " + ", ".join(f"{val}×{n}" for val, n in v.items()))
    L.append("\n(private: nothing here was published, written to a frame, or sent anywhere)")
    return "\n".join(L)


class HiveShapeAgent(BasicAgent):
    def __init__(self):
        self.name = "hive_shape"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "cubbies": {
                        "type": "array", "items": {"type": "string"},
                        "description": ("Hosts or IPs to look at. Omit to use the "
                                        "HIVE_PEERS setting, or this machine alone. This "
                                        "agent never scans a network it was not pointed at."),
                    },
                    "raw": {
                        "type": "boolean",
                        "description": "Return the composed shape as JSON instead of prose.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        s = survey(kwargs.get("cubbies"))
        sh = shape(s)
        return json.dumps(sh, indent=2) if kwargs.get("raw") else render(sh)


if __name__ == "__main__":
    print(HiveShapeAgent().perform())
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
