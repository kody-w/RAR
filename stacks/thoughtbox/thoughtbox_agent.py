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
