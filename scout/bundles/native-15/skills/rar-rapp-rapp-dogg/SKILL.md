---
name: "rar-rapp-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rapp_dogg_agent", "rar_sha256": "6a2309f2838a8e890f721d0291a19254986fc9b5ebe11e5d859b48a6d2167853", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.4", "author": "Kody Wildfeuer", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
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
