---
name: "rappstore-rapp-toaster"
description: "Convert a capability between agent.py, SKILL.md, openclaw and openrappter without losing fidelity; toast a raw SKILL.md so it gains a typed contract and can be measured; or soak it to prove it does not drift across conversion routes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/toaster", "rar_sha256": "d4d540104c288152b2761b7890aaf263e58af286acaf702d09422b6f3f198e16", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["skills", "portability", "drift", "conversion", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/toaster`. The original RAPP
agent is preserved byte-for-byte in `toaster_agent.py` and in the RCI capsule.

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

<!-- rci-capsule:v1:H4sIAAAAAAAC/7y6aberRtIm+ld2n/7QdmObQYx+13vXBQECxCSBEFCu5WIexCRmcNd/v6m9z/FQtqvqdr/3ap11hJLMyMjIiCeeyNw/fQqmMW/7T983U1V98ylOhqgvurFom0/ffzq2zZz041vwFgVdEBZVMW5vYTIuSdK8BVnSjN912zdv1llW1e/q+Ju3tkuaqAqWt6CJ33/0QdeNSf+2FGCWaXyr2qFosre0iJOXsP94G9tgeE3Qg0Ff5LwN7VsxvmVB0Qzg1bh1SfwWtc3YB9H4LjoKGqDHW50Ew9Qn8X+8tT0YFDxew8b2revbOXk9x20yvDUteOiLFAyN+nYYXqLAsgawxrceKJUM33365lOyBnVXJcOn7//y128+FeD50/c/fQKLGUDTJ/ulZtKzrzWDzlXQZKC128CqGvC7S/q07WvQFCfp2+dfXw1JlX7z9j//52MJ+mz4+vsfmrfPH7CO1+z/+fbx6rssGb/64dNH6w+fvv6lYxeM+T92e7X9plORvq/xvS8wxOu5Hb57/fwuWYthHL56Pf96/tenT8apb97KoW2+i6e6G7766YdPwxiM0/DDp+/ffviU9H3b//Dpm98O+4PPD5/qZBiAP7zGpT98eimQtlMTf//202vmv//w6e/fvBVNDIz3n9ivFB/77R+UAkv5Ypv/BHKBA3RJNAK5v1eijwpgmaoN4o/l/b5HF/RBPYBOoOvPtgNNCdhJsMavX8b66e+/H/fa/N+MejX8k/5/ZMnmjw31a/u2D2Bc8N0AjV4tv8z30fL16+VQTdlvX360fP3Nn03xqxB+Dfzql5G/efO+mh8+gYe/fI8hyF//VN57+P34a8N9D2KtH5OX3V8G/mLaHgR8PxbJ8FrWT3//+s9VzIPhx6iN31cdtm311cvAX8R8BM9nBX//4sewjTfw9p8ZoC9moDII2O5d2yppfj3D5/Z3+X/565/LAc439tO7N/4Y5UH/s6xfOcYvXYZfm/TPZQ4/AqT7MeyTIH6J+/j94cB/OugX8P2xeB/1m4aXOq89xP98C7s+GZL+ZZOXBYPx13v4q9j40uuf7N9v4/ifxu47sv9h5H7Gq1+v/fs/Vv1fx/i/hWRfIi2oXnbffvyi2pvdT8m/xrf/sp34Q5nAFMmHmu9qvdJjMbyBBFl34E0z/hl4fvmk9QhsFIPYjMY/s9I/2PGb16A/7vbdkIwghwVT9Ucu8V3Xdl+Bsd+86W2T/JGEpANuBeZ6X8uPQOC7UX7fMamL8as+AcvqXz0+NPrm7U/0D4Po8e8sANgyfxnwPwHsvWvyl8+QP/wYpAC8fvj015dz/uO7MAFxATbhr/90217E4+eRn0HkXRzy9X95Tng3XxL/Cx/9Y3AGzv9lQd//+VL/fRd9zfPZer+X98Wsf//mz5cHLPXjZ1D+jYgvNvznSB58yWS/TP2id03QRK91/OV7FPvr/y50vvzqX2Dnl/D86v3x3bvqIALfybd9EgFF+iCsANls3sDL4UU9h+TthwlDUPzFQEETyAjNv8SABTh32307BGnyFgKiDICgqt4sUzi+gZTav5LLB2y+a5BUQ/LPhYIte8eEvi4aQAGL6K0KthcRD4a3z3vx7tDAioD+vwf4/xHaf3DqP8Z7wMj/gcKO7W8I7K9kgr7vuaF5E42rxtrW9/+bmP9vs9c/Y7F/G9u/vdUTqE5ApQHQ7q1N336qgC2/+qzZ1++89t+V/08Q/F9nuVfp9A8mBE2fGccXrl+2RfPVH6vzpUtc9C9u+THNB1v57gU4nxH/RyD0A43H9us/UGPpixGkJKDK7+AbDPjmpeYfQf36KtteKeG1rX/ON/7AcYDnf/O25BsY/aVk/PHV+DGnGIAw+K/H3qX/HPKfl/un0FB/prA/fAIrGV9R9BZuY/Lt+4J/+PRy54+1v8L1NdnWjHkyFMOfhNtnSO8DUPUApPvxy5I/5lANy1IFy3pn9C8cGyaAO0kdJnGcxF//E4lhkgdz0U59UP1GJoiYD2z5/rOlwdrz9zfg6+//Z3jwqsb/jPz9O8Tv393C329jn6TTP7PwxwhABIePtAKeg+XtnZF/we0vMBsFTdsUUVC9fPfzYcNb8H4uMf4L+WmxfhY+NZ8N858fZx1p0Q/jf7wfV7zm+Jg4amuQUJPhbVzaf50wPhbwCr7hHcTHpKqGt62dvmj+p8r9cyoJiqQXexsB9UyL6g8yzBI0r0j+bRL9Bbj+N9lpGhTVq0z/yx/wr48DmhehA4n//cjpRRjewI8vZ02//v35uOlLEwiUf8V0fpH6cv/3Aa+HXwn/IxwsxvxnK31nv5h6H/QbXwBGAHBg++rrN5Bmx/hPnBswsI91vePh+wK//3MdowlEJvgvBUb4mfv+efeXcICNzfqeRJNmqgFDGZOv3uf5+vt/7llgGjDLjzlg+T9P+y4LAHz8zSsr9j8Vf/8JNPz9DxP4P8h6qQz6/nk/AAZ/4Es/T/3112//7T/fne5f6P3uQd+BzQdBATLLt/8XyGvv6fAvwFZ/fYM+rPz1f32u+Ni9H6M8iR4f7Pb9gOC99d8q6H+VBL9/Zz7vS/nTka+3gPB/TPBOVP5p99/R35ct/z2++yKQr7NakGP611ne29gX3QsRX0oOCcDBKJrqqXqn5//x9kpsyb9Eri8GA8EzfD6wfMHRa9uSdzr//zLp/H93hjk1D0DKv0D3208f3/+t//u/J2wOqg+D/+Xng5Bvfn2e+c2vKfM3P+fLv/4xPidrlHTjm/D+9VIHoEvy/9tx7k+vIvOr5OvvfvzxRR5//PHvgDok/3CoC3785jTs0/ef/vt/f9OK14l7m45vVvTisCAZjkWdvLbRflVL4B9wHKD7+3n8q4766AeqqDL5sDxg3X/7v1+4Dn/UxP3fvnuzwZi2L7KiAan5yprmD807iL+9F2CfA+qDiwE4/Pb18ALDv32W8OOXq4u/vWfP99Itebse5S+s6ruXgvccMN0PdV7XDcmaRC/IrtoXH3gB//ANUHxoqzn5KP2Gx6tki78kgY/zgqn5/iXsb3/7WxgM+Q/Nx5XB4e3jJHaAQYef1Xn79lugfVoVWQ4wMwGF2dv/+Onv/+Ptf739s1Hvwl9zmMHwxZxAQ8Uy9DdQLwD8b0ZgabA3L6LxMudPf/9sQyCmATUhMH6RFsnH4KpoXkj22aCWxH6LEeTbx7HBZ4LwfkQ1fvcmp28/6/u5On/d1+QtiO2fg3oDUgOwnJ8t+Y4fADWGdPvmDTC191n/FvbvrCqpX0et49/etKMJSFf7zrxeFOrV6Wc69vN2f7QDIf3/GN64LyK+e9NfDvV+/t/lffB5jjT42BeQIL8MB8KDtyZZfmhe58PJy1TvePZhHtAJWCb6vKXfvvb8RdRqsLHDl7nf+4D8Gr99viL6oRk+ey7gc2+fjwi2t2wq4teJxX98dqkhb6cqfrcf0PQl6fMuxJ935d0HP8v8wkujoH/51Z/exr19Pt79x+s2sFkvaeybaVztb97TTABU+6M1g19gtW9TB0I5Ceq3Rxtv3y7wKwC/Hb+s8LcDX1H30uylO1hECBrr/wAVc7W9rwt0A0p3IBuD7c+DJkvi797YH5p/nP/jjm54S/u2BhoPv0T4++a9WPPbCzzeErA4YJMBVDJg6h/AJk4g/wJ68k6FX1H7YsKg5Ene2fTLi4Z3JwQbCWCtf+Uu0LNpQTbcXv71os+g5Cmi/F1e//Ln776kmg/S/o6wv76izIPXxeKvKoSX6b953Vz+qnj49R3lP8Lu5zLiPZDsLwe/HyczH4H4R6c3r/b3E6bfSYvGKaiAxZO5eE+lwze/Ot4ZPjzg4xjiPQO9SOzLIkC1+X3G4Fe3ot98ni3cPh4+Rn5OV697tQ90/hw/X8AL/sU48C8XwfBvroHhV/n/Ie79uvbjmu5Pbmu//fb3DOHLFW4KlP5MnV8bpb6D8svlQOyDLQBB0faPb953CNj+5dRB9X7NWxVRAiL0y333K6H9cr37usn9+Sj1df37y53W69cHB3g9/faa/P6yJDBF3L5fJAPK/en7v3yk/U/ffMn54OmzBcHTa/GgMHk/vgUCQKyB3X+lULCi38sXAWJ9Hvv964ylmz6403dv/Me5zQAc7T0cXv4xgEI/Sl6a/E76a9Dvxdvv0PozorzD3Fc/7yWY+3/+nGu+/kOxY/svdH6pNYJclHxBqF/bKfh8p/6ePsH3F9f5/PjZdcAv4Dp/YDMwf588JwBa8bu0jz36vNZfurfhy2XfjQAo68dl/U+A6IxBHIzB573+zDlAd1DOfTu8gBpGv0NecwefWQN49xs28vndkAcgTb7u//GYwBEUwSOMplECCzGKREOKZpAgSDHykBA0+KbJIApSCsFihMExLCTTQ4oydIKS787x2sAfX5mmGL846ufGBwgGMEsKfPo963z70gX49DuCvhvjZ/7z7rEfKv/0KSRxMEzCB5n9+BxhCGPIgxc6hDxBHGM+bpRzf1zP7HHrXMkxLqRHj4IdUkfdvhdXEJLPM2/dWU551A+5OimPYvXOKypNKt3AjwN1uCceR+R4O3sotbGVME+k/yCoAr9eDDyeLGj16IhZSpbeIKOwxZCD4X2GN8Nbz7PjXnn7gN1oe4q75JpoD1jGrFDO5se2aV1ZPREnEgdxvFdURe5nj0DugXvxOyPJEb5VDiECG8njdK+Wa1EFlkrYq387Q7ht6oOgrLFyERkLjZVBxO+E9VREWkTN/tAfDiRRdKmaFg+eTEsm6+3MC1xFV3PFqU0ySoViU03CddjzhetX7cF0kWL0hjpqXWtmragzyc7Fna0FDLY5KlYgV/84I8OAFFCk+UowFaWcLaxlKo9AvQW2netUdE5NlDg+faaV8ZpUOnHcKxJin/OjPtKlZ27llorwlXLZ0B6BGRykOaqhRk8y2mX6pagjiMfIEYkyZ2F0uVdFh4VhEaEt0VvDlCNdmkpmvR6UzKJYNVYOp7sP1QLXZhW1OGLZ3JmlVm2ZeTqeIgmr+3RsrvZgC4JK3dBY3bhz6oaSvKI7U6XfZu7RLY+RLlT91rTIMQlX6Ya488a4iS/estvhHNtb092IKRBOm+WosjXYPnHsUjHc50CIZ/fo2bvh3QNEKqdJOghWWJ0SNLg48+UG0cGBfkhUUZiILybwMrKIENZZvfGEc1g6B/NUXKetm+EhmKpcN1YXzFT1eEc5Oc/rykRbJCunO2Fb43RVlmupHDkegWhhU+vHPNTVUZZyQxemwJiEE29XnuB4zTVId2VIA5ZGTot9Gk0fO6aSG+Mkll8vUbLCeoGwDT/oet5zT92fJkuvL8gxKw9R190a/aSeUkSWz1L3YFOldOvjemcjEaoeihCrcdrezfWQVQi1Rb48bBBQY90mZ66eJ+AT2fP8UL2ySXw/M0oro73nwRSbS5vOhzjo1qwLzn7t5nx0qO1O83k/vrTcpk+P29YwJxp/3LcUWZYEv3q+vekbUcDXh2YqseyP63qnZevePFmNPpYesYaOm3ethcBMLfV9uaLzpI2P3DOy6zzjdOqMs9oO56ceKuGFu1/ZhABqRzOpyPIF6nk5xRN260+eXFNH+r6FucbmDYltR+myUvsU58O50mXaGkiv8guRZDb70inPEXneOVwAm6TUrhsg7MyftZOsjfg1ZhXaG+uTRu1uz/vXcRw72GyLDXbXpFcjv2Pq++WwpGfjKaXYdTvOsqE4U82TMM48qjRuYv3KQfO4N2xHZRrq4PpikCVxUYzDA9cRiltn/XwhIaqnNUqo7z0EXIiEn1cpIsNduxA2MAEqGgRUe/wmp2bL1kV5ke3R8xE/HagulOPrmcbXh5iuO70Rena9MSQqsZuLQAokue2V1wiCkRTudrmVHm4gEHp7HtVUFvQLQ9ziGBEPB2k/EycjQti6xmNhrE6h5a2kW6skewLMBmqEpw5Jpgmc3zDnnOQvOGzMVzKuOkRwqWt4Bu5wUhA/KlRLSYaL3kyWRzRJjXiqQlRXTenwZmk8O5kEqvBAOBiOlAD48fc47GQ2SajumV/h631LkKd6uR0vZrhUAIKvVyhPSiF2NnkcMZ9m9/uCFbikH0/JE6sUZ29HCTPM+yM42k7EkVx+xXlF0XAJszqRKCk9s1qYkvvq6qy8aRTGOfG02MqKdddcdV+z+5inNnJcZIaiDLoa8+upqI4j8cTaZJcWkh8IOOVq2oAbH4+GJ8OTDdrYw/mgxitOurK4HmrtVtfk6sbcvO/tWVOKeOI1PjMuvFEvIZTM5WFqVtUd5MI3aVZp63v+xNGLhjdr6ve3snfJHhsXHuQgiCJwL4L0wxi03oYTpm2TJR4shZi6CLxgOGps99JYl2m5M4K3CLNOpNWEzGNXXhLbictLdzuGIuPtzlZEQsN4VNQkLorCSzmK2V5FabvuDGxQDyqkgW4tBdgn3SlIFT+yXPQxEKDn3BURf9Y8sYdRpLIg5XbRYCfbjjf67OQGkVN8kOAsb/P0tiJVCMMp/whTPkaSmdeRuEmXGTyh6LhP9RJhC0sUTig8N5aL5UJZNToMM0K/XYez4u2EnkdmbcZmLVBT+NhRWoQue6vs6aFuMgLgx/h41FBdPm/5LCKpGNVwcikPtY/v8rk9zoLPya1ctUdri+J9abNOuLbFc9EPUpSuhNIlN8UmrF4cuTxPbsdsui+EgFQQVzkPPctgYa6vNtb1FYeduESDllqrpF1JTocs0ZXD89xecrtjCdrv0o4gjV1iKCg+hpJ4G4+JUHmP24GSj1HlXoQA+GuBGBXdzzWeNb54EtSEhuRJwNQm0rmj2vY43w2G3D2PK9QhadkykEku8roNU3dmE6XjYK4bMGQ49lTDuzgofOfTDOUhgYYPOC0cSOPLmVgkHQ9k41Ya/fFpHw6bDmATwQVyRVnIfF5sqw/bmHjQIRfvUMIG6tLmHiDAi7+EOltsDpqp5T3wU7VrTPLMFTNyaPyO0HBrh474Yjkdj3nIcKuvKIkjLVFf0MRdOe0SkhAsbKIjLa7E2Ek2p4SmG8ezWlEMA7Bgh+1m1o+pk/l1dI8hVTFMwjqM13PM+1iPiNuZjo1A6Zcp5X3y1DiRRCEEnDQabpT1o0FDxVPkuWrsa4xGeeh0aUMfQ582J+gmwdRBgiUEpmBYfWwwSL6o4AlX2m7ObbfVWHkVwe44zwXnfJcfJt8wVUFUlqjJ8aRZMZbUCu7haXgnG7wTbTW9XJoMT2I/Z+Gi4GiGLWjON843lcWaqGZy4sH1rlgTnnU8zcrlqJDMDfbOzXJsPI5p20eVP2+xGWlLIhydrFjWEMjIzJJ7ZsJFrbo2nhZL3+SbeY44xIISXNDre5gdfdLi8UeAC5pwMhHJ53T6gpaeHCjbRMZkTOuUtCxXVVflgxTrZeeCzCHfvfPk3RcrjqI4QtmJPyJ6jDFnMoIjVH+qx+HCc935dJpyfgDktMWog5dI4yogWdGESXCfIt3RV8kZlkYmbKLZvYc38U8OqdlJNYycTg85nUjKEs8FmVfXozSYB8yO0xQXrse+1fbUknD8en9kIRzNR7y/AJwtL9mJv1yy5nAOzCJGWt279KKG13ORUQyVwGrJhiINIaKbnOaFvm1PWhDtM4z6grXSSnqR8twc4DqlSpzjSOfMDCU1G3t7eUbhbqhDglw3UrgW18DurvjTuz/Z3V2uWsxlxDjwZ6N6isd7fkwJ8xTvyblq+FRExmNENBs0TXCR9SQtN+397vJiKh38I0vKl+2iumbisglkGJkkCFIwPw4CrVTqI3PkTTizV8nSz0S7ByI0a9hKrlomtLB38drZ3oRqmR4+Zwxb3vgRQfPGIt1GjrvLcmmpJSfWRaFIO5k25BpfwvyWr40oQ0g4xKXXGpOfuzGayOIpPV3hKrN4UZBY9mKbRXCRlVK7YWKY0JYTHcfmdLxiGEkZj5o5XjpJHbjo7AeyaT2txl6ukOilIeBtubY+EzjENHUZE5BmD4ndKUNx7nQKL7Z+egxoDg+P5z25CQUKCla43aagzi7BE756HRwI/MgdjzkTcT4wd8TZ5IPNt6egYnH8tA1UiQ/hljxPMSNzV7UgztIJuLS4ijYMIwTTJZEPw20PcRG1QXFBXuQC3QxleAzZwl85KXjGayeZ0zAdZO+KjFDIIcUmxudigAbz6u7FlCuKgHZPWRRizFKncE937UBHN/tSDK1NnsJIYw4nloDkS01O+5Ka/eD1QmW4uVAlnDzsBK2rRMmqB9E/NhZpE9GVPVQVNayXEkdNFzIvjMrfvbW7McQ0MzTstGd10uE5Ewu8aJQKir08maHu0UkPJOO3ndLPh0DgjsIjnO0HnNnJs+zsw7Ns0+MDnkrHRhxpv1/2ZDNaWnTo5hQguZPGhSZeA/1YIWX5OAG3REvWYo583BRt7ZI6e/ABHrvbZVIJOD/PBHQzzt51sgclMWbcSKZj4ODyqeLSTJIa/AHb0RKf1GjtL5yFPS505qQZUYn3wiv74By5QQtpA5cGIlVuOSZuS+3StDAlLITcjwF9NA4jLaGtX207oud6cq5FRwtmy8FSX342fuEfz7MACfFTPQxaY3nxTroOd34yGnWRj3PH+C1DDKceZHzlyQ2A786+6BvHoLrUEHZOQBJPAb5Ujq2tKa3E+PwgvIWZYiwSTqe1L6uM0g/20pSgaCGIDLW1i+gWd5vEzgzN0vnsZX7Ba1hg2fvTVnSJ41IHcP7WFA+gwFk1cVcaIcgqsT/KrK0ZzbKwcHNZ1lgP5qPOX9rhcKBZCom1IZaytdZb/8IPLgNDsaTQEB/X7XBiD5N/Wo8bohQVVouAmxbohO+P1a+ds8p5t0usAwtpOmK1V+IichncU9ycJ5wQNx0ez3Njek4XSlCxXaqwtvjWcnwa4bWr6SInebkfy4AIgpPJStf+mAOWxRkI+Wh55ULgxHgJzIdnaxlKeVbLdWvlWwLvEZN/QYsFNegVGjb0Mhbp5WYUKOt70kkyPFL1yOUawJ2Koos1n+B+Xtxnc781/UnwOLU83cln2aian3h1/SjwlVUezxsfq+4SxtJNOWlzOZCpqQeQeIEC+yCq823oGU19Zl3nUGnUC+kG+VxSBnNb3yamI6lVf/CkOdFETJ3qWvK669TchOyUsrnWGRvqt6xwXUvcw2LC356m7XZc4pfN7e5a0mE5S2r7iFj9oemXq4szMkg9Kn4cx6G6oj0XzRLRdO2pQqXUgEB1k4cx1KBnM/OVh3Msd8XnGvNoagLs15WPMV3b5/oNzYPrUfbFLPTlu3rTj4UQyH7QtCffATUMMENWXWsB3Yepx5XAOQhH6MIZ9HW96aR/AxBQmCHf2fKz9PQc5fjFtyyd2Q1Q6JmsA8oQXRxwuzOkKec2Bjuwj9hhittwDTokysLTVUO8XXETYOZnldPYxRtO20nsgtDLG9OXQnJw5CFn9so9bICS3SQsFGimlRBpPvkX1YPpM18uZX+mOAoEmsq5OEvbV0aSrawe0+C4R6TrrpLaaJVWaJtaZ6XP0iR8w0KZkhUrYfL9SUE8yMPG8+ZFjOeeck95ZshJ09qdzJ4IWi7X7jlGC6dkrfiQvFGkxJodAcfr2azJOSPTgFtFiIGPqpfrzkR6N3GrOgWOD/nRsivEoyUFhvTTTe+I61xSCoHfHuL4gG8Q795Nt5sMg+HGK6TTyTNdFrCvyZUbY5hbuLK4ea3ZJb0wTHlml6bVP/LSmzAVLoUc52n/dBB5ChfaU5EZ51PZsIkkM7fhOUuJPVSxeiryVlS4OyaTB2iZpNpAaOqY8Tx/aWxXsyADJGbHPdyuF3mzodUZYrqaPLOl9qNGmRkz9lAxspNChJBEoGYZmRk0XsJ+FwfxwHmTuUTIoPX8xZeEJ/1wRviMT8KNErFooDWCd7NJ66Ay2Rh85LpUUIqN2klFjtzyfJFgOcVLTA9haoBGJH1e9rk4nuCalkyK5Ipi6QtHON4ZWL8YDeFDZhJxKcNPbSJmqLQ/xx4j7xi7Q3bI3ld+sVTuvEKHzfXuJSqwPXctb3w5FjTjYw+M8sJZg+0n59KIQaM605rQwGCXvlO8bO9heb8SIm4QwmwnPu4fump0x4vkKbToLsvgrmh1oAbE8c5awsB2TkZmhGqncyh6xPWxNip5tNFlPgWYcmlj7XgJtK4wcUHoUc7dWZver6WTI2zl7ka4kqQopiylaJo+0A2KSXp20dmZR3JsONP8ceiIo1SLusPoID+xa8kFTnqhzYU4pskoiPV0fB2ZrspyOBH9YcnPwUE0rOV0LotaMVopERf0jloHG2ace19Ljm48Mr/FsWwrT+d5OazUZSErmi6AXQo6jZfEbHn8WtZC/+jrQHzylgFTrXvQuH0FaNHMDe2eh7t5Zg+Ydp2g4ySTJMNSKVvBkBGXkde5wwwsS00SqJvOVx/hJMecjT6pWf22XE9Qk1TxQhMzxhKo/SwkxHu2KHqTlxZTZQZdsq1OEcYpDtDzSp68Lb1r7tAdaKNCZ0afG+sWxBmRUotrJNRwIJBlGJYIJWCmFmHvhinNAohwI3H5ymVSaOajtVkNv8QCu2H8lig6xjCMhYrQJiaERKjuasLY6cmcQHlGcol9PjxKlhPWddr6oz6gHB7fo7B75sXWGvzODVzwVBujDonkJPVcoVWkfrAG7wSqhwV4NO5fZfuS7hs8Xdx8wS93Cq8vyEKMCcLdYl6GhmyQaf2BoD6Ix6QcND3DzWjSd0kaGNXgFhV/YnsjmsR8PbfcWl8Yo27CHVZD5k7K9wHJtUFYhRbw6N0+50//eSId0z0mLnql3YYPnkOyP0JVr41SvbXLJWPnNkf4w6RxOTEWT2YkdsgNGD6bo60gZNcaIaPZtXVo8iUBLgidqJCID55pa4RU4vJBbs6Vl1VVVzerpgxu4z8kYThIyA3x3YgnYSsINh1S7xY7wbea1OObV8JSNxr9QQhaFDJKnDClA0UUkNQjQqveSr7CSas+ZNA2sBye09Y8DFZHsESsGcGMNF2mhbuZ93wD4loeEFE2y5WHtpHZXXKGlyx9HodHmOtMjVvUBTD1esa4vZErOTDQptOnZb9CG6mKmx3HdwNLU9dL79P1qne+X6FP4mqcOsJyKV2MHnN2mqAaRcsydqfbwyqPu1yT65kqkMtcCdl08/YqXYChZieDi8adUAlwrznqiZE6Q/gp2ydZJKMtYVn0acfqMgWWP0RpGh5ZDnD73U4TKFbcE4FOyOlsG5LseFTPYnKMM6I5kVxPHdjFU1piz1MMQd1xu+yh4UkVVFjmUQIa7k60+B6qoM9+v4GdIbU71Z8smtsNPSd652hPgMyh68wEEObAAu7CiASFWwubDUuP3hzSHK9l+h4lLOysLoqNq1Uxi57gJeuH6Wyvl4CxEqkqBKYhISei4q7DR/Q88j59t599J0MoaWzeCoWMNflV5Eh9ohljopiEcsDSrIoR9EmdzlB5KoMSzWsG9bOChMeukKsDUjotRWNXh8KVpUbn+To5cBcNZe2Tx8vd2D2UiaAHq9ZKZ5t7QR9CoTY61LP9ehMUIk3EHPYYX4vU7YSXFI8IMjoraYvh8Hy/CCF0L7VQEOJByptKq2+U1eq4mEJb+Fi5sw/dRrt14CQ5YknauOFhx/ZqP1dP++aGT9EhsqAxAFHLt5SvzYrd8QtxrRm7eHqXIpaSUDof6K3BOYhiqeDuGNORaOAUPsPFfoS3YvKvKi+NSYa3NTL6QtKi0nlrDqKITo2Q3zbgOkHq44cDOkC5ZKZMw+eA9sfKtoM0es/8zSx3vRUhIQ/L6iZfE/EpgVyqCLB4fwQ6B/FRvqHR4GpUVqFE41xLPuDAfBqytocqXkmqWpGZyxAHkx8NYItyKhz3NjdLSZn3zYCIJ0dJhjr3eb64S7mD1BMWTIZJ19wrA1hJpNzc3NP4zA4BipE7t/fN9SncIxWEsl6x1Vn3Sy8Va82wu/3O9oMq7ExvbTFqDUqJ4LJAnUs4HxiWd1IauXc1lwWBjCAKQhVScG7PpVzCbd1mEXojhRnCRec6xuacY/OlPmcNVfKl3D+EwYPWKUsybCtinQyfM04yURbECALR7iHBKDIboQoHZSQnaacSF6+EGUD1KpFnDrBP2pYGWdnZhn/ydLSpPneyhws9nS9PZZqURVezbLAT5nRs8f18ajlIbCtEGpf6wJ3cAd24xzT7BdOuN0ZMDQQTKVY/ahf2TJ1FAHRMfNdGmHcyvpXth+U9TIHmh0tOgnoL0re+smLar9QyQIUJM0+JTl8lTH4W20NMYvFMx87pUaHNLT1pKNWhUGRVGx3IUWWezo9z3OZPMTk0buJWoQ9VgVoaYXqICDTtGMa7zh5E+D7lbz4+XWmx5ZrJH1REAWV+1TdM3EtLzBsW4SE1lxgESoQNuecd1yrXmCXI/gGTXhCcB/kRpOjr3mFdgWk06iikDzwWDsZweajtcaJM0rL1jDH25ZA0UqIR62Pxl5xQmSwhbq7/oO9cz2+KAw+F7ACDj/LZ9Uu0kgkf7PPdSj2td5rMmfLpLDhZOJzDzpHx8wkjJFO1zYijD1JW8NRhbcbpTPGUMeBkebQryhq4R39qb9WFspinHWyJ3DphZq33LX1qpCLKVnkTpL2beG8BCCUnZ7EwYOlS7o+bqbnzJOo6fIwPfkBb5dqULlWg9Ozv7iQuEUnNm3fbx+bZAhq24afR7M1zoTuq5TjbQhAjQ6hUkELs0gyeR6VFuYwoarELN6EkDg+qhjFsOTuhIUO3yMDsOzbfyN5/4nUy+3g4AkinRuOc3BftNG+gThUGX83ye9Q9D13YPM64Osc3UG/fLpq0aWWmY+a+jMlFEskTxR/10wFLXPxcRyxLhCUSVFWxSHYM1JXOE0E++G2qTubFF05TvhtMjCLInehMmWwfOcMuPtIcbXHRBcDnYV7MY/ZwDenQCDsVSpvROW2ur4RVZkdXE46PKd24MH7gewfF46aFaKNEaRSUdzRkchxtZnQiMolpEJB2WB7NynOaeZ0yKAuTVIbIBU/SVb/aq4bTCZURBi9Jd4ZgjFKBIHU1DqZAajNFsRWXqTU7o1eW6wFyotLNSA8hGUz7jINRKDyy0vKUZmjmzIdgsOaQ9iZsThoGRsMJaomUV0qzqcIBKCROt0e/VaUTnlk3OD+V0x7y+yjIp+i4b3x2k6MV0JMClRgdfRSbLjFYDBvdMXYQxFXy6QQZGigNQywLBHS1TJhmrf7+nHpvv/eTsNT95QiEFxRR+m0DwtKa6rgvUZ7REeLKYM56KF33EIQxQXik0zFRaLVkLTLpHI8qVGG0S3pmp58rzFFJN7zB6A3ow5xj7A6VaSiypG9nJraTC4uPNJvH4x07SqR1fXD1avkEqHFyZ5yOKIbsAeJep9VYlCNhMtKznIxbPIY1TzSGK0SkUe/7SSH5ySNqAhr4MGMNLpanK+cxYxQHa7yn2xlHo0ttVG7fGeyImi0CexSldeeZbVm0C/PDNvLq41jpFo44z7RhyUDRZDHdmanSG1jq7f7EBZ5o3QnVM57AcE6mqTe9OJzukCI5LaP3FUVFx9Rwy34TcrTJETMhKbTvxBIRBUgooMXNZZy8dj5OtXgUWfLzAdVphIurSelPekDj48g8asnD/apErc4wxpVwKih1A32REMzTCVbCp8t6Z7g0vUrZoQcpbEL6RdgibD/a49VOJa8Kw9MR8kd2hE1DE+noAJ/ifNa32+VxcrudYovACy0Vv9iLBxcA0Buc9I9YBJxplQRk4OLdVzz+ojLqueJiND8I+vWQ9I7S0tmRRR/aAfIv/rlEmAhFNz48kQEjc2bQsNWEoTdWysYesNbn8ox2qRHzEGeja3CWq4hU7XUWvPopDUoOlZnQhtPZxe74yDj2DRQNx1hEb9tVeTxOuVAhZR9I5JU9KggJ4xsLRwc/g67JuY+W3F+rgQLM50RcJbKLgGW3lX+6DxUxZ6/KxSzsj0F3ZagnfHSZTSxzuhNRf027e43aBLXTS3C18ZCiXQhutmd4iCpmFPSJ0LqEoZuByizcQqXBNKH0MLdJH6HZPqP0nmEhfu6hNdeyRWbs8w4/GLJa4njnroN5S4jqVBWrltwh+GGeV0RjBJK5UfXDpksr0N1679KnuhHlE/F7Dk90ib2LbqDVBAJIXS4XqNNL4z137ATGb9EyxISKVeLRsLiN3nL8ZO/UDt41e8SiFBOcbb2Rt2X0q5tjE3fn2eb9ocuykpeUe84rHqhWdXWOUPwKkh9EJtgo2ommOViBs0llLVdS15N+oB4Ek2KnBCdSP4RkTBJZ3dRSxMRtHzKbB3naJJ1BG79AEs6LVMKY/KJ6Moyuc3KLlXcjommcLy+018nO/d5T1kU6Kjo75hfFEq/lCeasBla44EyTnqLMT942rYNA7Af16BePSDxyHazR7kIe2125cB1YzmM1+YEB9VR9v/D5/doowi1/ZJcY8+wrtRTRYJcsejDCRUcJdebV58XnzqC+t8waU3m3OTmyJAj27tr1NbWz2TwaJ1Bu8rf78fgY8bxJrrflgHdTdoij1ZasMzOHGDWM9ll4DOehEqHnE2Wcq3mkyWbKochFB38BFQjUXFUEOzuiJjdP9AYYqnfxW0HbAqMl+8M4j2nxbEd86vMoOpAKZ65XTB87dNGut4CT7Ek+M7GBrdgDHw4qPCUDJy+lfSS3UimHkImL+Zz0eD6eBGR5LkPgFkO/eefMxZJbkS74FAxeHJNMbXl5XLGc3iNXm1jYpypx1VIfU+Y0USBpCSB88Ed9YftepJIJZP6FNcJw9w0IOmBwRsAIq9+maxnsKkSDTZnrS24ORQLtFyRxoGVuov3cmCj9sJ9sdrgWT8Hle+J0Zb2HhwJLwC6tXFsTWhPA0cipueMXHFGG4FqfD0nOmR2K6PNB7urNP6KX05PeuWgPmINKZIqwu95IGaiUkDIKLc8GYRzjQRYyXSPBOgrTJl2LxNLULQqQ/VBsT9zw6Grf+dcfuh1piloVt9PQdmvsuA9Lq+YY95QdDcfN93iMF8qQHlAedgdzgRNpxZJyoLX4EIIXfOs+c0tSrkwHB8Por2tr5XPVLSVRKtUW+Hjgz+mho0y7Ha0LMSjRc0XMU4z1hsQWRnqW1kPAEqaFZ/5cwysgDUxoNDuuQIPIrXG3LiMGT7pyMAHQVMjqePNDma+oHxdeSK/CRjNkWsAuo6sjqMzHCjeu9Pykzv3dr0hlOBESe6iTwVK2B/DQxC8MV3FpoQXFWBh1Q1r0hqBx7FMJKo+04gXnrFhudMVJFdN6EhkII30pCMayW/58v6GUGIamhS0kyS1xQ5AxrNm+6YuWNxkQKQ+ODbKCV150ec9Nn7zbCIMa2G165OiKXU/SXW9pWkNhWnyGwcZm5fXw2EFshX15uDyug4N3q8ExUuRRIecuG0ZZ15E5Jc3mtzOKn7gdSpO2QxiYI5enql0N+IkNqNA8goBLeaGMuUnHZOehi/0F0BVzQlLuCUgjFViMRHkkIR1rV7k1y0nRbERSo6rbkm5WAoywztsIufRK06QlzCjnaextIabmQvDMHdezZTN9yiAscc9muXAx8XCIwS6EznhiY62H4o6/iGoSIfxmm513Nxzm1OTxA33c1puH+oEdUJsnQy0XC6vAzrXr5TYGqjI0qScWGheysQYTW4SBGqWGcuGmTwu5cpRIoFJpnqX8dtIz8SRwrE4KlqyqyH5ulaxq0NPQZlc+SzBcKA7dUGCU+pz5gqN1nb/rkhaQVnA7CM39MQtKco49sjxHrRWt7q1/rCgiHnhTdq6dcyXFtIcge/UQQPsSlba7ZY4C41ZWc644rXWJuSFGckX2l9tcgiITpFVqE0kh1belrGyytGWZGOnmaSupQg6kKlyTJcWiZh6lR1RJz9SPWkSbLLh60q0xnnzT2JLUc3mRP5Mo6ylOgkp5GJBezvZiTkScv+loYMONdbHvyGVux4t+aKpwVjL8rM7uBPPe1bpJRSshpTDeheoRdOxT7i4YyUKsfV0haGdg3jjKBA4nxR5nOWcYmV1ByezG7BHjcMncbhK0esuksk9LYs/szXfGAVoSSjDKmbcimJ34ytWu0ZLMAjFpk1H7vOZGR7My0W59KIprLdMDut0MnXmezJLy9BMh3Mpa1Ch1xzC5P2cOQmBSV3TPjTxn7dTLHXsDZJK4zZ1VX8vn8HjeEr1AdAp2nPHsNobtG2rQFFBS8cpFZiPudACV4kbc12P5hM0Td+7TMpemWj3S8TXqsiJWM9JGO97LgG9uWzagRl7lI29IN88xoOecDqHAtWq2tbVaJPf8PpuPYDdKsTummBVwJy0W4blnjfRCguITOgnJcjsRrRtw/r3zlOLSbUHjHdQuvm+b3WGdHjx672C06306QCkW3gluxadbSRTz1YRGyzlULaf2Beb0DIai7j2Ja1O73JIoV0xbzmxN1bECzmGfEjEuZNtyHhV+HiBI5+EG3wuvFEmCbhkI5hYzdPtLLByfpBwWuyCclQeiwTe5ua9N5QsZf1ew0bAPUxNBt6rTbbczUJFPnlJX7YuErUV6su9695hGB7DM2zMZibAHKzGV9awcr3Ekd9s5EDK8Us9FuzixYJ7DhhOMzpRQmTUV4gTN0lMzsCA2xaaKpPoMG9Y2ZjWhVXMSY+QhtDS6bPBiH6I1SkSaoE8ZBMEXGFpM9dxi0oJk4z6OYyCTR9iB451N/arSUp/rj2g3KBLMMFBs9I/nzNxHedqddKYh0mTECLvz8y7c9rBnaqTz6nQ+3NAhrXujuHJSvsFmU+7MnC+x2fOPu1zClPHsUtKtpwd8GQ4ITGJHm94IacbkpFlHK5Vg/l5Cc5MVhUklq2uTjnuMzSoXnCOAeqOSqKuhA/pU3nFysOhUM4TgMAwVohPoyqgyIxywDgqMotoz34tI8dEdaWY4dHcksXHfo26wer/fJsgjD9ygV1lBgoWudqdV6fVI1aHD+TrapVeZelYP8ej0XYNouSbm1TkRVqtUEZ0xM7QRlG1L8ky6q8GVsDdbRs99ydz0s+9rt70Uq4TF2WBLVpIvixo9I6zCTTTUNAZENH4C4uUsXxCKj5MqSomW443hoTJX7HrDOQJWay47MaGE6dnTtGP+MDlTsa8UAahUkijsIU7XcNz0U+mJIGu4xe1MhqGtrcFZbOvuzBJ8POWDDEcZfVzk05wDtA4EKOc8G9Nul3nKj5A1qfrEyIF/VC34FjGeaodewESZXjQq4Fxbsjsjj6pP/SJCNMsJUxrCBo5EgiZcW3HeghLXnjdF5nHoaHuIiWFdvo+nbhIXL+x4siutymzdW+TQbJtoJmbqFnOLEgXJCkHqwltQAz9aykddnbCsaWKkKBgfI+XlbEFVOKyafHhs9UzmVw11GhVMY6XdKSR2zbzSq/nEbVs/a1DT90cZUG1ki5OgOU+UlwrYydeRO+kINMIpagfbC2nYyAnanZvnyZ5dxX0sFoQa89l6JJr6dfLP6Qwi9U7YPmDREKjorhD6bQeAUTeRYA8Sb7jhsr7+TlZFmGdiZ3uMWfyl6DvIrQCpXd0YR2puzSkiwawVK6cW7dBsDIVK2dtg5ESmPqmsUNQPjz4pihCOqng63gqC4stztV5zdYQFPLxY7KwuVe74/ri5QUai9vUI4pAPgwykOSThZRI+ztIsu/iJ6c6gzN+sWwc7rna54i0BEJhdMCtsXn8LQqwalwT9SMKcLof4CXou9LFyY8A3AZRiWCyjvoi30IIrerJvyZagCoDa2+nJrvil6mmcZcxLzMPW9dylrSOkt8PzFKVQITrtw9ZyOb6RnaGpotWCTJszVCxEpHNf1qOYRkXY2bK6avb+lBHwlmSO3Qk9zg2G2HDY6SddhFAyCxkfabdy2R+XuuPPYxnHj7vlj1qU+5IO6Nup4Iy+Q2dHcSO9ALldtAkzQDlRTDsjv7lVtLXEckzXA/c8L0zH3gEFlU4dnlzvaaE7J/UeBMf8bM3zUSv4Nq7syp2ya+s6kRfnAnS9GK54EfLZ2e2pU7XClEGtywyY19yzy2zo2QZJrl5dCzgSqts53Z3ZPkSIfBlj84aVEkmPRTuHNhpGdaYc5gZ+9tXpFHIQCgq+naxP5RIUHBJF7sXexC6F+RaUoHxIMTeuyjZd0GdhbtWnYLnH2wzNB9oXEGRkyVMKkmorQabBbStNZq2LjDpznMRG5xX4QqB60d2uMxNVbhJmvaidpWjcn/21MKz78/nwH/I6di0iRyx0VU/HnYH6IjlRNZ85N9Z17+7Jui+iZjXj2C3+EOGstdygfBK2QIW59JayM9zDMAPDC7zU2GMyzXLEEumComcDFIUAGCZHObdJWhdHbI21M3GA+QvEUsajORZNZBrFgELrvZe8KLtGIAtH4mm/HtdQHz0/UHFaDPvVAcXyNeVKCLVaaivOSfA4ZiBpbgUkD+rJaIZ9vGplsRt7hhb00zBqfhGtS5Neek+5kFucX/ik5O7IJh00H7Bw21FCaaO7W1CUHeRkYxzF7sUzTXqf7QS6zrJTceKF8Zwtt8X9lMqZcS7uUXwxFNMpytmxyoGMyEvaNop9zyvNWijT1QzE3BbGQn3Oie/lCKh72+QJEezinXOsoKbimpg8LoBiW9EnuojX7LxDxVlXfe31p9sbjMX+ej0xNjYYDImd666ttWNa7lWxofxtPx2dZ8KJKJrq2iq2PRPmZFs8iD1TLgPfUWe0xRtDDBy0O624UVbshB2E436/oue52e16k3f/9DxdjvRcHTtkJBWoBGTbQWNpx9BanxNUJkr7YTqPprhXLmsI2DQFV2EQeN3jHwLcYT1JPYK82bIzRIkFfS630jndzlA/ntE9j4ynFS7j3qDeHj5mMuRTH44c64St7knvzADntva4Q+PmQ3x9Fa0Dm+to7j4btayMZzkDjzJguMUw2OP1SfJ3TGQFsKmtf7/5ksLofb0OHAsIbDBozwa3U6pJuOdgJDtx9GB8M3aEGZgbPNXQ6i/QsKB2PIZdc4c3PGlJDhXgkRQP68UDKFmVDHQ659vWKfvDPVgJXS7WmR5RKoROia5O2kxebgqnznjC6OYWAFA5JvQLzXD1SWlqn/Wc5JqktM5DV07ujU2Vu1DKBOpuxwv1nCOQ4A59FZZ44StFh2n2fSsJt6XYx3FCjvThKnXL0GXTTkBdLN0q5WKbQaf0GSc0CyjO+Rtw1Uk8GFk2p1Gwe6/ieTyy4tK7htaLrtW7XeIT8VLZFk0X1bm6jCjEeFRAH4mJvRwE13ORmOIkkzibAXvDvZt/y4sWr/AhveMBj9Ze++RIq0/aPt66mPPzee3iwJnDIKKq0Fyft/hcdsZ0ikjEKk7PuBZ1srg8zfN4WY+jscEpPtzgouSxW+rTqYkEK2k5xjFTm4vlM0/VvEzV4zKzUHgPQ6bVm7TtFstk0KYTeRRXr4ptNZMSHM+kc2qEZ1xoEf7/tHYeOw5rXXp9l57SDebUM1HMOSfAA+ack0ig392s+7cbhj31rEqiyCPynP2tpbRn1XUsYPQaeJWfF7RjnCw2n/zp+Khj641WpkK2VDNXHtl5XGKKebbj3Y3OmZ84ZPeTRnK5Z0ZRSVCFne5R+ez7CRotIE6pZ1d6O1j960DR4iArXboGEqiXueIGSb+OfDIF+xMPxDEaInEiQZuTJkFvvSl1U0wtJGMdNmeRkMi9jR2/iZ1G0iuq1tLttxz3y4HuN0RJkKrn6aRzmmPoidqFp6dCC//pHBMAv/b7wLrnf/2qRAxzN5nlrwcbLNu2cDT4Tkd3yV0AreIAEtmkvKvEScHy1pQKwiD8d+FoQZcgwranhzCab3/b8pPtaJfex7iFkhE8VT/Qtz76+fLNkahAZMAvxfLMMPC5Ozx7+YM8hn1Tevpadnhh1h9vXhNkWC1zq8Ri5UurYPoLqW7vIY9ki65byjaqz9hZxkSBbldQhdDIzhgbWRBhpwR2pp9l7VBEE19M2tS4NqSbDRTQwwmdzVsn1I+Bps2xSIe95PSSTU422DJ7Bb1TKXPKBKUkHSM4V4eaFgltUqgb8AnsTgihmN7TUx/ezmmP22rKLz0UZM5/8U1aZO2nVRcIaVLcC0F6SBYGCZL2v6XBkDTc1MnQSVMAQRPYzoK8hSVEpH3Z6t9IGaNXZr3B++pZ+Wbw7rIOU7rVqJTKoK0zHsEzQ+nl6w02vbXH5ljQ31X9M2lxRtxf00Sg8wU6Hw6cJuqdmz+PDPfrhglo315GVP2OLGxWhOIYpFdaeZJaH5Tt6Hyul7gCR9EgBnUaidF04ffGzbPjKweY4jvl20zJj1pzkkDJXje/kl5f60Ix2q7sxxQJ+mApFMo0/puHpTHx5IFzakmk6hnitlEhq5+pqZZ/oTkZv8QXOfhfsAs/iKkUDrd13u2lII9hVSWMF4O7jukGp9/ZHxNlrcOZ9KY3REVsAO39ZjaHl4Q2L6v6DQRn01kBO88ctQts65dngJFB8ucYUtwN1CuOAWWxXI60F5owa99sh10WJt1xM37F3Jl9XlxRDHNfZ11vQXKBokBjkBMSvDLcgwGMSETdIDQkbVAe2Q8OzootKkToFuOgPk/5wNVNzdc7fyvKJoTeCfJBFqthXjUH93yA+nZvQV7MZy4r5snnTd5wKDsULiG9VpyW1OTzRb91C48dIQ/ONx0zS+vaj5puy3Fss8m5697AZX6OPjxCDCq3u5C31G1NGUKzX9Has3ZBg+W5LKw83uC9VDLBBccP1ik2SAHmDJDsD56m08w20dY2LwHyjRz4GnbwCHt3MwAy0fCClCxygw2aporyMLdt6w4EkUBqA4yAUQlbfoxU+KAL0cPLx5DzZH73cmrgGYNx0BNfpzILg0V00mLWS7OhAiLWwuC9vkAUYbnEb54c6i6Ddym9bj11GxwWJae8eV84hC53HMN/dJR9ndUuS8MwqWEXQp+eRiT0xIRrR06TMHliGzwzOkLj4+4dp0bp8sdx4QMLYFn5nd9D5vdfkPRxEvMU8hqpMZblDCqDBaXw9opQX7XmnhRHV0QVVYiFpY1hurQyRyHpCOpq+1CgePZybISYaI7JPUi413MaGrc/NfcdF2fSfniq4hahkEUZvcWel+T0B1T6t/Rupw4K1aP64/4Wo5d3ydCLdruC97KzL1zDrLny6QChpR8oZexTk6gyKzs6aVIyZRIaTjTrDW2xcuMH6DZrnlUyqhMQSV2WFWuUor9oEi24D4QU335wNVp4MbP74qTGZ/+10+WWF7qMUSATETo6CbzBHW4IK4BD1Jmbax3OOj+PsvRT3G6c5WXkRfhN35Nhck2L60wtlflzehB40yDQm6vgGenNdXdJ/Q41dUsiUvc4vSVEOIPtnp/Zr6PdPJB8UaDAjqFOq4lHnS+Z0MjSfhdKcbefAF7o312AbdRtTDH5/vfH1CUq70sLYLBks5LjJn7DH8y9PsDQYE5BliC+xOAmblr8FftaLKsQoET3W43D8VG5yKSpTJSp3HxoiF9z4XPGuneQoD7v33lmj/RI30UNTbxBBxX3o89ESzpm+YSMTiA4hI4Ugn/vFUfPkuThbaKiLd0bpbS90SoZqhto08TpH71BzvH7ZAviuEh5Z8R+yUjFm9AlrDusyE6SK5Qf/46f/rrl2tIH5It8v5zbO05j514m3gYScS/aePa7EFfMOOhoMenlfsRr1wsiB42HJLGShQjz3SzHEIqJQ2ydeY9CfqjNwRInpYVsWfBNjA5siROzgFWNFqrorwC80bGEFSfak8W5DpTpeHxsCpmDx61szro8AIvmwEZpLFUAKLO1vYxh7cH1QXf5SSHujJ+YWcwGKAluzGvDgsR3bgjwYgbWoTC0uSnCRkc/+GU898g/oR27DRP38UfzW19MPL2sXMIGYLfcqawUtHtEQO2arE7ZRsVFuSdhF1SyD+yXnu0HQN1lYJ/tRYptEd3ctuoqx9D8efZASD7oGnCY+cyPxrJhEh4Z5dqEVvweIAFfz/E0PgNWJf8sX+WGqieUlLGkCXW5QtW7jrraxNIs0k+olDJmjg9CGz3PZ+76+hHb/QCznd4LgeGFkdTKhSMvHvBYA8Dxo9Mt1fnPQp5ZxdYszop+TR8kRVY3cmbvHOpMRs/1brwCXcKHTF2ZsZsjTFJWzmrAxdCgT26RtiG+xcWeTeFEPEPjUnAf2J86jzVj2ZVTj1R+fsMYnkXcOiKFwoFVpl97Le6JZD4Iou82KiN0KabksCm68qteI7KSAaCejbIT41CO5tM7afGzC6T0oEt0VGDDPYvv7EOmjVetQ6CdlZn6iaMFlCXqM47+OuYHaC6w2wBzEKvH/OEG7PcVlXxEjseix15+N28u55uO+QCADNyAK7ZQtQwrvkTr/o1ScCNb/lvCah3MEeKxcZWjvQz7kjH2klrcS0ut7JH7Oq2gutC9c+a35d1pMt8nRYRSrQjQ2i/miJSAP5M89Ojbt/3O2aEI1PfAdhx0afv3AtCXcjxMifnU0IoYGPyrXxj5VGdy9cNV55LuVZGuskIlHGen7UoJtpW6O8ZKnpAUdBCaikt3bPKYtN6kNzGoY7jQ0UfR/vnGTaARmM/+5Fqhg/MF3zAtEpLV0y3gRT0Cq7TJFwUN1EGwRU/xuXqz5N0QTd21JMh3w9MqDO1pj2UPXuytp6wRwfC87sU9xBICzm+0TgurQ09DMP73holSFGHUH7LlgG6IVo+WTDNNTOk6NC2a2ocbVBd5du4j0Do35VLo9pRWAFCTB357ZSXWSlhMhSfi60ETe44xDhdM9m24u89iDgzXDLc562vhFfggiKdfLMxEQP0Kzal1T2OrteeCWu8t1dgA1ec+m4MzPn0jyaLDcspbPd4/jSCnmeF7hif6gj19sjPLtpeGO4yVMV1HHdZyUEP4CTvXpb9J3myM4lMJ4fCjgRuj87jE+xDesD+ZZz25hbUcueaUU0cZnfq9tCmE5CqkK6jbCc1IIQm/rk/MoTIbR16qpFPZEfzONdqzP660DD2kR/wFT+925Df0Ab1qAAOc1ttLT7TG8vHyssB+TKfB0FH7OjvWjth5cxcLdDLcDaPmK+k0fn/KRSULgjrAyeJRxtQibDAUZ3flRSJzWZ0Ys9xaBtJke3/0BOzYtsUxs0IzMWYp0aaKk82xEmKBOYnGX4WX2wnkLRre84gET2JUro8uvE5VHjGDuHosF8RxN5c3DNtx2Kobj05kgllTeBaIBofAox/kETzynF6dqF60R624WiLlItWuMPR7mgODLCof4KtTHkV8F8B60WBplkir52y0if09pLvj4LNvfX8nB42NZ4PrKaf2kCbQSAC90M4V8DP8RKm4C+jiGfG+PbhIzkVweIZ+4y8iaBgmUuQDMguw8Z3DHlYi0uK5vnrBeSuc+ov3tAV27Eo+qYRPBQHLZ5IdlLd655xbrEXy2darGEN9smcmV0DEY3MP6BTROXDn8nhYteG1b5R6WZMfNu5Cyxltqb/klkCC0ZLel/dH/8B73119skIFz/Wbb5C4Pufca9Y5FlGui6B2X828OuYFFehrS7j8zPELPo1QsFaaCam1hjCtIHuRnVbHVV7vwWvQ+1ZnD+vXwwSOs3jDyOJDfixjasdbY5BiPPmpUlvb8r2KwIm6jFCZae9+nUSmOyjQc7nm5cdUAoMKvu2yfSXgRdXDBgPjx/egMzVnO5m4j18zMNEJGw0CwWoL2kLdWv9EwfbHvooPzOF9diz7huSLGhq5c3AP9XXpvvhInF+vig0EqL+lD5dTBEA5MoU8fdwbq6w/6O623IC+QwFXHDoWkua+Ee1JSm9g9zYQE/z3Coz/tB85h21Bb0WiunVAlK8MZPa7KgWhKX36slbmnBnnDeR1UBgfDUzhobL1VIJo0Ipm8106eUtLvg8g6Sdv4uYZvYwWwk7MjHHordshhQufu/o5NSPj3MA3cyL0ukcDO5a+eR0KoqXKt8sQcfLdQ8Vs/fNrwuUHHbuLR7M4vhxZJm47MDJJ7wJqMK9hCZCzU+C4WbgWWhYZ83h5ay7EoRWu/oydg2EOsIPoSCNTGJq9L42YgDqpANNG5KN2jBXtfSGbCT6F/GgIfT/D4ZEzirUgsbqkeMVHE/50Cb5u/ZYaVLyjUO3buyuF4YQAwbHd/aiACaaensmPTnrCt5xCOsZRurP8aBaWY3hSYn07g49JJaS2KhzyCLauyw/gBe2ghs2eBcb81swmRGeGXvmtEGA1tR84Xy4E+MSo9LnldOQcbyjrZNaP9UnAVNMn/lfB4PFrkXxVpLA26W7kkmBpGe0QOLv33uz/Ynhsm4Wd9+g4S+kmLY/frYCj2Qp17lqbnKv6gfQIPUi3GIUO8FX0w4UPqeIcpiYW6Cwge4CDxbUdQYKKZtT7ZRvDfjGnzOOz3jsY1X0tOlEU8FXK31Ww3YdN2uij0yrWlO5JIKKVpIysA85JlUYUIGQ2onNC1U44qLWt0PjnKjcYsYvPKccbDUXcG58tTbFgjYU7aTKDgPDAh0YwHGShwU7H5dLNq729+NfauJTneYFaRnk4rupcgwt5v22o6NBkMzF5g9JV499FCkt+REDvm/KYlfpoB3yi+K829XQ4HsbUoEdSeL+dwQP9hAb9QmRbIH5i2CJBLsRQUp3W+cN6n37qobJXoeffMA2b0Xcgw97fyVyzReQ2y2uq0MKmz7K9a6TRCKw8P1NwAX8/H6A2bJYzP26gO3arSETnjYvGZRDAKvSLqOdlCI0inSc6EX2rffYl/JUm+QU7Ps9XSaFpzRCv/uK/swtu51WgdXgT0OT3H7l0Q3d5bt8PumhvXndeK1iSqQxDSKWmR4DtEerxlU9RXEaTIaNLrglU8sgsUI/rfeb2hM8NTAEaf0ZeD4E9tSTgfs18LNSHBuHFUGR2HyiKuD6/HTbg6Pwuw/XDxwatr0KUyuZxUb5tL9+f46sTyYhZfjU7bxl7pjdxs9ECZq8IdTqLPBhtA+Aya/JnoxE94Iodn0CwaTdKL0kBJMj575uOl7cn2NKMWgHCBU8VvXtuL+aPCdI6zv0tVPkLNwyw4IpBqH5S0tMuSggWHl/CnZ9qIumDU8b+a5GgdbzqGiFLdPCUa55flqVzZdHwuzUMysrTCRMylqSJYucW/SdxqBlp0bUj1Qgead0k0HGYeGhyB1WZvVoAMvaVFrPVAgf88o8P5A1SVbSNspJBSzL8Rb4trtFmQH9NhUQZBfHUeyTPVFjiZLwLW9Q/KzzBdy4jGRjat2HIHahEAZYB8swGH3wA6FW3tgiGdfytx2jox5oVeCX47HAWIrzc0PQpN6MHSmpPyLp1lpB0s7SvrAmuyfyH/YxuE01CncEBGH8pNNWFAssg8xZO+S6+PCHl5FdEbVOJpA9NjYrH07/YhwngZjN9d0pamusv35QS6R4aDtRsf45XPC657Sg7OWFO/5kXXZa6rlaOuH62IdBn4HHVsFKAix6xu7AyuP4BIxsq7mpoFcLCxI75xySQGu0u6sRdga9MYwwYVg1UWxzY6H1+KQv7hTnPcWTg1fKkNlHDylouj/CFJd826ZzyYGnU2CmX8+Hbq8gu5r6Gn8+20R0QSr/BHbqsqPLyyoufBDwkc8t+/GF+K+FLkL2Qt9v6hWhRilJWsQhJv+oTbx/X+Rpu64IVzdUl12MXxS74xS7rFU1H+NauNOBpObgmF+Z0qG++41tBMMJ7ud1ITrbDqlMO2ZTSJKUhTq08DgGlw5Zc47nznuwD6FYDfCa9g09EahQ5gln6GTCXyXBwBhmzs0QGgVBu97JhVJfEX5qJfoINbJQeI5KF99HPHjkOFoCNjznotfRjbHXE3mUbrLwjKYEGCa4FIir/3iq0jb8KN6VtoF2nfYvmD0PKtmpmduLpDshBEZoqKCvobFbpa55/ZEsqGNeQqKmOP9E2UJ+nw89m+9zVbi+lyFnV75174sUO+nAMxdB3ucDP+R2UKY7kvqeg5hU8YdZWKNtY/j5761yvTcjxy1itv++++gvWJAKMeEFyRNErPSuW7NKjHMeBVDQ2VEa4MhsIib+oe7iKTX0MgEuHxeskbSF5l7qEsdUPh4mdh3l2tzzHt0Sfl2JcImmZS6mhEvFKYtH38jLK1wmYDkrmi+5fD+uR7jFMiChGlAatohhw9PwhP3zPXwtTTetO4uAwS0rFf/v2k1tccBXVhyO8qpzndmC8hxz9pR1kHLNGV7/f+lBbNdJwo7lFSnzaeslI5mfa7N/HtzjKO7iRoGyqfASmlk1nRiNrqc43lRNFOowbdr8xaqOa/SCjL79B/AhKv2heGJ7a6q/G9fG5kZpRxa5Kd9MKNH6TGmTKyRp4jHG70TAGZDAbvAqxyCHcdBw/67308ZwUYH4Vw0zerzhmoi08tdS4TNIXBZ+gzR2Cvp3ULIHrIddwzUjG5bHCOxJ1w8BGuNm03A87uScCwEAgvB0dlGCmdhE/itiW6nP2DFRZXyuEkMUiGOlH88dIS8aPofBiNRoUTPLs2g+ZFqepN44qiFTiKFHEXdxcntwoXmPBRzJvjC6p+Htdb/d8idV9d5h+mrCKFw7WMpWXboWBJ27BQM81WdZztVL+1GLr5nth1J7/TPK1+8Sl/7Iik+Tn1rah8a9fJxeTL3I64oWta273xQgLpkwyJfxYvy0imvTJ4Z7F5KL9FgyAN8TuPohlE8eNJcyYozUt2FE1bdXYdn7BofycNnLZpEiTH9ZglebD9DB2EK0l/bT+izvakEjpyn28ym/slwSqeQYYJ/I9Qk0+E2u/hNb9pCIMfmD/7X3DMz6RIiLLoRKI2izqsm61y2I3qqdruwQf8K0w6bfSWz3s5tKwDtUZJ62tyPjmmbce0L9k7aLC8YgWukfJLxJLrtLQUCAUD2YW4Dvw0CZZw3Ghoy/yYITcak0zxg4AZS4senzehO390uGJ/PKDbHmFXY4fSFFp19rjQiNWFKfMcq0pg4UVuyxkVbBjZVQVcB63HrPnn1m8F0URvMcuZQhgZ9CRSyRV7ZIioZJyfrnsW5sl9VBhFjoIbiJobcnnJ8fmunG/+oWaYIMcFTvBKqSPJug7v/q2gx591OOT1V6Oga/lYzDUA587aQwypA3qBG+8laPOcL3xenbuqn/pSZitDpVCvfZgzbNwWtsAgYPgCwMwsoVjAQDrDCEoVOXz065luMdRac6PCIZURpsgsJvUOd0l3VDleJXnjZ0iubI7BnIIl238OyEgiFh/ZAayCyUVaApj5Tg9hRjfuRhj2fibfnOxM2C6rBWPR5jGT5AKRqaiMWlihKSpea9EOK8WApWZpcAKNpsVPdnx1dQ2NgWrokvyjXTEtwwG4OwAtcCTASgIRUctbyv2CiV9PwXu66D5w6ksFufkx5ttEutF/3fX6ylg9U1rF0driC9RWln1HzIc21CgdlkZdOn2fy1ft56edkxmMqKrFWQ5fHlx4nWoFgTM6ZYVqg5rXL28COpxFFGs+S7hwLQfRWaoDy5/0TA2ATP3nV8Lce1xSbhg5rncgGZizBU6aJy7JbcG6576md9LzCSsQ35+aJBnsjYj73Nbmi3NCUH9wBmuPYk/uu18letWUSt0+t3AiucSuJu/RziJP7WO4PpS4yNEGz/2p566JkE6K3r9qRaxlQaG5WKy9+S65msLoIXC6IUfUL1cy84IwRoNqihnfkDZ750ImCyHRjI1VFD3UA82j+6LEUMR/M/aOwpYBuCMlsf0+7ThtE5GmLyY01m2P06jZgXWHHeqd8pKnEyAFT9lrJI+DDuy7b/7YTkuLvYOkc2iw+/+XV3Jp/F5hDiYZ6+gac4y7DlthhnszCB+HzrlQzsygx8P3+PU8ZM05nAXT7/sfG8fTDbta9G0C3k03WMc/NQ3KmKDXsmHnYL0NEOQAp0ZsE08S/50oK29n1LG1uHudmsuJISgLu77oxb2wWxjAifRMMiF75jknLHVtvf08FfkzylhiP1sj1ljcEEspU1XGrTDev4yKQOfebyIgot4JJMd8iCIGVIKkcBa5nsmUOxX45zZ3zXxotW4LSd3PUV7esWNWhKuWAbAa+TVEwlP0c0UEXazWDmxnZ/HAZk2IBCimht+OKBhcXbDeea9rSP1yFFjG8BNOzcSwK+CUmXarsIqk7ov+PkE+WxOMofAFEnzNh8dDvBy580S/u2OqolMgfCcBK8d1s8e2RStoIVa8j29zkkzPB/n0mmXO4taUNHTIIgXo4SUzFkp0DdoVrFoXnSYk9R5l4N2cvGje8Dw7CCDni8lpbtbI3NT+yri5RD8DMs7IYZTCKCJ/ahROkvOWqHNat74amB8fwkOXQbFcbA1VNmYW2kniI3xB8NDmOeks1lCNFGtDTSrpbLd7hpLg9PQOZXPMklvxAJzhqmfMycxUezNp9M5ApQl1WkBx2eS23F8c1w4gMKvNZGYhfhApKXAFNTJMTsb7OhldCF6FzHTTdIKcMfgEtqAvhcmQD5CpQSApI9GCq9otzf/iqM1uC+2yNJa6rY65drTWTdosU/7Cpert0qQtNBia7/BChdncvZ32GCVc4Oh2NxKPdQ8GatDtk+zuE+4S+zyMRCvn1GiwKmzlOjEwA16DqHSGyRpt4VF4x5gvPPCH+GPD8WJzzN9agvU9IVtSZxzprtdrtT8ZXxtjP7cizDMfYYWkrGZk175xSOT+KqV/tDIvlLqRyRNiJQcUuhdvhK8GQNpftRBY/EZTh3JpqkQfqf6BiW1rX7ApOqTIsQXLxmyxIuW7MlCuDbu+Obo4TtyICH01TVT/YoO3XXm8nPy+ddn91jh091K+rAtlmnTfHLJmAfLIum+wlOIb7msOZaSWnViYmAQ5I2bcCgJdGe1hVbPukftjem7ny8U9h7Avxi6zeQ0pTVC2LKLVZOJu3vQCAIVMS3rbfCIk5vGxf1yLYtuIA43VPLPZ2qlKZW0r1Qf4TY/SRRrUisDTZTOXdUKYFLDbpE5agQf568vLlmvjg03R7YRq0GlfeudREzRjQs/koJwFYa4Hk+SGI+45FhQIXtqf8XLUFNIVQ6fSa9j9sppA8uGPhSJQVi7cy0y1Zizij7uiE1TKXBsXNnuisCTIUn95R1apXe7fkj463TTJMvt3ccfITGExKY/8RRc4VEWa2ucpqudd8CmzIsXdG4ijLtmmSj5FHhGm4GNTNXy9h78IlDIvi9ZPL20qlej+5TDXq8gCMNDvjz9cKRo30Lx7fv2Qs9vOcz2OOMsnZiV7v5eJoRofiICY/z6668I0NOHZczxPuRaVuNTzF3YfHgzOD+VMILysncJtLeza1UuXtf8CcDHjHEvRn2xFu08UdSOaWiiKHVtl+EDwZjhLPPg2i8Vk8+dqvqOixqXM/oRhd7xoC3uuqhLWowEB4cIPfwVq9NzH1UdYFrjmJ9lJ00VfHNVtkNiGdb1+dZTgOV1MLnOjT7tdTpVbu0Alm2fQm02jJCqcHM9r5PL77L9OB3lkGOT+mJfQEbracSNHCah8UYkZDp8STkUy2nFQ/uXL3MryA5yLdTVqGRln7MC8De7NpqCcmr/98pUZLbw1SY/EO6TmPN6Mua4b7EidmLyc/S9StYcnImvpnN92NAJuzN/6m6H9pB6RgbCJ3mAN/OWNzwn5OaKMKLPKDSkWiLOjSAiipTKifytATsWjygw+5oMkYwBa7hKeumnSr5ruC6m2eFbaFGv134M/ODYT4ato7nzKzh/DLEcaWKlsH0p4XAl5KN59qsYY6w4gb/fC9RTkChbiDTYVMfyrVswR8sojCC7LxMfP6eOboXM/Tmi729FEC74ibQNDwT6fq8MSzvrzVDVLDgUxDRS9YyNSbrUhtlicayiep06Hozy1cN8dw6NkY0fEESNNVK5gXdMtfkWeM6qNACOP1XGcDCCQwfdPISQFuU1sC8DLv0PBiqtULZqx/gKHp12ov3alZAjLbogMcFZinc1NxJNVtCf7C1mTygTNulev1MDaGxnBmQprGAOQazq2sLlixANl7/Z2P94j4NzDyNvdR5ipSBFZCaBdh7uYE7OTQ2KO1pEOj2ipzwdNGBEIzvC75Chid6FdjvGehkLQiYn7Z7PSazpTZwecRNXYTvUSWzyuvGbRDOh804/vu/yC+KzpgRm2VaY3ekg9HPYom7rkPRytnaxLIbJO0v2vIv1VEB+ZMmQTaMbbVkrnBGu+AJ7KnXn3DsneKjh1oxBhLPj58Xvr9l/itDmeazD6b4/0eddcbyFRIVxtgoqY8k4I7EXdQ3OMK1fFrYvkBnVyw9J1oCgG2Pn3y2c404nO+e20EucM9B2o6gEwm+hHvOaPdjsqL87O3at4KEE6KrGyoHpu04c6TnOfvH2WJSuh0bxUIOlddJ/kbwGcx/2MBCsbnIMSls5n7X7PHr/5ubgUSMj7h/7Rs4c7fg5VsuH7viB4D4bqSPjjrvw0YSwvm6xuvjIZd2ngYQRVDqnmKCM20gXZkL2GjqZ0gsDCqDP7Sb7FbS0AGum1onD0A2K07yahIzFYyTLqdYLPHyHKPDujeG6ooTcgHJFoODVZEhP14I0xtI/3AWqEnH7X5vHiM+qxLY+Xy4hUk9himcN0clwhqTKI1CqLAn6XecviQ4062Aef9cXxBxBlx+Tn/6OgfM7u2ROruCxdWWcMpRe5jVDFb6qRkKwFxVt8wkziqheMRmGXYKmiCmnUWzeoFQLH05didSnKa68MnVX1j6WcwdRkf/yraicFl93SK9guAP5X6tdpLZbK8kBWX4pXXOkj1pNJ1B4GZcgFOuDhHxzRArRkEvyheJlXc8UkPCul2ipEBa4bGEfgmWvNNC25xv41/gEuGR5hMrsyjvUAA8BjgI3iexfq8OMqbpE1m2mbs0S/XsfDoP9wg7BbHUEcg/4WYZGAgXrpi/YTyP3ISp4YZVD0OxKDFlN4bwta+ON5hvA6lRKGyfh1ryUtGCeApMFodt8BjWWjGgPY11d0mOhIbzvW32sh8UdRDU3iYA2UJqIymJcHJXxsSwSBV9gF9OtNAKi/eWJKEi4jYCgZUKr6ybn33Ylx68MXapMt70oK33pe0qnp5nb8dZLBZiB/j6omO5ddtkoApAkTuljs7AzZNSfE9SfB/DeUwFZIAMUas3wSggOMA8tJXXwzaZBNrx8C2SSX25YYnJSsOTa4GgV3FQ5LCt0KE4Lbs2wKkeLXhXN29txnzOjorJkXlTzpMmPGZ9LI/uuZ7ILozqfLBafrE/kPURfO0Ab4hFq+rjNA0kjE3tAHsbaOhB3viOljfUNSbePNGyUjpH4uIKfss9yzNlKvis0osdta8FYq9tF+3IndEoRmRVG2SxNxGUy4O/d4AhOQcXwpgTw0E2Ff+2HoCwfhkVZnA+dSzt70Qq0m26Hb1zb9fyxFtPCVkh9p8lrnLYN/fJK571FVpnDOoxE2f6+6NL6owPb94TlzvIm+hx4QP77TRoMKFbK6xf9xKJIXjuiPUSEi2WkZJ0lRRF5qLhuvdeHHhLgEPnEz/Sz8RfDwIjMOM9l0Whw75FAXjcuQo5HlFvsSmpKa9ygNGqHrJvkQzii7fbPlrlldVc3eD8+u9QO51TenPUnOX6ZuSxVghxvvNvLKKoNyj+zbnSw1qpDfOhb/NeIuYA7G8R3LrFNiZGjoHUZXp+Cdnl8BInKk29bhjtgC/m+e2+hU5ZM0zH3zY7v7PL29RYDZ41zoLP3auiNS0GYdeBt/ILrl+fXWkPEQt89tZqiOLnIHk4mAhboq8qSwUfUApo2kYTUcnnnqiTC75QWT7JMMYS+fwkFDpeC9+xHdBa4neDnYLvrXTu7q2AsKAUkmwYL7BXxVmkg6M52AuZGLMTBePi8ZgFybuZjH+2QgjeAyRtICfHrwetl1+LL7vFLiCCrNhWHjd38FC2LIixc6nwy89X6WVlC6gMZb6DOwcb+ulTjgg38SngLIc+KFeHKYjnjgCSwd7smkLagjMWMJgHCtbn92iz0HF8ju4uQTlldoYs8TQ2SVFGRQolFQnJ+8Wkh6extOTBa58LMJMvBtT4wBGOE2CpGuSz2r0U/2oldAeiBSXFTP6COXVwOXX/b8hUduuSo0PJ4oR023rpZJALHAqsX4WG8c3V7NcNguC5o44SZ3MuCcleRJkY36CbxSfNUqImMYlVPjUpz2UN+Ot/6a3vvTBiWOd/FLNBzNiXd3XxnARWf0uhMLsSRJ8yJa13PbS46bYKL7tlvjdhp7TP5BrkbSd2yXwH9syLvgHmPAvTgGgxyiAs9+BAyYpG+UzwvODx7Ddequ325Ooi8UzXNYZOmG0ZwbY3H2Kx3FdGqpGzah6Ve91BHIXVres9TNc13ro0SbU7Qjt6x1VEvGP0GrKSZ6HlkO9w2ThjhI5uM9U1etZcZBmuKHtp1BklkR2/J6EGdKZzzbY50pBOLNBC1PemtxorPzX3z5VemIqUC5iXRvmxzwhRyAVWWPtPjiMtLbo4GWBly7qrohbvFP8S+4BgbJ/HdqcKuKNE8hzl9luVSxzQtSimLfKBwrdjeR5L4xYwDWpfAHQ6GtVF5xS1BSkEv8eFup/Jovv/ewgNmgVlbfT8ZzheVvQ5JVmnfGt/INHQun5Td8WkHR/q3sta7RNYDWZlz55ffF2GRbXh0J4ipCb9GUUQ8g763xx31R2CMafSLGG01a+QOeIprvg6Wy7tR0ioaEcD8nw6RSylkpa+wdp+X/XZkDTV5Tmb14Lg9OqgH4W+Ue//ykDV35meVkUxOoS43laP/5qBFwzB+1UGFuIh8HX2l31/ttTMu8RQmSA/xEZsGg+mtGrqDrzHKK9910Oh6T0HJlm9ThvMGuZHk4DGkZaF8bDVt+kJFfI0pxq2BA9BLAHjPFmBm9H1YtAzU9Rvkacw4FxKhoC+uEhA4Sc99R8p9yhCHUXYh5SUOPfpXSejfGyJQ+ZHy5/vAWU3Tkvt7r6mJPi457XG6gBQDcSOxCSWDss/cDxMuEN2bqXnGYc74NE85PJPT0VZFXw/2a2IW/thwuB3BvOVB2gVF0ljxYEKKlhqWvizDBHZ9vRaxQQ3x0KyrGs/zeAN09kO0W0qPuZjjEE2IEMKobJgWccIGX+JPH/ygyi1jfiZ9uM+//Y9/++vE918NCv/vzrV/beL+v7Wc+1fbuOl8DzZmxV8Xvb+e9P/xz7H+4/858v/8Vye+//i3f3XG2/qj+qdh3jxv+7QW//5/tgr9u//+V1fXadyL33+3s9uTavs70D9N/7a/dn3Tuv9XB8L3v38aQP53x8TtXx39/um8++//NAL92+8/van39553QP97o38G9Q7rP/8XEJVCn9iQAAA= -->
