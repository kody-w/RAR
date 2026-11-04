---
name: "rar-kody-w-rapp-sdk-builder"
description: "RAPP SDK toolkit. Use for any RAPP protocol operation: mint a compliant rappid, scaffold a new organism seed, build or verify a frame, canonicalize/content-address a value, or check a repo for RAPP compliance."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_sdk_builder", "rar_sha256": "eaf3bf3a686d9fb08fc8f3c0b05f59075c8a334a68c5d8fe678f39aa81dc27e5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["starter", "rapp", "sdk", "identity", "frame", "builder"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/617Z7PjRrLlX+H2+yDpobtJwkMbinjwIEGQAOH5NDGCt4S31Gp/+xZ5b7fs7Cg2lqHQJYiqrMyT7qSi9PMHbxzSuvvw/Qe5DteNnZVhHI1R9+HjhzDqgy5rhqyuwOsrraobnZM3Q12XRTZ83ph9tInrbuNV6+b1tunqoQ7qclM3Uec9932/uWfVsPE2QX1vyswD3zuvabLw46YPvDiuyxC8rKJ5U3eJV2X9fdNHEXjrj0AR8ONmirosXsGiuPPu0cdN4FV1lQVemT2ibVBXQ1QNn7ww7KK+B6smrxzBKrAxSKOgAL90UVO/1Hyp+EWPIPoMLIwWDzxG/Yfv//sfHz9k4PuH73/+EJRe3z8tBprqYcE8VYk6OgEngT2lVyXgZbMC2CrwDEwF0u/gpzCKN+9P3/ZRGX/c/Od/FrPXJf133/9Ybd4/XvAEZvPD5tu3d5+TaPj2xw9vP//44bun7j9+AF8+9wNA/9vvPpf1HHXffveriKFbfyPw+cnir3J/ALufoP/44Q9rnp8uGsau2jy1+/zP56p3Jb77v4r74qp/L/LLyr8l9uXRfy/ztexvCXyLlX8v8W3d3xL523D794Jfq/+e3Gd0/g2Bz2V/z0drFfwN/4BV3/5B0PuCvK+rz+F4b/pvfwbiBm8YeyAQiI66ru5+/PDxz7L/8AGBB7LQS55IbeIfP4xVUdVz9UXPn9/+/o/ul78n7G35S4n//hLTH38Xjh9/jaKPv/H/xz857uOvkH/8CtY/fvkNEtESRM2w4V9/ntp6/Sb6/v8Rqc2v+fz9u/Uff48OyO1vo+9++e7DL6DuVOBpfDMWlJH/+I+NkgVd3dfxsNGDegQ1c6yGDFhZ/VgZadZvwD9DGgF9gMV95pfR+zpQgPPoDew63vz0XwUo6Z/m7bPk/rMPi3/6b6Xsp88bA2yvuyzJKq98VcYfK+9Z4J6iG1BLo26Kwo2/DtEnUM8+Pb9ssmrz0x9F/fO163Oz/gTaQPhc8lTsyh5AoW76sYw+P5W206h6VxH4BWAdBSMQWNbAP5s4AxX4IzCmr8spAvuBCn2RleUmzDpgTd2tL9kAhO+fwn766Sff69Mfq7cSjGzeulS/BQu+qrP59AmYEZdZkg4/VlGQ1ptvfv7lm83/2vzfdr2EP89QQQd4hxhoeNQv5w1IwfEOlgH0gb8iL3xB/PMv72ACMVX03q6y6G1zmVVFFH5BVpfoTzCGb/wIIArQvDd1N2RVsnn20kO8+arvq2V1w7OdpXU/bMKoiaowqoIVSPWAOV+RrOph04NG28frx83YR69Tf/I776XiHZQPb/hpo7Dqq2mDfz3VfC36mh5f/f72OxDSfdNvmC8iPm/OzyDbNB7wfNp572fE3ptfnt3/fTsQ/urkP1bPPho9oXpRgDd4wCKATPDu0k9Pnz978R04tv9y9muNN4C4M2oPHN79WPXv0ex1T1cENVBl3SRjFj47+P98D6k+rUdAFp74AU2fkt69EL575RWD/zJyNz+O8G6PvtAeytoLvWdCfaE7H5+FwNt8xfTN3pdErqubt3Ctq+gVxu8wfOFDXzcBRH967eu3P/0mqr+t6mfYD143fPcKcaD7j9WvRyXPL+Dwue6KZ6C8hL7Tr3dm9SuvykCEDNmQPXPpjT09Jb6XxOpVJfvf06cNtPkjgXrRp/535AxkACgiQ/2pKZ/H/J6ngegBh5Qvjgesbka/BE5+Ua53pwLrAA37K/71hPAADPVApoMC6L1CP+7q+2vfuyjwugq9LnzJfKX/sxAHY1duPvX6aZMOQ9N/vwUlbv6cZEM6+s8IfjfrMzht+5sa+Gm/vQNIt++u+NcR8fb5VG/+9/bzV3f8221v5RlUunwEWQvsKp4Zt9Zj92skvHeUt3YG0C2itXwC/8aKXzj91z3agsSOQE/5svgPXPmF5FdHAGeWINSf20BN84Yg/XXjO3t+BekrBL7f/PyKdxjf/PLrsjeu/AXLNxx/C94wA2/+hQ+fEl42f+H/2R1E4ATK3zNho7sfhSFQLY26V076oCDcf3XxK19BWXvVwt9UjB8Bhfqt04DCu51PvDACMH8HwrN+CfjasZ7k5tPT6QDl6C3w6xgU0yr6BNrQM59fVQiU92fn/+kLIYkjANZ7rf6aGF+O+VMovqL6KRp02em16wkqyPpvetBhvtj6FQNQtuOsyl5d/QXHW4I+TwBRkQ1fyo6/vgD1umeG9yBYAB7fgsceCJuBJ0CK9cNH4PdnGX7vnOEbBtl7uwbqVE93PGPt1WBf/gR7QHsAzOK5/al378XRew94Dj/ApggU2A/fV2NZfvxQgej409DznG+8Z9yAatw/ZyNwGBhxnlXm+fSG4/Pb72fFZ3D/8B7h75H97sMvkfzDn2a+zbdvK6FnG+iz/rsvW15x+8Mr2aDfT4NfVrz9+sMfXtb+kwt9WfPbwvfDr85+EpseFMKwflaGTQqIxbOvvw+SXzc/8fyhfDcIxMH2N/n6azp8NRIE2RdtvgbGc3Se+t8G03MArUYwOf73CzDw+AUd8PVlA/j7JgZ8+a0Bz8enSs8t4KwPYHgd1ubpvufMCObTX74I+JNr/oAOCIevJ7yLeHvzIqbhn/e/t5n12Ra/+S/A7qNu25dj8s2LC2xiEEtfXP6uy1/oBrrZX4h+U+z57uMm+px83nzzLIOf5y4bom+ezRLE7bOKfPdXIhtvffbufyX1/fVm++5YYPcfAP2T9S8X/QV+b+XxrRyY19PT7jcYnhn0FPyKk99Hxl9pPA7BX2VOWWaA9dQgX02D3Xzjgs8nRfnEcYYkfa8o3+v65/v9fvvmr0S+bPsLnUFrPnx6sdi/tH773v4//PIyux0BQwmfYfme3//4C3QAGxje/rvHz2CuGQBrGrz3AvE+goDlndd96p8cbbv/vAMKg+e3bgne/avh5H1Zn3qALIN1kRcjfox4OImHVOzvyDggYyTY+TssxqgdgQWkhyAoeB9gIRlHOAFeU55H7sMAJiLsmSOvqvrPJ9/Mnke/86lPQxdFv75+C8qXzm86PtH4Ogu9yt2b6j9/8HEUrJTQ/kC/fdgtZJIw5vvn5jRBSc0/8vIMpycL8bGiXMoBHfILzKhxPkw3QjYMba9ke/HIF8aRCf0o291wkojHCHK9m4HlSMy30E3uZZou9b1iXajxwVEdD+YDvWVrG68TLnK7LUTYMbpQKBmrsCfEQi0nzaPFcr6okfzKcShX2idSkIs0gFbrxHW65qlSjuVgIKpYdzDGacBtc13LU4OJAxfF2N4nznf35J+Fx+hmJUVTpaBc0evevrGP41znwvUWCfj1tFxuZYMRx+tdcq+hIR1Tm115SW1oIjFyBLZShJfPsK+IweVxqulbat6dR3C6toQKkY80RKTHZaonQz6NtjpNI3GqusPVNuomJ7YGuq/u+kpyJLEd10JdhNQsFrekq+OunWl91Pcrwxtbd2dHwRF3kQqu1OZEc9y5vjsT3I1KRpYZrlg3dd5W5ILpAusdV3XC10YxqDKAuYvJu8c9ToilTUks6ZgcFyTCENxZhJMhXr3umkC23Uxslev+dAYpeCjGhJOd6UHy+5iKsG17RfXeFZWmF2Zev5DJESPI1elu0byFKEI7XIhTLF89iwh2nbybBXE/JTFmIsy1P9PF6Zye9bm6BAbhaYpisAl8Q9TYHbYae7yj4y52ZJy7GCnljY8BX9RacAP6cmUqBXWYOLhRj1XtHmQVjxYgG8v1XgjZRWKQqrX0QDF2Mr+qbONOZu7Lt06Zc/360CoXjMAtmZLb4EQlsYslgr2rmeZ8ZTFCcrQTvk3J0ofCXuITzCwnKN4+2oCE9iwUTWo8K9w5KGTruJ9ZtmGXsetJI0zOZwYuA7nZK0YXMkQFW2sjCO2gt4i2lFxVe5ZPENfDBJ+v1WG4FpF1wkpNxgt5YmU7NSERW+iJjo9IuXtk1F519yt2aPRJUQJZLB43BU3lHqUnZuG16XYzNJSukpKsMpI4PB7BwVU1zl7PtH/MEVInaGJnJFO918acVTKNYBtFGFIl7w+LmEh05fZaIyOHaFL43jaw2y0Xg94reEFEkjXRG/oiqQKpFEjGs82hCdBmlVz87vLUevXHNMx0OiIhk3IPsHLhTnogiZHh5U5aayqP58qBPNTDtrFO/uFcWJgnaLxleepKn5XYHNQoiynRYB7dvkxVRDcf9ui1JwRu6Qssi+b2dDcYV7gaFHcvsMw8VCvzuHe2ZgTmqrloPnNJxlU7jEeQmd0d130oe6lwDeTZswkGShk0q/PlUbqG6OEC1s6dnS77CoG1poAgqu+uo3JM5PsiMaq4RCcnMPcPATnlEu/VXU08IOWWnWsrOh1mYfdQ0kyWk+N6TASKng26R8tiXxGFO88XerZl+nj3aeWeac0Vrs6F05fAByrKhqc+S4Jiy7ucjpiZkUsFOpGCUqMBIboLDe2uoxDsry633TMYtg+a9oycmDllcteemTrhd6I136HZ55Mg0zG2GuObEDs6MR0PYd8wZX2uimsuee6CCgxkstmBvaswejgqq8Mc1HmZLftw5GkmCCC2YHa5OU/LWc74RqetJUcLTxFq+7C/pLmY367FeOCBEA5Ezr3n++V65Kcjbe75OEd6kyVRiSQHSQtRybYFeGYDk9c5ElElUmrul2f5mDT5nudYdKBwiboiJcKbXryTx3nldmE28cm8p9lFS6PTdLqcESFKcz5Q9zf9nDj+7OuVdlyOtQi3gjEw7poUh4zzT1ef2MFaTCLaqTvUkjMUuzvs+Y117FruJuoaP6pigQkOHwe5opMuv61ZyFcRtF/pst+mj4LDIuAAnBTreTH4oiG2EiFRtNm4pkgn6YHninoxGKTGIroMD5Zmpkbi160WdyCMtw9uSXH4pqltUkjy0demrJw5tMr8GYmE+2n0FXrWE+Ec+f1hBQEaeSNi44cwYcwHa5wiMnYGXIo8py+E8VQ3AldI1xVfa0HY81ILMUUxBh1KK5S5Z/jzlE6c3p8N+HTiuWrA1VOWxqcxYGnfXw6rRic+2XTKwQ6xfm6Bw6wOF7ijwt6XSg0b8sZwSH7fMw0dQRh8hkQ2Ty47upXJMM3tADoh0YA0DC3yecy7FkcfXBmzl1RQFvbBmzcxPB6rsUJyyRH5/QHifLpQDa5YFYtXs925J85xlIPYejizK+Z1ScBCvN9WNkwywYIlnZzc7q62vzHMrGXUidnOxWPnGqvXHYKrmd7n9MI0+vYhjVKGi8cjUzYmUlTK0tfKQdvf0eSgLVdchujrjb42N94lxFpmt6yOrUKww1NhwJxJuU4uc4XwGMjSZMPDdyt3emgBf0sPOpoG/Fkp/JT1bpq4bHvhKjgg++hDziYMtoAUzenlQYmwNtIVjQnRQd+JTZccTStgqUvuEjs1jLuASyoVhvoi55lsFBWUuMHbGtvFgn6uMbIgZkopt+opkQJJZvwoBsLhYAs55KhGk2tTZO80s7/dNfZxSgAzU89pR/EyMnbONEdevUUoufIRBEIVyUFiB2FA/YWix8KkSenEuPOoKheaq9kZlmWaGALTtsgwTPG2TxFfOIaLqgLEgqlKjFhVq4fo1c4VqdjI9etLdrzJLBdUmr1AmRShVJTVrA96xv1I21Q7VoVWH8kh9WKS0Yl5rWZpj7EsDxlo0V8K64bvRUvDbj5z5XB/t5dTfmCIGj8kAo3uM/zaOdnde3DSGMhgrp8NK3btlRFSn9LYpTlq/G7tCvaqec3Qr9253blnQNHc3HNo5Ua3TsBvY7iO72ri4PtK5C8oeYHc7PE4kuuCXE4mHeBHM+N5pZgMiLpkSqNNiTlj4vFALo0nJmR1sSD4suMG5Wje4sLecixKITttZPW1MMekZC9olc+hlqYP5ubq+uIz/Va92NfbpIyURCho6LW3UZKO7XmfXCSpdJv+hCQomhUB7CqJfzxkYyql4lXBrZQgwwE52TuOvLbuBXFi/5hI2CHgwl0NFbvzNglOAbvWDZ+rglu4gfdoa0RCB3tXAnhgJRjLZI2MdWuicoBGvFmfz2qzarezOwMPkRQePxqCsk5lA3HCLhi5iwwzc0IcIeEsPTIeJYxDjjZNIsULHqRyhFRQIlZ3LbP1a8BwQ6FSc7DMsCxdzyzFUUFExeNlwHmEN5ZbnJTYTkcpNpEAmV/vvO8os0rDDlxdZlwwqoPny2iqbLEzTdBieGcO45VlzYTbyYdhwimcbFssW49p3HK6SzV0VlBMZA0Op/bU9pRX4xmb2eu98WZqfhz2lpOKDL5FZdl6EPKqSVjJn6+cKbtKkxxPp8vhoS1552NI8gjvB2WhzZueJtsiSpS1SXDvtj86t9sjNbtZUurhWsJVB5NWgO4aqmgqa2dYrt0MMSPj65bDuAmu+okkTanvTxB304Mkg+ZiH816oF9aZKQZ3G7OVpjSW9Yrk8s+7dZF08PkTuR+z3AMdOpQqxwXeSu2OSzn+Dk0kRDwsEsA3Tu+lmRryYB6AqPoVyPJB3W2tVxxrEC5EFHs4CxZaqomJci8N00ehsajRfd6lPlNT/b3Q/1QOKYQGapAV8Ws1/VMLCWDzs5yVWG138mYlVcPDj+emsQWA1oUcsB5NHpysYstXfRyuog9u7eXJlZtWs/nqU8ZeeVne7/c3Ds1yFpxul9uQQ+qsAwIrEXKl1VI+LChDzcboJszj8M2uiCISpqAwDJh+IhKmG4f0LnoH+Kw85vjDQ84QSjCG4YKzSNLGJhUOEvWToJOaizg7rXQXC/86ZwPRcz0oMScKNWnICjG4j2sFBDbW8TcKXSnxhPRKto+HKPjYVkow7idYhdQsPqaVgJ5gDPQ5j2JCG64I87oNvfnMXeYtXa3WSmm8xEMuOMqGxmS2EuxdIbIkDXvibjr+FV/d8qY3Tsg1hkioNEI0aOzmJ8X1r5Xh+6U71Eop/jD0cg4Y+uV4hm754Z7dgL5foos9rDj2R01kNRkC1En2tfthSbuuQqIVIPhWm/XwalMp3v7MLrUj03MwE/eCV7LaTyJ+kEliEuztBxnxyRZ2A1xsdDTsHdtSGP3ucZcyxuc3QYYNDfmzuCdWJSRvhMCP0ARU8FPhdkeOT12HSuROZYXmdXYLniSsHdPYdaOt+Scvma0cBzjkMqPMTAeE0VI2pNjXzvFKeb2Hl/zYVjd8tkh7hTe77tCEK3yTCXROauIYUEZ25IcJuEntaYfwKO5CsuMABuLhzUiOl2I2WJ0qNKkNu48jy+mbX5FHFgk+YaHF3k3lEqA2vAR5saSfISZM3Uq5h0urQG6vHcWd9Z2duUDktS+lezdQOOmRmnqo+Lc506f1QuNHR64nJvT1Vghg3d4wuNm38fpU9a1KHU34blPeExI1HCJhiSrw4vSk61xyqrk3hfmcuF2I4nmiAL6XVs7yLWCu1Of6gmXuqQNlas0tF4493XQ1HB+toL9cnDCKNvPNxc6FD6DzQGNUFwWY7DqrWrZl74GONTMN+jlEqjX/bW7qK3etyaEFY2En/as3QezYNIWmx6hC0Q9VP0Boic0eHg10rCK+MlOCyu29oDwdO4BI1fi4XMCYgzLGDlwCw1ClmBxovddgFqUnfUGIfEw1tHMXef4fblVilO61DtA+Tu2wPfKvKODHQlCyi2nkjNqXDeKpRTi2LSHVI4buWM0xoqqgiO47NRU3fk++n7r1dm9CPzhmp1CxNunYZSSAQ4HRUvVJ+ZmyMnWb9eknKdhbL0pbNsEBf2VVx6PTklF2z0S1vaolV6zY28lEqZ6H53MRVPKY+dlKktOe70jIiVh61DjsRvXODCqinDJaT6MVuzZZjkbHk3bqcyj5cIPlz8LNxvf2kbZtec2Nur5FA10o+Q7hJGubM9bRuU6aeXNsm7z+34u9b0wNum10sQq49ccq+5D29JoLgQwBSWIUlf4KbxcWwOQiHtz4MeD750qjRltJ8bchzpkrg95tVWFO+9yzEhs93CC80Vb7tp6Xpt1nljTCcRcC9sqR5WchGPNsqHmYTbZQcw4ureHy0F0evgAz1GmHV2V73c4r+DQoNs5X1DZcbfKomVj2mHbRqszcNrVZ0QjjJvJUIZzq5EJ3AyJ2Ur0Y5dicX0X+hlPnXEm6Na+XU5ufySoY34lUmbxpwu6OwACgJfXqEnT4BRm7eBx5TB4l9kOWQ8gPjWn08kbWntoz7qO0GJ+750EWZ3CgZi1d257SoxRnNijO2cioQtiNFv8JGyJ292I/IePbuG6OeHxkUng7qCii4hvSRhmrxwz74qb3NYN+mgHGIrqNalXnd6m0xCZPtfV3WwpvugrXLwkXLRaEOub1MlhOvIc9P1gzu15Fa4tS81zWHpIGFmkAHOqFAadauRDDUymIOueNa0f5mOYbIMFFzsv4aq28DrLW5pwMv2hdbgDdTv1YlK0EXS+lEM9HwR65elY1ivAphYSV1jZo+E1D/ye0I725aaR6A5C6UJo7yGpGuz2SCR2cUPm83kwatpRdoC5CLKvQYweYLD0YPpQSclaUaPzEmtLJfl0xXbFyWdVrRPoQrFPOX1BUmESJUQXMShdsWTa3Qv52HPaUJ5ike2mFAeVYyCXpBNh3rARR+ZjfotLAQkYWngV9rBLe7KbIycQWNbY76nLcBQWW9aY5m4c2B08nLYeorCPC6iOsO9kA0crmCdqUpBceXgASY9KtQTPDeqP0WzavgGn3CkKOetyhRYCDMhGaiK+mDiozDoZNQmztMutk0qV/FHEsHCrqszFCcn2uBCWVx+lNruhD8jqVuxmD6ONKIPMN+n2ou9nT8xpTmAVmomdHaReGWKbPZC+Ar0wltQJeeQ1pE74NtM65X7GU0vsinQJVTWJnUMg+QGY2WE/XgeI407ybUquLBZ4/gHb1cia3Rx90BuzzRtn8Y9NSaJMeK72N7rc7bWmujcr1RiX4Ab3OWMWtN7UbTS4cDFZ6nnU25zen9T7ioh3e9QpqzHOIX+xyvm+y3uCn5MbUz1WA08EI4jMvnMkvGhKz/G6K9YGS6dnzMMZsoV+NCqV0JULXyGE3p/Z1rpXmXobblV8cq+w3yAdtO+GVNxaJHxeYIcihTS9B8uClf2+7HfVxNJreeWibZVCFiNJgSE6sJvuj2wwOSf1QTyIe38Faf3gubDN5CRDjcY/MuJA5mIXLjFeXRfCphSGMErDEE2xIdzBtE6RW2TmwefO1+qySOVIP4ZzuYOuVClBzUQX48FamyrwTGcRkgK2GKwq+KERfLVGQSOw9w3/kA+ChfFbMsyP4RHkVXTsyYxl++4me4KZWkbb3Fqb6pezsY66HJYx3UdWYrcNdCFdHSxo8gk+zMt8ILku7NFhXn0kLyPCYvNcrwnCrCifoMItyxJm4VLHseC8BFoVnq9pCHT+c0piCoPavsDtlR3LhWxJoWqiEL3YRzjsNe1ltAYz1/0be6A94uCte70dxZ3TIvhShK2nQIWJeFkDj8y6v5Dp0g12cmIiTFp717peey1DE7+Lp4SmT+Z093pS2F2E64UubiZLMOZxUFaT8O5tu1IjXBzbu5jefQkZEKSIuDCLY8WXavQijJKtT7rVQqZ7I9tegxczlrcBYuU8ZttY4hO2tBC7NQkODYnd10nwYGXGYhy1mRYpJ/18C4j7+WYeKkEzo/1ekXK8a/PoBKuC0rFwe/dksRo9b0ZDpCbO01TDoN9x5N0Z3Iz3dhFe2YVPkeSAWEMz3XJ9ke4DRx2HuGXONUpgyLZxqGXBY0BHEVYoDJlutoIbYTUMV/tWzG/SZRrPM/wwsz0Yk/RGiA7FrRfBqC5k4/pABsZg1bCM6Ca6oJGFhpScKccwtRHhEdy0I5YhynbmEYqUtkRQ0pFzV+CGbX10vsAYFhCno6SFvrlFUD2kQpPn6OzgwAnd0OdkwONYIk89Z56Tolopi6vuoVGrtljTMHqHaJynookoUHMYj16IymdfV9RUWrcLek/QqLWCQ3IxXXon6Z0keQE+sEuRdPewstZxuvg8VHssYJGwm+XX9YHfrLSrluw8iItFUfQhYan94s9Q4V48rB8HVV37iT0OoQRqVyEI1pmSWzdDr5ox80BJRoSztBHStjjSjCCFO4rgEYnDWMAtFywNGSIMXaruZBOXSrs6Q3jU5ZCwMJg/JnV3GtGOGrtU8uAjHuwYujDOznGv7WpMKfYqHq3F9mLb7WE3sbWZklt7mAfhmOSUMR2QkGp4FMMH+3BARzEyHDCMr4/r6JGIgLl3CMfwZUsj3dgzTbEftbMCqm+/0+XzPjpL3R4nweTUo8GIIEyCJLvjcs8piIQe3UA8HjEuQOXYNfK8DGenOHTGtUfYhEE427HRo2wPTb8/qwzlI6K23s3D2W9vuq6IaLjqy9aPy9zFMV2bFqVfh/xkwdtzZt3Z5kDg12RB4EYNsLrfLdYFGW8Zc7MkBNd3BZ93qXItYNbZsiRkXvRDsRewYIHuRwYjcfF+SSxIqFVVdGU5jPa7S4gJ4cmHimwKrwZ6BrmAW+xyCRnjou0pvhRXPFsOW7ja4iFTRky68rp/7IsJYqFK9K9E7+iA25IrVvV6rsew25/0rL4xkWDRsyqJl5Ygy3EX3yT1hNwgh7mp04Fst1tQuezCtsJ5kfQejuZddtunze0iz5d2NFmsMEdspoorPF9u+drG4da/F9Eg1JWHoxX1SK1k0B4xy7Cy4OrzeCiZrNdx52yZmaRQT6K2oGVPk0cNSoel1W8HVaJkRjFuypohB3wr36IeYllaCEO7DR717aS6065Oil4PJT3UZjFbzeSW55Rp3PTSp0YakRl/qQ+BHeptcQhP1316yBW8WR8No19Rjql56gEmVjQNALC7PlvERWGjG1+BMTXhjsmu6TlYvhwa93i1C1NjYly6XHz2xhayIMel7pgyckjIsptl1EPvOVfXLBP5Jgxrx6EhLNj13WOD66jXJzv3IiNncs0wUOQbB6fZboDbSHXsyYwyQrqFDAryb1cZg11A+P7OUzztODmdkfTV6aK9HDFwy1XsgOd0BMWSgLba8RE/kPPuJj0s/L5XveNNWzFP3buzszdN/5zNENuxAs4oWyNCrBkijM6f7Rw2hdDYzqdc9dXC5Zz6pl8iSvI6WPeJIfdY2d9Ox9lQRSvTjWSZOmtlul2belcEumec+egptfQkxK6m4Hq6pKVUi+tFVFx9RTXMVWDIvroDv4KZ1SgUaQ5suzyf6foGM5rLnuZCpMHglWtGqh0Zbkp8YY6ac5Lgvc90CsYclhGU1xsvNSpOSs2jzCKlIgKy6cfrZR+4dIm7+7gi4KtnaLI4752aYvrJS242NJu7Sm0Fu9LPRi0rXmQi2sm3uttxJ8+0OQrt/j5Nyt1Se4cXrIYsTzOjlY9y1+/27ZkS9ntBEiK45mSozQcqY0U9OtBKa0aDf7GlfRYdJH9wuq3m5JNGW3KitXLCHQqayxGvp5KMbJndGUk147Lc+rNuYNx5fmyH7Iosi+kz08WOhXTL1YwSqUukE45zw3vHVVsEJgdPFaLmCvoSPpLW7nFJ9VM7cc18lKWtVttgYLqPq+bYJ1xq3LWTTyh/faTHMt8ZN6hBKYMhsesVJwBGJt1CuGqueGqWTXAZ0Lto4UcfEh4RRZmMGyHpchBcrzLQHTEJOHHGMcvpY5bAQmZLO2rVIw0VT4ht+Q7i77pUzc9lUx7siqAJHD0UOKeJ4XbkLrBvQGM7QyeX27OTVhy3D9rhcvhxNsPmodAmaLf1LPfIgSj27MW+7Cv3sB9cgSZt8qzwFLUjo4LdUlQUbcml0e41N9w409bAAM6duxKJYLOFOrvtF8CBCVpXqH0bS9kkCOfpxB33cX8dMMHvSrE73YacvMDhdhYyFz16vcDTNP3DD8/bUVkZvV9Y+5fXMZ83O/6/XSJ5uwvy5aLd827M817s96+zvv/XKvzj44cuyIACb/dfnhel3q+YvN1++fS64Qi2fvr19ku/vt3dft5hXYYv1/MGL3n+b0ofXreF32/JNM1zefi8BvblWtZvbo59kfiP1yWy/u1GDtDjM/zhl/8DKa+7Ffc1AAA= -->
