---
name: "rar-rapp-estate-outbound"
description: "Write a signed neighborhood event to the operator's outbound lane on disk. Returns the file path + a publish hint. Refuses if the event is missing sig/pub/from or if the neighborhood rappid is empty."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/estate_outbound", "rar_sha256": "a918d6922c3ac93566aa0de306edee4caaba38b91d5b4818a00d338ab5c84861", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "RAPP", "tags": ["estate", "outbound", "federation", "neighborhood", "publish"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `estate_outbound_agent.py` and embedded as the fenced Python below (sha256 a918d6922c3ac935…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `estate_outbound_agent.py` first:

```bash
python3 estate_outbound_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 estate_outbound_agent.py   # or on stdin
python3 estate_outbound_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/estate_outbound_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/estate_outbound_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/estate_outbound/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
