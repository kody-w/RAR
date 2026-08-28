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
