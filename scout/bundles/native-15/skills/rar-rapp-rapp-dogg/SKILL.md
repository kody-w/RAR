---
name: "rar-rapp-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_dogg_agent", "rar_sha256": "6a2309f2838a8e890f721d0291a19254986fc9b5ebe11e5d859b48a6d2167853", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.4", "author": "Kody Wildfeuer", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_dogg_agent.py` and embedded as the fenced Python below (sha256 6a2309f2838a8e89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_dogg_agent.py` first:

```bash
python3 rapp_dogg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_dogg_agent.py   # or on stdin
python3 rapp_dogg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/rapp_dogg_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_dogg_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/rapp_dogg_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
