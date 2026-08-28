---
name: "rar-rapter-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/rapp_dogg_agent", "rar_sha256": "bf6bd60cb5c17a940141985ed82be8eac8112213af58fcf1fd80403b1573ff11", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "1.0.5", "author": "RapterBox", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
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

<!-- rci-capsule:v1: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 -->
