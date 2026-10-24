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
