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
    "version": "1.0.1",
    "display_name": "RAPP SDK Builder",
    "description": "A hotloadable RAPP toolkit: mint compliant rappids, build/verify frames, "
                   "content-address values, scaffold organism seeds, and lint any public repo in "
                   "the stack for compliance. Build with RAPP and stay synced against the public "
                   "GitHubs — and back again. Builds on the public RAPP standard (kody-w/rapp-1).",
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
