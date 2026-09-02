---
name: "rappstore-rapp-csv-surgeon"
description: "Profile a CSV: per-column types, null rate, cardinality, min/max; or find ragged rows, duplicate headers and mixed types; or find duplicate records; or slice rows. Stdlib only, no network."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/csv-surgeon", "rar_sha256": "4d500fd77ebdc677d2860167748f06d1280bfd10de365f759e3b0e9a682b4076", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "csv_surgeon_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/csv-surgeon:3fb58c33eb2230129258ce6fcd1e96b91bfa8e53a3bbcd240d8c199f6d5af481", "kind": "skill"}, "tags": ["data", "csv", "profiling", "quality", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/csv-surgeon`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `csv_surgeon_agent.py` is
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
