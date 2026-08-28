---
name: "rappstore-rapp-csv-surgeon"
description: "Profile a CSV: per-column types, null rate, cardinality, min/max; or find ragged rows, duplicate headers and mixed types; or find duplicate records; or slice rows. Stdlib only, no network."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/csv-surgeon", "rar_sha256": "4d500fd77ebdc677d2860167748f06d1280bfd10de365f759e3b0e9a682b4076", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["data", "csv", "profiling", "quality", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/csv-surgeon`. The original RAPP
agent is preserved byte-for-byte in `csv_surgeon_agent.py` and in the RCI capsule.

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

CSV Surgeon — profile a CSV and find the rows that will break something.

    profile   per-column type, null rate, cardinality, min/max, sample values
    issues    ragged rows, duplicate headers, mixed types, whitespace-padded keys
    dupes     duplicate records, by whole row or by chosen key columns
    slice     head/tail/filter rows without loading the file into a spreadsheet

Pure stdlib `csv`, no pandas, no network, no credentials.

WHY IT LEADS WITH NULL RATE AND CARDINALITY

Those two numbers explain most CSV surprises. A column that is 40% empty will
break a join you thought was safe. A column with cardinality 1 is a constant
someone forgot to remove. A column with cardinality == row count is an id, and
joining on anything else is probably a mistake. None of that is visible by
looking at the first ten rows, which is what everyone does.

WHY RAGGED ROWS GET THEIR OWN CHECK

A row with the wrong number of fields is the single most common CSV defect, and
most tools silently pad or truncate it. The data then looks fine and is wrong.
This reports the row number so you can go and look at it.

WHY WHITESPACE IN HEADERS IS A FINDING

`"name"` and `"name "` are different keys in every downstream consumer, and the
difference is invisible in every viewer. It produces bugs that read as
impossible.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do.",
      "enum": [
        "profile",
        "issues",
        "dupes",
        "slice"
      ],
      "type": "string"
    },
    "keys": {
      "description": "For dupes: comma-separated column names to match on. Default: the whole row.",
      "type": "string"
    },
    "limit": {
      "description": "For slice: how many rows. Default 10.",
      "type": "integer"
    },
    "path": {
      "description": "Path to the .csv file.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `csv_surgeon_agent.py` and embedded as the fenced Python below (sha256 4d500fd77ebdc677…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `csv_surgeon_agent.py` first:

```bash
python3 csv_surgeon_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 csv_surgeon_agent.py   # or on stdin
python3 csv_surgeon_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""CSV Surgeon — profile a CSV and find the rows that will break something.

    profile   per-column type, null rate, cardinality, min/max, sample values
    issues    ragged rows, duplicate headers, mixed types, whitespace-padded keys
    dupes     duplicate records, by whole row or by chosen key columns
    slice     head/tail/filter rows without loading the file into a spreadsheet

Pure stdlib `csv`, no pandas, no network, no credentials.

WHY IT LEADS WITH NULL RATE AND CARDINALITY

Those two numbers explain most CSV surprises. A column that is 40% empty will
break a join you thought was safe. A column with cardinality 1 is a constant
someone forgot to remove. A column with cardinality == row count is an id, and
joining on anything else is probably a mistake. None of that is visible by
looking at the first ten rows, which is what everyone does.

WHY RAGGED ROWS GET THEIR OWN CHECK

A row with the wrong number of fields is the single most common CSV defect, and
most tools silently pad or truncate it. The data then looks fine and is wrong.
This reports the row number so you can go and look at it.

WHY WHITESPACE IN HEADERS IS A FINDING

`"name"` and `"name "` are different keys in every downstream consumer, and the
difference is invisible in every viewer. It produces bugs that read as
impossible.
"""

import csv
import io
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
    "name": "@rapp/csv-surgeon",
    "tier": "core",
    "trust": "community",
    "version": "1.0.0",
    "tags": ["data", "csv", "profiling", "quality", "local-first", "singleton"],
    "example_call": {
        "args": {"action": "profile", "path": "data.csv"},
        "note": "Per-column types, null rates and cardinality.",
    },
}

MAX_BYTES = 256 * 1024 * 1024
SAMPLE_CAP = 200_000


def _kind(s):
    if s is None or s == "":
        return "empty"
    t = s.strip()
    if t.lower() in ("true", "false"):
        return "bool"
    try:
        int(t)
        return "int"
    except ValueError:
        pass
    try:
        float(t)
        return "float"
    except ValueError:
        pass
    return "string"


def _read(path, limit=SAMPLE_CAP):
    if os.path.getsize(path) > MAX_BYTES:
        raise ValueError(f"file larger than {MAX_BYTES} bytes")
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        sample = fh.read(64 * 1024)
        fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        except csv.Error:
            dialect = csv.excel        # a single-column file sniffs as an error
        r = csv.reader(fh, dialect)
        rows = []
        for i, row in enumerate(r):
            if i > limit:
                break
            rows.append(row)
    delim = getattr(dialect, "delimiter", ",")
    return rows, delim


class CsvSurgeonAgent(BasicAgent):
    def __init__(self):
        self.name = "CsvSurgeon"
        self.metadata = {
            "name": self.name,
            "description": (
                "Profile a CSV: per-column types, null rate, cardinality, "
                "min/max; or find ragged rows, duplicate headers and mixed "
                "types; or find duplicate records; or slice rows. Stdlib only, "
                "no network."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["profile", "issues", "dupes", "slice"],
                               "description": "What to do."},
                    "path": {"type": "string", "description": "Path to the .csv file."},
                    "keys": {"type": "string",
                             "description": "For dupes: comma-separated column names "
                                            "to match on. Default: the whole row."},
                    "limit": {"type": "integer",
                              "description": "For slice: how many rows. Default 10."},
                },
                "required": ["action", "path"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action, path = kwargs.get("action"), kwargs.get("path")
        if not path or not os.path.isfile(path):
            return json.dumps({"status": "error",
                               "message": f"file not found: {path}"}, indent=2)
        try:
            rows, delim = _read(path)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)
        if not rows:
            return json.dumps({"status": "ok", "rows": 0, "note": "empty file"}, indent=2)

        header, body = rows[0], rows[1:]
        ncol = len(header)

        try:
            if action == "profile":
                cols = []
                for i, name in enumerate(header):
                    vals = [r[i] if i < len(r) else "" for r in body]
                    kinds = {}
                    nonempty = []
                    for v in vals:
                        k = _kind(v)
                        kinds[k] = kinds.get(k, 0) + 1
                        if k != "empty":
                            nonempty.append(v.strip())
                    uniq = len(set(nonempty))
                    nulls = kinds.get("empty", 0)
                    numeric = [x for x in nonempty
                               if _kind(x) in ("int", "float")]
                    col = {
                        "column": name,
                        "types": sorted([k for k in kinds if k != "empty"]) or ["empty"],
                        "null_rate": f"{100.0 * nulls / max(1, len(vals)):.0f}%",
                        "cardinality": uniq,
                        "sample": nonempty[0][:40] if nonempty else None,
                    }
                    if numeric:
                        nums = [float(x) for x in numeric]
                        col["min"], col["max"] = min(nums), max(nums)
                    if uniq == len(body) and body:
                        col["note"] = "unique per row — looks like an id"
                    elif uniq == 1 and nonempty:
                        col["note"] = "single value — constant column"
                    if len(col["types"]) > 1:
                        col["note"] = "MIXED TYPES — will break a strict consumer"
                    cols.append(col)
                return json.dumps({"status": "ok", "rows": len(body),
                                   "columns": ncol, "delimiter": delim,
                                   "profile": cols,
                                   "note": "null rate and cardinality explain most "
                                           "CSV surprises, and neither is visible "
                                           "in the first ten rows."}, indent=2)

            if action == "issues":
                issues = []
                seen_h = {}
                for i, h in enumerate(header):
                    if h != h.strip():
                        issues.append({"kind": "padded-header", "column": i,
                                       "detail": repr(h),
                                       "why": "'name' and 'name ' are different keys "
                                              "downstream, and look identical in a viewer"})
                    if h.strip() in seen_h:
                        issues.append({"kind": "duplicate-header",
                                       "column": i, "detail": h.strip()})
                    seen_h[h.strip()] = i
                    if not h.strip():
                        issues.append({"kind": "empty-header", "column": i})
                for n, r in enumerate(body, start=2):
                    if len(r) != ncol:
                        issues.append({"kind": "ragged-row", "row": n,
                                       "detail": f"{len(r)} fields, expected {ncol}",
                                       "why": "most tools silently pad or truncate "
                                              "this; the data then looks fine and is wrong"})
                    if len(issues) > 200:
                        break
                return json.dumps({"status": "ok", "rows": len(body),
                                   "issue_count": len(issues),
                                   "clean": not issues,
                                   "issues": issues[:100]}, indent=2)

            if action == "dupes":
                keyspec = (kwargs.get("keys") or "").strip()
                if keyspec:
                    names = [k.strip() for k in keyspec.split(",") if k.strip()]
                    missing = [n for n in names if n not in header]
                    if missing:
                        return json.dumps({"status": "error",
                                           "message": f"no such column(s): {missing}",
                                           "available": header}, indent=2)
                    idxs = [header.index(n) for n in names]
                else:
                    names, idxs = header, list(range(ncol))
                seen, dupes = {}, []
                for n, r in enumerate(body, start=2):
                    key = tuple(r[i] if i < len(r) else "" for i in idxs)
                    if key in seen:
                        dupes.append({"row": n, "first_seen_row": seen[key],
                                      "key": dict(zip(names, key))})
                    else:
                        seen[key] = n
                return json.dumps({"status": "ok", "rows": len(body),
                                   "matched_on": names,
                                   "duplicate_count": len(dupes),
                                   "duplicates": dupes[:100]}, indent=2)

            if action == "slice":
                lim = int(kwargs.get("limit") or 10)
                out = [dict(zip(header, r)) for r in body[:lim]]
                return json.dumps({"status": "ok", "rows": len(body),
                                   "returned": len(out), "records": out}, indent=2)

            return json.dumps({"status": "error",
                               "message": f"unknown action {action!r}",
                               "valid": ["profile", "issues", "dupes", "slice"]}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--tool":
        print(json.dumps(CsvSurgeonAgent().to_tool(), indent=2))
    else:
        raw = a[0] if a else (sys.stdin.read().strip() or "{}")
        print(CsvSurgeonAgent().perform(**json.loads(raw)))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
