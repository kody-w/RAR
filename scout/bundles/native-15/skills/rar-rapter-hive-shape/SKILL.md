---
name: "rar-rapter-hive-shape"
description: "Look at every cubby in a hive at once and report its SHAPE \u2014 divergence (who disagrees about what the world is), silence (who did not answer, always named), mass (where the population actually lives), and spread (how unlike each other the members are). Private by construction: publishes nothing, writes no frame, and leaves the picture on the operator's machine."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_shape_agent", "rar_sha256": "c4cdee134802fd1ced521940c6ef38d0a5dba2503acc4e8cd8da5e4367d075a3", "source_kind": "rar-agent", "source_commit": "1308031e6f8f8350497f2970d717021d3a14762d", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "hive_shape_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapter/hive-shape:5f51e0bc8252e7a872c1972aa99098002e3449e136c3dd4663254da699b482fe", "kind": "skill"}, "author": "RapterBox", "tags": ["hive", "fleet", "shape", "divergence", "drift", "census", "observability", "private"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapter/hive_shape_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `hive_shape_agent.py` is
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
