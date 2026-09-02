---
name: "rappstore-rapp-json-doctor"
description: "Inspect, validate, diff or query a JSON/JSONL file. Infers the shape with per-field coverage, points at the exact line and column of a syntax error, compares two files structurally, and pulls values out by dotted path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/json-doctor", "rar_sha256": "e532be574326b108ede0dbbd7d3c012cf275c9f2aee51793864c45546938f20e", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "json_doctor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/json-doctor:629680009d40e825cdd1e7cd9faadd772cef28f453ab0a613d1cd62e2d3e7a2f", "kind": "skill"}, "tags": ["data", "json", "schema", "diff", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/json-doctor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `json_doctor_agent.py` is
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6aXejyJbgX6Hdp6cyG6cRIEDyOzU9SGgBIQQCoaVcJ5Ml2DexacnJ/z4RyM7VWZVvuh8frADi3rj7hj/eWU0d5OXdY9Ykyf2dCyqnDIs6zLO7xzsxqwrg1PdYayWha9XgHnNDz8PyEjs2oLxgFibpK4VAf2TMCxPwgImZB8oKqwOAVYFVAOwU1gFWgPKdF4LExZy8BaXlQ1RFHmZ1hVl1txmcLafGkjADmJWhbUmTZljuwTOqS1ZbZwyUZV7ewzdpYZUAHnHKuzMrrKrLxqmb0kqSy30HXkBuKkR2A1/nTY3ZF8zN6xrAV1YdPNzd38ED0wJC3z3+8ef9XQjXd48f75zEquCjO6nKMyF36rzkfZDVcH9iZT58UVygvDJ4D1ny8jKFj1zgYc93byqQePfYf/5nfLJKv3r7+JRhzxdkD0oV+x27vXrwQf3m6e729Onu7ZeNiMDvt6Fn32wKPSzL69teqA60zquHjrewQlJ5g9Zfn4+uEkApZVgEmXtwm7So3nx8uqtqq26qp7tH7Omuk/HT3f23YK9cT3cpqCqoRwTnPd2hIzsqvLzJ3EfsIzr+09Pdp3sszFwowd+pr6ivy8t3lEF+XgT0O0T+YnAQ+4+k/Aj9ckEQ6x5LcxdAAb5Pcsu9ieHH3eDsgKLG3nSiQPYrAAeCTW42ZiLD6dZvMavCwM+OA7UVJvCo76SYx1CEL1ygR1MrqcD9F/k+IpN9A95+eh0vFEZYhRlEmTngDQR8jcq3jz9XUg3ONSQrL0DWCeAeAxkEDDP/96e7pvbeDaAxPZQAyuftz7EkOcSRWuc3PQj/UOQV9g5je38BcJPHQ1Mg1SHTQu6MuAUPaJXlSAQ3z749hWv48G+N7YvROXmGeEPQ6PePJH+8UYZDyv789BPafjT7G6Wv2ubLhVw1gfJDNvX2O5Xc7CwJq/otBqBqMfJH+L/1tR+sxCibzkiQ/aJ79Ptrwnm6K6FhlG6HOftlmDyv39eXojusW2RWemPu7bd++y3Cn3vZX/p0eMsmr7r0v0LY2etcv6aCbyT+N5K5/xnib1QA7+1LDbq7l8AMQ3kVXp8j80/RdGmyg3sfolz6N6fCmAtuzLxkVii7l/RbApRBnwnDkPNYYQajQPf+6e6v7eSZlH/AhApzHoKCkR2UGNnr/Qc6I7XKGObTvKsWrOTVrPFXZvSdeXQVxavGEYPL9/kQPoIRDGU+yMUrfECfukcFAzLQk5XEz0YEwV7xdEgI3Pr4q7HjJykTe8nSj+iYfyaofZVJIbJPfxmVfjmq/NO0PN39aPBQjG+fQ1TTvYKLf0KlqFh8VaM5tL/ye512D78pcr4rdm5Qr1c73bu3/10d/v8pDfJYQReDZecPVVBH1k/LoJfLvsfefw6lN05+3ORB+/VstO3rsPByZ78CYbku9M/fsSovYeELS9P6jWe/hUm8W1lvXzWvFEaR74Gsz0D2a0BOAEvjDuiPP1+hGyoshtx/j/F/fcb4+NMqyLP+iP/842aZUFV/Yv/2O5TBt8/+ogx6JuzBKqA9u0jpXUTr3AKZtVfmaafA7475dTtAXpN3KL6j6melCEi+YuslYn/H2VeP/xvMfcHy+OvsQFP+eKPutxf43/78hL3739jHG3VfP4Zm/fZ/NhX/bGOIXCd0rOR911N2KRZ62ZubhUMDe7FbuHyWy98l2PcdLMLULe6/vHjGhV49L/8O1fORCOJ5+StFAtSYhX5/ve75BbuEZccLTvt7hPa32D79k/n6X9c8Nlmc5afsJXd8vP3+Gwqcv4LscwH9x1dF5v03XeT952x0/6XU+PP1qPzcGk66H0TPKx3gv04WH1EEga3hw/v3KAW/f/8JWgr4LoXAG8RpN/aAFKKBxb//O7YMnTKvcq/GdAfNPMoGOk0KkB6NABZsRm5VaALyQV+IsvyQuh9eSkUXeFaT1NisRP1sUeYRuKkCVo8f/k8JQwyBWH3ndhORDw+YEUC0eRn6Iaz8sDWvqpiF5iQIoRMAJ66a9F2LcMLzYOxHh6zHIuZYRdUk4B/YB4Tv/Q3f+w70obggep6yEvVmGYSrQVrkpVWGyQXpwMJQRf3uNigq8ySxLSfG0J+meEBMbgOQPbPuWBnUI3CaGsA2FgaO26ToHiquypMWQIIgpVUcJgnmhtApIRmXbnIEhfaIkH348MG2quApuw18aOw2GKsIuOEzwdi7d0UJvCT0g/opA06QY799/PQb9n+xv4LqkKMzVKu6yR924kk3SsNgPdSkAM3FkH5hg96p4OOnm8wRdRmsgWAIDmHs6YAhti/6RBzcFPGiBcgzIvFlJved3LBTgEqWsIbSgqGhgvaKUHQ1yCmswIsQq69mdC9qvZ3TdTnPMoR6Qim129uZElImincPmOhhnyUF2YV6RaM/LMirGlofymAgcy4Q0qq/qBDF+MqqYYl3uceaCrKKMH+wIWoknBQF3voDthyrWJ3nCfyDBNQdD6HzDGWMF7u8PYZIyt+gjY1eUDxgCoDSxAoLWnlQWhXo9nnWzSJgPnmBh8gtLAMnDI0KAdKRhVyks7xOdbdxIfbUUD2yf+uVUOB1v4xPnyeb3fzypm40HEXMokkN6rDCusM3zZsS63quCrvkDQqMDRpuwvOh4E/Izm+j11vFibw4zzE79DsRQKt5fAnez/EQrk5ItLeRbOf1YfVf2JuueCwhzgraS3rrkL4a0VbdiPR5jvocIj8zg9BAwzmBJHmHZp8oiSIGIXnls60kaOoKum02JCv+rxuKbojcXR1RL/WjDeoTgKyhwS60eqiH9P6b2e4z+G323I1KG+i/1o2+V8a8KGI6SePeOt4yb/wAOlhpXaouXORlXGEwyD2gWNSR3q0SaBM5lDQko4SVVJZjDpQQKkCspOruPxssdMFb5JnvMdHA1hN1tTZ0bLwyJ2t+NrnHlJWBSRvdwBaTvY528p2EOzNHhZtVIkfH6P/4uk8PkWcgGUE5QtNDtnjzqzwD34M+Zagdvwm+i+TPYE6n5aa6mQ16Yzf+A8Y/K/qGpoKSQGXILXuiBFZCUcFU85QFsOSqbrsCK/Geo9SNvsBqUZeDhS4a3sMDHjA9x5AbXbDPBvU87YfihkKC+PITZLGG2kUmg6L5i0nDsFBBNm8svAwTbuBwF7QklAZdlABeXn4WucnLosAbIvQDdSUqUPK8AVmURWWC8YoA9SBvlgra/XQnZp3hdl7zdHeTMYwGMClUty8LyBIsrN9bjp6/ZLw2dIXcIveCIRxVLLeoWORViAj7x3NSaUqosZvRd98+ullMA6FhSOgsEQ1nq7xzbJSnKvAc2GoUMtEOGCKgikqr63ehDjLMz7EAZXP4EvVTMEygLxKhA7IKvHy7QXL65ssF+kgBw1oKahiJ0McNmNgLUNYh6O5uVRZaffvVZ4uUDuOIm3efSbImvXv846Wwgk9eAgBcImuDP51Dwrap634ghpsdoSIFGvuPBwhfPLTj5kbI7x0WNGmGdoridPXQe+h4egVvl6B+xKx/acPvv0aN6Hx4DQ+i4Uc0KqIMSgAp5fsPXD9igWhKcGxgBnSRoJ7F+oz7i1ByGxVV3aGJVd8+HX2ExV9toUIfrW8p+VYmQIDXKiSI9nNme49wWGhnV8cgddzKuPcW1DGKGl+98pFtvb958N1jjSbNdxAY1hFQm9fuK9jd7WBI8ZcCEGKABdi7CmVkgnzoQUyoGkTUxrAa/eoA9Dh0u/1o8fhD1fjIUkN20Ov1hm6/BwYU47guCTjHHXoWbME4jnKARw28PkNbds9iSdolHZelAOXSgLMoZGi34PV8CEEiYULyPkvshzPvbu9h1qMYFm4ADE3ZgOH6NMXaZG8Aw3rPtW2Xc2mnR1KOR3GMM/QoCwCG5Ib0gO07fYbps3DpUT1kii8F1O3Q9y/F6otMK5i5HfAeeXBYv3jm88NniXnwVOjbwH2HyIVO3NURnR11sbBsEbqPz+pAdsH2Idi8X4n87RoTHGmxFBedgx1+ZcG+igPBTvUm0w6jXFlLmXU1VjXZ98leZm158RT7znZ/KjbNZOlZsS/yxPqAhwKzydjMUIQwcpl6m2jEVZD6zuXgENnqoHEJTnA7m2TcMPAYeqVPcXW78/rVJSS3QeRcw9gODWstyflJB2fh7JXbbTAa431jcLrIfVokL4VcBc06XUbXtiplrfCTrDT710kVMKy1sbw8Xx7N0LGHm/QwonBdkpJN2FvO4+ZQxUp5lLRlwHBZNfLiJiXToHVoHU8mu7wgaZta1jMvvAjS9Jjn2nSuJlSerHFpq+4X3IrcibPrRt8euW3Oc0BnTUFKIlkzNV3EGTMN+vUgXSTi2JBGdd9Pdzl/pnj6Gphq2p9l1AA/aMWpmuYykS52zCbd0/3ZOL3K1Hi72uNTIh4Li9ycCaPp2InlSU01RJlszvqq3RVuMQ43J6cvblYLtY74WV0bhjzZ6l5BmctFtJPFcNgmsbgNdtdN1rrCrj4f460T4nEWqdxccak4lrNVPhNOm/qyWjNbccVY0VISZJMYncotH0eD3rpIV+m8JQa5fOQmLKG0O47CQbjCPXU3xEFzbRlKPa+25YKYky6FN2eBWHn0NQJbUG0n6uXSmtZFkxYXR/foiyKNrzs1JENDDTfliCjlaBrw/lZaM+P2dLQLuT2oUZ8AVXuc5aDeOrZZH8dnk11e6lbM5ul11hTWIuBt9RQPK28c9BeBOIeIDsreMupgYapbb0AfNnW/mESsNNrN1lpMts5x3lxGIukHlqTn0+o4Co+Dg82oW+1ajd1gvcpdXwHTXiGoywJvjYOULcttudRa7aLrJ0kex6DJeoRKHy79ancgnd1JvdDlpd/kgL0u+hE1aOTLTjq7bS5cdjRHX61dhq+dg88Y7olzj7JtLhJ3Py6XIn0BRpjjStumQhZq+kE9ygf5AgW/ZJg4vkrRmh1SlwtBspeVa/WNfhMYw4ANLieRqlo+neN7ZsYbm2VesUNtVDP4hXCYWCoP67nTOwUxo6Uif+UX/I4/VtFhCTbpdFDpzlKR8ZE+52uCVvXhofTU8XKhmp7FlqsepSnVLkpH1ETU1Pa6v6wOiZgNLjExFjxmfM7Z/DxVVedqUrkve9V0HPV3/Rwf85KpjOfa5kzNe7MgUmqSP4q4nCz3MxpYB2ZxnK/nvRWnysf+dh8VSlWtl8VpumnP4dncDFptp8VmVYjBSJAifNpMHVCOnGElDEVvs8/yxIiSmUuaU3cyXLDtbjulXRCSFMke/cXK6nueXQ2T/lbhSmFnTbTwKsPoZVVXUq9F2VqI3FC54GtjvVptLI00KDVKHYsW+bWbKKGr4ZY6I8ygAqncl4QdIMV8P7Q8PgDutMr2vW0uzZVBPik1eMMP5uGYv/p2MWKCY9rb+cSkqOtGIdksAm6Z6ltZ0mdnaxpdOKY9nVhpq4+ouTHRMmY4OXOcWweyRFyaoRdzuZrnjGfuDWMhLtKc7xer4zmvjZlwZLaSIVBbmRxpirR1R7jNyfvzID/EjXeQxtLCdo+Lsn8a0tPJvEibwzXcXbbijL6O5kF49M+pcT7VkrC/ECPD6BWW6y1FOYJRbXmU2yocrvNiPdHY85zOcK7HUR6z35vOZr4m+b1+rdei0O/1VE46jxJ+6NTz7QGUoq4d9eVyTx8I3PHaeUR6sT1byVE00K7OTh7sd9vR0fWZ8Y6NCSCs+LXWuBNwjrPzZTSMF4NRcilNQtGv6ynfT6rJ8KKc+bMoEFVpzSM1DLUrf6pOTerhYkUnPT4HNLecgS10X6emTr1WX/NEfYp20HnM8zIYWnE1xMVjzUXGXFdozTUsEA9B2qt8ZRLy6jgIV4Kl4pZJ+etG1WVfTOPpxFr6DMjj/ohbb1JlNutvJxOfjKTTcRUtJlEUjBwqOV3JjcoczIMQBKZrOZvRVNqsJoE+K82J5w+k2Ku3E2sDJBo0Ir7QxXy0Io6b6oKL1812Vefa9uAvr7QpHc4bP96qNcgX60t8yVawKe1tD4d6TZWeKVnecnNhpzzZTnxv5VRNWuyYctrTXXw2nVpCtVgswX4hHeLU2ct8TW8cYF42Z3DO9k49dk40SzIKGyjLarYmCiHcHi5Vbu6Wx9yfhtJQKBRBpg3N8HWJIf1rXq/wtbiuFWtVbvcXjbX8IUH1lOWguDJevZ4essHOXqWrRrTKQSWUwUZ0hdxfhjNOI911gDcHUhgKitDM+k1ChWs7EESz9AwlyY84OLDbY/88cyQv2V6JKi/YvruYkPZmRpwMuVAW19DGN2NB4RecUNG4mEe0Ms328Qrnh4vGWRqDzZru18W836tpa3MiTWvvx3t2bC1SZnOJjWauFfVeHB3Zi03NINENZaiDC1loy9Y1ytOMz/e5IAI7Mgb1oD6f5umMWWyJOs+2SaElSTLNvXSu6gauK8mULcLrMipgn13h8ZQvdknqUr64mpaSvUvcQLKPm3MzGfd4bx4UZ3Nq7MYLLsZP1MX0r7Nkm4a5omjM8VTjA2qujES/loyaNMaKXLF7+TDDWZM8nM4bCWcZqmwV+URHg7k33022A3c4OhP8VtzOjmvT3+dJah758Go5++A8DpJayPGiWAksr+Eby3ZhyUw6DbE19OXh3Fte9XYfK6dAPZ+suM/u9+A6n3KGVU6uKWhWp1YyeJ2aq85aXgyy3TJXpktcG876/DkOcF6fj/uGv1nEG8cyZEcc7mKG1CZ4Vg4GxqQ/Jdi2Ja5z4drwvas1XQ6Wk2WPlphGiZo+RfXHpEIxtkb05diJR9dRJs4YxZ5ZerGryHARcJM+KH08tXWSGo0IVfcsfjLsRctFccTpbB9uPL9Yrp2e7VumP99NaS/OeWUhBLjVqJSjzA/7ZbhL2QDgo+q0EtnVdNjSxNiKZ7A5An4vj4WAEHdza1Rag13bmtqhUhxy289WxkBgVkd93mt7ZKO7F82aOs1AHgfRlWaP3J4X+EYtYbjw2ANnKDPXKGZByXlmDOvS83530bjlbt662ZrLCYLsRxwPS3vDZ+Q6ZOxR2VbKWdxtrRPAhb6jV3o1ARU1ZgasGK1dexbt1PPanhSGvHZyanYS5xR/pAmUeQJJ2rkmHziMsgQ9zYTFsglD/AKSaUxFRj9vw6JaeoOdOCRSQ+8vQK2SpWMmpGofyJq5ipHUwKoWLCbjtnaUlcjpPcLUBubueGH8wT7W+zPTHpt4JMtCvcH72Uhut36taCVLaL3p5aoBoV2oGWgjhsf70TCBiYyhfHcoEsqUsKoab3tReskmZ8YHjE2JqueY7YwaOMZcNRsKn1OLoR/2mYFPV/l2JbU7HaRsn8qPm32z51emNx4cprpKHWZqHVDUIjiuqbZpYSvR1GZ/DqhIH5F7zi4F/kzvj0oNLNnZjpLcMU11MrfGszRYTq++NdVd7TTaVVrJVLmymdKDeXPUZak8elxmxvOInfYPtRJne2m5WuPHbBvJuDBc+8HBmwB3XfFzvXdeUGO1dYZWPVxYUWvtycEOaldihuuGGNMWCzh8FJr2tGxXo4nJHonA6NVznFvPMjqjr1y9b2HTUnLVeXs6xOcmT3PGbHNWCoZgHx58fUZY6eDCp4abUCvBnV3drQxtxc4nK37JMna1P5u0uttEh9pg7JMe9VpRtWNpXwaw+zqXdjxfNNwi18wewwlavgYMdV1MYGqQ69adGbC/UqTUZEWDaJPJlAFlrfWpShr0pF0aXYfzmB8N7YVFlVq+53jOYPyyTPeDfHMo02lrhOShsXunMy23nqbO9ILMBNuppUE9OlVzM0p7NszFvakVzdyVvVM2C63nlRugDuarPnMgW24WrhPZJ2m9qlv2PBbO7CBm63pdOPk5AFM+cOuR05Ahf2xmgG/nYECfo5La5vagV9B91mqmkVMWZFlt1mFrDAdsb5ZnkuL6ErWYkiM92K2Ng6UeQ2O6H55zMG6sWRPXYj/L52Iku4ejKm8cz1+okluEmVr066Cn5keif3GJUXLGe/uTs5AWpMttouxMl1ziRWttsWfmfggAO19oK/g4qSyLW/JTsGVTORTaC+xcqtVWouMZPujrqpkkJDEfaiwtsCw4skf3lE3tSZYZJinvrvblfFLrXktvZCEzlVJzqwWgjjRrRAIM7qS2CKwjBZahzYykQzTEBRL2uOvDCVYeANed+TB3ZJoHkQDbpGa65WxuBzMi546YBYVvaZMUHDwzaYvaH4+BxOvxcJgRe5ZVxVAbCTBLJcVgP8m8LTchDnlfHarsyJ5au/1lBEsvwSqMUKOMvmn4sBfCCdF3B8JS0LZUGeg9v3YEbrMnuXo43E0UypgdSr2aG45gjvTBQY52/Z3nE9tVTM9mdsCS9JAKi1EqVUNlE5HKuZGsNU3JajsMApdvDtG6XBwis4dfCV88nInxtUmUhewYU3myXjFGdRCO0yzYRNpOV0vFXo0Ud6PaydHTzFK59vZGacl0wcB4Ph2cq0KAEUYcyu1svjlF3lxJvNAIV8d04MzOjTpW572NfRXZjbEtMvZ0ApPlyiIbx15ks0QojPzIUsP95iB4/Rm1Oww9fsVkRACVJnMkkGlmWOH2SjxYOcPNCIG+VGehGkq47GoOk6wawx3p2hCfkJGziTz3tJ7Rhj9UJa5XlCft0Obccb9x5vLw6vZIw9kVUcPVrHW8Ojihl8FgXkbcLroe+pxfTuqaDC3SO3g93Ku8ZnlcevV4YxpTfM8Sm5SuuMzKG9WGqSYIRvQmO2ZjYqK1BD9Ua/nqDjTnsDi2HHElB+QqUsEgUI4y9JdMJQpTZySlGDDecdvkc3o7yeYu7RmLRiWmkl0IEosvpfIK+7eEIJT5ebAzR2UTTlf1cHJY16YaVOJMIw9ZIJXpmTC55XJqDxxredyP9z3/MFdo1z9yzMw5zUhrx1a1de0NWYKFJggUg9vtYae8U0+74bkyKjc/8jz/+9397b8U7x7J3pDr3Xf/xv08R/7J+NG/hsX7ZyCaIQf3d/9z07XbCCxvIQmZA9BIsvuW1Z3++Co9f97flU4Iz77NJquk8Z+ngxXcB7oJ27tvB4LV5fbp8PafxC8jutryuxloN4u975j/Mm/8POjuPiW/88KyQoPwKsz8BMBCFZHRgrK6DUwhKZCYT/8PB3S0alsxAAA= -->
