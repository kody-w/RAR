---
name: "rappstore-rapp-json-doctor"
description: "Inspect, validate, diff or query a JSON/JSONL file. Infers the shape with per-field coverage, points at the exact line and column of a syntax error, compares two files structurally, and pulls values out by dotted path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/json-doctor", "rar_sha256": "e532be574326b108ede0dbbd7d3c012cf275c9f2aee51793864c45546938f20e", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["data", "json", "schema", "diff", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/json-doctor`. The original RAPP
agent is preserved byte-for-byte in `json_doctor_agent.py` and in the RCI capsule.

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

JSON Doctor — understand, validate and compare JSON without opening it.

Four things you actually need when a JSON file is too big to read:

    inspect   what shape is this? (inferred schema, key coverage, sample values)
    validate  is it well-formed, and where exactly does it break?
    diff      what changed between two of them, structurally?
    query     pull a value out by dotted path, including through arrays

Works on .json and .jsonl. No network, no credentials, no dependencies.

WHY IT REPORTS COVERAGE, NOT JUST KEYS

A key that appears in 3% of records is a different fact from one that appears in
100%, and the difference is usually the bug. A schema that says {"id": "string"}
hides that half the records have no id at all. So every inferred field carries
how often it was actually present, and optional fields are named as optional.

WHY VALIDATION POINTS AT A LINE AND COLUMN

"Invalid JSON" is a useless error on a 40MB file. json.JSONDecodeError already
knows the position; this surfaces it with the surrounding text so you can see
the trailing comma rather than go hunting for it.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do.",
      "enum": [
        "inspect",
        "validate",
        "diff",
        "query"
      ],
      "type": "string"
    },
    "key": {
      "description": "Dotted path for action=query, e.g. users.0.name",
      "type": "string"
    },
    "other": {
      "description": "Second file, for action=diff.",
      "type": "string"
    },
    "path": {
      "description": "Path to the JSON/JSONL file.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `json_doctor_agent.py` and embedded as the fenced Python below (sha256 e532be574326b108…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `json_doctor_agent.py` first:

```bash
python3 json_doctor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 json_doctor_agent.py   # or on stdin
python3 json_doctor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""JSON Doctor — understand, validate and compare JSON without opening it.

Four things you actually need when a JSON file is too big to read:

    inspect   what shape is this? (inferred schema, key coverage, sample values)
    validate  is it well-formed, and where exactly does it break?
    diff      what changed between two of them, structurally?
    query     pull a value out by dotted path, including through arrays

Works on .json and .jsonl. No network, no credentials, no dependencies.

WHY IT REPORTS COVERAGE, NOT JUST KEYS

A key that appears in 3% of records is a different fact from one that appears in
100%, and the difference is usually the bug. A schema that says {"id": "string"}
hides that half the records have no id at all. So every inferred field carries
how often it was actually present, and optional fields are named as optional.

WHY VALIDATION POINTS AT A LINE AND COLUMN

"Invalid JSON" is a useless error on a 40MB file. json.JSONDecodeError already
knows the position; this surfaces it with the surrounding text so you can see
the trailing comma rather than go hunting for it.
"""

import json
import os
import sys

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # standalone — no brainstem required
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


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/json-doctor",
    "tier": "core",
    "trust": "community",
    "version": "1.0.0",
    "tags": ["data", "json", "schema", "diff", "local-first", "singleton"],
    "example_call": {
        "args": {"action": "inspect", "path": "data.json"},
        "note": "Infer the shape of a JSON file, with per-field coverage.",
    },
}

MAX_BYTES = 64 * 1024 * 1024


def _typename(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if isinstance(v, str):
        return "string"
    if isinstance(v, list):
        return "array"
    if isinstance(v, dict):
        return "object"
    return type(v).__name__


def _load(path):
    """Returns (records, mode). JSONL becomes a list of records so the same
    shape-inference works for both without a special case downstream."""
    if os.path.getsize(path) > MAX_BYTES:
        raise ValueError(f"file larger than {MAX_BYTES} bytes")
    text = open(path, encoding="utf-8").read()
    if path.endswith((".jsonl", ".ndjson")):
        recs = []
        for i, line in enumerate(text.splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                recs.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"line {i}: {e.msg} at column {e.colno}")
        return recs, "jsonl"
    return json.loads(text), "json"


def _infer(records):
    """Field -> {types, present_in, coverage}. Coverage is the point: a key in
    3% of records is a different fact from one in 100%."""
    if isinstance(records, dict):
        records = [records]
    if not isinstance(records, list):
        return {"_root": {"types": [_typename(records)], "present_in": 1,
                          "coverage": "100%"}}
    objs = [r for r in records if isinstance(r, dict)]
    total = len(records)
    if not objs:
        kinds = sorted({_typename(r) for r in records})
        return {"_items": {"types": kinds, "present_in": total, "coverage": "100%"}}
    fields = {}
    for r in objs:
        for k, v in r.items():
            f = fields.setdefault(k, {"types": set(), "present_in": 0, "sample": None})
            f["types"].add(_typename(v))
            f["present_in"] += 1
            if f["sample"] is None and v not in (None, "", [], {}):
                s = v if not isinstance(v, (dict, list)) else _typename(v)
                f["sample"] = (s[:60] + "…") if isinstance(s, str) and len(s) > 60 else s
    out = {}
    for k, f in sorted(fields.items(), key=lambda x: -x[1]["present_in"]):
        pct = 100.0 * f["present_in"] / max(1, len(objs))
        out[k] = {"types": sorted(f["types"]), "present_in": f["present_in"],
                  "coverage": f"{pct:.0f}%", "sample": f["sample"]}
        if pct < 100:
            out[k]["optional"] = True
    return out


def _walk(obj, path):
    cur = obj
    for part in [p for p in path.split(".") if p]:
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
                continue
            except (ValueError, IndexError):
                return None, f"no index {part!r} in array of {len(cur)}"
        if isinstance(cur, dict):
            if part not in cur:
                return None, f"no key {part!r}; available: {sorted(cur)[:8]}"
            cur = cur[part]
            continue
        return None, f"cannot descend into {_typename(cur)} at {part!r}"
    return cur, None


class JsonDoctorAgent(BasicAgent):
    def __init__(self):
        self.name = "JsonDoctor"
        self.metadata = {
            "name": self.name,
            "description": (
                "Inspect, validate, diff or query a JSON/JSONL file. Infers the "
                "shape with per-field coverage, points at the exact line and "
                "column of a syntax error, compares two files structurally, and "
                "pulls values out by dotted path."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["inspect", "validate", "diff", "query"],
                               "description": "What to do."},
                    "path": {"type": "string", "description": "Path to the JSON/JSONL file."},
                    "other": {"type": "string",
                              "description": "Second file, for action=diff."},
                    "key": {"type": "string",
                            "description": "Dotted path for action=query, e.g. users.0.name"},
                },
                "required": ["action", "path"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action")
        path = kwargs.get("path")
        if not path or not os.path.isfile(path):
            return json.dumps({"status": "error",
                               "message": f"file not found: {path}"}, indent=2)
        try:
            if action == "validate":
                try:
                    data, mode = _load(path)
                except (json.JSONDecodeError, ValueError) as e:
                    detail = {"status": "ok", "valid": False, "error": str(e)}
                    if isinstance(e, json.JSONDecodeError):
                        text = open(path, encoding="utf-8").read()
                        lo = max(0, e.pos - 60)
                        detail.update({"line": e.lineno, "column": e.colno,
                                       "context": text[lo:e.pos + 60]})
                    return json.dumps(detail, indent=2)
                n = len(data) if isinstance(data, list) else 1
                return json.dumps({"status": "ok", "valid": True, "mode": mode,
                                   "records": n,
                                   "root_type": _typename(data)}, indent=2)

            data, mode = _load(path)

            if action == "inspect":
                n = len(data) if isinstance(data, list) else 1
                return json.dumps({
                    "status": "ok", "mode": mode, "root_type": _typename(data),
                    "records": n, "bytes": os.path.getsize(path),
                    "fields": _infer(data),
                    "note": "coverage is the share of records containing the "
                            "field; anything under 100% is marked optional",
                }, indent=2)

            if action == "query":
                key = kwargs.get("key") or ""
                val, err = _walk(data, key)
                if err:
                    return json.dumps({"status": "error", "path": key,
                                       "message": err}, indent=2)
                return json.dumps({"status": "ok", "path": key,
                                   "type": _typename(val), "value": val}, indent=2)

            if action == "diff":
                other = kwargs.get("other")
                if not other or not os.path.isfile(other):
                    return json.dumps({"status": "error",
                                       "message": f"second file not found: {other}"}, indent=2)
                b, _ = _load(other)
                fa, fb = _infer(data), _infer(b)
                added = sorted(set(fb) - set(fa))
                removed = sorted(set(fa) - set(fb))
                changed = []
                for k in sorted(set(fa) & set(fb)):
                    if fa[k]["types"] != fb[k]["types"]:
                        changed.append({"field": k, "from": fa[k]["types"],
                                        "to": fb[k]["types"]})
                    elif fa[k]["coverage"] != fb[k]["coverage"]:
                        changed.append({"field": k, "coverage":
                                        f"{fa[k]['coverage']} -> {fb[k]['coverage']}"})
                return json.dumps({
                    "status": "ok",
                    "identical_shape": not (added or removed or changed),
                    "fields_added": added, "fields_removed": removed,
                    "fields_changed": changed,
                    "records": {"a": len(data) if isinstance(data, list) else 1,
                                "b": len(b) if isinstance(b, list) else 1},
                }, indent=2)

            return json.dumps({"status": "error",
                               "message": f"unknown action {action!r}",
                               "valid": ["inspect", "validate", "diff", "query"]}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--tool":
        print(json.dumps(JsonDoctorAgent().to_tool(), indent=2))
    else:
        raw = a[0] if a else (sys.stdin.read().strip() or "{}")
        print(JsonDoctorAgent().perform(**json.loads(raw)))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
