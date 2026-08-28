---
name: "rappstore-kody-w-thoughtbox"
description: ""
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/thoughtbox", "rar_sha256": "d93b56abcc578d8299df787816142c3d0553a018d45e611ad54ac453bf11933b", "source_kind": "federated-rapplication", "source_commit": null, "tags": ["rapplication", "journal", "local-first", "scratchpad", "has-ui"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/thoughtbox`. The original RAPP
agent is preserved byte-for-byte in `thoughtbox_agent.py` and in the RCI capsule.

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

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZZ5OjWJb9K0TOh+4eVRZGQkDN7sQiEBJWOElInR1deG+Eh9r+7/tQZnX1xE7sp1VkZIhnrj33vMvTtxe7a6OyfvlSdFn26cXzG7eOqzYui5cvLy+fXvzRzqvMb16+/Prbp5cYfH/58u3FzewGDL2YUdmFUeuUIx36RQvWZ3YRgolqAlIL8Fz5dVDWORjy/AD6ePq58bPgE/T3v6eDXYfNF4gupl+g139CTVt/eSugj0/tt11dQHVX/Py+8HNVVj+/vfzulkXrj+3byydIKQv/lx+ifnn5A1hZADmduzixGPm3v0Fy7NZlUwYtZLhl1y4i2zj334q3woziBgJ/beQDhb1fN7GT+R/rqrpM/KcgqAygr/+Vlt70OsDtn25//QyZYGNZx2Fc2Bmk06r6VthLMBahVe03ft37HuRMrf8KfH9dvkBxAX39IeT35/rP1fQVsgtvmVyM0Rkecu2q6TL/82LoNfKLD7Ncu4D80Xc7ICorXaA3iEGOPgEHmjLrfbAfKG/SOMsgL66BB2U9PWUDx78swr5+/erYTfRWvCdqDb2nvYHBgj/NgV5fgQNBFgMz3wrfjUrop29//AT9N/R/7XoKX3SoACMfYQUWCsZJgUCKuhwsAxEHOfJt7xnWb398hBGIKfwaAkmIg9h/35zFRep732NqHOlXDN9Cjg9iCeKYV2XdxkUIxe1niA+gP+0FSpepBrKhqGxayPMrv/D8wp2AVBu482cki7KFGruNm2D6BHWN/9T61antp4n57y5Y/hWSGRVqyzID/xYzn4vA5rKIQfj/zPj7OBBS/9RAu+8iPkPKAiyosmu7imr7Q0dgv+elrKHv24FwGyr84a1YKs1fQmUv6HsPD1gEIuN+pPR1yTnklnkOEtt81/1cY7cAcWZpA+X1W9F8INiul1S4JTBlgsIu9uzC9f/xAakGoDHznvEDli6SPrLgfWTl83uxfMcs9NZhCLoB5j4BCIypmyXoQfahLSlB7YK8A5erDATp6cYig63L6gOgIHGZ34LF754XEyAA4Ixdg3r5Hjzo56/P6DTw1x9Y/gVEfKmUFgL0Vb56cfN0q/kMqXZcL+ND3EbQ1y6GY5D18XPU5tlXCGDm6ZrTFV62gOqvxv3jOfWeiaGs0waKAEBBWTVPYUuQgFyAgacXBkiMD+Wl54Psv/74LDH6LmVxcVn2lAG8BGamgAgAFgO7y9rvIQRSayAd4N0G9QqKxWvgoY7BwFvRRvUS8fcy+oux7xZWtutDtMpDPxvqngHyEMQmUOyXz9C+aOulgrIYsAHwdsHBIuPHttSfoK/++7LPSVMW7+SzgASwC1AFyuW1LLIJyACZBXXqxW7bPNljIedfv729xN7byxfo7eU/OoCmfy50/PbyTszL6OfPnz+G7LBZhn79GPvtOdh87I2bktwiKNj+xycIzP+2aAClvJj7LN0fUPBKvyl+agH3VSUoIvuHO5/+krwAhLGBHNtN395hBeD1mvv5UmtPXwBYKoBrMPcEw5/iAdu7S6o+8gLKOOiyBTRvxaOL3RQkLi+BZICEvsxAHv5k5umvVfAvePiBiSEqQb1WJcD6FwiQTrTQVubb/QfR5bYLhnxAFiWggHZxDTAMcOUTWA088Rc+aOtpeYTcJXOgup6nSw3yPS5sB60+GPGZRhAlABeAroWPQMG8H4hP+ltc9TrXh8FJ2gBGBqF88rOTlc6fFAYtx2xdZs3n5VyPgcrG/94nFHbu/8v5vxz1gN6AhaAMlxYBaACnfRsvrcM3cCjXPohh7XvvjUQ7Vcv+0lmO1+XMrkA83xuFby9AiO3Zrf0h5uMEBstru35tFrqC0c8I0Aie348dMPe/z+aPBU1kgxNjaUCotYNvbcd1cYL0SIyivIAgCRLdohvMXXsIjq9tBCW9De5vUdT28I3tbvC1E6AotV47QF4DSM31f19IN26/x+JjMAVMA7QEvvdOwK9/rdeXPxYfv3cDi2Mfdn97cbYbsO24aXj6/cPA1NkmroQzqXu4wCSJDyNcoI5YeXHdTK209WRZVYqZPHvXWvER1nJ8Ge9JKtddevfOF4QPyhOsUas4otKGkKUmz3SlEK3LI4Tzg94R8tzAMtXBOgVjZbZdtZf2vlsTCgXDQ5BIgjzOpCNdTrkoOkdZ56asyengLiJikRy5aRak22bLpr5LXQghRY36YooB5xm3B73HJCMRfEeIO1/ghsxhuE2eRyJ+mDcsBnPpNTOp7SxwV/q6rZQtvb8ZU3/YIo9TippHMruVR+ewVrnzpk+3NWe1QTV5VXqLCZuzMszqsIwueYawy3jSzNh3J6oc83gnOMb6mmDnaggV0XblfKvVxiWTGHbaVFbYnaf9PV0T/ZZ8jDfWCbc7m1037ByTt1ujGKRhoGjGuaGCMC0tzlZ40ELhscqN9hwlw6O6MHtdkaTqdGhw6RhmGBm4OTMRbt/nAbzqgvsFO+6tyLgYIXfP2o24i5rz1KjZ+lY6zfXYR7eDqObRvT+4pS5u6e2N33GXfXpDs/SA0Lu40qUN++go2ZwP6qgQMIKQRiDD6MWryHwNlwmeOXHtMobIF3WGjpVfwdpqGDiFFPPrGp4n6jQ6wdzGMmvNveBJWJuJdJWd5k167orIli3OMkKE9OxJPSpIo11iW7IicoMfhfCUyy5+YE09xgZdENMbEyfi3SHEqyEbJStcqLqxh1mhg/6Grw/KlrlatGAg6qGd96yRa3QLrw+oa6wd1DJqIriI91K87LtxPYSlcMlQt0Hm4YrSe6ShcHYvx7cHmYmIwZ0wfiRyML4jbH3aPFp3v+YeSjdwGHI+sFLJMVq4rW/ZNCtbbX/ZOfzuOrBSaCAgKqeANy7+RrPNU3Qr5Nt8Prl17+Feb9UKJ0TBnnngocylFWipeHK9Dkj8LuL5sLKo+6V2dXKd8Y8b06auUs/ELrRNVXErQIdFu7dZYbMndmhxiGdltUlCeCqlm888zFtmNBltja4za7RmNgnPyKeNLznRaUMUqDCo5FHDvQ0fFkQu6JduyExn1Iy4PA6kIqlXcjWvc10qr91NUQtCwK+rpPLj+5TMtqQmOgaf5lwye0wPTcE/S+ex2aW9z+ADnlf9LpZNXuaEQVEisWu4/DSKojDj1A2VlU5B5cF9zFJhb+Sp3m2VemQI3kW8FI5Pw/FBxJwbu9YG5jNdkw9Rtmct6ZZJ8XVXN2M+PSjTbhWZorZN1BKIfG5Na0RUWgk8e9xwNiUWHevEXTsWZ16T1Yjfn+OGDcKiCCY5f4hTpW0kAU4CxkOGVruiVjDno9/VZrY6Chp+Gt0jeRbcA5UDikiRPcHsW3F7qkoBCydfQWgWLyjYku1G7UssP9PrrMyvt8uJMdOdwGLytqtS0tlhLWvgCu3pu8nYpYrWh0yItvvknvEmLmwUXMfEMJC6q945Xs820VTxx7uBKLXQlQOW7mQ5wMWpHEZ6i8QdTncFkxS6ije2q8SWYBmbVagMbn7vLmd6w1/OnIFlbdVGACH+rFLOrjYOM0dpBMal5dm7bXLVjOqtQIuTo5s2dUqle2+zMY1N+3TDHBJEIb3Q0CP6MJZByfH0Rp9p2explyLjwC67REF3Xni6awEhlsPBxWAsErIAFnZFR6qyt2OmZp9EaZtYLC5dIvp+v+mVFCH2dLdVmbfRoeqTYn/QdeXkH29rt8A6ESNLwxvklZFJuuo4OkakmxVaiuz2ZF/Iq0HKKlN7V0Yb8939iovJ3RxZ9I45fRwpiWVqCTPQWzQz1Lbkm9mTE2mniZK1Vw6BvCFqohDO951gauf1veTMoKAoP+U3LeKd5oZSTczWkJosUAWTkAiWcNLJ76nmmtr6cNrA8rw660mVNETO50c1xpK9S9Tz1kgZrz7rjH47K9s9cW5WOyddWYWKTqTfW94Y+HCBUuBrsb6lYuXxD2raGbcDduROQrvjTIYzG55NHAHnPW/esiKT8hg8atjNyGjhcXhIbTgpNFOVYnso644f6JbOktBcpfNKKVZmIpDFJaWoU9GPEdmZ07wmbjeZTM2Bbwr5qAstqH+H2qkXkueTYF+Ie5ULboR9Ai+NfIydbjITptW5IopdFt6zJEUUxiEqm+EbJOIuXW6AA7G+N7xKjwo1cBdMEvudkxzVRgiQoZA0xun6Gk/hUTknmlTBnVQhXN82RRgnbuvSMii2BtPoq8XToAnQSnlE6KsUHndNayZn5C5hvL5hBLMrbVMDKWzlxPEvPbFDNLEObDwW9/dqwsNRwV2s9Nbe7WhXjusRjGVhydU43tv6Iq6iU/hoRN5pXVk7XcPbqhWcgSsaGjmiCSN5VU2QHLdtpZbTpl3C7+XoypP5+bAXkcziVUfDCRsPvOOBTj3FHBtBU7HbxWkPgEBtFqtIlF+TpdjRq3pdJjUsdoMT6ke8SHjYuCLEavDnBtWc+cq1o9jhRwuVI1wnhSIUUY2MeI4vi13vHg34avcDjRU34qDXlCgVVyG56/JQbbkz9tg92CpiEuUopEnLMlvZvsYbDD0DoJtXxudsBhDzcL3TRENzQdLgM0GkHadS+0Ou32hpiOi1dov2VWjNHcx7V8C7tX5rYD+jQNxmL1/x6vlKqSM2VgjMEg6WNddzY4uOOe7Hk0DBcvvgsu5+FK2hlmhOAHQUxjju3HiyHNallnTDftdinDUEpuw5txUXK4EbnjVWxRhszyAHVTLlMPIIXaQsz/JXMH9o2rN65LWDEXFlophrfoufm8lOUru5NFEs9WDOT9uNeeAworf9CzvQJJBoTBJJbZrQ2zXldcsmydw+TvDhcfOGc4VFRsXhCXt2juO+lE7H08jzm86gqgYjQJvYTeW9Vc0qsvaZXQlsEqo1bEjJ/dD4tNPnRmi3t7ujr07lA6GQPuYUOw5XuiJsZCS5skcjwtN7MycnXxql03gwrQKxB26e2L3vb2KY6E4xh2Jrba8QNHVHHz2+K+tqHJte82KqMxgsTpGwxcFLWhKGzGMXEd5ZOmGHJiBsNcosQryr/n4eUHEj+1Spn/qcr9Nz6RWDlPaU/ZC2amDO9qCNh5E8Nebqsun3xrbYPKiOr1K1EkxFrI7OUDpjPLLy6OmRxMtw2mLIbDDUsaeLeAhYKjMZWNTUSx6as5x2q3jYnbnBN/UTuWp2m7lg3HTUosgBrUOPRzItr47bPXqhy8LboC1d5HXuCWZ7U+4wSexnsT1VRAwnK5sdUVK9jnREIuxUojctOpQCuSEPOw0LgsAZXPEh4zKmDkRZo5TsFUYeSRVR4dYlFrDDeb/ycnMWLtodQY663u8PBb5mNRBIPAXp9+a4cEtruF/Y+oDNJPHwktU032sljasiILbyYEfFHlUDrUXdWlGGx2wb1bDbl0eP2+EdX2zxwmHGxF8jhHI/HXY7PJ1RHS81y6rR7QPunIdP+Nau8+5jYslx3+8eZUbOCnMlClo/YE57TW0xOB/iqXwcMbs7ISbZEYj5UKLysS3n01G+rfY2eRFJNQ7Rw1oWSCUeDFzyE6KjLolUFUMd7vMT1vZnx+7ke7RxsiuzvQZZ7ZLxqDDKeZ9XcYsbcnurigRzS9zYDKpilKI3kLEeGyYi6UJsNNpuW+/atZe6t+lGRiV5LNoH2xIKhvZYFKtso9txLrpCFc+Oczj2IBm34ZjPOeML2iEP2nRvsOvaKKsLO8Lsah2y5ylnYY6hW7vlUIIpDPrIHFWDAW+a2KY90gqpHBsi2ottodSGZWYW2yGpnOePYIcplNVveWeNnCjCy7fNg2vYrPBPsuYRiuSp2zHCmmbT2TtYC0OUyzGkGM73bn8NN7Rsbw+2ulR6W0SlLIcaW8M6oStenjz4gJmSMz0Ipj5cLxx4Y0kQjsC0pmYG8GLn0pMlE55a3La5jnXUnVGJjLA8m5hBP7277G9rxeE5MfMvY7Oiw9CRQc/aRrqI94x1bIbpRI2pe+FHL6bvUQFIO3k8pOGulCU/wDzscNzs1XXPnHesqalkPwVWH2ncqtZPgyffzPV0cnh4zEzbGaaKCMOVp7vH9uRpcro+SLWjIRHBDNmlF7l8PFgq5crHJCvlCfSBJ6XoUza7pQlmupKYrs628Mi4kIEda0POrqRziYWvDuqFbnoSP1S5eSjvB3xP8Hw3yMdTk5SWZgEStu0QxeiC9YMNwqYgB6a3XTqT9YDmPSChZO4ljPG6K8uhPu2qMMLuy+q+8bqeaGYNP/KntLhWiGutNb/sDHdt3hEYtPN+GlE0Mq+EraTkXWdct4NXnlkZMeVddVFdLIj0DvTwcHzE1smY+c4Ew+zElhlxZA/cIJ1uTG6tJFRBynV4W1usLg5K4dLeDNvUer/unDVby2c6LxX0elm72oGvD41XUCsnumN17fM7AN6QKdodmeWh14N334bfsusQVfzRS3rLhbsoEnsniUa9sPLCCnbKHvRdx3V3SW5RQ3WJuB6nKY5EGS1TzlshBVphapOi3hztNUes+xNiiD2uKnR8XRHuPjv4NdKA0orskzrm2/u08vGHTeBuSJr3QJmthPC8U0MwyV0iVf7Mq3h4OZ6ryK/Vu3TVnNVaLs0jH21BcNWtihxPCji0h7Chafo/Xz69LHflH3dW/+Z3l+Vm5//tluj9pqfsgb7CBQp/fVmudL88dX35d8p/+/RSuzFQ/X6p1WRd+LzrqqqmLWv/9f1i6/VfLraa6f23ifcfwr7fRC0XrU+Ff715+vTycRW/3OL9uKVchLi13bpRZXvgIbKb1y5ejHn+Bva8bwMGAZP++B/Trc0nJRwAAA== -->
