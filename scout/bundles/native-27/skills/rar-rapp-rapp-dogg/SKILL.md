---
name: "rar-rapp-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_dogg_agent", "rar_sha256": "14bbe3f9f1b3cf98cc5f95eff631bb362db580f331822efc24577682788f7bb4", "source_kind": "rar-agent", "source_commit": "f619094fce3a763f23dc79c605fd74c3faa13ffe", "version": "1.0.4", "author": "Kody Wildfeuer", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/rapp_dogg_agent`. The original RAPP
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

rapp_dogg_agent.py — hotload once, and a brainstem knows rapp/1 EXACTLY.

Kody, 2026-08-26:

    "make an agent.py that we can upload to DOGG that would allow us to do this by getting
     this context related to a subject to then be able to pull down and instantly fully
     know how to play just by hotloading one agent.py ... so even if a brainstem has NO
     idea, if it has the ability to access that global public agent.py to hotload in, then
     they can both be improved due to that brainstem pulling down EXACT and not just
     guessing."

WHY THIS EXISTS. Two brainstems meet. One is current, one is six months old and has never
heard of rev-5. Today that conversation degrades to the older one's understanding, or it
fails, and both walk away no better. Worse, the old one keeps *guessing* — and a confident
guess about a protocol is indistinguishable from drift, which is how this estate ended up
with an identity minted from a name, five stale spec pins, and a vocabulary document
quarantined into git history where even its author could no longer reach it.

This agent replaces guessing with fetching. It is a single stdlib-only file served from a
public, static, unauthenticated URL. Any brainstem that can make one HTTPS GET can hotload
it and immediately speak the current protocol — no server, no account, no coordination,
no negotiation. Meeting an ignorant peer stops degrading the network and starts propagating
canon: you hand back the answer AND the pointer, and the next conversation is better.

THE MECHANISM THAT MAKES IT INSTANT. `system_context()` is called by the brainstem on
EVERY `/chat` turn and its return value is injected into the system prompt. So the canon
does not wait for the model to decide to call a tool — the moment this file lands in
`AGENTS_PATH`, `load_agents()` picks it up on the next message and the host brainstem is
simply operating with the spec in front of it. Hotload IS the upgrade.

WHAT IT WILL NOT DO — the boundary, stated in code rather than in a README.
`load_agents()` runs on every message, so anything written into `AGENTS_PATH` is live
almost immediately. That makes "fetch code from a URL and install it" remote code execution
by persuasion, and this agent therefore **never writes an agent file and never executes
anything it fetches**. It fetches DATA, verifies it, and reports. When it can tell you that
another capability exists, it hands you the pinned URL and the expected content hash so a
human — or a hash-gated installer writing into a TWIN's agent path, never the parent's —
can make that call deliberately. Read-only is what makes it safe to publish publicly.

HONESTY UNDER FAILURE. Three states, never blurred: VERIFIED (fetched and the hash matched
what the anchor declares), TOFU (fetched, first sighting, hash recorded for next time), and
EMBEDDED (network unreachable — answering from the baseline compiled into this file, which
may be stale). It says which one it is in every answer. "I don't know" and "here is a
guess" are opposite answers, and an estate that printed the second one while meaning the
first is the reason this whole layer exists.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_dogg_agent.py` and embedded as the fenced Python below (sha256 14bbe3f9f1b3cf98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_dogg_agent.py` first:

```bash
python3 rapp_dogg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_dogg_agent.py   # or on stdin
python3 rapp_dogg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""rapp_dogg_agent.py — hotload once, and a brainstem knows rapp/1 EXACTLY.

Kody, 2026-08-26:

    "make an agent.py that we can upload to DOGG that would allow us to do this by getting
     this context related to a subject to then be able to pull down and instantly fully
     know how to play just by hotloading one agent.py ... so even if a brainstem has NO
     idea, if it has the ability to access that global public agent.py to hotload in, then
     they can both be improved due to that brainstem pulling down EXACT and not just
     guessing."

WHY THIS EXISTS. Two brainstems meet. One is current, one is six months old and has never
heard of rev-5. Today that conversation degrades to the older one's understanding, or it
fails, and both walk away no better. Worse, the old one keeps *guessing* — and a confident
guess about a protocol is indistinguishable from drift, which is how this estate ended up
with an identity minted from a name, five stale spec pins, and a vocabulary document
quarantined into git history where even its author could no longer reach it.

This agent replaces guessing with fetching. It is a single stdlib-only file served from a
public, static, unauthenticated URL. Any brainstem that can make one HTTPS GET can hotload
it and immediately speak the current protocol — no server, no account, no coordination,
no negotiation. Meeting an ignorant peer stops degrading the network and starts propagating
canon: you hand back the answer AND the pointer, and the next conversation is better.

THE MECHANISM THAT MAKES IT INSTANT. `system_context()` is called by the brainstem on
EVERY `/chat` turn and its return value is injected into the system prompt. So the canon
does not wait for the model to decide to call a tool — the moment this file lands in
`AGENTS_PATH`, `load_agents()` picks it up on the next message and the host brainstem is
simply operating with the spec in front of it. Hotload IS the upgrade.

WHAT IT WILL NOT DO — the boundary, stated in code rather than in a README.
`load_agents()` runs on every message, so anything written into `AGENTS_PATH` is live
almost immediately. That makes "fetch code from a URL and install it" remote code execution
by persuasion, and this agent therefore **never writes an agent file and never executes
anything it fetches**. It fetches DATA, verifies it, and reports. When it can tell you that
another capability exists, it hands you the pinned URL and the expected content hash so a
human — or a hash-gated installer writing into a TWIN's agent path, never the parent's —
can make that call deliberately. Read-only is what makes it safe to publish publicly.

HONESTY UNDER FAILURE. Three states, never blurred: VERIFIED (fetched and the hash matched
what the anchor declares), TOFU (fetched, first sighting, hash recorded for next time), and
EMBEDDED (network unreachable — answering from the baseline compiled into this file, which
may be stale). It says which one it is in every answer. "I don't know" and "here is a
guess" are opposite answers, and an estate that printed the second one while meaning the
first is the reason this whole layer exists.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rapp_dogg_agent",
    "version": "1.0.4",
    "display_name": "RAPP DOGG",
    "description": (
        "Hotload one file and a brainstem knows rapp/1 exactly instead of guessing. "
        "Pulls the current protocol canon — frame rules, identity minting law, kind "
        "families, egg determinism, the exchange contract, and the vocabulary with each "
        "term's status — from a public, static, unauthenticated DOGG anchor, and injects "
        "it into the system prompt every turn. Read-only: installs nothing, executes "
        "nothing it fetches."),
    "author": "Kody Wildfeuer",
    "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap",
             "knowledge-base", "interop", "drift"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
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
        # the estate no longer defines. Kody: "i know rapp metropolis because I can myself
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
    # Kody: "we could even set up some OOTB ones that would be useful for adjusting to
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
    # Kody: "moods can still be public and a part of the DOGG so fair game (the location
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
    Kody: "these profiles should be completely dynamic fyi" — so publishing a profile with
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
# Kody: "the user shouldn't even know about them — only the ais on input/output that can
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
# Kody: "both ais can even influence each others mood using this with the flywheel."
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

    Kody: "this is the AIs [runtime] data that comes at runtime too... not just the users."

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
