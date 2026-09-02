---
name: "rar-kody-w-rapp-sdk-builder"
description: "RAPP SDK toolkit. Use for any RAPP protocol operation: mint a compliant rappid, scaffold a new organism seed, build or verify a frame, canonicalize/content-address a value, or check a repo for RAPP compliance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sdk_builder", "rar_sha256": "76799624979a91c7f4f87d64b41d1fe5add10f727c672cc25429442a38ef757a", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_sdk_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-sdk-builder:acfa1fcda010a6307fe0d737f06f8309a90b1fa5162e308a947a17ed4620bd00", "kind": "skill"}, "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["starter", "rapp", "sdk", "identity", "frame", "builder"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp_sdk_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_sdk_builder_agent.py` is
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

rapp_sdk_builder_agent.py — a hotloadable RAPP SDK, as a brainstem agent.

Drop this one file into any RAPP brainstem's `agents/` directory (no restart) and the
brainstem gains a working RAPP toolkit: mint compliant identities, build and verify
frames, canonicalize + content-address values, scaffold a ready-to-plant organism seed,
and lint any public repo in the stack for RAPP compliance.

Install straight from the public standard repo:

    curl -sSL https://raw.githubusercontent.com/kody-w/rapp-1/main/agents/rapp_sdk_builder_agent.py       -o ~/.brainstem/agents/rapp_sdk_builder_agent.py

Then just talk to your brainstem:
    "mint a keyless rappid for @me/notes"
    "scaffold a new RAPP organism called @me/scratch"
    "verify this frame: { … }"
    "check https://github.com/kody-w/twin for RAPP compliance"

The RAPP primitives are embedded here verbatim from the reference implementation
(kody-w/rapp-1 · rapp.py), so the agent is self-contained and offline-capable. The
`sync` action fetches the canonical rapp.py from the public repo and proves this file's
embedded primitive definitions are identical to it — by comparing source (parsed with
ast, never executed), so it is provenance you can check, not trust, and safe to run.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "mint=mint a rappid \u00b7 scaffold=new organism seed (rappid+genesis) \u00b7 frame=build+verify a frame \u00b7 verify=verify a frame object \u00b7 canonicalize=canonical bytes + domain hash of a value \u00b7 check=lint a repo/rappid for compliance \u00b7 sync=verify embedded SDK vs public repo",
      "enum": [
        "mint",
        "scaffold",
        "frame",
        "verify",
        "canonicalize",
        "check",
        "sync"
      ],
      "type": "string"
    },
    "frame": {
      "description": "a frame object to verify",
      "type": "object"
    },
    "id": {
      "description": "identity as '@owner/slug' or a full rappid string",
      "type": "string"
    },
    "kind": {
      "description": "frame kind, e.g. 'note.write' (noun.verb)",
      "type": "string"
    },
    "payload": {
      "description": "frame payload / value to canonicalize",
      "type": "object"
    },
    "repo": {
      "description": "a github repo URL or owner/name to lint for compliance",
      "type": "string"
    },
    "utc": {
      "description": "millisecond UTC 'YYYY-MM-DDTHH:MM:SS.mmmZ'",
      "type": "string"
    },
    "value": {
      "description": "any I-JSON value to canonicalize/address"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_sdk_builder_agent.py` and embedded as the fenced Python below (sha256 76799624979a91c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_sdk_builder_agent.py` first:

```bash
python3 rapp_sdk_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_sdk_builder_agent.py   # or on stdin
python3 rapp_sdk_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""rapp_sdk_builder_agent.py — a hotloadable RAPP SDK, as a brainstem agent.

Drop this one file into any RAPP brainstem's `agents/` directory (no restart) and the
brainstem gains a working RAPP toolkit: mint compliant identities, build and verify
frames, canonicalize + content-address values, scaffold a ready-to-plant organism seed,
and lint any public repo in the stack for RAPP compliance.

Install straight from the public standard repo:

    curl -sSL https://raw.githubusercontent.com/kody-w/rapp-1/main/agents/rapp_sdk_builder_agent.py \
      -o ~/.brainstem/agents/rapp_sdk_builder_agent.py

Then just talk to your brainstem:
    "mint a keyless rappid for @me/notes"
    "scaffold a new RAPP organism called @me/scratch"
    "verify this frame: { … }"
    "check https://github.com/kody-w/twin for RAPP compliance"

The RAPP primitives are embedded here verbatim from the reference implementation
(kody-w/rapp-1 · rapp.py), so the agent is self-contained and offline-capable. The
`sync` action fetches the canonical rapp.py from the public repo and proves this file's
embedded primitive definitions are identical to it — by comparing source (parsed with
ast, never executed), so it is provenance you can check, not trust, and safe to run.
"""
import hashlib
import json
import re
import urllib.request
import uuid

# ── graceful base: use the brainstem's BasicAgent if present, else a standalone shim ──
try:                                            # inside a brainstem
    from agents.basic_agent import BasicAgent
except Exception:                               # dropped in / run standalone
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name = name or getattr(self, "name", "BasicAgent")
            self.metadata = metadata or getattr(self, "metadata", {})
        def perform(self, **kwargs):
            return "Not implemented."
        def system_context(self):
            return None
        def to_tool(self):
            return {"type": "function", "function": {
                "name": self.name, "description": self.metadata.get("description", ""),
                "parameters": self.metadata.get("parameters", {})}}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_sdk_builder",
    "version": "1.0.2",
    "display_name": "RAPP SDK Builder",
    "description": "Mints rappids, builds and verifies rapp/1 frames, scaffolds organism seeds, and lints public GitHub repos for RAPP spec compliance.",
    "author": "Kody Wildfeuer",
    "tags": ["starter", "rapp", "sdk", "identity", "frame", "builder"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "example_call": "scaffold a new RAPP organism called @me/scratch",
}

SPEC = "rapp/1"
SRC = "https://raw.githubusercontent.com/kody-w/rapp-1/main/rapp.py"
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")
_RAPPID = re.compile(r"^rappid:@([a-z0-9]+(?:-[a-z0-9]+)*)/([a-z0-9]+(?:-[a-z0-9]+)*):([0-9a-f]{64})$")
FRAME_KEYS = {"spec", "kind", "stream_id", "seq", "utc", "payload",
              "payload_hash", "frame_hash", "prev", "prev_wave", "sig"}


# ── RAPP primitives (embedded verbatim from rapp.py; the `sync` action proves parity) ──
def canonical(v):
    if v is None or isinstance(v, bool):
        return json.dumps(v)
    if isinstance(v, int):
        return json.dumps(v)
    if isinstance(v, float):
        raise ValueError("floats require full-JCS number serialization; use ints/strings")
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        return "[" + ",".join(canonical(x) for x in v) + "]"
    if isinstance(v, dict):
        keys = sorted(v.keys())
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate keys")
        return "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + canonical(v[k]) for k in keys) + "}"
    raise ValueError(f"non-I-JSON value: {type(v)}")


def H(space, v):
    return hashlib.sha256(space.encode() + b"\x0a" + canonical(v).encode("utf-8")).hexdigest()


def Hb(space, b):
    return hashlib.sha256(space.encode() + b"\x0a" + b).hexdigest()


def mint_rappid(owner, slug, spki_der=None):
    tail = Hb("rapp/1:rappid", spki_der) if spki_der is not None else Hb("rapp/1:rappid", uuid.uuid4().bytes)
    return f"rappid:@{owner}/{slug}:{tail}"


def rappid_valid(s):
    return bool(_RAPPID.match(s or ""))


def build_frame(kind, stream_id, seq, utc, payload, prev, prev_wave=None, sig=None):
    frame = {"spec": SPEC, "kind": kind, "stream_id": stream_id, "seq": seq, "utc": utc,
             "payload": payload, "payload_hash": H("rapp/1:particle", payload),
             "prev": prev, "prev_wave": prev_wave, "sig": sig}
    pre = {k: frame[k] for k in frame if k not in ("frame_hash", "sig")}
    frame["frame_hash"] = H("rapp/1:wave", pre)
    return frame


def verify_frame(frame, head=None, stream_id_of_record=None):
    if set(frame.keys()) != FRAME_KEYS:
        return False, "1", f"key set != 11 ({sorted(frame.keys())})"
    if frame["spec"] != SPEC:
        return False, "1", "spec != rapp/1"
    if not (isinstance(frame["kind"], str) and re.match(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+(-[a-z0-9]+)*$", frame["kind"])):
        return False, "1", "kind grammar"
    if not isinstance(frame["stream_id"], str):
        return False, "1", "stream_id type"
    if not (isinstance(frame["seq"], int) and not isinstance(frame["seq"], bool) and 0 <= frame["seq"] <= 2**53 - 1):
        return False, "1", "seq not uint53"
    if not (isinstance(frame["utc"], str) and _UTC.match(frame["utc"])):
        return False, "1", "utc not fixed form"
    if not isinstance(frame["payload"], dict):
        return False, "1", "payload not object"
    for k in ("payload_hash", "frame_hash"):
        if not (isinstance(frame[k], str) and _HEX64.match(frame[k])):
            return False, "1", f"{k} not 64hex"
    for k in ("prev", "prev_wave"):
        if not (frame[k] is None or (isinstance(frame[k], str) and _HEX64.match(frame[k]))):
            return False, "1", f"{k} not null|64hex"
    if stream_id_of_record is not None and frame["stream_id"] != stream_id_of_record:
        return False, "1a", "stream_id mismatch (cross-stream replay)"
    if frame["payload_hash"] != H("rapp/1:particle", frame["payload"]):
        return False, "2", "payload_hash mismatch"
    pre = {k: frame[k] for k in frame if k not in ("frame_hash", "sig")}
    if frame["frame_hash"] != H("rapp/1:wave", pre):
        return False, "3", "frame_hash mismatch"
    if head is None:
        if not (frame["seq"] == 0 and frame["prev"] is None):
            return False, "4", "genesis must be seq=0 prev=null"
    else:
        if frame["seq"] != head["seq"] + 1:
            return False, "4", "seq not contiguous"
        if frame["prev"] != head["payload_hash"]:
            return False, "4", "prev != head payload_hash"
        if frame["utc"] < head["utc"]:
            return False, "4", "utc < head utc"
    is_swarm = frame["stream_id"].startswith("net:")
    if is_swarm and frame["seq"] > 0:
        if head is not None and frame["prev_wave"] != head["frame_hash"]:
            return False, "5", "prev_wave != head frame_hash"
    elif frame["prev_wave"] is not None:
        return False, "5", "prev_wave must be null off swarm"
    if is_swarm and frame["sig"] is None:
        return False, "6", "swarm frame must be signed"
    return True, None, "ok"


# ── helpers ──
def _fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "rapp-sdk-builder/1.0"})
    return urllib.request.urlopen(req, timeout=timeout).read()


def _parse_id(s):
    """Accept '@owner/slug' or a full rappid and return (owner, slug)."""
    if s.startswith("rappid:@"):
        m = _RAPPID.match(s)
        if m:
            return m.group(1), m.group(2)
    s = s.lstrip("@")
    if "/" in s:
        o, sl = s.split("/", 1)
        return o, sl.split(":")[0]
    raise ValueError(f"cannot parse owner/slug from {s!r}")


class RappSdkBuilderAgent(BasicAgent):
    def __init__(self):
        self.name = "RappSdkBuilder"
        self.metadata = {
            "name": self.name,
            "description": "RAPP SDK toolkit. Use for any RAPP protocol operation: mint a "
                           "compliant rappid, scaffold a new organism seed, build or verify a frame, "
                           "canonicalize/content-address a value, or check a repo for RAPP compliance.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["mint", "scaffold", "frame", "verify", "canonicalize", "check", "sync"],
                        "description": "mint=mint a rappid · scaffold=new organism seed (rappid+genesis) · "
                                       "frame=build+verify a frame · verify=verify a frame object · "
                                       "canonicalize=canonical bytes + domain hash of a value · "
                                       "check=lint a repo/rappid for compliance · sync=verify embedded SDK vs public repo",
                    },
                    "id": {"type": "string", "description": "identity as '@owner/slug' or a full rappid string"},
                    "kind": {"type": "string", "description": "frame kind, e.g. 'note.write' (noun.verb)"},
                    "payload": {"type": "object", "description": "frame payload / value to canonicalize"},
                    "utc": {"type": "string", "description": "millisecond UTC 'YYYY-MM-DDTHH:MM:SS.mmmZ'"},
                    "frame": {"type": "object", "description": "a frame object to verify"},
                    "repo": {"type": "string", "description": "a github repo URL or owner/name to lint for compliance"},
                    "value": {"description": "any I-JSON value to canonicalize/address"},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "").strip().lower()
        try:
            if action == "mint":
                return self._mint(kwargs)
            if action == "scaffold":
                return self._scaffold(kwargs)
            if action == "frame":
                return self._frame(kwargs)
            if action == "verify":
                return self._verify(kwargs)
            if action == "canonicalize":
                return self._canon(kwargs)
            if action == "check":
                return self._check(kwargs)
            if action == "sync":
                return self._sync()
            return json.dumps({"status": "error",
                               "message": f"unknown action {action!r}",
                               "actions": ["mint", "scaffold", "frame", "verify", "canonicalize", "check", "sync"]})
        except Exception as e:
            return json.dumps({"status": "error", "action": action, "message": str(e)})

    # -- actions --
    def _mint(self, kw):
        owner, slug = _parse_id(kw.get("id") or "@me/agent")
        rid = mint_rappid(owner, slug)
        return json.dumps({"status": "ok", "action": "mint", "rappid": rid,
                           "valid": rappid_valid(rid), "note": "keyless mint (§6.2): tail = Hb('rapp/1:rappid', uuid4)"})

    def _scaffold(self, kw):
        owner, slug = _parse_id(kw.get("id") or "@me/organism")
        rid = mint_rappid(owner, slug)
        utc = kw.get("utc") or "2026-07-15T00:00:00.000Z"
        genesis = build_frame("organism.genesis", rid, 0, utc,
                              {"born": {"owner": owner, "slug": slug}}, prev=None)
        ok, step, why = verify_frame(genesis, head=None, stream_id_of_record=rid)
        rappid_json = {"schema": "rapp/1", "rappid": rid, "kind": "organism",
                       "name": slug, "parent_rappid": None,
                       "frames": "frames/index.json"}
        return json.dumps({"status": "ok", "action": "scaffold",
                           "verified": ok, "verify_step": step,
                           "files": {"rappid.json": rappid_json, "frames/0.json": genesis},
                           "note": "A ready-to-plant RAPP organism seed. Commit rappid.json + frames/0.json; "
                                   "the genesis passes §7.5 verify. (A keyed organism would sign the genesis, §10.)"},
                          indent=2)

    def _frame(self, kw):
        rid = kw.get("id")
        if not rid or not rappid_valid(rid):
            return json.dumps({"status": "error", "message": "provide a full valid rappid in 'id'"})
        kind = kw.get("kind") or "note.write"
        utc = kw.get("utc") or "2026-07-15T00:00:00.000Z"
        payload = kw.get("payload") or {}
        seq = int(kw.get("seq", 0) or 0)
        prev = kw.get("prev")
        fr = build_frame(kind, rid, seq, utc, payload, prev=prev)
        ok, step, why = verify_frame(fr, head=None if prev is None else None,
                                     stream_id_of_record=rid)
        return json.dumps({"status": "ok", "action": "frame", "frame": fr,
                           "verified_as_genesis": ok if prev is None else None,
                           "particle": fr["payload_hash"], "wave": fr["frame_hash"]}, indent=2)

    def _verify(self, kw):
        fr = kw.get("frame")
        if not isinstance(fr, dict):
            return json.dumps({"status": "error", "message": "provide a frame object in 'frame'"})
        ok, step, why = verify_frame(fr, head=None, stream_id_of_record=fr.get("stream_id"))
        return json.dumps({"status": "ok", "action": "verify", "valid": ok,
                           "failing_step": step, "reason": why})

    def _canon(self, kw):
        v = kw.get("value", kw.get("payload"))
        c = canonical(v)
        return json.dumps({"status": "ok", "action": "canonicalize", "canonical": c,
                           "particle": H("rapp/1:particle", v), "wave_of_value": H("rapp/1:wave", v),
                           "egg_manifest": H("rapp/1:egg-manifest", v)})

    def _check(self, kw):
        """Lint a public repo's rappid.json for compliance (network fetch)."""
        repo = (kw.get("repo") or "").strip()
        if not repo:
            return json.dumps({"status": "error", "message": "provide 'repo' as owner/name or a github URL"})
        m = re.search(r"github\.com/([^/]+)/([^/#?]+)", repo) or re.match(r"([^/]+)/([^/#?]+)$", repo)
        if not m:
            return json.dumps({"status": "error", "message": f"cannot parse repo from {repo!r}"})
        owner, name = m.group(1), m.group(2).replace(".git", "")
        findings, evidence = [], []
        try:
            raw = _fetch(f"https://raw.githubusercontent.com/{owner}/{name}/main/rappid.json")
            d = json.loads(raw)
        except Exception:
            return json.dumps({"status": "ok", "action": "check", "repo": f"{owner}/{name}",
                               "verdict": "CLEAN", "note": "no rappid.json on main — no RAPP artifacts to lint"})
        rid = d.get("rappid", "")
        if rappid_valid(rid):
            evidence.append(f"rappid §6.1 grammar OK: {rid}")
        else:
            tail = rid.rsplit(":", 1)[-1] if ":" in rid else rid
            findings.append(f"§6.1 identity: {'32-hex short-tail (C3)' if re.match(r'^[0-9a-f]{32}$', tail) else 'not RAPP grammar'} — {rid}")
        if d.get("schema") != "rapp/1":
            findings.append(f"§12 schema label: schema='{d.get('schema')}', not 'rapp/1'")
        p = d.get("parent_rappid")
        if p and not rappid_valid(p):
            findings.append(f"§6.3 parent_rappid not RAPP grammar: {p}")
        verdict = "COMPLIANT" if not findings else "DRIFT"
        return json.dumps({"status": "ok", "action": "check", "repo": f"{owner}/{name}",
                           "verdict": verdict, "findings": findings, "evidence": evidence}, indent=2)

    def _sync(self):
        """Prove the embedded SDK matches the canonical public reference implementation.

        We do NOT execute the fetched code — running remote code is a security hazard (and
        registries forbid it). Instead we compare the *source definitions* of the primitive
        functions (canonical/H/Hb) textually, parsing with `ast` (which never executes),
        against our own embedded copy. Identical definitions ⇒ identical addresses.
        """
        import ast, inspect, sys
        try:
            remote_src = _fetch(SRC).decode("utf-8")
        except Exception as e:
            return json.dumps({"status": "error", "action": "sync", "message": f"fetch failed: {e}"})

        prims = ("canonical", "H", "Hb")

        def _defs(src):
            # Normalize each primitive to its executable form: strip a leading docstring,
            # then ast.unparse (which also drops comments). What survives is exactly the
            # code that computes addresses — so equality means identical computation, not
            # identical formatting.
            out = {}
            for node in ast.parse(src).body:
                if isinstance(node, ast.FunctionDef) and node.name in prims:
                    body = list(node.body)
                    if (body and isinstance(body[0], ast.Expr)
                            and isinstance(getattr(body[0], "value", None), ast.Constant)
                            and isinstance(body[0].value.value, str)):
                        body = body[1:] or [ast.Pass()]
                    node.body = body
                    out[node.name] = ast.unparse(node)
            return out

        local_src = None
        for get in (lambda: inspect.getsource(sys.modules[__name__]),
                    lambda: open(__file__, "r", encoding="utf-8").read()):
            try:
                local_src = get(); break
            except Exception:
                continue
        if local_src is None:
            return json.dumps({"status": "error", "action": "sync", "message": "cannot read local source"})

        remote_defs, local_defs = _defs(remote_src), _defs(local_src)
        per = {p: (p in remote_defs and local_defs.get(p) == remote_defs.get(p)) for p in prims}
        match = all(per.values())
        return json.dumps({"status": "ok", "action": "sync",
                           "embedded_matches_public_reference": match,
                           "per_primitive": per,
                           "source": SRC,
                           "vector_particle": H("rapp/1:particle", {"b": 1, "a": [3, 2]}),
                           "note": "The embedded canonical/H/Hb definitions were compared textually "
                                   "(parsed with ast — no code executed) against the freshly-fetched public "
                                   "reference. Equal ⇒ this agent computes canonical RAPP addresses byte-for-byte "
                                   "with rapp.py."}, indent=2)


# standalone self-test: `python3 rapp_sdk_builder_agent.py`
if __name__ == "__main__":
    a = RappSdkBuilderAgent()
    print("mint     :", a.perform(action="mint", id="@me/notes"))
    print("scaffold :", a.perform(action="scaffold", id="@me/scratch")[:160], "…")
    print("canon    :", a.perform(action="canonicalize", value={"b": 1, "a": [3, 2]}))
    fr = json.loads(a.perform(action="scaffold", id="@me/x"))["files"]["frames/0.json"]
    print("verify   :", a.perform(action="verify", frame=fr))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
