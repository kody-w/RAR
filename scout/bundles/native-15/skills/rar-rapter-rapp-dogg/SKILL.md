---
name: "rar-rapter-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/rapp_dogg_agent", "rar_sha256": "bf6bd60cb5c17a940141985ed82be8eac8112213af58fcf1fd80403b1573ff11", "source_kind": "rar-agent", "source_commit": "b4ba983328bbb00340c62a83332318dc0ffc22aa", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_dogg_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapter/rapp-dogg:8b5b28c43430e15a934793dd0b24fee11dcc09cf648424be2c555f28864c9ded", "kind": "skill"}, "version": "1.0.5", "author": "RapterBox", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapter/rapp_dogg_agent`. The
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
