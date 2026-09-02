---
name: "rappstore-rapp-log-detective"
description: "Summarise a log file, cluster near-identical errors into signatures, build a timeline of events per bucket, or grep with context. Reads plain text and JSON-lines. Never uploads anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/log-detective", "rar_sha256": "5d3b06228dddc510fb3a84a30b1e3517387d52388cdf66e6879e4be9e5c7a81f", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "log_detective_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/log-detective:2d4ab305c3145c0e16960f41f58c082334de16a872388e1f62264ea14ef1ad42", "kind": "skill"}, "tags": ["logs", "debugging", "observability", "local-first", "singleton"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/log-detective`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `log_detective_agent.py` is
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
