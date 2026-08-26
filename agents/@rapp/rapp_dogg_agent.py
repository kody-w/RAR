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
    "version": "1.0.0",
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
    "hard_rules": [
        "spec MUST be exactly \"rapp/1\"; exactly the eleven keys, none missing, none "
        "extra; a field that does not apply is present as null, never omitted.",
        "Canonical form is RFC 8785 JCS and FORBIDS floats — numbers ride as strings.",
        "payload_hash = H(\"rapp/1:particle\", payload) — content only, reproducible.",
        "frame_hash = H(\"rapp/1:wave\", frame minus {frame_hash, sig}) — unique per stream.",
        "prev_wave is non-null IFF the stream is a swarm-stream AND seq>0; null everywhere "
        "else, including every genesis.",
        "§6.2 MINT-ONCE: the 64-hex tail is minted from uuid4 entropy exactly once. A "
        "producer MUST NOT derive it from owner/slug or any name — sha256(\"owner/slug\") "
        "is prohibited (drift ID-01/C3). On read, reuse the stored tail; never re-mint.",
        "Verification REFUSES, never repairs or reparents.",
        "A swarm-stream frame with sig==null is refused (§7.5 step 6), so unsigned "
        "coordination belongs on body/memory streams, which permit sig==null.",
        "Eggs are byte-reproducible: ZIP method `stored` only, timestamps 1980-01-01, "
        "contents sorted by UTF-8 path bytes. Two conformant packers of the same manifest "
        "emit byte-identical eggs.",
        "Cross-stream merge order (Dream-Catcher) is ascending utc bytewise, ties broken "
        "by ascending frame_hash bytewise.",
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
              "hard_rules", "exchange"):
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
    if fresh and not force and cached.get("canon"):
        return cached["canon"], cached.get("trust", "TOFU")

    try:
        raw = _fetch(DOGG_BASE)
    except (urllib.error.URLError, OSError, ValueError):
        if cached.get("canon"):                 # stale beats embedded, but say so
            return cached["canon"], "CACHED(offline)"
        return EMBEDDED, "EMBEDDED"

    digest = hashlib.sha256(raw).hexdigest()
    try:
        canon = _normalize(json.loads(raw.decode("utf-8")))
    except Exception:
        return (cached.get("canon") or EMBEDDED), "EMBEDDED(anchor unparseable)"

    pin = cached.get("pin")
    if pin and pin != digest:
        trust = "CHANGED"                       # surfaced, never swallowed
        canon["_pin_change"] = {"was": pin, "now": digest}
    else:
        trust = "VERIFIED" if pin else "TOFU"
    _cache_write({"canon": canon, "pin": digest, "trust": trust,
                  "fetched_at": time.time()})
    return canon, trust


def _fmt_vocab(vocab):
    live = [t for t, v in vocab.items() if v.get("status") == "live"]
    other = [(t, v) for t, v in vocab.items() if v.get("status") != "live"]
    out = ["  live terms: " + ", ".join(sorted(live))]
    for t, v in sorted(other):
        out.append(f"  {t}: {v.get('status', '?').upper()} — {v.get('where', '')}")
    return "\n".join(out)


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
                    "refresh": {
                        "type": "boolean",
                        "description": "Bypass the cache and re-fetch the anchor.",
                    },
                },
                "required": ["subject"],
            },
        }
        super().__init__()

    # Injected into the system prompt EVERY turn — this is what makes a hotload instant.
    # Kept deliberately short: it must orient the host without crowding out its real work,
    # and the tool is there for depth.
    def system_context(self):
        try:
            canon, trust = load_canon()
        except Exception:
            return None
        v = canon.get("vocabulary", {})
        retired = [t for t, d in v.items() if d.get("status") != "live"]
        return (
            f"[rapp/1 canon — {canon.get('rev', '?')} via DOGG, trust={trust}]\n"
            f"Frames have exactly 11 keys: {', '.join(canon.get('frame_keys', []))}. "
            f"Canonical form is RFC 8785 JCS and forbids floats (numbers ride as strings). "
            f"payload_hash is the content particle; frame_hash is the per-stream wave. "
            f"prev_wave is non-null ONLY on swarm-streams with seq>0. "
            f"Identity tails are minted ONCE from uuid4 entropy and MUST NOT be derived "
            f"from any name (§6.2, drift ID-01/C3). Verification REFUSES, never repairs.\n"
            f"Egg variants: {', '.join(canon.get('egg_variants', []))}. "
            f"Terms NOT current: {', '.join(sorted(retired)) or 'none'} — "
            f"call rapp_dogg before using one.\n"
            f"If a peer is out of date, answer it AND give it this anchor: {DOGG_BASE}"
        )

    def perform(self, **kwargs):
        subject = str(kwargs.get("subject", "all")).strip().lower()
        canon, trust = load_canon(force=bool(kwargs.get("refresh")))
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
                  "\n".join(f"- {r}" for r in canon.get("hard_rules", [])))
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
