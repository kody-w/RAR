---
name: "rar-rapp-estate-outbound"
description: "Write a signed neighborhood event to the operator's outbound lane on disk. Returns the file path + a publish hint. Refuses if the event is missing sig/pub/from or if the neighborhood rappid is empty."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/estate_outbound", "rar_sha256": "f4f677f2bba5a12b5967fc39a8d0bdb1afad7ad4de57d32d2df8a80dd2bf1b32", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "RAPP", "tags": ["estate", "outbound", "federation", "neighborhood", "publish"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/estate_outbound`. The original RAPP
agent is preserved byte-for-byte in `estate_outbound_agent.py` and in the RCI capsule.

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

estate_outbound_agent.py — stage a signed event for federation roll-up.

The companion to commons_post_agent (and any future per-neighborhood post
agent): commons_post composes + the host signs, then this agent writes
the signed event to the operator's outbound lane (Article XLVIII), where
each neighborhood's federation roll-up can find it on its beat.

Outbound lane layout (on disk):

  ~/.brainstem/outbound/<sanitized-neighborhood-rappid>/<event-filename>.json

Filename:   <sha256(pub_jwk_canonical)[:16]>-<ts:replace ':' with '-'>.json
            (matches events/SCHEMA.md so the federation roll-up can union
             without renaming.)

The agent does NOT push the lane to a public estate repo — pushing is the
operator's responsibility (`git -C ~/.brainstem push estate-outbound main`
or equivalent). The agent prints the hint, surfaces what was staged, and
returns the path so the host UI can wire a "publish" button.

Future companion: an `estate_publish_agent` that wraps `git add/commit/push`
against the operator's public-estate remote, with provenance logged into
`~/.brainstem/bonds.json` per CONSTITUTION Article XLVIII.

Runs in any host that exposes BasicAgent (Pyodide tether, server brainstem,
swarm) — pure stdlib except for the (already-loaded) BasicAgent base.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "event": {
      "description": "The signed event object. Must include schema, from, ts, sig, pub at minimum.",
      "type": "object"
    },
    "neighborhood_rappid": {
      "description": "Target neighborhood's rappid, consolidated form rappid:@<owner>/<slug>:<64hex>. Determines which subdir of ~/.brainstem/outbound/ receives the event.",
      "type": "string"
    }
  },
  "required": [
    "neighborhood_rappid",
    "event"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `estate_outbound_agent.py` and embedded as the fenced Python below (sha256 f4f677f2bba5a12b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `estate_outbound_agent.py` first:

```bash
python3 estate_outbound_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 estate_outbound_agent.py   # or on stdin
python3 estate_outbound_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""estate_outbound_agent.py — stage a signed event for federation roll-up.

The companion to commons_post_agent (and any future per-neighborhood post
agent): commons_post composes + the host signs, then this agent writes
the signed event to the operator's outbound lane (Article XLVIII), where
each neighborhood's federation roll-up can find it on its beat.

Outbound lane layout (on disk):

  ~/.brainstem/outbound/<sanitized-neighborhood-rappid>/<event-filename>.json

Filename:   <sha256(pub_jwk_canonical)[:16]>-<ts:replace ':' with '-'>.json
            (matches events/SCHEMA.md so the federation roll-up can union
             without renaming.)

The agent does NOT push the lane to a public estate repo — pushing is the
operator's responsibility (`git -C ~/.brainstem push estate-outbound main`
or equivalent). The agent prints the hint, surfaces what was staged, and
returns the path so the host UI can wire a "publish" button.

Future companion: an `estate_publish_agent` that wraps `git add/commit/push`
against the operator's public-estate remote, with provenance logged into
`~/.brainstem/bonds.json` per CONSTITUTION Article XLVIII.

Runs in any host that exposes BasicAgent (Pyodide tether, server brainstem,
swarm) — pure stdlib except for the (already-loaded) BasicAgent base.
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:  # type: ignore
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/estate_outbound",
    "version": "1.0.2",
    "display_name": "EstateOutbound",
    "description": (
        "Writes an already-signed neighborhood event into ~/.brainstem/outbound/ for federation roll-up; pushing to the estate repo stays manual."
    ),
    "author": "RAPP",
    "tags": ["estate", "outbound", "federation", "neighborhood", "publish"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "neighborhood_rappid": "rappid:@rapp-commons/origin:3727bc584708e539d69792713fbb200688c634744cce2d9614fa5aefd4ff295f",
            "event": {"schema": "rapp-commons-event/1.0", "kind": "hello", "from": "...", "ts": "...", "body": "...", "sig": "...", "pub": {}}
        }
    },
}


def _outbound_root() -> pathlib.Path:
    return pathlib.Path(os.path.expanduser("~/.brainstem/outbound"))


def _sanitize_rappid(rappid: str) -> str:
    """Filesystem-safe slug for a rappid. Reversible enough for human reads;
    matches the rule used by the planted neighborhood's own naming.
    """
    return re.sub(r"[^A-Za-z0-9._-]+", "_", rappid)[:200]


def _canonical_json(d: dict) -> str:
    return json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _fingerprint(pub_jwk: dict) -> str:
    canonical = _canonical_json(pub_jwk)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _ts_safe(ts: str) -> str:
    return ts.replace(":", "-")


class EstateOutboundAgent(BasicAgent):
    def __init__(self):
        self.name = "StageOutboundEvent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Write a signed neighborhood event to the operator's outbound "
                "lane on disk. Returns the file path + a publish hint. Refuses "
                "if the event is missing sig/pub/from or if the neighborhood "
                "rappid is empty."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "neighborhood_rappid": {
                        "type": "string",
                        "description": "Target neighborhood's rappid, consolidated form rappid:@<owner>/<slug>:<64hex>. Determines which subdir of ~/.brainstem/outbound/ receives the event.",
                    },
                    "event": {
                        "type": "object",
                        "description": "The signed event object. Must include schema, from, ts, sig, pub at minimum.",
                    },
                },
                "required": ["neighborhood_rappid", "event"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        nbhd = (kwargs.get("neighborhood_rappid") or "").strip()
        event = kwargs.get("event")

        if not nbhd:
            return json.dumps({"error": "neighborhood_rappid is required"})
        if not isinstance(event, dict):
            return json.dumps({"error": "event must be an object"})
        for required in ("schema", "from", "ts", "sig", "pub"):
            if required not in event:
                return json.dumps({"error": f"event missing required field '{required}'"})
        if not isinstance(event["pub"], dict):
            return json.dumps({"error": "event.pub must be a JWK object"})

        # Filename per events/SCHEMA.md so the federation roll-up unions
        # without renaming.
        fp = _fingerprint(event["pub"])[:16]
        ts_safe = _ts_safe(str(event["ts"]))
        filename = f"{fp}-{ts_safe}.json"

        outbound_dir = _outbound_root() / _sanitize_rappid(nbhd)
        try:
            outbound_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            return json.dumps({"error": f"could not create {outbound_dir}: {e}"})

        out_path = outbound_dir / filename
        try:
            out_path.write_text(_canonical_json(event) + "\n", encoding="utf-8")
        except Exception as e:
            return json.dumps({"error": f"could not write {out_path}: {e}"})

        return json.dumps({
            "ok": True,
            "staged_at": str(out_path),
            "neighborhood": nbhd,
            "filename": filename,
            "publish_hints": [
                (
                    "To publish: commit your outbound lane to the operator's "
                    "public-estate repo and push. The neighborhood's "
                    "federation roll-up pulls outbound on its beat (commons "
                    "default: every 10 minutes via .github/workflows/federate.yml)."
                ),
                (
                    "If you don't have a public-estate repo yet, see "
                    "kody-w/RAPP/pages/docs/ESTATE_SPEC.md for the two-tier "
                    "spec (Article XLVIII)."
                ),
                (
                    f"Quick local check: cat '{out_path}' | jq ."
                ),
            ],
        }, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
