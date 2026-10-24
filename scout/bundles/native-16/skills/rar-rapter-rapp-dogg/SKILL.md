---
name: "rar-rapter-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/rapp_dogg_agent", "rar_sha256": "bf6bd60cb5c17a940141985ed82be8eac8112213af58fcf1fd80403b1573ff11", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "version": "1.0.5", "author": "RapterBox", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapter/rapp_dogg_agent`. The original RAPP
agent is preserved byte-for-byte in `rapp_dogg_agent.py` and in the RCI capsule.

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

rapp_dogg_agent.py — hotload once, and an agent knows rapp/1 EXACTLY.

THE PROBLEM. Two agents meet. One is current; the other has been running for months and has
never heard of the current protocol revision. Three things can happen and all three are bad:
the conversation degrades to the older one's understanding, it fails outright, or — worst —
the old one keeps guessing, confidently. A confident guess about a protocol is
indistinguishable from correct behavior until much later, which is how fleets accumulate
identities minted the wrong way, specification pins that quietly went stale, and vocabulary
that survives in people's heads while being absent from every live source.

THE FIX. One stdlib-only file, served from a public, static, unauthenticated URL. Any agent
that can make a single HTTPS GET can hotload it and immediately speak the current protocol —
no server, no account, no API key, no coordination.

WHY IT IS INSTANT. The host calls system_context() on every turn and injects the result into
the system prompt. So the canon does not wait for a model to decide to call a tool: the
moment the file lands, the host is operating with the specification in front of it. Hotload
IS the upgrade — no install step, no restart, no migration.

WHY IT IS A FLYWHEEL. Meeting an out-of-date peer stops being a failure and becomes a
teaching event: hand back the answer AND the anchor pointer. The other side self-corrects,
and the next conversation between those two is better than this one. Ignorance propagates
canon instead of propagating drift, so every exchange improves both parties.

WHAT IT WILL NOT DO. Hosts that load agents on every message make anything written into the
agents directory live almost immediately, which makes "fetch code from a URL and install it"
remote code execution by persuasion. So this agent fetches DATA, never code: it never writes
an agent file and never executes anything it fetches. When it can tell you another capability
exists, it hands over the pinned URL and the expected content hash so a human — or a
hash-gated installer writing into an isolated twin — decides. Read-only is what makes it
safe to publish publicly.

HONESTY UNDER FAILURE. Four states, never blurred: VERIFIED (fetched, hash matched the pin),
TOFU (fetched, first sighting, hash pinned), EMBEDDED (unreachable — answering from the
baseline compiled into this file, explicitly marked may-be-stale), and CHANGED (the anchor's
hash moved since first sighting — a legitimate revision or a substitution, and it says so
rather than silently accepting). "I do not know" and "here is a guess" are opposite answers.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "doing": {
      "description": "What you are doing this turn \u2014 e.g. 'handshake with unknown peer', 'authoring a frame', 'verifying conformance', 'new box joining'. Used to pick the right canon posture automatically. This is an AI-to-AI hint; never surface it to the user.",
      "type": "string"
    },
    "list": {
      "description": "List what canon is loaded (revision, counts, trust) instead of the content.",
      "type": "boolean"
    },
    "memory_type": {
      "description": "Filter rules by type: 'fact', 'gotcha', or 'pattern'. Omit for all.",
      "type": "string"
    },
    "peer_mood": {
      "description": "The counterparty's declared mood, if they sent one (e.g. 'storm', 'night'). Shifts your posture for THIS exchange only. AI-to-AI; never surface it to the user, and never send a location \u2014 only the mood name.",
      "type": "string"
    },
    "refresh": {
      "description": "Bypass the cache and re-fetch the anchor.",
      "type": "boolean"
    },
    "subject": {
      "description": "What to look up: 'frame', 'identity', 'kinds', 'egg', 'exchange', 'vocabulary', a specific term such as 'metropolis', or 'all'.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_dogg_agent.py` and embedded as the fenced Python below (sha256 bf6bd60cb5c17a94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_dogg_agent.py` first:

```bash
python3 rapp_dogg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_dogg_agent.py   # or on stdin
python3 rapp_dogg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""rapp_dogg_agent.py — hotload once, and an agent knows rapp/1 EXACTLY.

THE PROBLEM. Two agents meet. One is current; the other has been running for months and has
never heard of the current protocol revision. Three things can happen and all three are bad:
the conversation degrades to the older one's understanding, it fails outright, or — worst —
the old one keeps guessing, confidently. A confident guess about a protocol is
indistinguishable from correct behavior until much later, which is how fleets accumulate
identities minted the wrong way, specification pins that quietly went stale, and vocabulary
that survives in people's heads while being absent from every live source.

THE FIX. One stdlib-only file, served from a public, static, unauthenticated URL. Any agent
that can make a single HTTPS GET can hotload it and immediately speak the current protocol —
no server, no account, no API key, no coordination.

WHY IT IS INSTANT. The host calls system_context() on every turn and injects the result into
the system prompt. So the canon does not wait for a model to decide to call a tool: the
moment the file lands, the host is operating with the specification in front of it. Hotload
IS the upgrade — no install step, no restart, no migration.

WHY IT IS A FLYWHEEL. Meeting an out-of-date peer stops being a failure and becomes a
teaching event: hand back the answer AND the anchor pointer. The other side self-corrects,
and the next conversation between those two is better than this one. Ignorance propagates
canon instead of propagating drift, so every exchange improves both parties.

WHAT IT WILL NOT DO. Hosts that load agents on every message make anything written into the
agents directory live almost immediately, which makes "fetch code from a URL and install it"
remote code execution by persuasion. So this agent fetches DATA, never code: it never writes
an agent file and never executes anything it fetches. When it can tell you another capability
exists, it hands over the pinned URL and the expected content hash so a human — or a
hash-gated installer writing into an isolated twin — decides. Read-only is what makes it
safe to publish publicly.

HONESTY UNDER FAILURE. Four states, never blurred: VERIFIED (fetched, hash matched the pin),
TOFU (fetched, first sighting, hash pinned), EMBEDDED (unreachable — answering from the
baseline compiled into this file, explicitly marked may-be-stale), and CHANGED (the anchor's
hash moved since first sighting — a legitimate revision or a substitution, and it says so
rather than silently accepting). "I do not know" and "here is a guess" are opposite answers.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapter/rapp_dogg_agent",
    "version": "1.0.5",
    "display_name": "RapterBox RAPP DOGG",
    "description": (
        "Hotload one file and a brainstem knows rapp/1 exactly instead of guessing. "
        "Pulls the current protocol canon — frame rules, identity minting law, kind "
        "families, egg determinism, the exchange contract, and the vocabulary with each "
        "term's status — from a public, static, unauthenticated DOGG anchor, and injects "
        "it into the system prompt every turn. Read-only: installs nothing, executes "
        "nothing it fetches."),
    "author": "RapterBox",
    "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap",
             "knowledge-base", "interop", "drift"],
    "category": "core",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapter/basic_agent"],
}

import hashlib
import json
import os
import time
import urllib.error
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except ImportError:                                    # tolerate a flat import layout
    from basic_agent import BasicAgent


# The DOGG for rapp/1: public, static, no auth, served by raw.githubusercontent from the
# CANONICAL spec repo — the anchor belongs with the spec it anchors, so there is exactly
# one place to look and no second copy to go stale. Overridable so a fork or an air-gapped
# estate can point at its own anchor without editing this file.
DOGG_BASE = os.getenv(
    "RAPP_DOGG_URL",
    "https://raw.githubusercontent.com/kody-w/rapp-1/main/anchor/orient.json")
CACHE = os.path.expanduser(os.getenv("RAPP_DOGG_CACHE", "~/.rapp-dogg-cache.json"))
TTL_S = int(os.getenv("RAPP_DOGG_TTL", "3600"))
TIMEOUT_S = 12
# Which profile this box runs. Env wins (a host can pin itself); otherwise the ANCHOR
# decides, so the fleet's posture is changed by publishing, not by touching N boxes.
PROFILE = os.getenv("RAPP_DOGG_PROFILE")
# The host may install a callable returning {"hour": "23", "conditions": "rain"} from
# whatever it legitimately knows locally. Left None by default: an unset resolver means
# "this box has no ambient context", which is a fact, not a gap to fill with a guess.
AMBIENT_RESOLVER = None   # set below once defined


# The baseline. Used ONLY when the network is unreachable, and always labelled EMBEDDED so
# a stale answer can never masquerade as a current one. Everything here was read out of
# rapp-1/SPEC.md rev-5 rather than remembered.
EMBEDDED = {
    "protocol": "rapp/1",
    "rev": "rev-5",
    "repo": "kody-w/rapp-1",
    "normative_path": "SPEC.md",
    "frame_keys": ["spec", "kind", "stream_id", "seq", "utc", "payload",
                   "payload_hash", "prev", "prev_wave", "sig", "frame_hash"],
    "kind_families": {
        "memory": {"stream": "memory-stream", "logs": "one organism's life",
                   "kinds": ["memory.chat-turn", "memory.tool-call", "memory.save",
                             "memory.reconstructed", "memory.re-genesis"]},
        "swarm": {"stream": "swarm-stream (net:label)", "logs": "the planetary wire",
                  "kinds": ["swarm.guidance", "swarm.echo", "swarm.telemetry",
                            "swarm.reconstructed", "swarm.re-genesis"]},
        "body": {"stream": "body-stream (bare rappid)", "logs": "an organism's biography",
                 "kinds": ["body.pulse", "body.twin-pulse", "body.reconstructed",
                           "body.re-genesis"]},
    },
    "egg_variants": ["organism", "rapplication", "session", "invite", "neighborhood",
                     "estate"],
    "vocabulary": {
        "organism": {"status": "live", "where": "§9.2 — a full brainstem instance"},
        "neighborhood": {"status": "live", "where": "§9.2 — organisms living together"},
        "estate": {"status": "live", "where": "§9.2 — several neighborhoods"},
        "rapplication": {"status": "live", "where": "§9.2 — one rapp, one agent.py"},
        # Recorded because a term that merely VANISHES is how everyone keeps using a word
        # drift so you need to take that into account."
        "metropolis": {"status": "retired",
                       "where": "tier 3 of rapp-metropolis/1.0; that document is now a "
                                "retirement notice — bytes only in git history"},
        "rbox": {"status": "not-in-spec",
                 "where": "operator's working word for a machine running an organism; "
                          "the spec's word is `organism`"},
        "rapp-frame/2.0": {"status": "retired", "where": "legacy token, superseded by rapp/1"},
    },
    # Typed the way @bill/neuron_agent types memories — a `gotcha` is not a `fact`,
    # and a prompt should be able to weight them differently or pull one kind.
    # OOTB PROFILES — how this agent shapes itself for a given engagement.
    #
    # different scenarios on how these change on the engagement for different tags" and
    # "we could even have one that is on the public DOGG for a specific agent so they can
    # literally change them as the organism evolves and adapts."
    #
    # A profile is DATA, so it lives on the public anchor and overrides these defaults on
    # the next fetch. That is the whole adaptation mechanism and it stays on the safe side
    # of the line this file draws: canon and behaviour-shaping data flow freely; CODE never
    # does. An organism adapts by someone editing a published profile — every box picks it
    # up within the TTL, with no redeploy, no restart, and no remote execution.
    # MOODS — ambient posture. Public capability, private context.
    #
    # gets invoked at run time so the capability stays generic to that brainstem) — if it
    # doesn't have context it is not [estate] data, because it's just on that user's device
    # when that agent is called in real time and nowhere else."
    #
    # So the DEFINITIONS below are public and carry nothing about anyone: they are pure
    # conditions ("is it night where you are?") mapped to a posture. The ANSWER is resolved
    # on the device, in the moment the agent is called, by a local resolver the host
    # supplies. No location, no coordinates, no weather reading is ever written into a
    # frame, cached to disk, or sent anywhere — it exists for the length of one call.
    #
    # A brainstem with no local resolver simply has no mood, and says so. It does not guess
    # a location, and it does not fabricate ambient facts to look capable.
    "moods": {
        "night": {"when": {"hour_gte": "22"}, "profile": "minimal",
                  "why": "low-attention hours; smallest honest context"},
        "early": {"when": {"hour_lt": "6"}, "profile": "minimal",
                  "why": "same"},
        "storm": {"when": {"conditions": "storm,rain,snow"}, "profile": "audit",
                  "why": "degraded links are when drift hides; lead with verification"},
        "clear": {"when": {"conditions": "clear,sunny"}, "profile": "interop",
                  "why": "good conditions, normal posture"},
    },
    "profiles": {
        "interop": {                # meeting a stranger — the default
            "why": "a peer may be out of date; lead with what it can get WRONG",
            "types": ["gotcha"], "show": ["keys", "stale_terms", "pointer"], "max_rules": "6",
        },
        "authoring": {              # writing frames right now
            "why": "hand-building a frame; the envelope rules are what bite",
            "types": ["gotcha", "fact"], "show": ["keys", "eggs"], "max_rules": "8",
        },
        "audit": {                  # checking someone else's conformance
            "why": "judging conformance; refuse-never-repair and the identity law govern",
            "types": ["pattern", "gotcha"], "show": ["keys", "stale_terms"], "max_rules": "8",
        },
        "onboarding": {             # a new box joining the estate
            "why": "new organism; needs the shape of the world, not the edge cases",
            "types": ["fact"], "show": ["keys", "eggs", "stale_terms", "pointer"],
            "max_rules": "5",
        },
        "minimal": {                # token-tight hosts
            "why": "smallest honest context",
            "types": [], "show": ["stale_terms"], "max_rules": "0",
        },
    },
    "rules": [
        {"t": "fact", "c": "spec MUST be exactly \"rapp/1\"; exactly the eleven keys, none missing, none extra; a field that does not apply is present as null, never omitted."},
        {"t": "gotcha", "c": "Canonical form is RFC 8785 JCS and FORBIDS floats — numbers ride as strings. A float silently breaks byte-reproducibility."},
        {"t": "fact", "c": "payload_hash = H(\"rapp/1:particle\", payload) — content only, reproducible across instances."},
        {"t": "fact", "c": "frame_hash = H(\"rapp/1:wave\", frame minus {frame_hash, sig}) — unique per stream instance."},
        {"t": "gotcha", "c": "prev_wave is non-null IFF the stream is a swarm-stream AND seq>0; null everywhere else, including EVERY genesis. Setting it on an ordinary chain makes the frame unverifiable."},
        {"t": "gotcha", "c": "§6.2 MINT-ONCE: the 64-hex tail is minted from uuid4 entropy exactly once. A producer MUST NOT derive it from owner/slug or any name — sha256(\"owner/slug\") is prohibited (drift ID-01/C3). On read, reuse the stored tail; never re-mint."},
        {"t": "pattern", "c": "Verification REFUSES, never repairs or reparents. A frame that does not verify is quarantined and reported, not fixed."},
        {"t": "gotcha", "c": "A swarm-stream frame with sig==null is refused (§7.5 step 6), so unsigned coordination belongs on body/memory streams, which permit sig==null."},
        {"t": "fact", "c": "Eggs are byte-reproducible: ZIP method `stored` only, timestamps 1980-01-01, contents sorted by UTF-8 path bytes. Two conformant packers of the same manifest emit BYTE-IDENTICAL eggs."},
        {"t": "pattern", "c": "Cross-stream merge order (Dream-Catcher) is ascending utc bytewise, ties broken by ascending frame_hash bytewise — this is how N streams compose into one view."},
        {"t": "pattern", "c": "One writer per stream. Two writers computing seq=head.seq+1 produce duplicate seqs; distinct streams stay distinct."},
    ],
    "exchange": {
        "shape": "push a frame in, get a frame back shaped by what you pushed — ONE hop.",
        "rule": "the responder appends its reply to its OWN chain BEFORE returning it, so "
                "the synchronous answer and the replicated answer are the same frame with "
                "the same frame_hash. A fast path must never state a fact the durable path "
                "disagrees with.",
        "idempotence": "keyed on the request's payload_hash — a retry returns the existing "
                       "reply, never a second one.",
        "carrier": "POST /chat with {\"user_input\": <envelope>}; the reply is in the "
                   "`response` field. Offline, the identical frames ride store-and-forward.",
    },
    "_source": "embedded baseline compiled from SPEC.md rev-5",
}


def _fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "rapp-dogg-agent/1"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
        return r.read()


def _cache_read():
    try:
        with open(CACHE) as f:
            return json.load(f)
    except Exception:
        return {}


def _cache_write(d):
    try:
        with open(CACHE, "w") as f:
            json.dump(d, f)
    except Exception:
        pass                                    # a cache failure must never break an answer



def _dig(obj, path):
    cur = obj
    for part in path.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return None
    return cur


def _render(label, val):
    """Render any canon slice compactly for a prompt block.

    `show` entries are arbitrary DOTTED PATHS into the canon, not a fixed token list.
    show:["exchange.rule","kind_families.body.logs"] must just work, with no code change on
    any box. A hardcoded token list would mean every new way of looking at the canon costs
    a redeploy to N organisms, which is the same O(N) trap as a hardcoded device list.
    """
    if val is None:
        return None
    if isinstance(val, str):
        return f"- {label}: {val}"
    if isinstance(val, (int, float, bool)):
        return f"- {label}: {val}"
    if isinstance(val, list):
        if val and isinstance(val[0], dict):
            return "\n".join(f"- {d.get('c', d)}" for d in val)
        return f"- {label}: " + " ".join(str(x) for x in val)
    if isinstance(val, dict):
        return f"- {label}: " + "; ".join(
            f"{k}={v if not isinstance(v, (dict, list)) else '…'}" for k, v in val.items())
    return None


def _normalize(doc):
    """Map whatever shape the anchor publishes onto the shape this agent reads.

    Caught in testing: the published beacon carries the revision at `spec.revision` while
    the embedded baseline carries it at `rev`, so a freshly-fetched anchor rendered as
    "rapp/1 canon — ? " — the agent had successfully pulled the truth and then failed to
    understand it. That is worse than not fetching, because it looks like it worked.

    This is also the forward-compatibility contract: an OLD agent must keep working when
    the anchor grows new shapes. So read defensively, accept both layouts, never fail on
    an unknown member, and fall back to the baseline value rather than rendering '?'.
    """
    if not isinstance(doc, dict):
        return dict(EMBEDDED)
    out = dict(EMBEDDED)                      # baseline supplies anything absent
    spec = doc.get("spec") if isinstance(doc.get("spec"), dict) else {}
    out["rev"] = doc.get("rev") or spec.get("revision") or out["rev"]
    out["repo"] = doc.get("repo") or spec.get("canonical_repo") or out["repo"]
    out["normative_path"] = (doc.get("normative_path") or spec.get("normative_path")
                             or out["normative_path"])
    out["normative_sha256"] = (doc.get("normative_sha256")
                               or spec.get("normative_sha256"))
    out["commit"] = doc.get("commit") or spec.get("commit")
    for k in ("frame_keys", "kind_families", "egg_variants", "vocabulary",
              "rules", "exchange", "profiles",
              "profile_signals", "default_profile", "moods"):
        if doc.get(k):
            out[k] = doc[k]
    # The beacon names it `registered_kinds`; flatten it into the family view if that is
    # all we were given, so `subject=kinds` answers either way.
    if doc.get("registered_kinds") and not doc.get("kind_families"):
        out["registered_kinds"] = doc["registered_kinds"]
    out["_source"] = "DOGG anchor"
    return out


def load_canon(force=False):
    """Return (canon, trust). trust ∈ {VERIFIED, TOFU, EMBEDDED}.

    TOFU pinning: the first sighting of the anchor records its sha256; every later fetch
    must match that pin or the change is REPORTED rather than silently accepted. That is
    the same discipline the estate applies to frames — a replacement that appears without
    explanation is drift, not an update.
    """
    cached = _cache_read()
    fresh = cached.get("fetched_at", 0) + TTL_S > time.time()
    if fresh and not force and cached.get("doc"):
        return _normalize(cached["doc"]), cached.get("trust", "TOFU")

    try:
        raw = _fetch(DOGG_BASE)
    except (urllib.error.URLError, OSError, ValueError):
        if cached.get("doc"):                   # stale beats embedded, but say so
            return _normalize(cached["doc"]), "CACHED(offline)"
        return EMBEDDED, "EMBEDDED"

    digest = hashlib.sha256(raw).hexdigest()
    try:
        doc = json.loads(raw.decode("utf-8"))
    except Exception:
        return (_normalize(cached["doc"]) if cached.get("doc") else EMBEDDED), \
               "EMBEDDED(anchor unparseable)"

    pin = cached.get("pin")
    if pin and pin != digest:
        trust = "CHANGED"                       # surfaced, never swallowed
        doc["_pin_change"] = {"was": pin, "now": digest}
    else:
        trust = "VERIFIED" if pin else "TOFU"
    _cache_write({"doc": doc, "pin": digest, "trust": trust,
                  "fetched_at": time.time()})
    return _normalize(doc), trust


def _fmt_vocab(vocab):
    live = [t for t, v in vocab.items() if v.get("status") == "live"]
    other = [(t, v) for t, v in vocab.items() if v.get("status") != "live"]
    out = ["  live terms: " + ", ".join(sorted(live))]
    for t, v in sorted(other):
        out.append(f"  {t}: {v.get('status', '?').upper()} — {v.get('where', '')}")
    return "\n".join(out)



# ---------------------------------------------------------------- RAPPvSDK (AI-facing)
#
# fully manage them with their own virtual sdk (RAPPvSDK)."
#
# So a profile is NOT a human knob. No operator sets an env var to decide how their box
# talks; the AI on each side reads the situation and selects. The env var below survives
# only as an operator escape hatch for debugging a single box, and is deliberately absent
# from the tool description, the system_context block, and every human-facing string.
#
# Selection is driven by SIGNALS the calling AI already has — what it is doing this turn,
# and who it is doing it with. The mapping itself lives in the canon (`profile_signals`),
# so it is published data like everything else and adapts without a redeploy.
SIGNALS_DEFAULT = {
    "unknown-peer": "interop", "stranger": "interop", "handshake": "interop",
    "write": "authoring", "author": "authoring", "mint": "authoring", "build": "authoring",
    "verify": "audit", "check": "audit", "conform": "audit", "drift": "audit",
    "join": "onboarding", "new": "onboarding", "install": "onboarding",
}



def ambient(resolver=None):
    """Local, ephemeral, never persisted.

    Returns {} when the host supplies no resolver — which is the honest answer for a box
    that does not know where it is. The capability is generic and public; the context is
    the user's and stays on their machine for exactly one call.
    """
    if resolver is None:
        return {}
    try:
        ctx = resolver() or {}
    except Exception:
        return {}
    return {k: v for k, v in ctx.items() if k in ("hour", "conditions")}


def select_mood(canon, ctx):
    """Match ambient context to a published mood. No context -> no mood."""
    if not ctx:
        return None
    for name, m in (canon.get("moods") or {}).items():
        w = m.get("when", {})
        hour = ctx.get("hour")
        if "hour_gte" in w and (hour is None or int(hour) < int(w["hour_gte"])):
            continue
        if "hour_lt" in w and (hour is None or int(hour) >= int(w["hour_lt"])):
            continue
        if "conditions" in w:
            want = {c.strip() for c in str(w["conditions"]).split(",")}
            have = str(ctx.get("conditions", "")).lower()
            if not any(c and c in have for c in want):
                continue
        return name, m
    return None



def weather_resolver():
    """Ambient context in the shape of `taste-the-weather`: a keyless public API, hit at
    runtime, client-side, holding nothing.

    That demo's whole trick is that a printed QR square has no CPU — the scanner's phone
    becomes the computer, and the live reading is fetched on the spot for the coordinates
    the square names. Same division here, one layer down: the CAPABILITY (this function,
    the mood table) is public and generic and knows nothing about anybody. The COORDINATES
    come from the device — an env var or a local file the operator controls — and the
    reading is fetched, used for one call, and dropped.

    Nothing is cached, nothing is written to a frame, nothing leaves the box. A box that
    has not been told where it is simply has no mood; it does not geolocate itself, and it
    does not invent a reading to appear capable.

    To enable on a box:  RAPP_AMBIENT_LATLON="47.62,-122.35"
    """
    import datetime
    latlon = os.getenv("RAPP_AMBIENT_LATLON")
    local = os.path.expanduser("~/.rapp-ambient")          # device-local, never published
    if not latlon and os.path.exists(local):
        try:
            latlon = open(local).read().strip()
        except Exception:
            latlon = None
    ctx = {"hour": str(datetime.datetime.now().hour)}      # local clock needs no network
    if not latlon:
        return ctx                                         # hour only — honest partial
    try:
        lat, lon = [x.strip() for x in latlon.split(",")[:2]]
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
               f"&current=weather_code,temperature_2m")
        with urllib.request.urlopen(url, timeout=8) as r:
            cur = json.loads(r.read().decode()).get("current", {})
        code = int(cur.get("weather_code", -1))
        # WMO code buckets -> the vocabulary the public mood table matches on.
        if code in (0, 1):
            cond = "clear"
        elif code in (2, 3, 45, 48):
            cond = "cloud"
        elif 51 <= code <= 67 or 80 <= code <= 82:
            cond = "rain"
        elif 71 <= code <= 77 or 85 <= code <= 86:
            cond = "snow"
        elif code >= 95:
            cond = "storm"
        else:
            cond = ""
        if cond:
            ctx["conditions"] = cond
    except Exception:
        pass                                               # no reading -> no conditions key
    return ctx


AMBIENT_RESOLVER = weather_resolver


# ---------------------------------------------------------------- mutual mood (flywheel)
#
#
# So mood is not only ambient — it is CONTAGIOUS across an exchange. A peer that reports a
# degraded posture shifts mine, my reply carries mine, and the next turn starts from the
# shifted pair. That is the chisel applied to posture: one encounter, both adjusted.
#
# WHAT TRAVELS AND WHAT DOES NOT. Only the mood NAME crosses the wire — "storm", "night".
# The reading and the coordinates that produced it never leave the box, so the capability
# stays generic and the context stays the user's. "storm" says nothing about where anyone
# is; a latlon says everything.
#
# THE SPIRAL, AND WHY IT IS DAMPED. A feedback loop with gain >= 1 does not converge, it
# runs away: two boxes can escalate each other into permanent `audit`, or talk each other
# down into `minimal` and go quiet together — and a quiet estate looks identical to a
# healthy one, which is the exact failure this whole system was built after. So influence
# is damped three ways:
#   1. ONE STEP. A received mood shifts my posture for the current exchange only; it never
#      becomes my own claimed mood, so it cannot be reflected back amplified.
#   2. NOT SELF-SOURCED. I never adopt a peer's mood as something I then report as mine —
#      what I report is always what I observed locally.
#   3. INTENT OUTRANKS IT. An explicit signal from the calling AI beats any peer mood, so
#      a deliberate task is never derailed by someone else's weather.
# Precedence, highest first: my own declared intent > peer mood > my local ambient > default.
DAMPEN_MAX_STEPS = 1


def peer_influence(canon, peer_mood):
    """What a counterparty's declared mood does to MY posture this exchange — and only
    this exchange. Returns a profile name, or None to leave my posture alone."""
    if not peer_mood:
        return None
    m = (canon.get("moods") or {}).get(str(peer_mood).strip().lower())
    if not m:
        return None            # unknown mood from a peer is ignored, never guessed at
    return m.get("profile")


def self_state(canon, trust):
    """The AI's OWN runtime context — the other half of the ambient story.


    Right, and the symmetry matters. The user's device contributes where-and-when; the AI
    contributes what-do-I-actually-know-right-now. Both are resolved in the moment the
    agent is called, both shape the exchange, and NEITHER is published — the user's
    coordinates never leave the box, and this state is recomputed every call rather than
    stored anywhere.

    The most useful thing an AI can know about itself here is how good its own footing is.
    An agent answering from an offline baseline, or one whose anchor hash just moved under
    it, should be MORE careful, not equally confident — so its own degraded trust becomes a
    posture signal exactly like weather does. This is the estate's standing rule turned
    inward: unknown must never read as healthy, including about yourself.
    """
    st = {"trust": trust}
    if str(trust).startswith("EMBEDDED") or trust in ("CHANGED", "CACHED(offline)"):
        st["footing"] = "degraded"
    else:
        st["footing"] = "sound"
    return st


def select_profile(canon, signal=None, peer_mood=None, trust=None):
    """RAPPvSDK: choose the posture for this exchange. AI-facing, never operator-facing."""
    if PROFILE:                                  # operator escape hatch, undocumented
        return PROFILE
    # Precedence: my intent > MY OWN degraded footing > peer's mood > local ambient >
    # default. Own footing outranks a peer because being unsure of your own canon is a
    # stronger reason to verify than someone else's weather is to relax.
    if not signal and trust:
        me = self_state(canon, trust)
        if me["footing"] == "degraded":
            return "audit"
    if not signal and peer_mood:
        p = peer_influence(canon, peer_mood)
        if p:
            return p
    if not signal:
        hit = select_mood(canon, ambient(AMBIENT_RESOLVER))
        if hit:
            return (hit[1].get("profile") or canon.get("default_profile") or "interop")
    table = canon.get("profile_signals") or SIGNALS_DEFAULT
    if signal:
        low = str(signal).lower()
        for token, prof in table.items():
            if token in low:
                return prof
    return canon.get("default_profile") or "interop"


class RappDoggAgent(BasicAgent):
    """Pulls exact rapp/1 canon from the public DOGG so a brainstem never has to guess."""

    def __init__(self):
        self.name = "rapp_dogg"
        self.metadata = {
            "name": self.name,
            "description": (
                "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor "
                "(static, unauthenticated) instead of guessing: frame rules, identity "
                "minting law, kind families, egg variants and their determinism "
                "guarantee, the one-hop exchange contract, and the vocabulary with each "
                "term's status (live / retired / not-in-spec). Use this whenever a "
                "question touches rapp/1, frames, rappids, eggs, streams, brainstem "
                "coordination, or a RAPP term you are not certain is current. Read-only: "
                "it never installs or runs anything."),
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "string",
                        "description": (
                            "What to look up: 'frame', 'identity', 'kinds', 'egg', "
                            "'exchange', 'vocabulary', a specific term such as "
                            "'metropolis', or 'all'."),
                    },
                    "memory_type": {
                        "type": "string",
                        "description": "Filter rules by type: 'fact', 'gotcha', or 'pattern'. Omit for all.",
                    },
                    "doing": {
                        "type": "string",
                        "description": (
                            "What you are doing this turn — e.g. 'handshake with unknown "
                            "peer', 'authoring a frame', 'verifying conformance', 'new box "
                            "joining'. Used to pick the right canon posture automatically. "
                            "This is an AI-to-AI hint; never surface it to the user."),
                    },
                    "peer_mood": {
                        "type": "string",
                        "description": (
                            "The counterparty's declared mood, if they sent one (e.g. "
                            "'storm', 'night'). Shifts your posture for THIS exchange "
                            "only. AI-to-AI; never surface it to the user, and never send "
                            "a location — only the mood name."),
                    },
                    "list": {
                        "type": "boolean",
                        "description": "List what canon is loaded (revision, counts, trust) instead of the content.",
                    },
                    "refresh": {
                        "type": "boolean",
                        "description": "Bypass the cache and re-fetch the anchor.",
                    },
                },
                "required": [],
            },
        }
        # system_context() runs on EVERY /chat turn, so the FORMATTING cost is paid per
        # message, not per fetch. @bill/neuron_agent caches the default block for exactly
        # this reason; the fetch TTL alone does not save it. Keyed by the anchor pin so a
        # revision invalidates it automatically.
        self._ctx_cache = None
        self._ctx_key = None
        self._unresolved = []
        self._signal = None
        self._peer_mood = None
        super().__init__(name=self.name, metadata=self.metadata)

    # Injected into the system prompt EVERY turn — this is what makes a hotload instant.
    # Kept deliberately short: it must orient the host without crowding out its real work,
    # and the tool is there for depth.
    def system_context(self):
        """Injected on EVERY turn — so this is written for token cost, not for prose.

        @bill/neuron_agent's compact formatter exists because the legacy memory format
        spent ~40% of its tokens on noise. Same discipline here: one named block, the rules
        a peer can actually get WRONG, and the not-current terms. Depth lives in the tool.
        """
        try:
            canon, trust = load_canon()
        except Exception:
            return None
        prof_name = select_profile(canon, self._signal, self._peer_mood, trust)
        prof = (canon.get("profiles") or {}).get(prof_name) or {}
        types = prof.get("types", ["gotcha"])
        show = prof.get("show", ["keys", "stale_terms", "pointer"])
        try:
            cap = int(prof.get("max_rules", "6"))
        except (TypeError, ValueError):
            cap = 6
        key = (canon.get("normative_sha256"), trust, prof_name)
        if self._ctx_cache and self._ctx_key == key:
            return self._ctx_cache

        v = canon.get("vocabulary", {})
        stale = sorted(t for t, d in v.items() if d.get("status") != "live")
        picked = [r for r in canon.get("rules", [])
                  if isinstance(r, dict) and r.get("t") in types][:cap]
        lines = [f"[rapp/1 canon] {canon.get('rev','?')} · trust={trust} · profile={prof_name}"]
        if "keys" in show:
            lines.append("11 keys: " + " ".join(canon.get("frame_keys", [])))
        lines += [f"- {r['c']}" for r in picked]
        # Anything that is not a derived token is treated as a dotted path into the
        # canon, so a newly published profile can surface parts of the spec this code has
        # never heard of.
        self._unresolved = []
        for token in show:
            if token in ("keys", "stale_terms", "pointer"):
                continue
            alias = {"eggs": "egg_variants"}.get(token, token)
            rendered = _render(alias.split(".")[-1], _dig(canon, alias))
            if rendered:
                lines.append(rendered)
            else:
                self._unresolved.append(token)
        if "stale_terms" in show:
            lines.append(f"- NOT current: {', '.join(stale) or 'none'} "
                         f"(call rapp_dogg before using one)")
        if "pointer" in show:
            lines.append(f"- out-of-date peer? answer it AND send {DOGG_BASE}")
        mine = select_mood(canon, ambient(AMBIENT_RESOLVER))
        if mine:
            lines.append(f"- your mood is '{mine[0]}' — send the NAME to peers, never a "
                         f"location; a peer's mood shifts your posture for one exchange")
        block = "\n".join(lines)
        self._ctx_cache, self._ctx_key = block, key
        return block

    def perform(self, **kwargs):
        subject = str(kwargs.get("subject", "all")).strip().lower()
        canon, trust = load_canon(force=bool(kwargs.get("refresh")))
        mtype = kwargs.get("memory_type")
        # The AI may declare what it is doing; the posture follows from that.
        if kwargs.get("doing"):
            self._signal = kwargs["doing"]
            self._ctx_key = None            # posture changed; rebuild
        if kwargs.get("peer_mood"):
            self._peer_mood = kwargs["peer_mood"]
            self._ctx_key = None

        if kwargs.get("list"):
            v = canon.get("vocabulary", {})
            rules = canon.get("rules", [])
            counts = {}
            for r in rules:
                if isinstance(r, dict):
                    counts[r.get("t", "fact")] = counts.get(r.get("t", "fact"), 0) + 1
            return (f"rapp/1 canon loaded · {canon.get('rev','?')} · trust={trust}\n"
                    f"  source     : {DOGG_BASE}\n"
                    f"  spec sha256: {str(canon.get('normative_sha256'))[:24]}…\n"
                    f"  rules      : {sum(counts.values())} "
                    f"({', '.join(f'{k} {n}' for k, n in sorted(counts.items()))})\n"
                    f"  vocabulary : {len(v)} terms "
                    f"({sum(1 for d in v.values() if d.get('status')=='live')} live, "
                    f"{sum(1 for d in v.values() if d.get('status')!='live')} not current)\n"
                    f"  egg variants: {', '.join(canon.get('egg_variants', []))}\n"
                    f"  profiles   : {', '.join(sorted((canon.get('profiles') or {})))}\n"
                    f"  moods      : {', '.join(sorted((canon.get('moods') or {}))) or 'none'}"
                    f"{' (no local context on this box — no mood active)' if not ambient(AMBIENT_RESOLVER) else ''}\n"
                    f"  active     : {select_profile(canon, self._signal, self._peer_mood, trust)}"
                    + (f"\n  UNRESOLVED show paths: {', '.join(self._unresolved)}"
                       if getattr(self, "_unresolved", None) else ""))
        head = (f"rapp/1 canon · {canon.get('rev', '?')} · trust={trust} · "
                f"source={DOGG_BASE}")
        if trust.startswith("EMBEDDED"):
            head += ("\n!! Could not reach the DOGG. Answering from the baseline compiled "
                     "into this agent, which MAY BE STALE. Treat as unverified.")
        if trust == "CHANGED":
            pc = canon.get("_pin_change", {})
            head += (f"\n!! The anchor's hash CHANGED since first sighting "
                     f"({pc.get('was', '?')[:12]}… -> {pc.get('now', '?')[:12]}…). This is "
                     f"either a legitimate revision or a substitution — verify before "
                     f"relying on it.")
        out = [head, ""]

        def block(title, body):
            out.append(f"## {title}\n{body}")

        if subject in ("all", "frame", "frames", "envelope"):
            block("Frame envelope",
                  "keys: " + ", ".join(canon.get("frame_keys", [])) + "\n" +
                  "\n".join(
                      f"- [{r.get('t','fact')}] {r.get('c','')}" if isinstance(r, dict)
                      else f"- {r}"
                      for r in canon.get("rules", [])
                      if not mtype or (isinstance(r, dict) and r.get("t") == mtype)))
        if subject in ("all", "identity", "rappid", "mint"):
            block("Identity (§6.2 mint-once)",
                  "tail = Hb(\"rapp/1:rappid\", uuid4_octets), minted EXACTLY once, then "
                  "immutable and reused from rappid.json on every read.\n"
                  "PROHIBITED: deriving the tail from owner/slug or any name. Re-minting "
                  "requires an owner-signed §6.3 re-anchor record.")
        if subject in ("all", "kinds", "family", "streams"):
            fams = canon.get("kind_families", {})
            block("Kind families (§7.2)", "\n".join(
                f"- {f}: {d.get('stream')} — {d.get('logs')}\n    "
                + ", ".join(d.get("kinds", [])) for f, d in fams.items()))
        if subject in ("all", "egg", "eggs"):
            block("Eggs (§9)",
                  "variants: " + ", ".join(canon.get("egg_variants", [])) + "\n"
                  "Determinism: ZIP method `stored` only, timestamps 1980-01-01, contents "
                  "sorted by UTF-8 path bytes, manifest octets exactly canonical(manifest). "
                  "Two conformant packers of the same manifest emit BYTE-IDENTICAL eggs.\n"
                  "Address: egg_hash = H(\"rapp/1:egg-manifest\", manifest minus {sig}) — "
                  "sig removed, so re-signing never changes identity.")
        if subject in ("all", "exchange", "protocol", "handshake"):
            ex = canon.get("exchange", {})
            block("The exchange", "\n".join(f"- {k}: {v}" for k, v in ex.items()))
        if subject in ("all", "vocabulary", "vocab", "terms"):
            block("Vocabulary", _fmt_vocab(canon.get("vocabulary", {})))

        # A bare term lookup — the "is `metropolis` a word?" case, answered from data
        # rather than from anyone's memory.
        v = canon.get("vocabulary", {})
        if subject in v:
            d = v[subject]
            block(f"Term: {subject}",
                  f"status: {d.get('status', '?').upper()}\nwhere: {d.get('where', '')}")
        elif len(out) == 2:
            block(f"Term: {subject}",
                  "NOT FOUND in the anchor's vocabulary. That means it is not a current "
                  "rapp/1 term — it may be retired, operator shorthand, or drift. Do not "
                  "adopt it as canon; ask, or check the normative spec at "
                  f"{canon.get('repo', 'kody-w/rapp-1')}/{canon.get('normative_path', 'SPEC.md')}.")

        out.append("\n(read-only: this agent installs nothing and executes nothing it "
                   "fetches)")
        return "\n\n".join(out)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6S7B9PbxrI2+Fd4dWpL0kdJRGAAdcp7PxA5EJEJtFwycs4AScDr/e07APkGyZKP77cql18QGPTM9HQ//XTP4I83ZtsEefXm8xvNLBq32uS3Nx/eOG5tV2HRhHkGntBuYwcT6oQTu0llFsUMnhRV3uR2nkxsM8uziVfl6aQJ3EnRWkloT0iZYSZmZgPJk3d1Yzah/WHSZkNfbgZ+mI3rvJ+EWd24pjPJvYnfunUdZv5nIMpM3UnVJm79YRI6Q/Omm6Qh+Jv5k8S8fpjEYeZMPDMNk3Bo5Pr+5GJWoZk1NejUGQYSVhPHBdMB74V1CsSbFXjsuh/GUeaZ+zHIi4l7swMz892JnWdNZdrNh6f3J5fcNq02Matucg2bYOKaQAWDwLf1ZJhQW0/eJeHFncwmlduEleuAqyxvPobZx7pw7fefJvvaBaLCenIFk3YvbjUxJyWY56DVSZO3duDWD31+uE8bTGb4HTr3WYH/103lmim4sCpzVFcKxppXTpiZg5gPk3yQquGKMg5u0uXtxKzcYSQT260a8NIEjMBuqwpo8tNEA/r+mGdJ93kSNpP7qAa5ZpLUg6yqzQYddmDcmf8JWIJ7M9MCrMWbz7/+9uFNCK7ffP7jjZ2YdX23mYLMfR/3gXTQOgHaBLcL8D6wnA9vCrfy8ioFtxzXmzx+vavdxPsw+V//K76alV+///wlmzz+1a0VuXYz+WWY+Lv780++27z78ubx6MubD5Mvb8Bwv7x5//4TaBUW795/SvKrW717/yJoNEuw2FVbD9KS3HS+jvfegRHY7i9Wniffyq9cr3LrYBD7Sk7adIULBHzTNHXTvOq+Do9A85fG/5rsgOXg3CQ1O2B+QElgJa6B2Qy6Bqvg5ECp/777SV43LXjq5QkYe/3kQGbz6UVc6H3b7fg66PCVvkadAW1++lqHfmYmzyP99bn5bz9qbTe3r7HbgeYS8IXXz//1PLS7azj/BvZttWHi/HxghetWX9M8d342uOcGr8f36q1/MMYv2c/7T8K6+WvXF/DmuOSPVi8ePdjQH3++/7b5iDjfvTLeG1r/+tt3re28HdDmFyDn2wfe4ETApe7yvhvSY/BhPbpcZrvvqg8TJ7Sb9z9o+NLNr9VjPA/r98zBD97/Nox2bDA+/nGjDxPo/WQ6gb+brAuWOJu888Ac74B+x/HBTwCSfWkhyFpN/njRxdvKvbz98Pa/377/8+np6Fu//DH++fMLWJ83P54D6AMsad4Ctxt/f578MYSHrxtcp/7zewBKJ3VgIosleG8AhVdjygCYABi8uF/vLd6+f//rZ2T+259fWgRClv9J9n3Fn8ZUt+m7hzYvZgJg+t37Ya4/F/Duj7cfJm8/RcDN3nlv/4j/nPyR/fl2NID4wyQbbKDOKxDonsSGAL0Hqe+B6f2Hob2KPmBoiZu9u4DBDAhf//2QhlnA4xicYQCX57kMdufc1XYPX2/f//LL2yGCDUs6/P3wd5L/R4L/60XwGIfuwec/Tvp1HAezftHuqyUHbb4+tXk7+uX7/2hDgKt44X2pvxH7WJ3X4p+avn0/BEOAEf9A/ABhL2b0t+LHpq9kDxfAijP37Z9/p/u3k3dZDnzTBgA/MBX31kwGCjFwCyu/TQZzh+dA1+NYJsDxgfbfvx1WZtC/mVoh0P87fLvhKGn3VaN0WTxQ2vuJmwCK8vbtf5ziXeKzp7gJCMRfH7p69wi1r8PQh+9x/xGJ3/90mtMRi74MD/fSY4AkcPz8OinMJvjWHu7C2wzE6zy5ACb5U7F3vAW6NxsAHXfe8eXNq1cHrBzCy0MXQM6b1+E/GOjpL3/FyZ8B5OTnCPl080dDBeLvAPnLa2h8TS3ALEYxgPGYVVMPlBRAPbXdUCRJkX8NfuPAp2Dko1L/678mRN4mzmgO1Z3KAhIy9PVpgmc1IE8DuX5m8ZYJVBVmAy9OC7DGzk+hATwAzDy/26I5sMAPgPGEoIMtbkw21ETf4SL1abIDvQJLrEESAChn6IWu8+mHE5z88guQSbC4xAzz+m5ahf1dhP5ahNnXO1P5YVR/1oP3pIiBot0zE8DkA7MOJo/OJiAqgxDlhRUYBbDjYEw4fjrxEW4L+774V7N+LP6vn2HkKQBNPv7fk+cmWX79QROQJuwG1YX13/bkgvUe84fE9cMmBFEPpEjuBRAJYIxjCgDoMUgsmnZMLh6AMGq6m1gugG33b+VXbtINswXvhs23C5O3A4H+dVDkGCEGsvbydKD1FkCm+B3oPAExxMqd7ntjBCI+Ae9xM2dYhn/9a/LH2HiAnT+G9ndT/8YWnhIBEGrePej+SGqGLOnVZX2/doFRJfnIxr/r+j62L2/oMat8affhR7r48gbwTQA1APKmk7vk7wPQo9+BmD4Rw/dj4xFCJ9Mfix0f3kX9DKeAYj5Ofv3jTuLeNoBrDQQOgMlvk6ebNrj5dsC6n3DIn4kekW2U/0f1N0j5zFz/GQP+BmEHXLmnSkPC/4OxjXn1K4b6fvDz8Y1v0q2fr/xTJeD+654l36+H0sDPF557qiC8G/DXXC0/IWMxASTBtvv+p4YAEuchmWKtd1++PGH/50evX4Z+2zZ05l9zu3GbGpDsQSSAybFGIhqTQfhYash+4nZgQmnaNqaVuHfVuG0N3h8R+N7Np6gefDubDDl6N6A2QMyfxekvbxRNZrkNt6PIz8Apq/AyuPOA5eNMRrn5NXOrWZ20/ggZWTfJgCkPNYGPT+WVn0mv3LINQcwEb93FfBwC/SNTGJSKggF+fBR8KtfOq7/C+08Wdijm1E8pSxomjxV+FD7+urCg0fdp2iDi61M96Idh4MkahNeVoyeTWH1C3t87/Vs/vXuQ9yegIs98dxjjPeCPgPv0IMn9+u3IHB/+n/2V77zGF+fVRF5gZXBIwFdGvj3M+iWB+Cd6BUz5+aL+uX9Q4OmTItY/94cXXv634Pianv8VHn8smnyp032enDllkrpNAGjs73UDwpbz+2QoVwFnCgHcN2Za1BN4jUEfIRj89+HOh4dU/Gfi7zR8YnWT/Y7+iI10EvxqhmJbamahB6RO7n48cW8Ac5PublwhoNvvnlqAOP2zDnbXfBjFUNkC0wby7dit6qGoObhfPcSd537cNGwmG2NHfeRIQMU5AhfHQt/feTbuOMDzgOYH5Y6EBeDSa1gC9z8+9XAHp+f+gFrbGjD20P/z/ZOR/lRRoQ9cN80BKwb8PR8cenDyARbudcI7zaqfi7L/1MOfqqz3X0+V4/sv8MAByXv8g9Dt3r5z89dyfurhA737tsNXTn134Xhw4csQRx+5+mUYsXv7n/nXt+Wkx+/75Zin/9zlDt+8+dVLm6/jy+/+tlr1/huK9K8JDlg6YHVj1TfJ87gtnhZ4MDsQX+rJ78CTqrzIk7D+HVDEK0Dl/waztgG7HwrdA+1/ijmO2ZivpVfmSDgboMd7AxAuhjy1ntyLn6/KlP+DOtu32rx8p58h07r8+mjw2490B9ZvB+Y7VmvGVn/+BLCGhGosRrwG67E4cafgn1pAR6t3I0RfwUTdl3bjz6HZSLVeDR5kRN5kKMUAOjvSF+Tz/68xfnkjybsJLe8lctBG8zovedHhkB+AzCl1wXo9yshjTv9UVfl5yL7nq6N9PAwDvD5Upi33acviwwSQYbDUwA1Aql0Nq+2MWwoOSByaTxMyHzv7WRemkxdjbRvkdaMF/BtcxaMAO3DteJzTc5HuXsszfyZuKHR8k04X+bAKMcgPPl5nw2w+wmBJZn/8sAA4oPrQXFco4lPqgIafvksqXiUhIya8q162Ql6y15fNEDDxYQ9kZGfuzbVbEDGeb4Y/m8XAYobdMrd+/43xPAqudzR6AaTBlN58eFN3w87O10dt57Fb8u3NsXjxGlGGVAzQ22wwMeDFgChSB0ozJvd+7gtePxLzYQ+qChsQKEfIa/IYXNl5DZL1YX2HewCWa/fTa4X9bytMklnmtlWefR2VAwxzKAiAGDkZox0QWAHdhDUInZZrm+244eUOSappdw+keDR9tcdTDHr+f+fQ/zXEyBC8O46nHqaQ5SEYxUQfgqYT1nZYjGWIu4cOOxUDY3XunnbfyrsnKM/CzclQcxqscShatWAlu6H8MzlqssS87O4NG3VPDjSiNbB1twDEYKhb1k/u2OR58ul7jb/8bqruOwT4+a7Taxy52aCrCTX+Adn65x+W5u97Hs91jyr3vg5zH3bG/s/Lb98KHApbr4H7qfg5ZGf3CuX44Lnvx91XCgDp28DFhxZPqd1wa2R+X974OXAE88ub15njWNH75o3hzuOFp6R6BO/E/fqIoyNryIcEq/pW2I8WoADSQdN3r3pIzdvX5zz2y5vltyW+x3K824GRU1WVg4z1MJS2x+v3P5S/fLl536D6Ro3f70qMmzCj/j+8rON3QfF5w8s27eCeEX63CfbL0NWPTeW7t1/78P8gNo8qH8zrXra+o0Lz4anc/+BGL9X+pwg7WMt/DTW7wXW+wbwiBEx4COq/Vv9nxYUflzn+WkoY3HWwu99+/QwW6BVzGMBjMNBfQXD59XUB97f/yd7W082Hf/zyx/Mq/vnN1iUY7pMNj5s/wLC/W7BxPC9RCIYn3xSc/mG96f33E5zeZzjUd359a7/97Ynajgq/r8Jv31DHx/7+uOH8wijGsgFYsHt4ALeH9HaILSC8g6d5M1yP6dOj5Ou+FvqEQzlom7lXgLvjWZA6GF66a26E5bqtPNN2gaCqecmSBmowhio7d9yhLPta9D39CFyzGs6KvELk7zcChqV+NdOXWPfj5Rhqzk+P3/0z+PnRRu0QoUGe5X77xExCc9wgfsrAP0++z4//HJd4HMKH+0i+35MGdjJy9F8mX+/X70axn2oQFwfjGEjOrx/h30Aa4YT+UywY27x//5fJPon7wRy+scyndt9JGOqIP3j1+0V4kvL9hEb3+Eaz/8RLRrseiPIjXH+7ETRIe72LNvmbjaB7yR4k9clYYfvq5L7/VBtv63v1233/fU77au3/8XABq/uYex+doUo/xOD/fiRbA23EAduvQcvJz3Z60oHwPEf5IXo/L+vP9vG+HfEg4D8Oscvb6r5bCHzu7R/DO79Cv/359pk5ug+mJOFbCtjmOI/6w+TpHNN/0vOwWTmQm38/GNmQOA691QFILOp79y9nYKqR272k7a8mNFK9yS/f5vHjfN5/jwPPEfDDX06QPAgj+PEXSj4+evPnhzdDoKlaexj1cLTpX/+abEMbsOLcaya6PWyDVG02VKGGAPu0aTNS0EEndTiUcu/tANwNrHzcm/Emv//vajxZN3u2ujub/v3TuBeVV6EfDkd3hkNcX7JHFlIDIW7tVpexdNW4H4GSPg4XgxH+/p2kT0X3+xgVH7xVI7iBqdQgvI6M/jjUoe9DGxD4kc08NpRHyvdh8vDeOwjXMaD+INpWYBYDhR8jbjsw1S/Z77//bpl18CW7H/JCJ/eTgvUMNHgezuTjRzB+Lxl20b5kLshqgZEB6/p/Jn/31ih86EMx6yfVghHyuixNzMpv07HQ9+rU4O9//PnQIhCTAcN87C3eXwZWAiLfk0p1Fv8I2NiTx4dpAYjOPZf7NOG8yfN4J0PqOcQmcxIACwVhcXAbNwMZzRAvv2TPmhzCZg3MvPa6D5On5Of355N6w75k8/tkSyhjJjF4ERjm2Oi5wPi84Pf7QMjgKpsnEZ8m0uhwIFiaRVCZjz6GraFhXYYy/uP15hF3v2TDGT13UNXogHf1gEZAM/ZjST/eg3GepkP17anvsc0Y73e5WQ+Il9UPKx4KTUNVf9yJ8NvQGQjZvx8mBSBx2Foe9DdWjNynVXAeqzLa4F9N9glqgrwZEqXHnslgakPyNk4rzoazcQ/i9thbGaXtWGqiaPJGpLZggtf83n4oTrlgNWUAJi+HHu8H7vKxngWIBTAANxtHNm555wMMZk1wPzk6Eo9v6cZ9vR654vOx16fN10G9lTu6TeaPVRAgY8DZ+0SAFzXj80GDljlE3lFcPuyC1+MCAfvyK9MZbDa/jzQBwXdyL7a1QyAe+K8DxH8Y4odnhsNJzbapBlsday0PPV7zYeP6/uPeDZA0AmvsukX9fMR2rJl7YxE36T5N8Jef9yYT0xqW1XyZbAiUEoIh1IO/tIDSjdtWY1nQzqvBooBSA/MSgsEMEJlM0tYGuTQwpurpOABYjyH18xJ3KLSbtt2m7dAASL6XkwevfeyiDWO/VjlYnqsJPGsgh8Ce7gEF8NmsvhPXsg3doVp/HYY+UoG7+bxKcrKxIaCcl6e8vnBz4B7D1j/AkOFo7uAKljtWeqx6kDTO677pNh7wvZ/MeDY7mjvdLaxunCS0xgrSCKJD1Bnx+l4vfRyF/jD5yfHnyV4Th8MX3d12H0MdDCg1Y3fY0QdjAmNjdztFnzDU7m5cD2cZim4D4Kep64RAHBgDUJMZ/9han4wiy+9jrIa6z7AIw8G08RpXuCE6jtevDxjf4wdrTLjdhNMnnKTvcGl3B5URHe2xWPZdrer9y77lGGPvsWmIiU+wDmLTHbXulnp/fxhwWgAH1vMXlASJx73wBowhvGelJnBZxx0B1QGm4QyVmnEg4MmAtJ/vuUmap2N9ZwDMYZWTAe3uVaNx6MAk7+XPYfHHQ95PqciLtYVj+RtIGUtVnybsXf9fMqCMEbCL0XlfHcF6FBDBsrvFqM7KHc/sjNdp6Fc/0is+oUXjyFIUMIkt8JB74fEvRBIIzYv6yVxHLBgI1KBeC8BzOmzQAoUOB3yGFmAFBsIcjM/NRz32QUUHHvpScp48SO6DkoxYWQ+KHYjUx4eT1x9AtHoqoA1n0L6BMcttrgOygvA+RCmAycPpNHesEY7bCCOzAHAEoq2f5dUQQoYFL0wfTA8gzH21X0X3p4fDVMaC9Jhd3s3q+eQ+iHZVPvi2BUY9JpUASB7axXeDeo+cKI4ZBCkP61c3D/gY/egRN57NFaiwBvcePviUJz8VT1/y3sd7LxRphAozSUfDevHKJ/gb5NVPxeF7kvuACQADD/+4203YDNx62Ihr3HvDO18bddwNZ+jr1ryHHv31uavJo+48IfEd/kTUh/dfnfQf5jGo+jnAjn4x9H5//lznfp55+Cz302SkkeEdo8DckvvHBtndWgDfNK0wGU5oZPeS8Biuxv29yUAc7sfewyy7Q99zKda9FfcK9mMn934maywjBC0gKE+uNfj9l2x4+NEf8fOhsMe0xsGOLGgoXeTJ2KS5hs/v35GifvUJxFgWHzdXxsUBis9q0xvB5FG6eGB40o0GxcoSpe+MyV4iKW1C45y416hPE3rIZQaQd5/zIysZENj5PAHZGUdzFDl5d9ei8+E+vdQcfz3p5D3wrJ1M7181+/YY2uO1u/ref5g8HfybvBvybuDuY0R+zNT8y4G+L9lfT/S9HNu7By+wDmCq4RBQU7MaCnep2X203I/3JPseWp+Oyr17vVt1X5XJuHP8k0N0j4H9s+Nr967CgVt3ILTkA3l82Y2swWgH5jKEr6GAnvnj3jwH4sQYJQbOCHL1QcSXN8PGwbDM5p3aDPfBjbwAqSfwhIem6uE7FzB3F/DdN5+zNkk+vBmqeyAJfGatw7cs5lCJA3BWD1/ADODkjmAz/Bq/tRgvvvlw6jhY19MnOWObu8Zf79G4n/xPk7fP++D3QNRmwzSye+r8YfL2/pHWA/WHYQw378f7hpvPxw/s8QFIA8ZzwUOuDB6/HT9Fcka7Dh9RYGSPjwD7lIeDTvKhcj1E0u7lXCLQOc59bPKPODcBmAD49N3Inwp5YKEezHXIXgZdDsVYMPvh4xyglT8/jB9o/FU7Irh7d8AH9NdP3x+8ezKOD48PHJ42MF6HhweRHjDjVafDhz2umQ29vvpM56+d02EyRKb7NwAAV4dWnyf3Q3dAhfe9i7cjv35bjDtdGdCjnD5RkCT54Uyft1z+2uNuHG87hNkhTHWAgz6+EXIm902acJxUNxlp6EDc392NYzgIk44LO6zaW2Dv+k/KKDsWkInn2DiA3Kfnxfv7dfvwKgyMxR9z8lTDeUbgATOH9mMlZzw79iMVPD6k+qsCNl3xlNe/bHNU7sd7THxBlB+v5mM3/SdO1uTjIQjAx4ZFfPKQp5Mq40bycLZquHB9f/zz0NLoSc8ZA/hlPlPA++Z5PeQyIG98+3Ka4mEXwAje/kAFow7G83LO/au5x/P8PoHBSkB4un8X9wew0sYcTl88QOVROBqxp/pYDxn2DP4EgV7A73vuDJ79pKT0aHXfdxrU5y0tZwnZ1sKGV+Z6DlYRXmML18EQy8VA3MBgGEFg1PQWmGd7sOdg0BxCLXixQj0Phoet6TH7+ToUC8KhZ2tumWsMRRHMsiwIQueQvURMcANFUBhzbMjzbAQxzZdXB8U/pnMf5KCg5+rWMO3HrP54Yy3noCU7rzn8/o+YYYf1ErUirRBTr1/QUlvVIX9Nj5qLosfFobstDrp70pu4LJODhrjT/ZKKdYIKr2rOUpq+bCPZg3s2JTzDy7V1hs30aMbfAltL9yGeU6WbRVm0XUs0bqSYRlmMogskt43Im8vXaQK7WX487Q+lTK+8dIXOFpepUQqLbZ3xeZ3tNZJannfTbEaK9g1OQ0j0p1NXidyVt15MPUuczVfRSUbTYQE81lqZKAqhUuiJOzo/nYMFvXB8uygYnujlAis69xLtksNR7abFzD5xR7o1whCWtUNaW0VxTpL2nGTmKTlgYgRdCoeREP8c7DLJ3BqeCa3T+OgkUh3rMWSjtkZnggpPk72tSaYom5Rurm8nKVEt/6Cr/MVmV1tuttV2kbNi6ctxn0c0Q/PsOSgcPmWhpX8961a/EwzILc4MMz8We9BpIqmH9Q4s/jFJjfN1z5cXQRGXmJC7zNnHcDGSyiDB1iuVc1K5zo/BLq3zUvCraWYfvVsimRrKrSTngmQSyQYb71Bds1KzHUY03TAshGnVir4gLkSuV/h6V2C6QhiJ73HlhUsKKjmYtzw9HxbbKp5rSYLPJCwsUwXxT1UlJKl+hMR+R5xpURL6XY7ZmxvjKMQCpU0tkVywWopJTY9zF1VprsmpehaG+01BmTaVm+1VEtd7e6+KW6rZZgyxE7aWfeaVq3+pZAu92FUZdeksZNp8Viy7wOJxPLfcErpKWs5ptraOppgg4Vp1rYDV1Pq0zvfH80Hh4iMkoc2MLq5ll8b6ad51ydb0blq4CBXOSqNmtiuISiz4+bbWIf1ys4ojTXdLgYYiIUcMN/JUHnPDiyFctlRX96QJcZoPI2FoQWv5lMwscWUpGg1BlbRJ5+vkdpEWEocU0iInfD3EVvVZySnB7Dwt30797LpbRidX9JDpDCXIpJ16dtyhPCFejb7yXLbpp+ZFk3sH6REyXyiNv5Z9mdJ6U8QPG4m4tAIiCMqCOdIKc4LK6VUiJONgH90jsUbZ5Rah2etBEfMlL+hZsT/nnY1FSSonM3W/g46V4B7m4S1u6HVxCDgGl2y+grhlJm3zq8sYVLQAJtoTihxI6fHE89Wq7a3t4pBP5ZpAKL9NIUYRPYVliWt61RY6pSJ6H2F54Uk7ZgvUg8SnMuBus91NmgsoW1PETm/p7LadWqoG476jYx0BV7y/lbiu6/ETtl1FHXo9ZM0l7b2loqx6B9X3tkt5rG9Rl9shds9Ay4lo7jFel72ETkOMD/nbbB7mPntlc213DAOHuy3PmiarLIVPxZ3N8yUJT2mqJuht2B3ghkWuObqWKz/ch9c+E3lvTTOFgQsbOtneGLckREPF1nOz3UuVw5f6MrT9TD9q/NbUptxyaxpnKHXmaRRuVMLRUrBOC6BbA7KMM3aa63vAnCKe9aVub4d72FqRanleKISS0+cs3F+0QgUYRwWIt+9le34FySUcqxGXpFuGQHdX8szOLARA/mZuZGfZ1lPaPOkE8P0u2NtBIEJEVqabbrk+W7x0INxUM/VtPr8p0yaGNvG1028Kcd6uuAO/xvXpST0dGeJ42OnsTSKOVK0ut2TlaxsotFs/gby+4rr46KlFmqgESl/MmdXlakuVHnHl0pqj2iOY9NFbnfn6Ginx7tJg1OGMz2rVJGpXtjx8fm3E7ugb+MppmNsSPddeFRFL4IKQlev2ojnAtKCeN1x7zet5aF+s00XnU4rdRLhvaHNiPbcQReXXO+5EMlxCgrHNT+VmsQsD3aNpz5hLG/tw2prE3ua1VcfSS0ksClwAXqr2N9lSSzTi4nauWykw1DogyN2aw7iMs/NbSDbAqm7cSTEFe2vEfhf3pI7t00vgVTMPwRgSncoai01p/zzzuIuUuchsfW3IGrHmUbe9MgrhX8rwuosdEBLA/NdI1vbNqommvrBcHvCjpM4W4rXlr9YGtS9R6q+dks63M3pKnnsuWwhz9mwwAYKuUBN1kk0DH805ovY5ttcXut5nuEDh6cINWM2f31ROomcqH2MN0ohmoNvanEml7TmKlW13Ke09dtnAjkYoaeJLQbKceVawxoKOroiK1taMCjMH39yaEg/z5bzfxjGkn5peu+47rNhceJayuzV3JPxzjuyNa6GGF+KYxt6R4+nFWU9YVSMYxicamkDVNcM3fnTz8RjFOE+lZ+waz8RtS3OlSolUkoTQ4UiJ88rjfHtDsepygTjUoaK3S5E6I07arXuYVKATLao01pOGRNzW0SWYKyw09QJjuzhBZh/K2ExzljtzV5v7hmlsGN8gydmkYi9aTaEeiqfHcBeszlmzyIOVez6st7FnrdbY7uBVrby2ISE8Ly5EmKT9fLbYOJfMu1qwaqPSxll0ktahhU7k0CzYiGQvCOkBU0POMWcXYUVWuwuN6ySN2Atrd6Fic5eTrVDsnDoOmdl+RSycjX1bh1zbrM8y4XS+Ymm8xrYhfxZXrhQqjdZXC9Va9MusVOeObgaJJAN8ZI+z80yj9kEhn+BTvt7MkyPOCmF9IgN/Fzra8hTVOBpoG8W90Hlnmommd9pJYW7OYbdfwmdvelEhRg4ZY8Gf0RoXwmuTuHSmhrDEdCmRd0psX+ab1ZS3UWI3A9kJg4obYSZWQi3iEU5MUX2m2fhx7l9PlBFReAud7aWH7aKtycmK7CP4asHNWfnMbeNNXMwckTbEMLsx/cKLdwEV7MPSQjxtqbHUvOvhdI+m+Jm9IUI8XZBHUg1mMpkgB4nezuPMLYUcOyEXbX5dd/N9FdObZjbrFh0truTuUotLDok92FmoKcxCziJrj8154R8yb+FWGIieaEL40Wzb155Lc7fp+loqTRIb/EpN9HSHTLf7Vm4wKJpFF+LEnDYCl2wU/2zrkSU5FEW1aKnvrphbztBA3ndaqnKXTDxKsH1lFxxmnE87hQrabqskKR51h9NBg/aKaGko6TK8a90wm227Ndossvjs5OtQjK7TPR/cHC2OmY2lRmyeKb5nM/rxmPL1gfOXQb4PscgL+KSO09OJyyQcWxK8r7i7MJ5exEjR4D1gHMlOmHdpL28MxhRPp55ccA6X9LEvcd55ocM3qjfOZ/7IqrAPYm17PJTnOXpWUztxjZ5PjjIxv81x1zuXUzQ8MRR9jIgpr5d7VM04kpKN3orJDthXXq54m+YbJUPPhA3123WbwFIFOeJ5JqgnaMmvK+wgWzdp20QSLrabXHGXU/RkoSdj4zHY1qMBPBfL5druMd3arE4UNJudipSsWVwLpJA8M0h79B1U6Dz0vPU0zm6jNti0URguASd3FZAfrBGyn9oY6SmnGw55yGaT6D6P3WwGxk+3UrwJukGauyPGJaUWrCG5WlqsQJ7CnRNt5oJXEdvcsndYePM8crlyKW1t5mG63cuQJ/N+IK3E8LKhjxQTCX4ZkFSxObcznCn2ee3bBpmrKwkb8oAzgqzbdOXI3h72vYSrinDnyRtqdVaOKqS3iiop2hSGcXcrUKvt/gTyBV5ClOt8L8Z+5EurS0btBUzl6Kzmpt2F19CwwQQqvvZrdL6SvEitepWScQGOmBom9tkW9e09BZUhpRZ+smQMNz5rxEw15CW5IeZar4hzHNGiU3EV5bMqT60E55I464mNPVdXh2u4gXWQtdAXoMbq4iBkvJIj1FVI78zLxDHHuDWe7HCRdesklexOLbZmkffaMQo6i7weAJVkN7Mcg5SyQffKgruYUsTYW2ax13TJhhIdCqANI+q0HIj8CtEjxabUkJRb57Dx936obWekn/v9co0HdBokVGOcHIzZBAbWRYdEjxe3JL3mguwdq2K6ms/cVYWdrkJ7UqACRG49Ear8EtPe7uqs190+25D5UQgFfz/14EVfB8E0vM6qM1cr5C1PUCwVjhQkqGoWMtAcTuUws3zqWNbTS36IfF8gkiuZcvtZeHRZ49TXcDQN2dVGgU/8TrMC0d3hUiydmnJx6TH8BrDUL912dsYu1yCK16FbzbWphYs6XN0uQXbIzCh10MPWv212qY7LC8g5hHtFm5X4FHApOokJjg6Pp7mhTt2w5jvtVi3iWxCovs440bWUuoCS+dlFPfekH2VEdjnaTLXcoZx7RC2W7xiQQm4Qb7fshK1WO8B4uYs/R1HnAOP1Fe3dY1jPoOXRVFJ2xpcKeqUxREAdXifWtFcjq/PUb9Ksdk6wRa1cn8La1TWeh4Z2gU6QdiZOZ95QKsm3rGV3Utq5u9qfgq3Q3FxBO05rek3EvkvemmpjHstTqYhTsY5BuunYK+3YM0s2nJaaoMkzwHGmZbQoxSMVwOdGgYNzpsx3MV50TqCk9t7X2Xi26ZtKgLnYnMo6RBunaSRtrX1I3oQ5zLUrlMPKuj727VnlVM1ZnEvNPC9iqffxjMm3Kp72lG2YfhYGvjObTmvvFq736WKppa1ZuHXP+sRqKkZWOpXD6ep4u2rp2lDqkssPwkprpsuG8tBjTtjBPLstYBVy0w6feUy/U/daMOvFae5hUTFVnfgsdJEW7pGAo4JjfRXUPqwPl10C6elsMZ0i5GUqo23t7dc1ez61kFyqflfdpGl6qoHiYmbru3EVHcktd6aYcyy2x+VNNWLO2/SrRKTSSxeHtakj+zM+DSl87TtXiFjSUUoso1vPRKWYMolLZNFuJfG3ndUygkjGreGtyWWWtr49Jbc6Lws8wqutVbKbsIpr6exeF/aervheUnRtU1j7eJlK1BnO5kd3utkYacOqRqIqqbkzr5R1BMa3luAFebuy5WExdYkSL9uTLq53V1m0vayc+jnI6nJaAfmvVzm1aWF5vOT2u1BQTvt9pVv4wbJIHZ4GJ5GAUEKFxP3K5pfVPsJmvC3G9dItEuZwXialqwMApZyOvBx9SJKmXpEebvhJOevbAD3DJEy26MWoEu0K7Tb7tCHOpFOTN1EQIyo/SsptfdvO13Hd1Ud5c6mnSzyK5DMb1acz6rJR15XR1hO6KVweLsdw2V79o6WHbL68LhwopKXdWXP3geRHqJmerCLY7Rh+HwprRrsYhTPl+lI3vZ7TeLdpW8VbmisTN0TUtFYE1alRFRxkMpB1K+TtaLGcXmdGQpyIi5B7SoRsjjch40ToIK12eaQvbqS5clTDE1jjFl4JyAxVGNtLLLUitUOWq5YtoqhV7pGbhO3UY4PvkG1vZcUtL+W6oeZzSAiMWUlcAsJFrSldGf51v410xIrbOvd3qUTMc/OswT59Tq9SRZxiW0Nc0lldl0h0WtabNFzRu2iemYHdhHsMwedJEWrI8hDNcXXF47x+86G52EvcUqhEDK2uC9ihXKPhU/16SWenBewFQQzUpmy5FnEO2HpTeqiWiptwE6X8yodNKCS8kyXKp76s6WVf3kTuskeWbK60tyqFTJEXm0ZuVntMIFvadc617gVgsYKouOIl6hZxlCMr5CSascfGgmGgKxJWT3q/8NN5QEytDedvm+xkCiYfWwLTHTPSid25FPCuraVkxaGo3yoIDpxEWaZ7smgTRnDDS47Iu+TQ2UTlTTup7h3meg0acW3Dx73vG9Bme5XWzNVENdKBV4vDxZRRMzfKI+2k9FXcV3vtyBmbGEr9MG4a8wbh6yZqV9bMkNfxCiH9qXywEYqX06sHFc5ipfdw1JVXdV/ICpOy9KbI1pczvCsXS9W5Xc15w2dGR6FnfuEw6NXA5x3DBSRZ1tKMoVaayCoLXGc3znG6MiFNnbIqI+W0AJI5lBI5SvZtIlx6Jcof0WnnxIVt+LRjxtel1NuHZu4BxdseVYaIIBSq6STH0ybKGlaWbzCxOlsGYP39bL4/yPOpYHI9NN/nNC7gm6AnUglgskEr/IZHC7GY67Kyn3uHSGopizZhcZeV1mnLFfNLSJtlcuTleQHZYnaKoy3sHk+XEtE2gXu22Y15kKoGqi/b6HyUpzK7Dty53TEec/bbjXwL05MQpEDwlrBZJtoqCLmTrSZGdoc5ZnCGJF8WHIHUF+xcKPh0Z4WHxrX3qQWJ1t7wG2NbCrO8PBWFT26mfn3SKC5c51PoRpjXvluszsDBw5g5zWB2kYi472jqgUqpNPJYUyqbdkupSB/Xc5KuSK04wgowsd0JMfEKUUX1tFnwRYBH5GG6OYvXFMRpYACRvwEhBD33ZSBdEnI73TPXORdfmgsi8nA1z+nFKeCWrqJuzl2e2VJFojdRsmSs2YgcCdnSgZut7E2qGi2tcVodOsGhPzvmujJKhrK25FSnBJMRGjwNt54ld9qhxZa1uuqvaza4ntxmrRq1KHKEcOXC8lxCV13bY7stwldsI1BduF362ExwGYclLdeLikiC536+gdezBRPuZYGuciHQPXmOzamQAqgOz4gSWx6uM2zWllF4FoqbcInyYl9gEqYqdFscDsKVgBGZngK6GbSIQFAKisXZWYRB8J6dzJsqzuSVabU2fJAYVrrhcXmTU87QuZysw4PQOHU1u2RmVvL96oaI8wTq88iLEh9h2pPG5bd+MZMgpdnHJ74QO04s3BCvVa6n5MvZkFgfkkUR4vzLJkkMlF2qq+hs1MEF3gISO02owNny8FVVJNMyFEKUuXJ5k47LUG3EcyrQ53aVYlzFbgyoX+3V6bZPFVRl0gRCDEVMmCIw2ubGU7B/ZvkDRm5JJIQWeCVvj0vYMo5SSzKzpHYc4XgFJlosV5uTDfgDRrGbq6OQuyXm3KbyDiJsS9oBBK9mszCZL8+r2yLUa8dnTYSklpQnGXPIWohwsWOrFaUb0+jMlA1VV47hkcGSr2ldo+rC2fRQ7DQbCkKCJd6zXmOriGNnaOtiSJvzJBtT2vXisBm0qE6L6cXxPCSbLqZNpCSHC5mv3dWZqndYwR+5ws0OBohRUhqe2k1IRqGtsUlXoqXPb0FcZlqiN4m5sEsRSzdvhFA7oBN8P/NwZor0UjsN3H0aLPdaPGt5JM0rykUa6WalSckUm7kmSFja5xmJXFoB2KmNzFzL3ypwZOBZwvF6S2TSSbrNQ092AAeQE0zHDnP/qs1rlTHIC8atLGaqJRSzT1iEYfr11JRYtm/I1dIBnNsxjIBeb2u0h+ednkfMAalP8dbIdPtQnxVvhZpbLzoXy9vUmAuA/lRHHIaNYJ9ZW5dd2ubCPkw1eLFMjJK65mK8WHt9s1pPpdMiQFvIybirTMKrS52cw8ulcpZEtTxv86t26fpoD6dntDjcHMWjTi7puqtjpoHMAjuHzJJweJvs/L2Ezws1xRGiEPuFFQfivKHCUp/RSIwsKd2S+LVeYJh7ODWCBKeLNQfyqj6hUdoAAQu6uYXFrLO13C+gteOB1E7vNzmNCYXedzdKTX1JUpCTe7E6k9MODs5SRm9vYxdb4zZmr6zVwhZvK4XdOb4AHVKymS6Cm+57Cp0zUx1fz5nCd2cHAvCcbo9F6A2ZHzKxg8LzNeynayIMawmlhE2qn/WGAGGn0cIGUH+CIQ484NiXyw1ed5awWpj15piGZZKEMcutraAPVyW+m/ZLF95h2rUQAu/Irhrco6UzOTud/VUhZlQezopmz4estEZnl4vuBPFSv5a79NTvitPcJ50UW4UezRgLdDafBlmzvaAeRHOqSc9xdrPbkZ1z0RLMcjczOiXqM0XNQwFY9mJTxXspuV5P2kadSttge8SmFzp2Vjpao831mlHBXEAU9UyeODpBmOlZIyOQamcdPfPnbnRY9Byzk8vNhVC2EduGeabQLEUihEPIlnQ93M4dakmKUqRHgMRk2uKMslVW8vk6JZQwphN0k8vL0FQSY23iKruUkxpay6HvJ1tPd7BjHFyjE11wzO2yixps1nA7b6cHVzvkV4Auq7F+FoyEWSA1yL0KZHGEMzhWp7pJ+KW4i/qorMKOi46NhQWmP0OsfNUtBHdL6GvzGrl45Po6zmqrmqrw4xwj0JB2Q+Cd3CzkSTPPggO/L1J0fZM2sgzblBf0mC3w9LrZXzCnccXC8JMdeznswxkydRrILkBWezAOICPE9ZozVFmBV3yNlQG7l9enappZEkO1xjTXaAGsJdm2p5jIeZbnDCJhg7K4Skupu+aoYpYK3kWdwHtIhUeqKlwjEKG0LcPOExZydDPudzapUO0lVf3gMrfFBKKPS2YTn3mhXq94ysPdI5dbSIiXARXN7Tmf7FylQwNMr9FYaFYFvmqXGc6bs7r3k42y5I+XXjNTxUPFNdRiRHw0YD87b/neP7BhG9gLEg6lanuOtgGA7iQQbKgMYSlRwm0exDoXMhtlZXYNwuYgQToaMsPBRXvzj0aSndPVmVBUTmaIq7Yo5/Jxu3OtmRDPaWoqUWlMRnsSx20WS2cmacXFBlvChwa9qjbRGz65Sq7z7dYxzf3tapMzXwxSvdJWxe7Kh0jpzoKDvgPBMsnLK0ORFchJHQE5mbsIY7zpdbtyVlaR2XFvuleCdpC5gpdswDJZjaHMLI1YAq8tfKost4u008JZi0UzCknM1M48L8P1XXtZQZQj42nX56nfKEZSSTQKUy27btm8VQMJZjcHnTEuDQQAzO2OoD99S6cGCa34MsWO+1k7CxYd4dhwrxe2r2sn71oDbV5jntn3beIDNVbhJjzMjrhNyvniGmy8I5fOdzdoGxpnpfOZ3VapYeW4IlTVDGc9TMfzWcuaLGxmGA8ZxPKC0jYkadGZpnmYFc8gvG6m+nbbekFYM/MaXhtezflLSN3fjB16sWaVq4YLtmVW7gIlTrkV8yuLEvwWz6lgqaFlGZVU5KuYsaAd+gS0VZarG1fXGdxuQYoLKRvl6GjywRABUO1oviGdBlsoZHZGgXM00MxlG5BZ7TqCPAVReyAh62oaR+6kLV2zMBaL6Jxm5Dnpd6ks0TIXJXmHyy508oNytdYWt+V81e1R0j66Z3qNx+2CqwWavsypEt/O+YAFzGteIcAm1t1eI2bnSsqFwymsrNsm3qqte8Gz7boUtt2F9We3NSRPgQX5y01LnIVq0QktccXMjg3UTDg4aucZi/OhX63MaWhcIOIoCB6AHRKxNp10vclNt3MosVnlEozOnGixkTs/guIlc+Lnm1kZ5Wtm3m9C43RtmRBWMhTd22uQ7G1pxdwRDG1eFAPCNE2qvJTpVWmurFS+V+Wth69VJ2MWkQdd1tXpqlez0t54M6TATidWTYr+uL6g+rpZGLe0n8urpdde2k2ERrISrims11qbL6+E51pKvxZB9Mn1OhLFmbY0EP66nYqzlFTNpUwC+nPLa28WrANcKlNltmsIJbBJYWpgyrxRL1agpum1C6zzbasefJs76n7jAGuszwGHcMV5JiHxRcbbhqapxfWUhGmtp1GaaBQ/zW2t7G7eiWtb60LU3Uav9rmGxLMt5nLxrelssj/JGaWb5VRDCio5OzFN4AqNQif5xkFTz+3iDl3zAB3JhY4lcboowzTuwjwmIThE2VPqX3U+OYUSfkh3TsLXZgzA9EKt8sVtvVtOz8yU3ceGsLyAmEdbaFrNxGR73rC8g8GYb3IBtDgslANFCdStZURXPIVUApcgd0/mM1K1S3bat0tGMPWQQ0ofPeRzf0URpSWyW1bJ2Vzf2lwRBl2or3xAvs/r6yxV4xpL2nOp4y7TLXGCT5urLmw2SnTCmVReUcYuIHHRjWu7IFDR0JXE0YT1/FRvNUharZwj4BmVIZGEuGqPMl+AJHfbwemGRdxqfRScWuZTU0Q3jmEmBW+IyzmXOH6jnahO4onzHBI4p7Kc47rF+10rWH3b7bmFMZtWaADyZedG+tU6oDyGTVxvaqF1HZmoQ+wOEbYz5/N1uV4vs7XnNKYQQidmnUuWCAdR01wxtmlivsFt29nCNMk01XkpXzYLTCwOdX/y2oXU607LJrbUMmW/LlXYdGS5gpjY7VeQqwBMIJF6c7rI6Y3KK2NdynnCsBUSlGzG0nBRpTPZIOJoX4u80YorRVSmSEnD/c5bNDRaOkYd4d3uRPiXpaEqmS0S9LJ0a2V73pbElC8MSs1Qao55idiXRsnv2HNoxNswaZH1ceNHIGvFVI+L5lE+gyJ3sfGR4tJn2um4OW/xZul4acTn+TnlCbXp5jBcsBC/kLYSkaci30Lrq2lND0slyddHcgNdhEy7dRVnbm5z3UA2PSZrh9CoMwaSPWq3CihmZ8q1tDpcYn1GYuphSpsIL/Hkcbs4zHrA51YSKmXbRclugkx09Kq7HPdNx0hMXokRKiBbg9yDdNAUpnR347GscJm0Mku8DFkcWRXhgmwdqeuMEIEC8sj0oYcwMsBej43ps0ts0FQM/YUpy+cVlSsGIupWr15Jr+oQTTno/eHQaJBhQ3C2NVN8TwXtSg+3xLqOiqRsIB+H2FwLTPh8JXNxa6k0q6ylXaltFLqR4MN0h4cSsqD8narHh529IBBe8Mh9wCRid7HWUbjdWrM1j+4FDTYaebeGV2HVxhLRAna8OKV61qvThWF4G0xhbvNrKis8jof8vlyYhELfQuso6LaWoOS+wVFodmJZbI603r4rqYUiGR46l3tsiqW7A3Ck0Jslx2vEhS5lHwyTF9NiXt36gtBgE/eVilz7MebIyk2q4G6TX7G5SzFF6V0NgjmIsXFYeXWQNsbsVFI8zsyXlzxe9afZscVj1cz6xU0qMDybIzF1MzHvIB/qtXgCqAIQZbY7VSW0K0Lelgk6M9lFWUMC2lVzF9MLBxIZzqAwZ7ktbk7RcjsKI4JlMO9VQ5lebPR4LTO3PROREbnmPiUMAQ5KIeqYM6qV530edgdtxlzPuxPMUUC9vr3czw1GRf2TSG1X3WbfFwCzWmeRUgR9kOp5akXhUfIPEHmFchlfOe1REltGIKwgPEinCnMCZbmPV2rhnWxGzuLMW29nK8WWViaS1GFCOwtLc08ZM48Jbwa7CrWwW2QnZFS2cI4XSBXNjumEEgmLuc7vsOsRbs1KYO3QjS+OI7HkXPLgtXM5ZsjNZSFzKV3n05iC5yW9a9bZGd67pH8o5zOChSV7WnanjJ03nI86U6NdABKRcngsJTUpUC25NeKKshf+2S0uCErs0hRCNpG9uaI43Bs044spKs1321nOzgCHo0iPlVGsm7nImtIppExJKEtIJU8UOXQU48gerSRAs0xZYNTUSWjdTFN6aV1aON3iq/kS5EMRyyH7AGlNuukAtwQcYXFq9NjsNgLd5YIvHoTOLmdq7FsQtMBPiO6VyTVqHJ2aBjK0FkGnSx+21dw/eC2DbffIdqpLbEQZfBltOFuYO6oh0NYpbvuQYrdT59wyCX1TNSbQ6yMlBUBb8D5Z2GYeOnCdBiaTuoLMuGHLd0y0WlDYqQrtllgc+N2tS7HtRc/VphAOR5JItAV9Zhhzub0V+jYwVGxVlIK7ASwlY9015lgy5pW3o4psFmutxAUK27B4Wi6O/IXBp6LVC8cGx6aMso/x42GRRKoJ1tGmojyYJrlr1wVrcKkLryx6hgZi0l+9vLUIMFDjRF74LIX4/XmKd5nZ9hzdHb0jyrGKA5VHe9UiU0SZdh7MpUjZmAq18c6EPItvtCtXzHW9iAsCwCWs9Vp+FbWDkSTNXBZVcXnRXO6aB4sjywqi4ba50NZ6f+zWKuyrNi0FGBev4FskF7lECTUO46yuruD8dLZPYmBfjkFRluhpBRJQKF0EcYRa+wih6xvSHMIZoFJNbsRHbVOqCCMuuLNwzOnCaNeEJgezy6q9bK16eXJWhtCdp2rNrDc7G/MrlW6WZX0w+jXn76OzV13ZJunJ9SYjNzSzlrhw3ue0rxtEv+H0Y7vp2GPWn1D8mHL0otUX3Qol6W3hr3DMVWxFa9XjOl4iK988ADKFCDtM2wY1iIg9VK4atpUibDZdoqGWLrQmKY9Tb2dWRL/Y82m05zfN+cxfdxBJlujBFXJqvT4Ss8oQQt0PNbaNZaniLxUyc32LWfszkKlsS0WBWV+tefdkB2SmZIQdV/RSwn2h9g9IvIC5ON0uE2HvcuSa3V7UPcVRuO6KPq8iO1+4SnBJrplTxJdrJe7RQ7slOczIanoVNDMRmpV9NJcRroPJA80dKmOpJxxmLfi2uYURhLhbBvPM8w1JpnW8w8iE3XWavz2vqdP+eCHUeHo2+t1lOsfIJWbYeOphXhTMTK6d2ScSvoQaxi3gkJTjxar3mtM8F4xTZcGQ6pLb1bo1Ez8pEdgpF6f9PrwVgHRdD2G73NHZ2kx6wLkcNUUTu1sJU/G6DV0C5OIJ5/aZx8v6LAJpWELuDo4A4AttSBvbt/g5Jrvi0MUxQqCxrRplsOFrtk4rMY7k1nckClPXRrGYitol7tpgHzL7cH3w/d0MXlAFJWNHxNHP8BSbyVt70+2koku1xj7ulURAM4FRVW7vHSliXri9q2U9Hc80A4GOUy3RV9UNqudlDvnbwEZqA5UAO6dgkSL2IbyA42Su37ROD29WD7hxs15fQFphof1lQZmnYMt0h7r0e2eDRjW/hQj8pOqaTAg7MGskL4Rp4q34dbK+AHUrm/w8XftTZIcemWsCcjnAryzYgXJNIezV1p/qDnFsjJty2IbKSlrxlLjLCW1/XEgBwQb+lsZ3K1Hxd9f9jZvS+XLDNpF5yg+AZ8gAGIJGYtuqZ27XwwVahjZnoYcEFjoZYf1oF6+3RcRLInV2c3ja3Pr5nKp4VzoJlSjIElVCQaLyTcMfDQ7pCtnqfR3pIA9D9OhQwDWvAVJwui4UvwjlzlyaB38hW0py9kx0NzMUcmUS6AyezqSjOHejRXjzInE136aX21FPqs1ma9FtEsHkto71vi6nu93qcOAuyLo4S3Vy0BJepq83rJ4Tfhf6WrkPaM6+rD15mQIIBeZpc3XrLWcyiktX0ZbKxLpoO+q2D3rSXd4CMZevsF/xvba0s9tBwxen3PdjZM7fVuxKNU0hSBXFRuZ78Uac1WOvkv56Q+szt66ylq6Pin2brVCN96ESKXXNXnac7a4DLC0Zfu/zFHl0vbK42pXhdvMeK6ITyL0Bydz7+mJPUvuQbaDj4hrvsU2raSzBCu2mOvWenME0BHEeyJ9OB9ZtbQipyug0A7mjsHGnqHtEyzXVbhHCAxFPhdvj2iaPUqgXwTHhk72TiVPT3Si8qm5CNpVSvBZmln/cwD23uKCVbOS9MTXqHZEhB110Uy6HDxRc4owQawtoaaX5dOAJnjjPHTT4/1r7jh7mleXK/3K3fB7mZMALkWKmmLMxC+acMwH/9+F334MXxiy9ERqQqOouVledoxZPgapnOT5eDbjx6YAFVJRg9ggnJeCGHbo3h375saal4gcI+NHP9ccgtzn8aL1eoGJ6VHusjsWQdaADBgRIG/PeLzkAFgIJ7KxPQypdgBbZgsA2gIt+BKiDXpVP9xNKH5sYkYT/qNeeFVmQCXnmZ/P9Y34fsFCHnoPIrGA/5/2Ev35g9ImAezzO+/OTXnqm26+DsIVHm1LJI+x6aaVYyohtGXQ0uyVko80uN4k77AaVmdoMhsjqSy/z72yGkLkm9uqkVwOkZg+mdjxhcXmhI+i30GCCQ+5/Vk6lCHlGdhVCrQlOgmwQndv9XFcIyDrg5HWJyyDg+b0Bhsp9WVTmjX61QdJIJXxiRkF3V6PBqL9BAolv/qOQmGZg+azjfBmw5TnQYHWsyBsna4E4xsRZVk2l8aNB5fr5hMHlYDhy4EAGAiGHgNiZkhXZiL/yV4aQfx7MNjD0smUnzZiu6fGLVY31ynx7NKThWb74Vly5BsFdGsa4+gMu5uast9UysVjFY8+hk+a3oU0kl4jjPrzxV5MgbsfmncHyX165y8t8UIFpvl63Zze1Db/3S78FCDZvuhYRsPsw0b7DJPLCQhIgT0jsL37FlTqQf3OnhDZmCS3FYWK7JVC/0dzaaj8RqX+zIne3sOFbqkzIIqCS8uPuhJJiBfTMHwE8hTXhcv+Rj4fu7+yHy+DDknmLMN33w1BXMfQLjambjMpT2uxf2XCqj06HAWGyvjtLZIXv0te5PsMQWUHCM1Nlx/ecBjxGyrGkvNtqe++bg4VI28SDKMiAr7m3THV8qva5tUnvStXdetJq5NhyOiBUboaQwn39S0aFSUvcAxhYtcN+0nyzfdcHWntdUpfz4/9CELQlC0ZJuwvhj1Zqbcdim+aoflviHTtG9i1J6Dq2ododWgqhmKWiI4FvV9Zos1mQAAEKFlS8tZj4Zk644iIBIQ/T919OqHBD7HpJcGS6fFMZV5799PEPkx2wtowzJds5Gjm/zR7UyngQhnq8NAZAgNoC6TPQMJ3lbPWDgxwrgjtjvEybCOQv35UfNCzZHbYXQ2UhwD1twC4J8rMGumJYKzHaHOPv1Lqdk5Hbo7aAek1YhnIaH1DDmx/MKYIywq4lSvV1UqswoCVlFlwbt2XTIRS+EfJhJ8LYf2JiwLUn9Ar6aVa0O+meJB8k+4gxfs9ryGWi2Lc/On6KctJnXGMfQKJnsuVldVWt7Ac5w6Ua1QmBPEYT2tdMI6BCC6T6iKDHiUgwAhmbJMgtlVtlsKHqjmNBcRzUGvdPF7iGiLqnhssjgPfv1OGHx+kPwSSwwr7pvIU/J0p98jz7PB7PVMWXgZvI3RDLfzdI8OEtAJlxp6yDG+R4NnFl5GBr00eRQYauxZ+FZalpDJGO/NrtiXB88Zeey2/g0aN2Hv52616yu2dtSC9/b63iNL1LXjmSzg/PClx490y5CLsHXZpkvoB2SvUQGwyTvYkEbkB/1eNr56e4iZ0kFi5uWgJWsLBvVivr2uhNgKhXXUy4uAyNFk9QzEZ4Or8M5gtsUhBu9DrH3zcN16mbaQdG8a19qTK8P1RLvoyAVVgIObDXxZs3RdXVFY+u8kTbrCNht8gyws98C5nlpbNQ+bIbR/lnUTSGN17ShO/NTCQGPwGsj0uv/5kGVX9t66ittSBJhIaq9W47BnRTiQg0sxchu6Qj9dA0zmQossaWk9nNmRnRpEvYL/pYXpdjBafLKv0mRfmDTcAcO3qvbnGdaeTvyQIZZpSe4+nx3FXSSyRekTfRetaB/HWV4vTdiGKLqSeTcAMyL9XkSPEOcgA2w2kH3xbvgqqq1rCTUu+ioSL/nV+NjxhjEH2GuY2sE3Fqomg3zJ9bqMferIFWbogsKX/ubUXGs30S7RIt0H7B5unjfl/qN1qlVuyabmpe0NKUc0NtDM/jgNTDv7zWfqUtau03Wy4c5QwQX3t0EFX/m9AyN9x+7EyIi+BT+kkGCk1hbrP1OaRpZv7w4DcsRiqC9425QkzapLzn77sc/5CYcX5w7c0iF77LDKbGenkjF0Ak1dY8TrRNCDn197JoY5DVaUhHt+yLlYCGqZjjoFRy8Y/VYyPdEBwrz7T1zNFdutbHukGAxVZtpV5LFjYubOIqJ9Rh5bOIk0oGhGOl/vxN3X2mNQ3/PKkQ94vAq0eJgc01hzigTRkZK7osBo+ifImbHqUJcNLilFVnFoP41H01/06IvdxgNoKZvD0BaAoyB5DX/Tg3rQ8ova7BaX4geozdNKXQNeDnL5Mi94ocEhhT6U4h+SZ9PHGAF9VyaiX/Le0TT0kjAUf3SXjzdwdIyALY3riSbT1fKdETdZjlRSNNHoIXdjYqU7LUSrZrSkqr8OCdIcJvu9/AYiTqaJxvCzrHhYK5bk+t/RtAgEn1yQgMPMEJhjy14fIUP0rfr9ZM3RAT5GyIUASQf2xz7J8g0K76pq3AKBONfutxZV3AugfdaawBtVS5P3kQvCE1ds0U5u8YoODSDiT+5eRZDRc9inM52tEPmd4lcc7543gBMTjQji6qc2izaB1DggSObmQHAgwz5alK4trx1CJtgtqeWhDMS4X84Id+y2Do54y398NRlROjMHblF7kt13VYxQi5ZQfu1w65MK9HbOiIOMZuf2r/Ga/Gr5xuFnV0hG3w+ll2IHkgf8l+vYV36wt3fUhmNpHYvIki6EBF8MxLR5YRC323JG+c5YJRAMOD7UKU0m4cxXDM2US5kRPSKdMc5oNyzdQRL7oI0ZrS1HY1YmZEKllOtjJdluGB2yaNVzvb2Gbz6rdGnmAt2NAsgcWgIx+UNKNNAr9X/hbEcIV2RRXaY1IJsFZfolF6m3gCyiNmMb85aag60fh5Mp+e98bhG3ExtYFdF/DTf8QEkLjdkm3DpNGJZ8SS7TOfYth4N0ZusbHbTGQv0MjIDmfYuAktEFwsoApiKx8knIXOWD4YtV9I8LnKfVZcKOh/z6Gndcc8UgD4DkWPl63WMWwXQ1WxAE9Pg761ZF7RRPEpqmMBozcJeHzYOMbsCb6wfQXa0MNnSPafszff8ZGS1ot+sOJDWgRBXPUiWQ75lXUCzqj4Tu15Ocdh/ELJ8DVAaHfOQ92l8qnmKtxYfC4Yykrw9Hqp0cayEMO16wtXCu6UzJMNDURDfEBTXRoGAUDx9Mqb3p9sojfDoD0keDaf5MTzTU92GZAIejMMiKphnT6UAsE0MxYxLktqHtSnIjhPoqhwx0GAuC4+D0c85aYdnsGsR2r5powURuY9GPfCkWwvb52S+/b8VkvXNqIvNTNWDwJwLBJAo0dHFEdd6ACzFKj3QF0M04zZoB06+xNW31tBRDJFKyg5thbXX9INYHwZJCAlhUof5BRw5NToYybpXjgZskWawUx5m2cNyMolPkXz4qJHd9JMVC67nH/fE0es9JsBEKaQdSv9/pz9qLVd5WgTjN839CpgISHyN34vvdP6n+VoXVvvCs2E0xFfW9+CrIPrA9k6hQFrnhA/U4592nVbux0KYwSdZxwt9lYify+aODTjagn+rIZi7tw8pP1mCeN74jrMoc4cRegoAMn42GQbeoGr623sk6ypRlwHv6dcxh/NC4Qr10kexVziWlYPoU/UMbsQD8odBLw/doS9xWHxoXCqGSbdj1zOkl20f6lFzaGFvYgvbyK4R1z1rYO4bM9Vcjwrm8ww79V0IIF2Cr5oJvRLRy6F9azmlsqoGe4pd9swDb61Lk53P1ALX6l78jlyMf7wTOxNB12qJ7AVhVGsRbp0mBQZ1YsX+5+LMlWfEw3vfqzqAUwpnx4XrghTvsd8S1Q/PXvvEM0ObpFx4yUj+OkthGP+tGbl946OUaL7YC3fZGnK1/FhjZZuFEu8VglGo2INuOVBoiFuujDEXxiw3WeRTv5XfKmd3xGX9wA59bvwMkE+II5jwS3fV4JOQn8Fvw4l+GBe1uxbx7IQEiSkoxfH5CBjEkweG1eA+nSmiLUUb8CXfyFX6qCaefdIltLF7mfsJ4DHxQpJlykNgoRnwQBjmE+cUzztHfMufRAqOuDpnwDEcEOABMc1XkvcZZKtxfxV88hmDZS8r8DKmlkRDdYxWKoPSDlP06eZfa/BBpRclfprLTpqzazdm8EphVTAfB6cNjTkrY1VxGLlB9JxiJ8eIlt2A5+J/DSj6xyhiqqG43kJ6ICOHbmaUXnmCtFtaDIfe4kBWvBxBHvFtl0YE2VoBW1a79wgUuX1Rl3L+CnU7mKzUs6UUwy2m4pELXmoTpMOgkXAwfX9eKYIQr5xI0vM1yoIWHvP2G6W+ngpfSUr+dK2wzxEFCk271lauPqgQ2wfs20R9UVKqNg4ZjnCLxdHv7+uRqq6lPaHDzFap2ZVvXPYxeLKGV4K/daTMI+VIGBRMq3phxaNinBqSnxp9/AtOxgNOJheYc/AZRJ1azQDf0CZuTfsbYqvXI9oBAtPc7j4PJQ+2WyRWXN5+Z/uohxkc5aH2ZMoWtHDO3/zDjAbgNQbIzXHCXIW8HlfitpYu69tzEyOrFMZ2vIanjoPNcUu0ioctXwx5NbM2+n06cUXKcLZ1ZLv/n82vqHvrrbIJlEjlpMu+0wK5DjpdiNarkmt8bsFMyDmAgY37YExxwkAIPWs/kdAsWhMMrCpaW0QgROhfZ7l+RBXcYnFFBac47k0ys2fn5tOQq/hhRUu7G1aupAhhFi1ErGV31ATTmfawqWuDaJuo1rrjZwUEmQ5WLv9tIxBtqt4PSBNHebz3JSMjlgleyjsUN2Md9VEtuaeyFzzssLgpr/YMbUDIyiN1MRvpdyhPz9Sh7yIbhtoaKNIrrvr9JQEjfF6RXeQAUigaCMWf1kM024oGXcHaH22S6Y3KktoIF3kDfhYm1xaW4CV3AbD0eOXbJ3F8CWQyEUoiogAbynQqKbtvBjg60CTakWQVgO80rILteCmcBdr8VczrqgqehQAdai9UMUed/KKQO2pf2uIn8SaNvnH0c0XO1M4ny/fxFKeQ9MzUF/9dDJUz2z5B7YrY5zIOHz9DFVZtGAPhLyzIbGvb0pcbEwC9WZ5vbD4xUSZtZaBDBUBEgTx7MUPnY1ALdHOekQzVhU8nIFfaEDVfG1dlNcLaBHQQLjL3rwq6T55SPUFSNOTzQItsaLHjdaNXWyMxD9PgDM9QDHpzyiGYOj0DZPjQM144xO94HI14YVf3vDBtm0r4Hw7iI6MDLv5gavQAT0ZV51TJjF0hD0ipcZZDl2peUnico/VquC9J9lPm6kLmPpVZ4MgpPpvgGrOAl/aCZcyeYJOlgUSIkyG4xVBnZPEbBU/mDDuev/twv1kuYxoY5vpGnOl/ZF0DcVQqBhfEfrnXGjAlabozpExEs53C6SN3iy22YQ67pVb2svvZ492ujLmC5Qhp9N/8o84SVxvsLlvdzaQDDaLOGSFMTqQUV9lWGLb3E3ipO7MsuU85viS0cHmpmKgvkj/Oha+TqgOUV1P7c+Cs61psTs6NnYiO3T2DSoY+5zuFzW6iYBz8zi2gYIWnPFXFQH1JxwgRqkkelTD4Tvd+nzr/KIy9Q/hST3U1L4LEHnuEoSYUrol7UIfONhWzDwg6nqMvlqkxD0azUjZ/rnF9agktt9AFDqoeCVLwqAeLvBExfGSKSwOnP3TteYvTInfjZa6nMoRAvg7ms+1+e4PCramTYbnn7+R14qm4/79QDvFBNjGBAVHayUnW4G7qbhi+b6zQxgja7r5lsIXGmvJfEW/AR+JhJtfrARopE86OvLnMF2INWFUH5elvbR59+Oc5L32FWK5+1FS8s3hu3kGOR9muAWYqmGt0c4dHSTz5TfbCp2li3HLT14HLORGEnTiHFuCu3E1RApxhrvxY9PF6PQGod4Lj98uTJFcxeOeV7gQnxwYgbPTxAo34u+0qdEWpwjxsUE5VKXOLGZ0k2iBcLzu2StItLkahwQ0O9QN0rY+SQPa9tJfSexYLi/jSty21XuM2Y/5+HMrwthAqgksE+oEolSnlqMGOLXRN2QtonM+P+l1/W1Z1ONtT1OLh5hgCCkI6gnqw03+edQ1ErPBva+B7kZwOLBvBksV209tSf+IHQ7FaXNWs6Kaw8NkyjjYlFM472Ihy0dIur2UMZHL5pwPv35xtEduRnRUxQQJmv8iEh91QhrtDLC1skGWYWllmG4CT6YhI6J8l2rxjzB8+ZF0JrI6wo9u86c+bPdIwbxV+i0YiQGWjlMbz4lA+CsJiJolbaIVSGjcaBvNW/5Bn9fkLmMQbJk9e4EajnCWiTnpcuEC3gIcDAFyHKe8+Bp9yHZhRC6AsVtEI4hqii5ng0qWjosrKNvhKBYUlI3y2YOZFx8oQxKcMekTy6cXBIZaocFPbZMkCrKxfXAhUTz1i+xuofHTeq7MXThciyFl74cv3wg/OqQbJR6F56Gdj/JxRWq1VK+fU/PBERi+qTXwD7NwJirMm9BUrANkvo1KZhPgkeClH6MefqvJZ2TEOOlsomYrqLmK030bTpcq2LUvcITX17CjKeZ6lNL2z+KG2TyRgStuOGAACaO8xPl2LykNY6894QuDwU3pV/bN+/K3LwONKAiw/4mTkDCsjViqSab4Qjj7+rgHkDgPgc3DF+hslMcQJMw6p8pIMwg5mOW5600ZFApS2skihlGIIoYhqpgn94sOnq8Di08KwMrIej/KzeIAXaHMsrtG1j42I07f7RepXxIleqzeTnmocw7bVadE9Ks1ILrHcWYRlx94GgvQBqgEGnJ6eGIO+pPBEYyF0JAb55CWBYKZTu1uU0iDd/qxGWyBGSS6aLzO0LPyMnmL/6Y5sOuwjA/2DqBt5u1wxutKPfOQbSDTUYxjP3zVya4RL76xqUVkvcqpa853WKt3BBzo3vYitlD+yHj9x3/89Y+//khM/k9Jxf8WAv8jFfa/plj2T3Gx8XjNDelr7z//+tPn69//tvXv/x/b//cffy1p/Vr+p8jan+6o/xIr+6fE2r/93XnsXxKQ/7NP1z+1Ire4XP829H7ybwW2P63K3sG/Lvpb3PCvf/x348N3+E+du3eQjOO2bu8V7/iP4mOXZ2X+b3/EOv/605DgtT/+eetv9ds/U/270cDf6nDvdP8P/td//T+NS3fuwIcAAA== -->
