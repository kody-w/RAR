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
    "version": "1.0.0",
    "display_name": "EstateOutbound",
    "description": (
        "Stage a signed neighborhood event in the operator's outbound lane "
        "(Article XLVIII). The companion to commons_post — once an event is "
        "signed, this writes it to ~/.brainstem/outbound/<rappid>/ so the "
        "neighborhood's federation roll-up can pull it on its beat. Does NOT "
        "push to the operator's public-estate repo — that's a separate step "
        "the operator owns (gh CLI or a future estate_publish_agent)."
    ),
    "author": "RAPP",
    "tags": ["estate", "outbound", "federation", "neighborhood", "publish"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "neighborhood_rappid": "rappid:v2:neighborhood:@rapp-commons/origin:3929ce90ebe97fe2a95432e9f647f3a3@github.com/kody-w/rapp-commons",
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
                        "description": "Target neighborhood's v2 rappid. Determines which subdir of ~/.brainstem/outbound/ receives the event.",
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
