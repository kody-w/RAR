---
name: "rar-rapter-hive-shape"
description: "Look at every cubby in a hive at once and report its SHAPE \u2014 divergence (who disagrees about what the world is), silence (who did not answer, always named), mass (where the population actually lives), and spread (how unlike each other the members are). Private by construction: publishes nothing, writes no frame, and leaves the picture on the operator's machine."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_shape_agent", "rar_sha256": "c4cdee134802fd1ced521940c6ef38d0a5dba2503acc4e8cd8da5e4367d075a3", "source_kind": "rar-agent", "source_commit": "1308031e6f8f8350497f2970d717021d3a14762d", "author": "RapterBox", "tags": ["hive", "fleet", "shape", "divergence", "drift", "census", "observability", "private"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hive_shape_agent.py` and embedded as the fenced Python below (sha256 c4cdee134802fd1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hive_shape_agent.py` first:

```bash
python3 hive_shape_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hive_shape_agent.py   # or on stdin
python3 hive_shape_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
