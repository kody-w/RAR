---
name: "rar-kody-w-rapp-sdk-builder"
description: "RAPP SDK toolkit. Use for any RAPP protocol operation: mint a compliant rappid, scaffold a new organism seed, build or verify a frame, canonicalize/content-address a value, or check a repo for RAPP compliance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sdk_builder", "rar_sha256": "eaf3bf3a686d9fb08fc8f3c0b05f59075c8a334a68c5d8fe678f39aa81dc27e5", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["starter", "rapp", "sdk", "identity", "frame", "builder"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_sdk_builder_agent.py` and embedded as the fenced Python below (sha256 eaf3bf3a686d9fb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_sdk_builder_agent.py` first:

```bash
python3 rapp_sdk_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_sdk_builder_agent.py   # or on stdin
python3 rapp_sdk_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rapp_sdk_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_sdk_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rapp_sdk_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
