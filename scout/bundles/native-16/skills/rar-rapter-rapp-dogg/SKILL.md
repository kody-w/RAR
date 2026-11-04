---
name: "rar-rapter-rapp-dogg"
description: "Fetch EXACT rapp/1 protocol canon from the public DOGG anchor (static, unauthenticated) instead of guessing: frame rules, identity minting law, kind families, egg variants and their determinism guarantee, the one-hop exchange contract, and the vocabulary with each term's status (live / retired / not-in-spec). Use this whenever a question touches rapp/1, frames, rappids, eggs, streams, brainstem coordination, or a RAPP term you are not certain is current. Read-only: it never installs or runs anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapter/rapp_dogg_agent", "rar_sha256": "1a0d63eea1f887c89d03a2dc32d4bc3f1d94653d424444149d8224c146aa8c87", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.5", "author": "RapterBox", "tags": ["rapp", "rapp-1", "dogg", "canon", "protocol", "anchor", "bootstrap", "knowledge-base", "interop", "drift"]}
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
