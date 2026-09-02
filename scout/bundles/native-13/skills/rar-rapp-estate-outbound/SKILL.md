---
name: "rar-rapp-estate-outbound"
description: "Write a signed neighborhood event to the operator's outbound lane on disk. Returns the file path + a publish hint. Refuses if the event is missing sig/pub/from or if the neighborhood rappid is empty."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/estate_outbound", "rar_sha256": "f4f677f2bba5a12b5967fc39a8d0bdb1afad7ad4de57d32d2df8a80dd2bf1b32", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "estate_outbound_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/estate-outbound:487da63be5cb9b530abc7866f28748842003ff097f54b54ebabb879d733b0cb2", "kind": "skill"}, "version": "1.0.2", "author": "RAPP", "tags": ["estate", "outbound", "federation", "neighborhood", "publish"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/estate_outbound`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `estate_outbound_agent.py` is
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
