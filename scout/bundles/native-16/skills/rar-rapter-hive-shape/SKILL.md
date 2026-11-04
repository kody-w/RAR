---
name: "rar-rapter-hive-shape"
description: "Look at every cubby in a hive at once and report its SHAPE \u2014 divergence (who disagrees about what the world is), silence (who did not answer, always named), mass (where the population actually lives), and spread (how unlike each other the members are). Private by construction: publishes nothing, writes no frame, and leaves the picture on the operator's machine."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/hive_shape_agent", "rar_sha256": "a1c3e6b99c86bf1a8622779c5900fd17ef4c9b1a9feb93affb436e32fdaa4836", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "RapterBox", "tags": ["hive", "fleet", "shape", "divergence", "drift", "census", "observability", "private"]}
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
