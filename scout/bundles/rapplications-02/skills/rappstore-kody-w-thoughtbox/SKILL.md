---
name: "rappstore-kody-w-thoughtbox"
description: ""
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/thoughtbox", "rar_sha256": "d93b56abcc578d8299df787816142c3d0553a018d45e611ad54ac453bf11933b", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "thoughtbox_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/thoughtbox:bd0ae282d790619539ddd1e56cf2d37c1453dd7a83bf0c2d929a3701ad9d7fe9", "kind": "skill"}, "tags": ["rapplication", "journal", "local-first", "scratchpad", "has-ui"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/thoughtbox`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `thoughtbox_agent.py` is
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

Thoughtbox — a local-first reflection journal rapplication.

Drop this singleton into any standard brainstem (`agents/` directory)
and it auto-discovers. Pair it with `ui/index.html` for the bundled
rapplication; the agent works headless without it too.

State model
-----------
The agent is stateless on disk by default — it routes all reads/writes
through the rapplication workspace API (SPEC §12). Entries live under
the workspace key `entries.json` and are an append-only list of dicts:

    [{"id": "<uuid>", "text": "...", "tags": ["..."], "ts": "<iso8601>"}, ...]

If the host brainstem doesn't expose a workspace, the agent falls back
to an in-memory list scoped to the brainstem process — useful for
quick demos but volatile.

Why local-first
---------------
The whole point: nothing leaves the machine. No network calls, no
telemetry, no central server. Export + import are explicit user
actions that produce/consume a JSON blob the user controls.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `thoughtbox_agent.py` and embedded as the fenced Python below (sha256 d93b56abcc578d82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `thoughtbox_agent.py` first:

```bash
python3 thoughtbox_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 thoughtbox_agent.py   # or on stdin
python3 thoughtbox_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Thoughtbox — a local-first reflection journal rapplication.

Drop this singleton into any standard brainstem (`agents/` directory)
and it auto-discovers. Pair it with `ui/index.html` for the bundled
rapplication; the agent works headless without it too.

State model
-----------
The agent is stateless on disk by default — it routes all reads/writes
through the rapplication workspace API (SPEC §12). Entries live under
the workspace key `entries.json` and are an append-only list of dicts:

    [{"id": "<uuid>", "text": "...", "tags": ["..."], "ts": "<iso8601>"}, ...]

If the host brainstem doesn't expose a workspace, the agent falls back
to an in-memory list scoped to the brainstem process — useful for
quick demos but volatile.

Why local-first
---------------
The whole point: nothing leaves the machine. No network calls, no
telemetry, no central server. Export + import are explicit user
actions that produce/consume a JSON blob the user controls.
"""

from __future__ import annotations

import json
import time
import uuid
from datetime import datetime, timezone
from typing import Any

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-application/1.0",
    "id": "thoughtbox",
    "name": "Thoughtbox",
    "version": "1.0.0",
    "publisher": "@kody-w",
    "summary": "Local-first reflection journal. Append, list, search, tag, export, import.",
    "category": "productivity",
    "tags": ["rapplication", "journal", "local-first", "scratchpad", "has-ui"],
    "agent": "singleton/thoughtbox_agent.py",
    "ui": "ui/index.html",
}


AGENT = {
    "name": "Thoughtbox",
    "metadata": {
        "name": "Thoughtbox",
        "description": (
            "Local-first reflection journal. Append a thought; list, "
            "search, or filter by tag; export/import the whole journal "
            "as a portable JSON blob. State stays on the box; nothing "
            "leaves the machine unless you explicitly export it."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": [
                        "append", "list", "search", "tag",
                        "export", "import_json", "stats", "delete",
                    ],
                    "description": "The action to perform.",
                },
                "text": {
                    "type": "string",
                    "description": "Body of a new entry (for append).",
                },
                "tags": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional tags for the new entry.",
                },
                "query": {
                    "type": "string",
                    "description": "Substring to search for in entry text.",
                },
                "tag": {
                    "type": "string",
                    "description": "Tag to filter by (for tag action).",
                },
                "limit": {
                    "type": "integer",
                    "description": "Cap on results (default 50, max 1000).",
                },
                "id": {
                    "type": "string",
                    "description": "Entry ID (for delete).",
                },
                "blob": {
                    "type": "string",
                    "description": "JSON string to import (for import_json).",
                },
            },
            "required": ["action"],
        },
    },
}


_FALLBACK_STORE: list[dict[str, Any]] = []


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load(context: dict | None) -> list[dict[str, Any]]:
    """Read the entries list from workspace, falling back to in-memory."""
    if context and callable(context.get("workspace_read")):
        try:
            raw = context["workspace_read"]("entries.json")
            if raw:
                data = json.loads(raw)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError, RuntimeError):
            pass
    return _FALLBACK_STORE


def _save(entries: list[dict[str, Any]], context: dict | None) -> None:
    """Persist entries via workspace, or update fallback list in place."""
    global _FALLBACK_STORE
    if context and callable(context.get("workspace_write")):
        try:
            context["workspace_write"]("entries.json", json.dumps(entries, indent=2))
            return
        except (OSError, RuntimeError):
            pass
    _FALLBACK_STORE = entries


def _format_entries(entries: list[dict[str, Any]], limit: int) -> str:
    if not entries:
        return "(no entries)"
    rows = []
    for e in entries[:limit]:
        ts = e.get("ts", "")
        tags = e.get("tags") or []
        tag_str = (" #" + " #".join(tags)) if tags else ""
        rows.append(f"[{ts}] {e.get('text', '')}{tag_str}  ({e.get('id', '')[:8]})")
    return "\n".join(rows)


def _do_append(entries: list[dict[str, Any]], text: str,
               tags: list[str] | None) -> dict[str, Any]:
    text = (text or "").strip()
    if not text:
        return {"ok": False, "error": "text is required and non-empty"}
    entry = {
        "id": str(uuid.uuid4()),
        "text": text,
        "tags": [t.strip() for t in (tags or []) if t and t.strip()],
        "ts": _now_iso(),
    }
    entries.append(entry)
    return {"ok": True, "entry": entry, "total": len(entries)}


def _do_list(entries: list[dict[str, Any]], limit: int) -> dict[str, Any]:
    sorted_entries = sorted(entries, key=lambda e: e.get("ts", ""), reverse=True)
    return {
        "ok": True,
        "total": len(entries),
        "shown": min(len(entries), limit),
        "entries": sorted_entries[:limit],
        "rendered": _format_entries(sorted_entries, limit),
    }


def _do_search(entries: list[dict[str, Any]], query: str,
               limit: int) -> dict[str, Any]:
    q = (query or "").strip().lower()
    if not q:
        return {"ok": False, "error": "query is required"}
    matches = [e for e in entries if q in (e.get("text") or "").lower()]
    matches.sort(key=lambda e: e.get("ts", ""), reverse=True)
    return {
        "ok": True,
        "query": query,
        "total": len(matches),
        "shown": min(len(matches), limit),
        "entries": matches[:limit],
        "rendered": _format_entries(matches, limit),
    }


def _do_tag(entries: list[dict[str, Any]], tag: str,
            limit: int) -> dict[str, Any]:
    t = (tag or "").strip().lower()
    if not t:
        return {"ok": False, "error": "tag is required"}
    matches = [e for e in entries if t in [x.lower() for x in (e.get("tags") or [])]]
    matches.sort(key=lambda e: e.get("ts", ""), reverse=True)
    return {
        "ok": True,
        "tag": tag,
        "total": len(matches),
        "shown": min(len(matches), limit),
        "entries": matches[:limit],
        "rendered": _format_entries(matches, limit),
    }


def _do_stats(entries: list[dict[str, Any]]) -> dict[str, Any]:
    tag_counts: dict[str, int] = {}
    for e in entries:
        for t in e.get("tags") or []:
            tag_counts[t] = tag_counts.get(t, 0) + 1
    earliest = min((e.get("ts") for e in entries if e.get("ts")), default=None)
    latest = max((e.get("ts") for e in entries if e.get("ts")), default=None)
    return {
        "ok": True,
        "total": len(entries),
        "earliest": earliest,
        "latest": latest,
        "tag_counts": dict(sorted(tag_counts.items(), key=lambda kv: -kv[1])),
    }


def _do_export(entries: list[dict[str, Any]]) -> dict[str, Any]:
    blob = {
        "schema": "thoughtbox/1.0",
        "exported_at": _now_iso(),
        "count": len(entries),
        "entries": entries,
    }
    return {"ok": True, "json": json.dumps(blob, indent=2), "count": len(entries)}


def _do_import(entries: list[dict[str, Any]], blob: str) -> dict[str, Any]:
    if not blob:
        return {"ok": False, "error": "blob is required"}
    try:
        d = json.loads(blob)
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"invalid json: {e}"}
    incoming = d.get("entries") if isinstance(d, dict) else d
    if not isinstance(incoming, list):
        return {"ok": False, "error": "blob must contain a list of entries"}
    seen_ids = {e.get("id") for e in entries if e.get("id")}
    added = 0
    for raw in incoming:
        if not isinstance(raw, dict):
            continue
        eid = raw.get("id") or str(uuid.uuid4())
        if eid in seen_ids:
            continue
        text = raw.get("text") or raw.get("body") or ""
        if not text:
            continue
        entries.append({
            "id": eid,
            "text": text,
            "tags": raw.get("tags") or [],
            "ts": raw.get("ts") or _now_iso(),
        })
        seen_ids.add(eid)
        added += 1
    return {"ok": True, "added": added, "total": len(entries)}


def _do_delete(entries: list[dict[str, Any]], entry_id: str) -> dict[str, Any]:
    if not entry_id:
        return {"ok": False, "error": "id is required"}
    before = len(entries)
    entries[:] = [e for e in entries if not (
        e.get("id") == entry_id or e.get("id", "").startswith(entry_id)
    )]
    removed = before - len(entries)
    return {"ok": True, "removed": removed, "total": len(entries)}


def run(context: dict | None = None, **kwargs: Any) -> str:
    """Entry point. Returns a string; rich data is in the JSON payload."""
    action = (kwargs.get("action") or "").strip()
    if not action:
        return json.dumps({"ok": False, "error": "action is required"}, indent=2)

    limit = int(kwargs.get("limit") or 50)
    limit = max(1, min(limit, 1000))

    entries = list(_load(context))
    persistent_actions = {"append", "import_json", "delete"}

    if action == "append":
        result = _do_append(entries, kwargs.get("text") or "", kwargs.get("tags"))
    elif action == "list":
        result = _do_list(entries, limit)
    elif action == "search":
        result = _do_search(entries, kwargs.get("query") or "", limit)
    elif action == "tag":
        result = _do_tag(entries, kwargs.get("tag") or "", limit)
    elif action == "stats":
        result = _do_stats(entries)
    elif action == "export":
        result = _do_export(entries)
    elif action == "import_json":
        result = _do_import(entries, kwargs.get("blob") or "")
    elif action == "delete":
        result = _do_delete(entries, kwargs.get("id") or "")
    else:
        result = {"ok": False, "error": f"unknown action: {action!r}"}

    if result.get("ok") and action in persistent_actions:
        _save(entries, context)

    return json.dumps(result, indent=2)


class ThoughtboxAgent(BasicAgent):
    """BasicAgent wrapper for swarm/brainstem auto-discovery."""

    def __init__(self) -> None:
        super().__init__(name=AGENT["name"], metadata=AGENT["metadata"])

    def perform(self, **kwargs: Any) -> str:
        return run(kwargs.pop("_context", None), **kwargs)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
