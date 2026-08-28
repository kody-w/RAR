---
name: "rar-kody-w-rapp-sdk-builder"
description: "RAPP SDK toolkit. Use for any RAPP protocol operation: mint a compliant rappid, scaffold a new organism seed, build or verify a frame, canonicalize/content-address a value, or check a repo for RAPP compliance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sdk_builder", "rar_sha256": "76799624979a91c7f4f87d64b41d1fe5add10f727c672cc25429442a38ef757a", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["starter", "rapp", "sdk", "identity", "frame", "builder"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp_sdk_builder`. The original RAPP
agent is preserved byte-for-byte in `rapp_sdk_builder_agent.py` and in the RCI capsule.

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
