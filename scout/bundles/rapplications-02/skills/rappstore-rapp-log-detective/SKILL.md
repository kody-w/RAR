---
name: "rappstore-rapp-log-detective"
description: "Summarise a log file, cluster near-identical errors into signatures, build a timeline of events per bucket, or grep with context. Reads plain text and JSON-lines. Never uploads anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/log-detective", "rar_sha256": "5d3b06228dddc510fb3a84a30b1e3517387d52388cdf66e6879e4be9e5c7a81f", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["logs", "debugging", "observability", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/log-detective`. The original RAPP
agent is preserved byte-for-byte in `log_detective_agent.py` and in the RCI capsule.

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

Log Detective — turn a wall of log lines into the three things you needed.

    summarise   level counts, time span, busiest minute, top error signatures
    signatures  cluster near-identical errors by shape, not text
    timeline    events per bucket, so a spike has a timestamp
    grep        filtered lines with surrounding context

No network, no credentials, no parsing config. Handles plain text, and reads
JSON-lines logs structurally when it detects them.

WHY IT CLUSTERS BY SIGNATURE INSTEAD OF COUNTING LINES

Ten thousand errors are usually four errors. Raw counts hide that: every line
differs by a request id, a timestamp, a port number, so nothing groups and you
scroll. Normalising the variable parts — numbers, hex ids, UUIDs, paths, quoted
strings — collapses them into a handful of shapes, and the shape is the bug.

WHY 'BUSIEST MINUTE' IS ITS OWN NUMBER

An incident is a spike, and a spike is invisible in a total. Knowing that 80% of
the day's errors landed inside one minute changes what you go and look at.

WHY IT NEVER PHONES HOME

Logs are the single most PII-dense artifact most systems produce. Anything that
uploads them to be "analysed" is a data-egress decision disguised as a feature.
This reads local files and returns local results.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do.",
      "enum": [
        "summarise",
        "signatures",
        "timeline",
        "grep"
      ],
      "type": "string"
    },
    "context": {
      "description": "For grep: lines of context. Default 1.",
      "type": "integer"
    },
    "path": {
      "description": "Path to the log file.",
      "type": "string"
    },
    "pattern": {
      "description": "For grep: a regular expression.",
      "type": "string"
    },
    "top": {
      "description": "How many signatures/buckets. Default 10.",
      "type": "integer"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `log_detective_agent.py` and embedded as the fenced Python below (sha256 5d3b06228dddc510…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `log_detective_agent.py` first:

```bash
python3 log_detective_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 log_detective_agent.py   # or on stdin
python3 log_detective_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Log Detective — turn a wall of log lines into the three things you needed.

    summarise   level counts, time span, busiest minute, top error signatures
    signatures  cluster near-identical errors by shape, not text
    timeline    events per bucket, so a spike has a timestamp
    grep        filtered lines with surrounding context

No network, no credentials, no parsing config. Handles plain text, and reads
JSON-lines logs structurally when it detects them.

WHY IT CLUSTERS BY SIGNATURE INSTEAD OF COUNTING LINES

Ten thousand errors are usually four errors. Raw counts hide that: every line
differs by a request id, a timestamp, a port number, so nothing groups and you
scroll. Normalising the variable parts — numbers, hex ids, UUIDs, paths, quoted
strings — collapses them into a handful of shapes, and the shape is the bug.

WHY 'BUSIEST MINUTE' IS ITS OWN NUMBER

An incident is a spike, and a spike is invisible in a total. Knowing that 80% of
the day's errors landed inside one minute changes what you go and look at.

WHY IT NEVER PHONES HOME

Logs are the single most PII-dense artifact most systems produce. Anything that
uploads them to be "analysed" is a data-egress decision disguised as a feature.
This reads local files and returns local results.
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict

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
    "name": "@rapp/log-detective",
    "tier": "core",
    "trust": "community",
    "version": "1.0.0",
    "tags": ["logs", "debugging", "observability", "local-first", "singleton"],
    "example_call": {
        "args": {"action": "signatures", "path": "app.log"},
        "note": "Cluster near-identical errors by shape.",
    },
}

MAX_BYTES = 512 * 1024 * 1024
LEVEL = re.compile(r"\b(TRACE|DEBUG|INFO|NOTICE|WARN(?:ING)?|ERROR|ERR|FATAL|CRITICAL)\b", re.I)
TS = re.compile(
    r"(\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2})"          # 2026-07-25 04:10:11
    r"|(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})"             # apache
    r"|(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})")            # syslog

# Order matters: UUID before hex before plain number, or the general rules eat
# the specific ones and every signature collapses into the same mush.
NORMALISERS = [
    (re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I), "<uuid>"),
    (re.compile(r"\b0x[0-9a-f]+\b", re.I), "<hex>"),
    (re.compile(r"\b[0-9a-f]{16,}\b", re.I), "<hash>"),
    (re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b"), "<ip>"),
    (re.compile(r"[\"'][^\"']{1,80}[\"']"), "<str>"),
    (re.compile(r"(/[\w.\-]+){2,}"), "<path>"),
    # Numbers carry unit suffixes in real logs (815ms, 30s, 5KB, db-7). A
    # trailing \b never matches between a digit and a letter, so "815ms" kept
    # its number and every line became its own signature -- 96 clusters where
    # there were 3. Consume an optional unit so the shape actually groups.
    (re.compile(r"\b\d+(?:\.\d+)?(?:ms|s|m|h|d|kb|mb|gb|b|%)?\b", re.I), "<n>"),
]


def _norm(line):
    s = LEVEL.sub("", TS.sub("", line)).strip()
    for rx, rep in NORMALISERS:
        s = rx.sub(rep, s)
    return re.sub(r"\s+", " ", s).strip()[:200]


def _lines(path, cap=2_000_000):
    if os.path.getsize(path) > MAX_BYTES:
        raise ValueError(f"file larger than {MAX_BYTES} bytes")
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, ln in enumerate(fh):
            if i >= cap:
                break
            ln = ln.rstrip("\n")
            if ln.strip():
                out.append(ln)
    return out


def _structured(line):
    """A JSON-lines log carries level and message as fields; using them beats
    regexing text that was already structured."""
    t = line.lstrip()
    if not t.startswith("{"):
        return None
    try:
        d = json.loads(t)
    except Exception:
        return None
    if not isinstance(d, dict):
        return None
    lvl = d.get("level") or d.get("severity") or d.get("lvl")
    msg = d.get("message") or d.get("msg") or d.get("event")
    return {"level": str(lvl).upper() if lvl else None,
            "message": str(msg) if msg else None,
            "ts": d.get("time") or d.get("timestamp") or d.get("ts")}


class LogDetectiveAgent(BasicAgent):
    def __init__(self):
        self.name = "LogDetective"
        self.metadata = {
            "name": self.name,
            "description": (
                "Summarise a log file, cluster near-identical errors into "
                "signatures, build a timeline of events per bucket, or grep "
                "with context. Reads plain text and JSON-lines. Never uploads "
                "anything."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["summarise", "signatures", "timeline", "grep"],
                               "description": "What to do."},
                    "path": {"type": "string", "description": "Path to the log file."},
                    "pattern": {"type": "string",
                                "description": "For grep: a regular expression."},
                    "context": {"type": "integer",
                                "description": "For grep: lines of context. Default 1."},
                    "top": {"type": "integer",
                            "description": "How many signatures/buckets. Default 10."},
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
        top = int(kwargs.get("top") or 10)
        try:
            lines = _lines(path)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)
        if not lines:
            return json.dumps({"status": "ok", "lines": 0,
                               "note": "file is empty"}, indent=2)

        struct = sum(1 for ln in lines[:200] if _structured(ln))
        jsonl = struct > len(lines[:200]) * 0.6

        def level_of(ln):
            if jsonl:
                s = _structured(ln)
                if s and s["level"]:
                    return s["level"]
            m = LEVEL.search(ln)
            return m.group(1).upper() if m else None

        def body_of(ln):
            if jsonl:
                s = _structured(ln)
                if s and s["message"]:
                    return s["message"]
            return ln

        try:
            if action == "summarise":
                levels = Counter(level_of(l) or "UNLABELLED" for l in lines)
                stamps = [m.group(0) for l in lines
                          for m in [TS.search(l)] if m]
                minutes = Counter(s[:16] for s in stamps)
                bad = [l for l in lines
                       if (level_of(l) or "") in ("ERROR", "ERR", "FATAL", "CRITICAL")]
                sigs = Counter(_norm(body_of(l)) for l in bad)
                busiest = minutes.most_common(1)[0] if minutes else None
                return json.dumps({
                    "status": "ok", "format": "jsonl" if jsonl else "text",
                    "lines": len(lines), "levels": dict(levels.most_common()),
                    "first_timestamp": stamps[0] if stamps else None,
                    "last_timestamp": stamps[-1] if stamps else None,
                    "busiest_minute": ({"minute": busiest[0], "events": busiest[1]}
                                       if busiest else None),
                    "error_lines": len(bad),
                    "top_error_signatures": [
                        {"count": c, "signature": s} for s, c in sigs.most_common(top)],
                    "note": "an incident is a spike, and a spike is invisible in a total",
                }, indent=2)

            if action == "signatures":
                sigs, examples = Counter(), {}
                for l in lines:
                    lv = level_of(l) or ""
                    if lv in ("ERROR", "ERR", "FATAL", "CRITICAL", "WARN", "WARNING"):
                        s = _norm(body_of(l))
                        sigs[s] += 1
                        examples.setdefault(s, l[:200])
                total = sum(sigs.values())
                out = [{"count": c, "share": f"{100.0*c/max(1,total):.0f}%",
                        "signature": s, "example": examples[s]}
                       for s, c in sigs.most_common(top)]
                return json.dumps({
                    "status": "ok", "lines": len(lines),
                    "problem_lines": total, "distinct_signatures": len(sigs),
                    "signatures": out,
                    "note": "ten thousand errors are usually four errors — "
                            "variable parts are normalised so the shape groups",
                }, indent=2)

            if action == "timeline":
                buckets = Counter()
                for l in lines:
                    m = TS.search(l)
                    if m:
                        buckets[m.group(0)[:16]] += 1
                ordered = sorted(buckets.items())
                peak = max(buckets.values()) if buckets else 0
                return json.dumps({
                    "status": "ok", "buckets": len(ordered),
                    "peak_events": peak,
                    "timeline": [{"bucket": b, "events": c,
                                  "bar": "#" * max(1, round(20 * c / max(1, peak)))}
                                 for b, c in ordered[:120]],
                }, indent=2)

            if action == "grep":
                pat = kwargs.get("pattern")
                if not pat:
                    return json.dumps({"status": "error",
                                       "message": "pattern is required for grep"}, indent=2)
                try:
                    rx = re.compile(pat, re.I)
                except re.error as e:
                    return json.dumps({"status": "error",
                                       "message": f"bad regex: {e}"}, indent=2)
                ctx = int(kwargs.get("context") or 1)
                hits = []
                for i, l in enumerate(lines):
                    if rx.search(l):
                        hits.append({"line_no": i + 1,
                                     "before": lines[max(0, i - ctx):i],
                                     "match": l[:300],
                                     "after": lines[i + 1:i + 1 + ctx]})
                    if len(hits) >= 200:
                        break
                return json.dumps({"status": "ok", "lines": len(lines),
                                   "matches": len(hits), "hits": hits[:100]}, indent=2)

            return json.dumps({"status": "error",
                               "message": f"unknown action {action!r}",
                               "valid": ["summarise", "signatures", "timeline", "grep"]}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error",
                               "message": f"{type(e).__name__}: {e}"}, indent=2)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--tool":
        print(json.dumps(LogDetectiveAgent().to_tool(), indent=2))
    else:
        raw = a[0] if a else (sys.stdin.read().strip() or "{}")
        print(LogDetectiveAgent().perform(**json.loads(raw)))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
