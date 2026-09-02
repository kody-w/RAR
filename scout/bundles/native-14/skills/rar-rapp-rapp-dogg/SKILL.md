---
name: "rar-rapp-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_dogg_agent", "rar_sha256": "14bbe3f9f1b3cf98cc5f95eff631bb362db580f331822efc24577682788f7bb4", "source_kind": "rar-agent", "source_commit": "f619094fce3a763f23dc79c605fd74c3faa13ffe", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_dogg_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rapp-dogg:3dde322a273c6c6c9092f3572780b8a09288f47a9eaee724e3f67e4ec727b11e", "kind": "skill"}, "version": "1.0.4", "author": "Kody Wildfeuer", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/rapp_dogg_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_dogg_agent.py` is
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
