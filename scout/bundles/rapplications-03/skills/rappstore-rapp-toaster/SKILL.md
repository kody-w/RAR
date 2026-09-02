---
name: "rappstore-rapp-toaster"
description: "Convert a capability between agent.py, SKILL.md, openclaw and openrappter without losing fidelity; toast a raw SKILL.md so it gains a typed contract and can be measured; or soak it to prove it does not drift across conversion routes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/toaster", "rar_sha256": "d4d540104c288152b2761b7890aaf263e58af286acaf702d09422b6f3f198e16", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "toaster_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/toaster:8d8624ff9b7db3bd966f4552dbe3d26637fe7e1379ba1584d7ef34b295acca75", "kind": "skill"}, "tags": ["skills", "portability", "drift", "conversion", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/toaster`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `toaster_agent.py` is
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

Toaster — carry a capability between agent formats without losing it.

A PORT, not a reimplementation. The entire upstream kody-w/rapp-toaster
implementation is carried verbatim; only the entry point changed. A
reimplementation drifts from its original the first time either side is
touched, and then you have two tools that disagree and no way to tell which is
right.

    toast     raw SKILL.md has no canonical form, so nothing can be measured
              against it. Toasting derives the deterministic layer the prose
              actually evidences, and anchors it.
    inspect   what survives a conversion, layer by layer
    convert   project into agent.py / SKILL.md / openclaw / openrappter / rci
    soak      prove it does not drift -- path independence across five routes

Local only. No network, no credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do.",
      "enum": [
        "toast",
        "inspect",
        "convert",
        "soak"
      ],
      "type": "string"
    },
    "out": {
      "description": "For convert: output path. Defaults beside the source.",
      "type": "string"
    },
    "path": {
      "description": "The capability file (SKILL.md or *_agent.py).",
      "type": "string"
    },
    "to": {
      "description": "For convert: the target format.",
      "enum": [
        "agent",
        "skill",
        "openclaw",
        "openrappter",
        "rci"
      ],
      "type": "string"
    }
  },
  "required": [
    "action",
    "path"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `toaster_agent.py` and embedded as the fenced Python below (sha256 d4d540104c288152…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `toaster_agent.py` first:

```bash
python3 toaster_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 toaster_agent.py   # or on stdin
python3 toaster_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""Toaster — carry a capability between agent formats without losing it.

A PORT, not a reimplementation. The entire upstream kody-w/rapp-toaster
implementation is carried verbatim; only the entry point changed. A
reimplementation drifts from its original the first time either side is
touched, and then you have two tools that disagree and no way to tell which is
right.

    toast     raw SKILL.md has no canonical form, so nothing can be measured
              against it. Toasting derives the deterministic layer the prose
              actually evidences, and anchors it.
    inspect   what survives a conversion, layer by layer
    convert   project into agent.py / SKILL.md / openclaw / openrappter / rci
    soak      prove it does not drift -- path independence across five routes

Local only. No network, no credentials.
"""

from __future__ import annotations

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # standalone -- no brainstem required
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            if name:
                self.name = name
            if metadata:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."

        def to_tool(self):
            return {"type": "function", "function": {
                "name": self.name,
                "description": self.metadata.get("description", ""),
                "parameters": self.metadata.get("parameters", {})}}

#!/usr/bin/env python3
"""agentshim — zero-fidelity-loss conversion between capability formats.

    RAPP brainstem agent.py  <->  SKILL.md  <->  openclaw  <->  openrappter

One file, stdlib only, no install. Runs anywhere Python 3.9+ runs, including
outside RAPP entirely -- that is the point: your agent.py should not be
trapped in the platform that birthed it.

WHY THIS EXISTS (the membrane thesis)
    A brainstem colonises a host runtime the way a mitochondrion colonises a
    cell: it does not rewrite the host, it trades across a narrow membrane.
    A capability format IS that membrane. This shim is the transport protein.
    Convert a capability into whatever the host natively eats, and the host
    runs it without ever knowing it was RAPP.

THE TWO LAYERS
    Every capability has a deterministic layer and a procedural layer.
      deterministic -> a typed JSON-Schema tool contract + real code
                       (agent.py has this; SKILL.md does not)
      procedural    -> markdown instructions a model follows
                       (SKILL.md has this; agent.py hides it in a docstring)
    Converting is not translation, it is PROJECTION: each format shows some
    layers and drops others. So we never drop -- we carry.

ZERO FIDELITY LOSS
    Every artifact this tool emits embeds an RCI capsule: gzip+base64 of the
    full canonical record, including the byte-exact original source of any
    format already seen. Converting back restores the original bytes, not a
    re-render. `roundtrip` proves it and exits non-zero on any drift.
    An artifact WITHOUT a capsule (a hand-written SKILL.md) still converts --
    it is synthesised, and the shim says so plainly.

USAGE
    agentshim.py convert <path> --to agent|skill|openclaw|openrappter|rci [-o OUT]
    agentshim.py inspect <path>              # what the shim sees, layer by layer
    agentshim.py roundtrip <path> --via FMT  # prove byte-exact, exit 1 on drift
    agentshim.py selftest                    # built-in fixtures, all directions
"""


import argparse
import ast
import base64
import gzip
import hashlib
import json
import os
import re
import sys
import textwrap

RCI_VERSION = "1.0"
CAPSULE_RE = re.compile(r"rci-capsule:v1:([A-Za-z0-9+/=]+)")

# Sections the toaster itself wrote. They are PRESENTATION, not source: a
# bundled export injects "## Run this", and if that text is read back in as the
# capability's instructions it becomes canonical, the synthesised agent changes,
# and the export stops converging on the same agent as its own source. Marking
# them makes generated content identifiable so it can never be mistaken for
# authored content -- the same rule as "a projection must never be mistakable
# for the thing it projects from", applied inside a single file.
GENERATED_RE = re.compile(
    r"\n?<!-- toaster:generated:begin -->.*?<!-- toaster:generated:end -->\n?", re.S)

# Formats the shim speaks.
FORMATS = ("agent", "skill", "openclaw", "openrappter", "rci")


# --------------------------------------------------------------------------
# The canonical record
# --------------------------------------------------------------------------

def blank_rci() -> dict:
    return {
        "rci": RCI_VERSION,
        "name": "",             # tool name as the model calls it (PascalCase)
        "slug": "",             # filesystem / skill identity (kebab-case)
        "version": "1.0.0",
        "description": "",      # routing + trigger text
        "parameters": {"type": "object", "properties": {}, "required": []},
        "instructions": "",     # the procedural layer (markdown)
        "system_context": None,  # text injected every turn, or None
        "impl": None,           # {"lang","source","perform","extra"} or None
        "author": None,
        "tags": [],
        "license": None,
        "homepage": None,
        "repository": None,
        "examples": [],
        "platform": {},         # host-specific extras we must not lose
        "preserved": {},        # fmt -> {"sha256","b64","filename"}
        "provenance": [],       # conversion trail
    }


def _pascal(s: str) -> str:
    parts = re.split(r"[^A-Za-z0-9]+", s or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p) or "Capability"


def _kebab(s: str) -> str:
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", s or "")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s or "capability"


def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def preserve(rci: dict, fmt: str, raw: bytes, filename: str) -> None:
    """Vault the byte-exact original so a later conversion can restore it."""
    rci["preserved"][fmt] = {
        "sha256": _sha(raw),
        "b64": base64.b64encode(gzip.compress(raw)).decode(),
        "filename": filename,
    }


def restore(rci: dict, fmt: str):
    p = rci.get("preserved", {}).get(fmt)
    if not p:
        return None
    raw = gzip.decompress(base64.b64decode(p["b64"]))
    if _sha(raw) != p["sha256"]:
        raise ValueError(f"preserved {fmt} payload failed its checksum")
    return raw


# The fields that ARE the capability. Everything else in the record --
# `preserved`, `provenance`, `derivation` -- is metadata about the JOURNEY, and
# two artifacts that mean the same thing will legitimately differ there: each
# one vaults ITSELF so it can round-trip to itself, and each took a different
# route to exist. So "did this survive?" must be asked of the capability, not
# of the bytes of a synthesised file. Conflating the two makes a true statement
# ("the capability is intact") report as a false one ("the bytes differ").
CAPABILITY_FIELDS = ("name", "slug", "version", "description", "parameters",
                     "instructions", "system_context", "author", "tags",
                     "license", "examples")


def capability_id(rci: dict) -> str:
    """Stable hash of what the capability IS, ignoring how it got here."""
    impl = rci.get("impl") or {}
    core = {k: rci.get(k) for k in CAPABILITY_FIELDS}
    # When a step list exists it IS the deterministic layer, and perform() is
    # merely its rendering into Python -- so including both would make one
    # capability hash differently depending on which projection you are looking
    # at. Steps win; perform only counts when it is the authored article.
    if impl.get("steps"):
        core["impl"] = {"steps": impl["steps"]}
    else:
        perform = impl.get("perform")
        # A synthesised perform() is boilerplate this tool wrote, not something
        # the author supplied. Counting it would mean a capability with NO
        # deterministic layer acquires one merely by being projected into an
        # agent -- identity changing as a side effect of looking at it.
        if perform and GENERATED_PERFORM_MARK in perform:
            perform = None
        core["impl"] = {"perform": perform,
                        "perform_body": impl.get("perform_body")}
    return hashlib.sha256(
        json.dumps(core, sort_keys=True, default=str).encode()).hexdigest()


def pack_capsule(rci: dict) -> str:
    """Capsule never contains itself -- strip nothing else."""
    payload = json.dumps(rci, sort_keys=True, separators=(",", ":")).encode()
    return "rci-capsule:v1:" + base64.b64encode(gzip.compress(payload)).decode()


def unpack_capsule(text: str):
    m = CAPSULE_RE.search(text)
    if not m:
        return None
    try:
        return json.loads(gzip.decompress(base64.b64decode(m.group(1))))
    except Exception:
        return None


# --------------------------------------------------------------------------
# Minimal YAML frontmatter (no PyYAML dependency)
# --------------------------------------------------------------------------

def split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    head = text[3:end].lstrip("\n")
    rest = text[end + 4:]
    return parse_frontmatter(head), rest.lstrip("\n")


def parse_frontmatter(head: str) -> dict:
    out, key, buf, mode = {}, None, [], None
    for line in head.split("\n"):
        if mode == "block":
            if line.startswith("  ") or not line.strip():
                buf.append(line[2:] if line.startswith("  ") else "")
                continue
            out[key] = "\n".join(buf).rstrip("\n")
            key, buf, mode = None, [], None
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if v in ("|", "|-", ">", ">-"):
            key, buf, mode = k, [], "block"
            continue
        out[k] = _scalar(v)
    if mode == "block" and key:
        out[key] = "\n".join(buf).rstrip("\n")
    return out


def _scalar(v: str):
    if v.startswith(("{", "[")):
        try:
            return json.loads(v)
        except Exception:
            return v
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        body = v[1:-1]
        return body.replace('\\"', '"').replace("\\\\", "\\") if v[0] == '"' else body
    return v


def emit_frontmatter(pairs: list) -> str:
    lines = ["---"]
    for k, v in pairs:
        if v is None or v == "" or v == []:
            continue
        if isinstance(v, (dict, list)):
            lines.append(f"{k}: {json.dumps(v, separators=(',', ':'))}")
        elif "\n" in str(v):
            lines.append(f"{k}: |")
            lines += ["  " + ln for ln in str(v).split("\n")]
        else:
            s = str(v).replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{k}: "{s}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# READER: RAPP brainstem agent.py  (AST only -- never imports or execs)
# --------------------------------------------------------------------------

class _Unresolved:
    def __repr__(self):
        return "<unresolved>"


_UNRESOLVED = _Unresolved()


def _eval_node(node, attrs: dict):
    """Literal-eval an AST node, resolving `self.<attr>` from what we've already
    seen. Anything genuinely dynamic (a call, a name) drops out of the dict
    rather than sinking the whole parse -- partial truth beats no truth."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) \
            and node.value.id == "self":
        return attrs.get(node.attr, _UNRESOLVED)
    if isinstance(node, ast.Dict):
        out = {}
        for k, v in zip(node.keys, node.values):
            if k is None:
                continue
            kk, vv = _eval_node(k, attrs), _eval_node(v, attrs)
            if kk is _UNRESOLVED or vv is _UNRESOLVED:
                continue
            try:
                out[kk] = vv
            except TypeError:
                continue
        return out
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        vals = [_eval_node(e, attrs) for e in node.elts]
        vals = [v for v in vals if v is not _UNRESOLVED]
        return vals if isinstance(node, ast.List) else (
            tuple(vals) if isinstance(node, ast.Tuple) else set(vals))
    if isinstance(node, ast.JoinedStr):  # f-string -- only if fully static
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                r = _eval_node(v.value, attrs)
                if r is _UNRESOLVED:
                    return _UNRESOLVED
                parts.append(str(r))
        return "".join(parts)
    try:
        return ast.literal_eval(node)
    except Exception:
        return _UNRESOLVED


def read_agent(raw: bytes, filename: str) -> dict:
    text = raw.decode("utf-8", "replace")
    cap = unpack_capsule(text)
    rci = cap if cap else blank_rci()

    tree = ast.parse(text)
    rci["instructions"] = rci.get("instructions") or (ast.get_docstring(tree) or "")

    cls = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            bases = [b.id if isinstance(b, ast.Name) else getattr(b, "attr", "")
                     for b in node.bases]
            if any("Agent" in b for b in bases):
                cls = node
                break
    if cls is None:
        raise ValueError(f"{filename}: no BasicAgent subclass found")

    name, metadata, perform_src, sysctx_src = None, None, None, None
    for item in cls.body:
        if isinstance(item, ast.FunctionDef):
            if item.name == "perform":
                perform_src = ast.get_source_segment(text, item)
            elif item.name == "system_context":
                sysctx_src = ast.get_source_segment(text, item)
            if item.name != "__init__":
                continue
            # Source order matters: self.name is set before self.metadata, and
            # essentially every real agent writes "name": self.name inside the
            # metadata dict -- a non-literal that would sink a plain
            # literal_eval of the whole dict. Resolve self.* as we go.
            attrs: dict = {}
            for stmt in item.body:
                if not isinstance(stmt, ast.Assign):
                    continue
                for t in stmt.targets:
                    if not (isinstance(t, ast.Attribute)
                            and isinstance(t.value, ast.Name) and t.value.id == "self"):
                        continue
                    val = _eval_node(stmt.value, attrs)
                    if val is not _UNRESOLVED:
                        attrs[t.attr] = val
            name, metadata = attrs.get("name"), attrs.get("metadata")

    # A generated agent carries its derived step list as a module-level STEPS
    # constant. Not recovering it loses the deterministic layer on the way back
    # in, which shows up as "the capability changed" when nothing did.
    steps_const = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "STEPS":
                    try:
                        steps_const = ast.literal_eval(node.value)
                    except Exception:
                        pass

    metadata = metadata or {}
    rci["name"] = name or metadata.get("name") or cls.name
    rci["slug"] = rci.get("slug") or _kebab(rci["name"])
    rci["description"] = metadata.get("description") or rci.get("description") or ""
    if metadata.get("parameters"):
        rci["parameters"] = metadata["parameters"]
    rci["impl"] = {
        "lang": "python",
        "class": cls.name,
        "source": text,
        "perform": perform_src,
        "system_context": sysctx_src,
    }
    if steps_const:
        rci["impl"]["steps"] = steps_const
    if sysctx_src and rci.get("system_context") is None:
        rci["system_context"] = "<code>"  # real logic lives in impl
    preserve(rci, "agent", raw, filename)
    rci.setdefault("provenance", []).append(f"read:agent:{os.path.basename(filename)}")
    return rci


# --------------------------------------------------------------------------
# READER: SKILL.md  (Claude skill / openclaw skill)
# --------------------------------------------------------------------------

DET_FENCE = re.compile(
    r"```python[ \t]*(?:#[ \t]*rapp:deterministic)?[ \t]*\n(.*?)```", re.S)
PARAM_FENCE = re.compile(
    r"##+\s*Parameters\s*\n+```json\s*\n(.*?)```", re.S | re.I)
SYSCTX_SEC = re.compile(
    r"##+\s*System Context\s*\n+(.*?)(?=\n##+\s|\Z)", re.S | re.I)


def read_skill(raw: bytes, filename: str) -> dict:
    text = raw.decode("utf-8", "replace")
    cap = unpack_capsule(text)
    rci = cap if cap else blank_rci()

    fm, body = split_frontmatter(text)
    body = GENERATED_RE.sub("", body)      # drop what we wrote, keep what they wrote
    body = CAPSULE_RE.sub("", body)
    body = re.sub(r"<!--\s*-->\s*$", "", body).rstrip() + "\n"

    if not cap:
        rci["slug"] = fm.get("name") or _kebab(os.path.basename(os.path.dirname(filename)))
        rci["name"] = _pascal(rci["slug"])
        rci["description"] = fm.get("description", "")
        rci["version"] = fm.get("version", rci["version"])
        rci["author"] = fm.get("author")
        rci["license"] = fm.get("license")
        tags = fm.get("tags")
        rci["tags"] = tags if isinstance(tags, list) else (
            [t.strip() for t in tags.split(",")] if tags else [])

        # The deterministic layer, if the author declared one.
        pm = PARAM_FENCE.search(body)
        if pm:
            try:
                rci["parameters"] = json.loads(pm.group(1))
            except Exception:
                pass
        dm = DET_FENCE.search(body)
        if dm:
            rci["impl"] = {"lang": "python", "perform_body": textwrap.dedent(dm.group(1)).strip()}
        sm = SYSCTX_SEC.search(body)
        if sm:
            rci["system_context"] = sm.group(1).strip()

    rci["instructions"] = body.strip()

    meta = fm.get("metadata")
    if isinstance(meta, dict):
        rci.setdefault("platform", {}).update(meta)
    for k in ("allowed-tools", "argument-hint", "model"):
        if k in fm:
            rci.setdefault("platform", {}).setdefault("claude", {})[k] = fm[k]

    fmt = "openclaw" if isinstance(meta, dict) and "openclaw" in meta else "skill"
    preserve(rci, fmt, raw, filename)
    rci.setdefault("provenance", []).append(f"read:{fmt}:{os.path.basename(filename)}")
    return rci


# --------------------------------------------------------------------------
# READER: openrappter  (skill.json + skill.md pair)
# --------------------------------------------------------------------------

def read_openrappter(path: str) -> dict:
    d = path if os.path.isdir(path) else os.path.dirname(path) or "."
    jf = next((os.path.join(d, n) for n in ("skill.json", "SKILL.json")
               if os.path.exists(os.path.join(d, n))), None)
    mf = next((os.path.join(d, n) for n in ("skill.md", "SKILL.md")
               if os.path.exists(os.path.join(d, n))), None)
    if not jf:
        raise ValueError(f"{d}: no skill.json (openrappter needs skill.json + skill.md)")

    jraw = open(jf, "rb").read()
    manifest = json.loads(jraw.decode("utf-8"))
    rci = manifest.get("x-rci")
    if rci:
        rci = unpack_capsule(rci) or blank_rci()
    else:
        rci = blank_rci()
        rci["slug"] = manifest.get("id") or manifest.get("name") or _kebab(os.path.basename(d))
        rci["name"] = _pascal(manifest.get("name") or rci["slug"])
        rci["version"] = manifest.get("version", "1.0.0")
        rci["description"] = manifest.get("description", "")
        rci["author"] = manifest.get("author")
        rci["tags"] = manifest.get("tags", [])
        rci["license"] = manifest.get("license")
        rci["homepage"] = manifest.get("homepage")
        rci["repository"] = manifest.get("repository")
        rci["examples"] = manifest.get("examples", [])
        tools = manifest.get("tools") or []
        if tools:
            rci["parameters"] = tools[0].get("parameters", rci["parameters"])
            rci["description"] = rci["description"] or tools[0].get("description", "")
        if len(tools) > 1:
            rci.setdefault("platform", {}).setdefault("openrappter", {})["tools"] = tools

    if mf:
        rci["instructions"] = CAPSULE_RE.sub(
            "", open(mf, encoding="utf-8").read()).strip()
        preserve(rci, "openrappter.md", open(mf, "rb").read(), mf)
    preserve(rci, "openrappter", jraw, jf)
    rci.setdefault("provenance", []).append(f"read:openrappter:{os.path.basename(d)}")
    return rci


# --------------------------------------------------------------------------
# WRITER: RAPP brainstem agent.py
# --------------------------------------------------------------------------

# Emitted when toasting derived an ordered step list out of the prose. This is
# the deterministic layer: same arguments in, same resolved commands out, no
# model in the loop. It RESOLVES and RETURNS the steps -- it deliberately does
# not execute them, because a capability that shells out on import is a
# capability nobody can safely audit.
STEP_PERFORM = '''    def perform(self, **kwargs):  # toaster:generated-perform
        missing = [k for k in self.metadata["parameters"].get("required", [])
                   if k not in kwargs]
        if missing:
            return json.dumps({"status": "error",
                               "missing_required": missing}, indent=2)
        resolved, unresolved = [], set()
        for step in STEPS:
            cmd = step["cmd"]
            for key, value in kwargs.items():
                for token in ("<" + key.replace("_", "-") + ">",
                              "<" + key + ">",
                              "{{" + key + "}}",
                              "$" + key.upper()):
                    cmd = cmd.replace(token, str(value))
            for leftover in re.findall(r"<[a-zA-Z][a-zA-Z0-9 _.-]{1,40}>", cmd):
                unresolved.add(leftover)
            resolved.append(cmd)
        return json.dumps({"status": "ok",
                           "steps": resolved,
                           "unresolved_placeholders": sorted(unresolved),
                           "note": "Resolved deterministically by the agent; "
                                   "run in order. Nothing was executed here."},
                          indent=2)
'''

AGENT_TEMPLATE = '''"""{docstring}"""

import json
import re
import sys

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # running OUTSIDE the brainstem -- stay executable anyway.
    class BasicAgent:  # noqa: D101 - minimal stand-in, same contract
        def __init__(self, name=None, metadata=None):
            if name:
                self.name = name
            if metadata:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."

        def system_context(self):
            return None

        def to_tool(self):
            return {{"type": "function", "function": {{
                "name": self.name,
                "description": self.metadata.get("description", ""),
                "parameters": self.metadata.get("parameters", {{}})}}}}

# The procedural layer, verbatim from the source capability. The brainstem
# returns this to the model, so the skill's instructions still drive behaviour
# -- now behind a typed, deterministic tool contract.
INSTRUCTIONS = {instructions!r}

# Ordered commands lifted verbatim from the capability's own documentation.
STEPS = {steps}


class {cls}(BasicAgent):
    def __init__(self):
        self.name = {name!r}
        self.metadata = {metadata}
        super().__init__(name=self.name, metadata=self.metadata)
{sysctx}
{perform}

if __name__ == "__main__":
    # Standalone entry point: the deterministic layer runs with NO brainstem,
    # no framework, no install. This is what lets a "simple SKILL.md" platform
    # keep real determinism -- the host model shells out to this file instead
    # of improvising the procedure in prose.
    #     echo '{{"arg": "value"}}' | python3 {filename}
    #     python3 {filename} '{{"arg": "value"}}'
    #     python3 {filename} --tool          # emit the JSON tool contract
    _a = sys.argv[1:]
    if _a and _a[0] == "--tool":
        print(json.dumps({cls}().to_tool(), indent=2))
    else:
        _raw = _a[0] if _a else (sys.stdin.read().strip() or "{{}}")
        print({cls}().perform(**json.loads(_raw)))

# {capsule}
'''

GENERATED_PERFORM_MARK = "# toaster:generated-perform"

DEFAULT_PERFORM = '''    def perform(self, **kwargs):  # toaster:generated-perform
        """Render the capability's instructions with the caller's arguments.

        Deterministic: same inputs -> same bytes out. No model call happens
        here; the brainstem hands this text back to the model as tool output.
        """
        text = INSTRUCTIONS
        for key, value in kwargs.items():
            text = text.replace("{{" + key + "}}", str(value))
        if kwargs:
            text += "\\n\\n## Inputs\\n```json\\n" + json.dumps(
                kwargs, indent=2, default=str) + "\\n```"
        return text
'''


def write_agent(rci: dict) -> bytes:
    exact = restore(rci, "agent")
    if exact is not None:
        return exact  # byte-for-byte original -- zero loss, not a re-render

    impl = rci.get("impl") or {}
    if impl.get("steps") and not impl.get("perform") and not impl.get("perform_body"):
        perform = STEP_PERFORM.rstrip("\n")
    elif impl.get("perform"):
        perform = impl["perform"]
        if not perform.startswith("    "):
            perform = textwrap.indent(perform, "    ")
    elif impl.get("perform_body"):
        perform = ("    def perform(self, **kwargs):\n"
                   + textwrap.indent(impl["perform_body"], "        "))
    else:
        perform = DEFAULT_PERFORM.rstrip("\n")

    sysctx = ""
    sc = rci.get("system_context")
    if isinstance(sc, str) and sc and sc != "<code>":
        sysctx = ("\n    def system_context(self):\n"
                  f"        return {sc!r}\n")

    metadata = {
        "name": rci["name"],
        "description": rci.get("description", ""),
        "parameters": rci.get("parameters") or {
            "type": "object", "properties": {}, "required": []},
    }
    doc = (rci.get("description") or rci["name"]).replace('"""', "'''")
    doc = f"{rci['name']} -- {doc}\n\nGenerated by agentshim from {rci.get('slug')}. " \
          f"The RCI capsule at the bottom of this file carries the full original; " \
          f"`agentshim.py convert` restores it byte-exact."

    cls = _pascal(rci["name"])
    cls = cls if cls.endswith("Agent") else cls + "Agent"
    src = AGENT_TEMPLATE.format(
        docstring=doc,
        instructions=rci.get("instructions", ""),
        steps=json.dumps((rci.get("impl") or {}).get("steps") or [], indent=4),
        cls=cls,
        name=rci["name"],
        metadata=json.dumps(metadata, indent=8).replace("\n}", "\n        }"),
        sysctx=sysctx,
        perform=perform,
        filename=agent_filename(rci),
        capsule=pack_capsule(rci),
    )
    return src.encode()


STANDALONE_SHIM = '''try:
    from agents.basic_agent import BasicAgent
except ImportError:  # running OUTSIDE the brainstem -- stay executable anyway.
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            if name:
                self.name = name
            if metadata:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."

        def system_context(self):
            return None

        def to_tool(self):
            return {"type": "function", "function": {
                "name": self.name,
                "description": self.metadata.get("description", ""),
                "parameters": self.metadata.get("parameters", {})}}
'''

IMPORT_RE = re.compile(
    r"^from\s+agents\.basic_agent\s+import\s+BasicAgent\s*$", re.M)


def make_standalone(src: bytes, rci: dict) -> bytes:
    """Turn a brainstem-native agent into one that ALSO runs with no brainstem.

    The byte-exact original is what round-trips (transport fidelity); this is
    the sidecar a foreign host executes (behavioural fidelity). Same class,
    same perform(), same capsule -- it converts back to the true original.
    """
    text = src.decode("utf-8", "replace")
    cls = (rci.get("impl") or {}).get("class") or _pascal(rci["name"]) + "Agent"

    if "except ImportError" not in text:
        if IMPORT_RE.search(text):
            text = IMPORT_RE.sub(STANDALONE_SHIM.rstrip("\n"), text, count=1)
        else:
            text = STANDALONE_SHIM + "\n" + text
    if "import sys" not in text:
        text = "import sys\n" + text
    if "import json" not in text:
        text = "import json\n" + text

    if "__name__" not in text or "__main__" not in text:
        text = text.rstrip("\n") + f'''


if __name__ == "__main__":
    # Standalone entry point -- no brainstem, no framework, no install.
    #     python3 {agent_filename(rci)} '{{"arg": "value"}}'
    #     echo '{{"arg": "value"}}' | python3 {agent_filename(rci)}
    #     python3 {agent_filename(rci)} --tool
    _a = sys.argv[1:]
    if _a and _a[0] == "--tool":
        print(json.dumps({cls}().to_tool(), indent=2))
    else:
        _raw = _a[0] if _a else (sys.stdin.read().strip() or "{{}}")
        print({cls}().perform(**json.loads(_raw)))
'''
    if not CAPSULE_RE.search(text):
        text = text.rstrip("\n") + f"\n\n# {pack_capsule(rci)}\n"
    return text.encode()


def agent_filename(rci: dict) -> str:
    slug = rci.get("slug") or _kebab(rci.get("name", "capability"))
    return f"{slug.replace('-', '_')}_agent.py"


# --------------------------------------------------------------------------
# Fidelity tiers -- what actually survives a trip to a given host
# --------------------------------------------------------------------------
#
# There are TWO fidelities and conflating them is how capabilities rot:
#
#   TRANSPORT fidelity  -- can the original be recovered byte-exact later?
#                          Solved unconditionally by the RCI capsule.
#   BEHAVIOURAL fidelity -- does it still behave deterministically ON the host?
#                          Depends entirely on what the host can execute.
#
# So we grade the target honestly instead of pretending every export is equal.

TIER_EXEC = "EXEC"    # host runs the real code -> true determinism, no RAPP needed
TIER_CODE = "CODE"    # code travels in the markdown; host may or may not run it
TIER_CONTRACT = "SPEC"  # typed contract + examples only; model conforms, not computes


def fidelity_tier(rci: dict, bundled: bool) -> tuple:
    impl = rci.get("impl") or {}
    has_code = bool(impl.get("perform") or impl.get("perform_body") or impl.get("steps"))
    has_schema = bool((rci.get("parameters") or {}).get("properties"))
    if has_code and bundled:
        return (TIER_EXEC,
                "host executes the real agent file -- byte-identical behaviour")
    if has_code:
        return (TIER_CODE,
                "code travels in a fenced block; determinism only if the host runs it "
                "(pass --bundle to guarantee it)")
    if has_schema:
        return (TIER_CONTRACT,
                "typed contract + examples travel; the model conforms to the interface "
                "but computes the answer itself")
    return (TIER_CONTRACT,
            "prose only -- no typed contract to conform to; add a `## Parameters` "
            "json fence to raise this")


# --------------------------------------------------------------------------
# WRITER: SKILL.md (Claude + openclaw)
# --------------------------------------------------------------------------

def write_skill(rci: dict, openclaw: bool = False, bundled: bool = False) -> bytes:
    fmt = "openclaw" if openclaw else "skill"
    exact = restore(rci, fmt)
    if exact is not None and not bundled:
        return exact

    plat = rci.get("platform", {}) or {}
    meta = {}
    if openclaw:
        meta["openclaw"] = plat.get("openclaw", {"emoji": "🧠"})
    # NOTE: the plain-skill projection deliberately does NOT re-emit
    # metadata.openclaw in its frontmatter. It is not a fidelity loss -- the
    # capsule carries platform.openclaw verbatim -- but emitting it made
    # detect() reclassify this projection AS openclaw, so reading it back
    # overwrote the true openclaw original in the vault with a derived file.
    # That is drift: 26 soak chains failed on exactly this. A projection must
    # never be mistakable for the thing it is projecting from.

    pairs = [("name", rci.get("slug") or _kebab(rci["name"])),
             ("description", rci.get("description", ""))]
    for k, v in (plat.get("claude") or {}).items():
        pairs.append((k, v))
    if rci.get("version") and rci["version"] != "1.0.0":
        pairs.append(("version", rci["version"]))
    for k in ("author", "license"):
        if rci.get(k):
            pairs.append((k, rci[k]))
    if rci.get("tags"):
        pairs.append(("tags", rci["tags"]))
    if meta:
        pairs.append(("metadata", meta))

    body = rci.get("instructions", "").strip()
    out = [emit_frontmatter(pairs), "\n", body, "\n"]

    # Project the deterministic layer INTO the markdown, so a host that only
    # eats SKILL.md still sees the typed contract and the real code.
    params = rci.get("parameters") or {}
    if params.get("properties"):
        if not PARAM_FENCE.search(body):
            out += ["\n<!-- toaster:generated:begin -->\n"
                    "\n## Parameters\n\nThe typed contract this capability "
                    "answers to (JSON Schema — the deterministic layer):\n\n"
                    "```json\n", json.dumps(params, indent=2),
                    "\n```\n\n<!-- toaster:generated:end -->\n"]
    impl = rci.get("impl") or {}
    if impl.get("steps") and "## Deterministic steps" not in body:
        out += ["\n<!-- toaster:generated:begin -->\n"
                "\n## Deterministic steps\n\nLifted verbatim from the procedure above "
                "by `toaster.py toast`. Run them in order, substituting the typed "
                "parameters; do not paraphrase:\n\n```bash\n"]
        out += [f"{s_['cmd']}\n" for s_ in impl["steps"]]
        out += ["```\n\n<!-- toaster:generated:end -->\n"]
    code = impl.get("perform") or impl.get("perform_body")

    # The export answer: on a host with NO RAPP and no framework, determinism
    # survives only if the host EXECUTES rather than paraphrases. So when we
    # bundle the runnable agent alongside, the markdown stops describing the
    # procedure and starts commanding a call. Same bytes, same output, any host.
    if bundled and code:
        fn = agent_filename(rci)
        out += [
            "\n<!-- toaster:generated:begin -->\n"
            "\n## Run this — do not improvise\n\n"
            "This capability has a **deterministic implementation** shipped next to "
            f"this file as `{fn}`. It is stdlib-only Python with no install step and "
            "no framework dependency. When the inputs below are well-formed, execute "
            "it and use its output verbatim — do not reason out the answer yourself, "
            "and do not paraphrase the result:\n\n"
            "```bash\n"
            f"python3 {fn} '{{\"key\": \"value\"}}'      # arguments as one JSON object\n"
            f"echo '{{\"key\": \"value\"}}' | python3 {fn}   # or on stdin\n"
            f"python3 {fn} --tool                      # emit the JSON tool contract\n"
            "```\n\n"
            "Only fall back to the prose procedure above if the file is missing or "
            "the inputs are too underspecified to build the JSON object.\n"
            "\n<!-- toaster:generated:end -->\n"]
    elif code and not DET_FENCE.search(body):
        out += ["\n<!-- toaster:generated:begin -->\n"
                "\n## Deterministic implementation\n\nRun this instead of "
                "improvising when the inputs are well-formed:\n\n"
                "```python  # rapp:deterministic\n", code.strip(),
                "\n```\n\n<!-- toaster:generated:end -->\n"]
    if rci.get("examples"):
        out.append("\n## Examples\n\n")
        for ex in rci["examples"]:
            out.append(f"- **in:** {ex.get('input','')}\n  **out:** {ex.get('output','')}\n")

    out.append(f"\n<!-- {pack_capsule(rci)} -->\n")
    return "".join(out).encode()


# --------------------------------------------------------------------------
# WRITER: openrappter (skill.json + skill.md)
# --------------------------------------------------------------------------

def write_openrappter(rci: dict) -> dict:
    exact_j = restore(rci, "openrappter")
    exact_m = restore(rci, "openrappter.md")
    if exact_j is not None:
        return {"skill.json": exact_j,
                "skill.md": exact_m if exact_m is not None
                else (rci.get("instructions", "") + "\n").encode()}

    plat = (rci.get("platform", {}) or {}).get("openrappter", {})
    tools = plat.get("tools") or [{
        "name": rci["name"],
        "description": rci.get("description", ""),
        "parameters": rci.get("parameters") or {"type": "object", "properties": {}},
    }]
    manifest = {
        "id": rci.get("slug") or _kebab(rci["name"]),
        "name": rci["name"],
        "version": rci.get("version", "1.0.0"),
        "description": rci.get("description", ""),
        "tools": tools,
    }
    for k in ("author", "tags", "license", "homepage", "repository", "examples"):
        if rci.get(k):
            manifest[k] = rci[k]
    manifest["x-rci"] = pack_capsule(rci)

    md = rci.get("instructions", "").strip() + "\n"
    return {"skill.json": (json.dumps(manifest, indent=2) + "\n").encode(),
            "skill.md": md.encode()}


# --------------------------------------------------------------------------
# Dispatch
# --------------------------------------------------------------------------

def detect(path: str) -> str:
    base = os.path.basename(path).lower()
    if os.path.isdir(path):
        if os.path.exists(os.path.join(path, "skill.json")):
            return "openrappter"
        if os.path.exists(os.path.join(path, "SKILL.md")):
            return "skill"
        raise ValueError(f"{path}: directory holds neither skill.json nor SKILL.md")
    if base.endswith(".py"):
        return "agent"
    if base in ("skill.json",):
        return "openrappter"
    if base.endswith(".md"):
        head = open(path, encoding="utf-8", errors="replace").read(4000)
        fm, _ = split_frontmatter(head)
        meta = fm.get("metadata")
        return "openclaw" if isinstance(meta, dict) and "openclaw" in meta else "skill"
    if base.endswith(".json"):
        return "rci"
    raise ValueError(f"{path}: cannot detect format (use --from)")


def load(path: str, fmt: str | None = None) -> dict:
    fmt = fmt or detect(path)
    if fmt == "openrappter":
        return read_openrappter(path)
    raw = open(path, "rb").read()
    if fmt == "agent":
        return read_agent(raw, path)
    if fmt in ("skill", "openclaw"):
        return read_skill(raw, path)
    if fmt == "rci":
        return json.loads(raw.decode())
    raise ValueError(f"unknown format: {fmt}")


def render(rci: dict, fmt: str, bundled: bool = False):
    if fmt == "agent":
        return write_agent(rci)
    if fmt == "skill":
        return write_skill(rci, openclaw=False, bundled=bundled)
    if fmt == "openclaw":
        return write_skill(rci, openclaw=True, bundled=bundled)
    if fmt == "openrappter":
        return write_openrappter(rci)
    if fmt == "rci":
        return (json.dumps(rci, indent=2) + "\n").encode()
    raise ValueError(f"unknown format: {fmt}")


def default_out(rci: dict, fmt: str) -> str:
    slug = rci.get("slug") or _kebab(rci.get("name", "capability"))
    return {"agent": f"{slug.replace('-', '_')}_agent.py",
            "skill": os.path.join(slug, "SKILL.md"),
            "openclaw": os.path.join(slug, "SKILL.md"),
            "openrappter": slug,
            "rci": f"{slug}.rci.json"}[fmt]


def emit(result, out: str) -> list:
    written = []
    if isinstance(result, dict):
        os.makedirs(out, exist_ok=True)
        for fn, data in result.items():
            p = os.path.join(out, fn)
            open(p, "wb").write(data)
            written.append(p)
    else:
        d = os.path.dirname(out)
        if d:
            os.makedirs(d, exist_ok=True)
        open(out, "wb").write(result)
        written.append(out)
    return written


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_convert(a) -> int:
    rci = load(a.path, a.from_fmt)
    rci.setdefault("provenance", []).append(f"convert:->{a.to}")
    bundled = bool(getattr(a, "bundle", False)) and a.to in ("skill", "openclaw")
    out = a.out or default_out(rci, a.to)
    written = emit(render(rci, a.to, bundled=bundled), out)

    # --bundle: ship the runnable agent NEXT TO the markdown, so a host with no
    # RAPP still gets literal determinism by executing it.
    if bundled:
        side = os.path.join(os.path.dirname(written[0]) or ".", agent_filename(rci))
        open(side, "wb").write(make_standalone(write_agent(rci), rci))
        os.chmod(side, 0o755)
        written.append(side)
        # Never claim EXEC without proving the file actually executes.
        import subprocess
        probe = subprocess.run([sys.executable, side, "--tool"],
                               capture_output=True, text=True, timeout=60)
        if probe.returncode != 0:
            print(f"  WARNING: bundled agent does not run standalone "
                  f"({(probe.stderr or '').strip().splitlines()[-1:] or ['?']})",
                  file=sys.stderr)
            bundled = False  # do not overclaim the tier

    exact = a.to in rci.get("preserved", {}) and not bundled
    tier, why = fidelity_tier(rci, bundled)
    print(f"{'RESTORED (byte-exact)' if exact else 'SYNTHESISED'}  "
          f"{rci.get('name')}  ->  {a.to}")
    for p in written:
        print(f"  {p}")
    print(f"  transport fidelity   LOSSLESS (rci capsule embedded; converts back byte-exact)")
    print(f"  behavioural fidelity {tier} — {why}")
    if not exact:
        if not (rci.get("parameters") or {}).get("properties"):
            print("  note: no typed parameters — add a `## Parameters` json fence")
        _i = rci.get("impl") or {}
        if a.to == "agent" and not (_i.get("perform") or _i.get("steps")):
            print("  note: no deterministic code — perform() renders instructions."
                  " Run `toast` first to derive one from the prose.")
    return 0


def cmd_inspect(a) -> int:
    rci = load(a.path, a.from_fmt)
    params = rci.get("parameters") or {}
    impl = rci.get("impl") or {}
    print(f"name          {rci.get('name')}   (slug: {rci.get('slug')})")
    print(f"version       {rci.get('version')}")
    print(f"description   {(rci.get('description') or '')[:100]}")
    print(f"DETERMINISTIC parameters: {len(params.get('properties', {}))} typed "
          f"({', '.join(params.get('properties', {})) or 'none'})"
          f" | required: {', '.join(params.get('required') or []) or 'none'}")
    print(f"              code: {'yes (' + impl.get('lang', '?') + ')' if impl else 'NO'}"
          f" | system_context: {'yes' if rci.get('system_context') else 'no'}")
    print(f"PROCEDURAL    instructions: {len(rci.get('instructions') or '')} chars")
    print(f"platform      {', '.join(rci.get('platform', {})) or 'none'}")
    print(f"capability-id {capability_id(rci)[:24]}  (identity of WHAT it is,"
          f" independent of route)")
    print(f"preserved     {', '.join(rci.get('preserved', {})) or 'none'} "
          f"(these convert back byte-exact)")
    print(f"provenance    {' -> '.join(rci.get('provenance', []))}")
    return 0


def cmd_roundtrip(a) -> int:
    src_fmt = a.from_fmt or detect(a.path)
    original = (open(a.path, "rb").read() if not os.path.isdir(a.path)
                else open(os.path.join(a.path, "skill.json"), "rb").read())
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        mid = emit(render(load(a.path, src_fmt), a.via),
                   os.path.join(td, default_out(load(a.path, src_fmt), a.via)))
        mid_path = mid[0] if a.via != "openrappter" else os.path.dirname(mid[0])
        back = render(load(mid_path, a.via), src_fmt)
        back = back["skill.json"] if isinstance(back, dict) else back
    ok = back == original
    print(f"{src_fmt} -> {a.via} -> {src_fmt}: "
          f"{'IDENTICAL' if ok else 'DRIFT'}  "
          f"({len(original)}B -> {len(back)}B)")
    if not ok:
        print(f"  sha in  {_sha(original)[:16]}\n  sha out {_sha(back)[:16]}")
    return 0 if ok else 1


# --------------------------------------------------------------------------
# soak -- the anti-drift harness
# --------------------------------------------------------------------------
#
# A single clean round trip proves almost nothing. ".md drift disease" is an
# ACCUMULATION failure: each hop is individually plausible, the artifact bends
# a little, and twenty hops later the tool contract has quietly rotted. So we
# test three properties a single round trip cannot see:
#
#   1. FIXED POINT   -- after one normalising pass, repeated conversion must
#                       stop changing bytes. If cycle 7 != cycle 6, it drifts.
#   2. PATH INDEPENDENCE -- agent->skill->agent and
#                       agent->openrappter->openclaw->rci->agent must land on
#                       the SAME bytes. If the route changes the destination,
#                       the format is lying about being a projection.
#   3. IDEMPOTENCE   -- converting to a format twice in a row is a no-op.
#
# Any of these failing is drift, even when every individual hop "looks fine".

def _hop(path: str, src_fmt: str, dst_fmt: str, workdir: str, tag: str) -> str:
    rci = load(path, src_fmt)
    out = os.path.join(workdir, tag, default_out(rci, dst_fmt))
    written = emit(render(rci, dst_fmt), out)
    return os.path.dirname(written[0]) if dst_fmt == "openrappter" else written[0]


def _bytes_of(path: str, fmt: str) -> bytes:
    if fmt == "openrappter":
        return open(os.path.join(path, "skill.json"), "rb").read()
    return open(path, "rb").read()


def _chains(src: str, depth: int) -> list:
    """Every ordered route of length 1..depth through the other formats."""
    import itertools
    others = [f for f in FORMATS if f != src]
    routes = []
    for d in range(1, depth + 1):
        for combo in itertools.permutations(others, d):
            routes.append(list(combo))
    return routes


def cmd_soak(a) -> int:
    import tempfile
    targets = a.paths
    depth = a.depth
    cycles = a.cycles
    total_hops = 0
    failures = []

    skipped = []
    raw = [p for p in targets if is_raw(p)]
    if raw and not getattr(a, "allow_raw", False):
        print("RAW BREAD -- toast it first, or the soak measures the wrong thing:")
        for p in raw:
            print(f"  {p}")
        print("  run:  toaster.py toast <path>...   (then re-run soak)")
        return 2
    for path in targets:
        try:
            src_fmt = detect(path)
            load(path, src_fmt)  # must be readable before we soak it
        except Exception as e:
            skipped.append((os.path.basename(path), str(e).split(":")[-1].strip()))
            continue
        origin = _bytes_of(path, src_fmt)
        label = os.path.basename(path if not os.path.isdir(path) else path.rstrip("/"))
        routes = _chains(src_fmt, depth)
        bad = 0

        with tempfile.TemporaryDirectory() as td:
            # --- 2. PATH INDEPENDENCE: every route must land on the same bytes
            for i, route in enumerate(routes):
                cur, cur_fmt = path, src_fmt
                try:
                    for j, nxt in enumerate(route):
                        cur = _hop(cur, cur_fmt, nxt, td, f"r{i}h{j}")
                        cur_fmt = nxt
                        total_hops += 1
                    back = _hop(cur, cur_fmt, src_fmt, td, f"r{i}back")
                    total_hops += 1
                    got = _bytes_of(back, src_fmt)
                    if got != origin:
                        bad += 1
                        failures.append((label, f"{src_fmt}->" + "->".join(route)
                                         + f"->{src_fmt}", len(origin), len(got)))
                except Exception as e:
                    bad += 1
                    failures.append((label, f"{src_fmt}->" + "->".join(route)
                                     + f" RAISED {type(e).__name__}: {e}", 0, 0))

            # --- 1. FIXED POINT: hammer one route N times, bytes must freeze
            alt = [f for f in FORMATS if f != src_fmt][0]
            cur, cur_fmt, prev, frozen_at = path, src_fmt, None, None
            for c in range(cycles):
                cur = _hop(cur, cur_fmt, alt, td, f"fp{c}a")
                cur = _hop(cur, alt, src_fmt, td, f"fp{c}b")
                cur_fmt = src_fmt
                total_hops += 2
                now = _bytes_of(cur, src_fmt)
                if prev is not None and now != prev:
                    bad += 1
                    failures.append((label, f"FIXED-POINT broke at cycle {c} "
                                     f"(via {alt})", len(prev), len(now)))
                    break
                if prev is not None and frozen_at is None:
                    frozen_at = c
                prev = now
            if prev is not None and prev != origin:
                bad += 1
                failures.append((label, f"{cycles}x round trip via {alt} != original",
                                 len(origin), len(prev)))

            # --- 3. IDEMPOTENCE: render->read->render must be a no-op
            for fmt in FORMATS:
                if fmt == src_fmt:
                    continue
                one = _hop(path, src_fmt, fmt, td, f"id1-{fmt}")
                two = _hop(one, fmt, fmt, td, f"id2-{fmt}")
                total_hops += 2
                if _bytes_of(one, fmt) != _bytes_of(two, fmt):
                    bad += 1
                    failures.append((label, f"NOT IDEMPOTENT in {fmt}", 0, 0))

        status = "CLEAN" if bad == 0 else f"{bad} DRIFT"
        print(f"  {'ok  ' if bad == 0 else 'DRIFT'} {label:<34} "
              f"{len(routes)} routes x depth<={depth} + {cycles} cycles  -> {status}")

    print(f"\n{total_hops} conversions across {len(targets)} artifact(s)")
    if failures:
        print(f"\n{len(failures)} DRIFT EVENT(S):")
        for lbl, chain, a_len, b_len in failures[:40]:
            print(f"  {lbl}: {chain}" + (f"  ({a_len}B -> {b_len}B)" if a_len else ""))
        return 1
    print("NO DRIFT — path-independent, idempotent, and fixed-point stable "
          "in every direction.")
    return 0


FIXTURE_AGENT = '''"""Weather lookup, deterministic."""

from agents.basic_agent import BasicAgent


class WeatherAgent(BasicAgent):
    def __init__(self):
        self.name = 'Weather'
        self.metadata = {
            "name": self.name,
            "description": "Look up the forecast for a city.",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string", "description": "City name."}},
                "required": ["city"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        return "forecast for " + str(kwargs.get("city"))
'''

FIXTURE_SKILL = '''---
name: release-notes
description: Draft release notes from a git log. Use when the user says "cut a release" or "write release notes".
---

# Release notes

Group commits by type, drop noise, lead with user-visible change.

## Parameters

```json
{"type":"object","properties":{"tag":{"type":"string","description":"Git tag."}},"required":["tag"]}
```
'''


def cmd_selftest(a) -> int:
    import tempfile
    fails = 0
    with tempfile.TemporaryDirectory() as td:
        ap = os.path.join(td, "weather_agent.py")
        open(ap, "w").write(FIXTURE_AGENT)
        sp = os.path.join(td, "release-notes", "SKILL.md")
        os.makedirs(os.path.dirname(sp))
        open(sp, "w").write(FIXTURE_SKILL)

        # 1. readers pull the deterministic layer out of both shapes
        ra, rs = load(ap), load(sp)
        checks = [
            ("agent: name", ra["name"] == "Weather"),
            ("agent: typed params", "city" in ra["parameters"]["properties"]),
            ("agent: code captured", bool((ra["impl"] or {}).get("perform"))),
            ("skill: slug", rs["slug"] == "release-notes"),
            ("skill: typed params found in md", "tag" in rs["parameters"]["properties"]),
            ("skill: instructions", "Group commits" in rs["instructions"]),
        ]
        # 2. every round trip is byte-exact through every other format
        for src, path in (("agent", ap), ("skill", sp)):
            for via in ("skill", "openclaw", "openrappter", "agent", "rci"):
                if via == src:
                    continue
                orig = open(path, "rb").read()
                mid_out = os.path.join(td, f"rt-{src}-{via}", default_out(load(path), via))
                mid = emit(render(load(path), via), mid_out)
                mp = mid[0] if via != "openrappter" else os.path.dirname(mid[0])
                back = render(load(mp, via), src)
                back = back["skill.json"] if isinstance(back, dict) else back
                checks.append((f"roundtrip {src}->{via}->{src}", back == orig))
        # 3. synthesis: a skill with no code still becomes a runnable agent
        agent_src = render(load(sp), "agent").decode()
        checks.append(("synthesis: valid python", _compiles(agent_src)))
        checks.append(("synthesis: typed contract survived", '"tag"' in agent_src))
        checks.append(("synthesis: instructions carried", "Group commits" in agent_src))

        for label, ok in checks:
            print(f"  {'PASS' if ok else 'FAIL'}  {label}")
            fails += 0 if ok else 1
    print(f"\n{len(checks) - fails}/{len(checks)} passed")
    return 0 if fails == 0 else 1


def _compiles(src: str) -> bool:
    try:
        ast.parse(src)
        return True
    except SyntaxError as e:
        print(f"      syntax error: {e}")
        return False


# --------------------------------------------------------------------------
# The reaction: deriving a deterministic layer out of prose
# --------------------------------------------------------------------------
#
# Toasting is a CHEMICAL CHANGE, not a wrapper. Raw bread is prose: a human
# reads it and improvises. Toast has a typed contract and an ordered, resolved
# step list -- the same instructions, now machine-addressable.
#
# The reaction is deliberately EVIDENCE-BASED and conservative. Every derived
# parameter must appear inside an actual command, and every derived step must
# be a real command line lifted verbatim from the document. Nothing is
# invented, because a contract the author never implied is worse than no
# contract: it silently changes what the capability claims to accept.
# Each derivation records where it came from, so toast is auditable.

CMD_HEADS = ("git","gh","curl","wget","python","python3","pip","npm","npx","node",
             "bash","sh","zsh","make","docker","kubectl","az","aws","open","cd",
             "mkdir","cp","mv","grep","sed","awk","jq","pytest","cargo","go")

INLINE_CODE = re.compile(r"`([^`\n]{2,400})`")
FENCED = re.compile(r"```[a-zA-Z0-9_+-]*[ \t]*\n(.*?)```", re.S)
PLACEHOLDER_PATTERNS = [
    (re.compile(r"<([a-zA-Z][a-zA-Z0-9 _.-]{1,40})>"), "angle"),
    (re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]{0,40})\s*\}\}"), "mustache"),
    (re.compile(r"\$\{?([A-Z][A-Z0-9_]{2,40})\}?"), "envvar"),
]


def _is_command(line: str) -> bool:
    t = line.strip().lstrip("$ ").split()
    return bool(t) and t[0] in CMD_HEADS


def derive_layer(instructions: str) -> dict:
    """Scan prose -> (typed params, ordered steps, provenance). Pure function."""
    spans, steps = [], []
    for m in INLINE_CODE.finditer(instructions):
        spans.append((m.group(1), instructions[:m.start()].count("\n") + 1))
    for m in FENCED.finditer(instructions):
        base = instructions[:m.start()].count("\n") + 1
        for i, ln in enumerate(m.group(1).split("\n")):
            if ln.strip():
                spans.append((ln, base + i + 1))

    for text, line in spans:
        if _is_command(text):
            steps.append({"cmd": text.strip(), "line": line})

    # A parameter counts only if it appears inside a command span -- a
    # placeholder mentioned in a sentence is documentation, not an input.
    props, prov = {}, []
    cmd_text = "\n".join(s["cmd"] for s in steps)
    for text, line in spans:
        for rx, kind in PLACEHOLDER_PATTERNS:
            for m in rx.finditer(text):
                raw = m.group(1).strip()
                name = _kebab(raw).replace("-", "_")
                if not name or name in props:
                    continue
                if raw not in cmd_text and text not in cmd_text:
                    continue
                props[name] = {
                    "type": "string",
                    "description": f"Derived from `{m.group(0)}` used in the "
                                   f"documented command at line {line}.",
                }
                prov.append({"param": name, "token": m.group(0),
                             "kind": kind, "line": line})
    return {"properties": props, "steps": steps, "provenance": prov}


def toast_rci(rci: dict) -> dict:
    """Apply the reaction to a capability record, in place. Returns a report."""
    body = rci.get("instructions", "") or ""
    d = derive_layer(body)
    params = rci.get("parameters") or {"type": "object", "properties": {}, "required": []}
    before = len(params.get("properties", {}))

    # An explicit `## Parameters` fence is the author speaking; never override
    # it. Derived params only FILL GAPS.
    props = dict(params.get("properties", {}))
    for k, v in d["properties"].items():
        props.setdefault(k, v)
    params["type"] = "object"
    params["properties"] = props
    params.setdefault("required", [])
    rci["parameters"] = params

    impl = rci.get("impl") or {}
    if d["steps"] and not impl.get("perform") and not impl.get("perform_body"):
        impl = dict(impl)
        impl["lang"] = impl.get("lang") or "python"
        impl["steps"] = d["steps"]
        rci["impl"] = impl

    rci.setdefault("provenance", []).append(
        f"toast:derived params={len(props) - before} steps={len(d['steps'])}")
    rci["derivation"] = d["provenance"]
    return {"params_before": before, "params_after": len(props),
            "steps": len(d["steps"]), "provenance": d["provenance"]}


# --------------------------------------------------------------------------
# toast -- raw bread must be toasted before it enters the loop
# --------------------------------------------------------------------------
#
# A hand-written SKILL.md is RAW BREAD. It carries no RCI capsule, so there is
# nothing to restore from: every conversion has to SYNTHESISE, and synthesis is
# a re-render, not a recovery. That is why raw bread cannot round-trip
# byte-exact and must not be fed straight into the loop -- you would be testing
# whether two renders agree, not whether fidelity held.
#
# Toasting is the one-time normalising pass that turns bread into toast: it
# gives the artifact a capsule (so it has a canonical form to restore) and
# surfaces whatever deterministic layer it declared. After toasting, every
# guarantee in this file applies -- byte-exact round trips, path independence,
# fixed point. Before toasting, none of them do.
#
# Toast is idempotent: toasting toast is a no-op.

def is_raw(path: str, fmt: str = None) -> bool:
    """Raw bread = no capsule = nothing canonical to restore from."""
    try:
        fmt = fmt or detect(path)
    except Exception:
        return True
    if fmt == "openrappter":
        d = path if os.path.isdir(path) else os.path.dirname(path) or "."
        f = os.path.join(d, "skill.json")
        try:
            return "x-rci" not in json.load(open(f))
        except Exception:
            return True
    try:
        return unpack_capsule(open(path, encoding="utf-8", errors="replace").read()) is None
    except Exception:
        return True


def cmd_toast(a) -> int:
    rc = 0
    for path in a.paths:
        fmt = detect(path)
        if not is_raw(path, fmt) and not a.force:
            print(f"  already toast   {path}")
            continue
        rci = load(path, fmt)
        # Drop the vaulted copy of the RAW input before rendering. Otherwise
        # render() faithfully restores the very bytes we are trying to replace
        # and toasting silently no-ops -- which is exactly what it did until
        # the idempotence check caught it. Toast becomes the new canonical
        # form for this format; the raw original is superseded, not lost
        # (every other format's preserved entry survives in the capsule).
        rci.setdefault("preserved", {}).pop(fmt, None)
        report = toast_rci(rci)          # <-- the reaction: prose -> contract
        out = render(rci, fmt)           # now carries a capsule AND a layer
        target = path if fmt != "openrappter" else path
        emit(out, target)
        # prove it: the freshly toasted artifact must round-trip byte-exact
        again = render(load(target, fmt), fmt)
        again = again["skill.json"] if isinstance(again, dict) else again
        cur = _bytes_of(target, fmt)
        ok = (again == cur)
        b, aft, st = report["params_before"], report["params_after"], report["steps"]
        print(f"  {'toasted' if ok else 'TOASTED-BUT-UNSTABLE'}  {path}")
        print(f"     typed params  {b} -> {aft}"
              + (f"   (+{aft - b} derived)" if aft > b else "   (nothing derivable)"))
        print(f"     steps lifted  {st}")
        for d in report["provenance"][:6]:
            print(f"       {d['param']:<22} <- {d['token']} (line {d['line']}, {d['kind']})")
        if aft == b and st == 0:
            print("     NOTE: no deterministic layer was recoverable from this prose."
                  "\n           It is toast (loop-safe) but still SPEC tier -- add a"
                  "\n           `## Parameters` json fence or documented commands to raise it.")
        if not ok:
            print("     round trip did not stabilise -- do not feed this to the loop")
            rc = 1
    return rc


def main() -> int:
    p = argparse.ArgumentParser(
        prog="agentshim",
        description="Zero-fidelity-loss conversion: agent.py <-> SKILL.md <-> openclaw <-> openrappter")
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("path")
        sp.add_argument("--from", dest="from_fmt", choices=FORMATS,
                        help="override format detection")

    c = sub.add_parser("convert", help="convert a capability into another format")
    common(c)
    c.add_argument("--to", required=True, choices=FORMATS)
    c.add_argument("-o", "--out", help="output file or directory")
    c.add_argument("--bundle", action="store_true",
                   help="ship the runnable agent alongside the markdown, and tell the "
                        "host to execute it — keeps determinism on plain SKILL.md hosts")
    c.set_defaults(fn=cmd_convert)

    t = sub.add_parser("toast", help="normalise raw bread (a capsule-less SKILL.md) "
                                     "so it can enter the loop; idempotent")
    t.add_argument("paths", nargs="+")
    t.add_argument("--force", action="store_true", help="re-toast even if already toast")
    t.set_defaults(fn=cmd_toast)

    k = sub.add_parser("soak", help="hammer conversions in every direction; "
                                    "catches accumulated drift a single round trip misses")
    k.add_argument("paths", nargs="+")
    k.add_argument("--depth", type=int, default=3,
                   help="max intermediate hops per route (default 3)")
    k.add_argument("--allow-raw", action="store_true", dest="allow_raw",
                   help="soak capsule-less artifacts anyway (expect synthesis, not recovery)")
    k.add_argument("--cycles", type=int, default=25,
                   help="fixed-point cycles (default 25)")
    k.set_defaults(fn=cmd_soak)

    i = sub.add_parser("inspect", help="show what the shim sees, layer by layer")
    common(i)
    i.set_defaults(fn=cmd_inspect)

    r = sub.add_parser("roundtrip", help="prove byte-exact conversion; exit 1 on drift")
    common(r)
    r.add_argument("--via", required=True, choices=FORMATS)
    r.set_defaults(fn=cmd_roundtrip)

    s = sub.add_parser("selftest", help="built-in fixtures, all directions")
    s.set_defaults(fn=cmd_selftest)

    a = p.parse_args()
    try:
        return a.fn(a)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 2




__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/toaster",
    "tier": "core",
    "trust": "community",
    "version": "1.0.0",
    "tags": ["skills", "portability", "drift", "conversion", "local-first", "singleton"],
    "example_call": {
        "args": {"action": "toast", "path": "my-skill/SKILL.md"},
        "note": "Derive a deterministic layer from a prose skill and anchor it.",
    },
}


class ToasterAgent(BasicAgent):
    def __init__(self):
        self.name = "Toaster"
        self.metadata = {
            "name": self.name,
            "description": (
                "Convert a capability between agent.py, SKILL.md, openclaw and "
                "openrappter without losing fidelity; toast a raw SKILL.md so it "
                "gains a typed contract and can be measured; or soak it to prove "
                "it does not drift across conversion routes."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["toast", "inspect", "convert", "soak"],
                               "description": "What to do."},
                    "path": {"type": "string",
                             "description": "The capability file (SKILL.md or *_agent.py)."},
                    "to": {"type": "string",
                           "enum": ["agent", "skill", "openclaw", "openrappter", "rci"],
                           "description": "For convert: the target format."},
                    "out": {"type": "string",
                            "description": "For convert: output path. Defaults beside the source."},
                },
                "required": ["action", "path"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action")
        path = kwargs.get("path")
        if not path or not os.path.exists(path):
            return json.dumps({"status": "error",
                               "message": f"not found: {path}"}, indent=2)
        try:
            if action == "inspect":
                rci = load(path)
                params = rci.get("parameters") or {}
                impl = rci.get("impl") or {}
                return json.dumps({
                    "status": "ok", "name": rci.get("name"), "slug": rci.get("slug"),
                    "description": (rci.get("description") or "")[:200],
                    "typed_parameters": sorted(params.get("properties", {})),
                    "has_code": bool(impl.get("perform") or impl.get("perform_body")),
                    "derived_steps": len(impl.get("steps") or []),
                    "instruction_chars": len(rci.get("instructions") or ""),
                    "is_raw_bread": is_raw(path),
                    "capability_id": capability_id(rci)[:24],
                    "preserved_formats": sorted(rci.get("preserved", {})),
                }, indent=2)

            if action == "toast":
                if not is_raw(path):
                    rci = load(path)
                    return json.dumps({"status": "ok", "already_toast": True,
                                       "capability_id": capability_id(rci)[:24],
                                       "note": "toasting is idempotent"}, indent=2)
                fmt = detect(path)
                rci = load(path, fmt)
                rci.setdefault("preserved", {}).pop(fmt, None)
                report = toast_rci(rci)
                emit(render(rci, fmt), path)
                back = load(path, fmt)
                nothing = (report["params_after"] == report["params_before"]
                           and report["steps"] == 0)
                return json.dumps({
                    "status": "ok", "toasted": True,
                    "typed_parameters": {"before": report["params_before"],
                                         "after": report["params_after"]},
                    "steps_derived": report["steps"],
                    "derivation": report["provenance"][:12],
                    "capability_id": capability_id(back)[:24],
                    "note": ("nothing machine-recoverable in this prose — it is "
                             "now loop-safe but still SPEC tier") if nothing else
                            "a deterministic layer was derived and anchored",
                }, indent=2)

            if action == "convert":
                to = kwargs.get("to")
                if to not in FORMATS:
                    return json.dumps({"status": "error",
                                       "message": f"`to` must be one of {list(FORMATS)}"},
                                      indent=2)
                rci = load(path)
                out = kwargs.get("out") or os.path.join(
                    os.path.dirname(path) or ".", default_out(rci, to))
                written = emit(render(rci, to), out)
                exact = to in rci.get("preserved", {})
                tier, why = fidelity_tier(rci, False)
                return json.dumps({
                    "status": "ok", "wrote": written,
                    "mode": "restored byte-exact" if exact else "synthesised",
                    "transport_fidelity": "LOSSLESS (rci capsule embedded)",
                    "behavioural_fidelity": {"tier": tier, "why": why},
                }, indent=2)

            if action == "soak":
                if is_raw(path):
                    return json.dumps({
                        "status": "refused",
                        "reason": "raw bread — nothing canonical to measure against",
                        "fix": "run action=toast first; soaking bread compares two "
                               "renders and tells you nothing",
                    }, indent=2)
                import tempfile
                want = capability_id(load(path))
                fmt = detect(path)
                fails = []
                routes = (["agent"], ["openclaw"], ["openrappter"], ["rci"],
                          ["agent", "rci", "openclaw"])
                with tempfile.TemporaryDirectory() as td:
                    for route in routes:
                        cur, curf = path, fmt
                        for i, nxt in enumerate(route):
                            cur = _hop(cur, curf, nxt, td, f"r{i}{nxt}")
                            curf = nxt
                        if capability_id(load(cur, curf)) != want:
                            fails.append("->".join([fmt] + route))
                return json.dumps({
                    "status": "ok", "routes_checked": len(routes),
                    "capability_preserved": not fails,
                    "failed_routes": fails,
                    "capability_id": want[:24],
                    "note": "a single round trip cannot see accumulation; these "
                            "routes test path independence",
                }, indent=2)

            return json.dumps({"status": "error",
                               "message": f"unknown action {action!r}",
                               "valid": ["toast", "inspect", "convert", "soak"]}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)


if __name__ == "__main__":
    _a = sys.argv[1:]
    if _a and _a[0] == "--tool":
        print(json.dumps(ToasterAgent().to_tool(), indent=2))
    else:
        _raw = _a[0] if _a else (sys.stdin.read().strip() or "{}")
        print(ToasterAgent().perform(**json.loads(_raw)))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
