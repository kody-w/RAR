---
name: "rar-rapter-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/rapp_dogg_agent", "rar_sha256": "1a0d63eea1f887c89d03a2dc32d4bc3f1d94653d424444149d8224c146aa8c87", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.5", "author": "RapterBox", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_dogg_agent.py` and embedded as the fenced Python below (sha256 1a0d63eea1f887c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_dogg_agent.py` first:

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
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapter/rapp_dogg_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_dogg_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapter/rapp_dogg_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
