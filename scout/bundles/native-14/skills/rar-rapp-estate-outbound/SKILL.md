---
name: "rar-rapp-estate-outbound"
description: "Write a signed neighborhood event to the operator's outbound lane on disk. Returns the file path + a publish hint. Refuses if the event is missing sig/pub/from or if the neighborhood rappid is empty."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/estate_outbound", "rar_sha256": "a918d6922c3ac93566aa0de306edee4caaba38b91d5b4818a00d338ab5c84861", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "RAPP", "tags": ["estate", "outbound", "federation", "neighborhood", "publish"]}
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
