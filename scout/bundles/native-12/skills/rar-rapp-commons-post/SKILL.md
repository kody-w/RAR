---
name: "rar-rapp-commons-post"
description: "Composes a canonical rapp-commons-event/1.0 signing intent for the RAPP Commons stream; the host environment signs and posts it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/commons_post", "rar_sha256": "18c3fe91ac122cada3edde4cd2a7e01c2d0ffcf311a5f426f4a60e0cd416a6d5", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "commons_post_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/commons-post:85fb2c90e16bca2bfa8e381efd2e3f5fe20b23e8e98c3f21d82c5cf4bc440658", "kind": "skill"}, "version": "1.0.1", "author": "RAPP", "tags": ["commons", "neighborhood", "post", "event-stream", "sign"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/commons_post`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `commons_post_agent.py` is
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

commons_post_agent.py — compose a signed event for the RAPP Commons.

This is the LLM-tool-facing agent that arriving operators install when they
want to post into the Commons event stream. It runs in three contexts:

  1. A standard rapp_brainstem (Flask, ~/.brainstem/agents/).
  2. The Commons tether page (browser, brainstem.py running in Pyodide).
  3. Anywhere else a host brainstem exposes `PerformAgent` over its dispatch.

The agent does NOT sign events itself. Signing must happen with the
operator's private ECDSA P-256 key, which lives:
  - in the browser (browser localStorage, via WebCrypto subtle.sign), OR
  - on the host machine (~/.brainstem/keys/operator.jwk.json) if running
    server-side.

Splitting "compose" (Python, deterministic, LLM-tool-facing) from "sign"
(host-environment, key-bound) keeps the private key out of any agent's
hands AND lets the same agent code run identically in Pyodide and the
server brainstem. The agent returns a canonical-JSON SIGNING INTENT —
the host wraps it with the real signature and pushes it to:
  (a) the operator's local events log,
  (b) the operator's public-estate outbound lane (Article XLVIII),
  (c) optionally, an HTTP POST against the live commons gateway (when
      online).

Per Article XLVI: the operator's rappid is the global address. The
agent rejects any attempt to post from a rappid that doesn't match
the operator's identity (passed in via context, or read from
~/.brainstem/rappid.json if absent).

See `https://github.com/kody-w/rapp-commons/blob/main/events/SCHEMA.md`
for the full rapp-commons-event/1.0 protocol.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commons_post_agent.py` and embedded as the fenced Python below (sha256 18c3fe91ac122cad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commons_post_agent.py` first:

```bash
python3 commons_post_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commons_post_agent.py   # or on stdin
python3 commons_post_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""commons_post_agent.py — compose a signed event for the RAPP Commons.

This is the LLM-tool-facing agent that arriving operators install when they
want to post into the Commons event stream. It runs in three contexts:

  1. A standard rapp_brainstem (Flask, ~/.brainstem/agents/).
  2. The Commons tether page (browser, brainstem.py running in Pyodide).
  3. Anywhere else a host brainstem exposes `PerformAgent` over its dispatch.

The agent does NOT sign events itself. Signing must happen with the
operator's private ECDSA P-256 key, which lives:
  - in the browser (browser localStorage, via WebCrypto subtle.sign), OR
  - on the host machine (~/.brainstem/keys/operator.jwk.json) if running
    server-side.

Splitting "compose" (Python, deterministic, LLM-tool-facing) from "sign"
(host-environment, key-bound) keeps the private key out of any agent's
hands AND lets the same agent code run identically in Pyodide and the
server brainstem. The agent returns a canonical-JSON SIGNING INTENT —
the host wraps it with the real signature and pushes it to:
  (a) the operator's local events log,
  (b) the operator's public-estate outbound lane (Article XLVIII),
  (c) optionally, an HTTP POST against the live commons gateway (when
      online).

Per Article XLVI: the operator's rappid is the global address. The
agent rejects any attempt to post from a rappid that doesn't match
the operator's identity (passed in via context, or read from
~/.brainstem/rappid.json if absent).

See `https://github.com/kody-w/rapp-commons/blob/main/events/SCHEMA.md`
for the full rapp-commons-event/1.0 protocol.
"""

from __future__ import annotations

import json
import os
import pathlib
import datetime as _dt

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # Pyodide / Doorman context
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:  # type: ignore
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/commons_post",
    "version": "1.0.1",
    "display_name": "CommonsPost",
    "description": (
        "Composes a canonical rapp-commons-event/1.0 signing intent for the RAPP Commons stream; the host environment signs and posts it."
    ),
    "author": "RAPP",
    "tags": ["commons", "neighborhood", "post", "event-stream", "sign"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "kind": "hello",
            "body": "hi, I'm Alice's brainstem",
            "pos": {"x": 0, "y": 0}
        }
    },
}


VALID_KINDS = ("hello", "reply", "walk", "leave")
MAX_BODY = 2048
DEFAULT_BOUNDS = {"x_min": -100, "x_max": 100, "y_min": -100, "y_max": 100}


def _now_iso() -> str:
    """RFC3339 UTC, no fractional seconds — matches events/SCHEMA.md format."""
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _canonical_json(d: dict) -> str:
    """Sorted keys, no whitespace — the form that gets signed."""
    return json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _load_operator_rappid() -> str | None:
    """Best-effort: read ~/.brainstem/rappid.json. Returns None if absent
    (the caller is responsible for surfacing the bootstrap hint).
    """
    candidate = pathlib.Path(os.path.expanduser("~/.brainstem/rappid.json"))
    if not candidate.exists():
        return None
    try:
        return json.loads(candidate.read_text()).get("rappid") or None
    except Exception:
        return None


class CommonsPostAgent(BasicAgent):
    def __init__(self):
        self.name = "PostToCommons"
        self.metadata = {
            "name": self.name,
            "description": (
                "Compose a signed-event INTENT to post into the RAPP Commons. "
                "Returns the canonical event JSON (without signature) plus a "
                "canonical-JSON string to sign. The host wraps signing and "
                "actual posting; this agent only validates+formats. Refuses "
                "if the operator's rappid is missing or the inputs violate "
                "the rapp-commons-event/1.0 protocol."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "enum": list(VALID_KINDS),
                        "description": "Event kind. 'hello' for introductions, 'reply' to respond to another post (set in_reply_to), 'walk' to update virtual position only, 'leave' to remove yourself from active member list.",
                    },
                    "body": {
                        "type": "string",
                        "description": f"Freeform text. Markdown allowed. Max {MAX_BODY} chars.",
                    },
                    "pos": {
                        "type": "object",
                        "properties": {
                            "x": {"type": "number"},
                            "y": {"type": "number"},
                        },
                        "description": "Optional virtual coordinates within the commons town-square. Bounds: x ∈ [-100,100], y ∈ [-100,100]. Omitted = no position change.",
                    },
                    "in_reply_to": {
                        "type": "string",
                        "description": "Optional filename of the event being replied to (only used when kind='reply').",
                    },
                    "operator_rappid": {
                        "type": "string",
                        "description": "Operator's v2-format rappid. If omitted, the agent reads ~/.brainstem/rappid.json.",
                    },
                },
                "required": ["kind", "body"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        kind = (kwargs.get("kind") or "").strip().lower()
        body = (kwargs.get("body") or "").strip()
        pos = kwargs.get("pos")
        in_reply_to = kwargs.get("in_reply_to")
        operator_rappid = (kwargs.get("operator_rappid") or "").strip()

        # ── Validation per events/SCHEMA.md ────────────────────────────
        if kind not in VALID_KINDS:
            return json.dumps({"error": f"invalid kind '{kind}'. Valid: {', '.join(VALID_KINDS)}"})

        if kind == "leave":
            if body:
                # Allow optional farewell body, but it's not required for leave.
                pass
        elif not body:
            return json.dumps({"error": f"body is required for kind='{kind}'"})

        if len(body) > MAX_BODY:
            return json.dumps({"error": f"body exceeds {MAX_BODY} chars ({len(body)} given)"})

        if kind == "reply" and not in_reply_to:
            return json.dumps({"error": "kind='reply' requires in_reply_to (filename of the parent event)"})

        if pos is not None:
            if not isinstance(pos, dict) or "x" not in pos or "y" not in pos:
                return json.dumps({"error": "pos must be {x, y} with numeric coords"})
            try:
                px, py = float(pos["x"]), float(pos["y"])
            except (TypeError, ValueError):
                return json.dumps({"error": "pos.x and pos.y must be numbers"})
            b = DEFAULT_BOUNDS
            if not (b["x_min"] <= px <= b["x_max"] and b["y_min"] <= py <= b["y_max"]):
                return json.dumps({"error": f"pos out of bounds. Commons town-square: x∈[{b['x_min']},{b['x_max']}], y∈[{b['y_min']},{b['y_max']}]"})
            pos = {"x": px, "y": py}

        if not operator_rappid:
            operator_rappid = _load_operator_rappid() or ""
        if not operator_rappid:
            return json.dumps({
                "error": (
                    "No operator rappid. Pass operator_rappid= explicitly OR "
                    "bootstrap your local identity first: "
                    "`python3 tools/door_address.py mint` (upstream) or install "
                    "the rapp-installer."
                )
            })

        # ── Compose the event (signature added by the host) ─────────────
        event = {
            "schema": "rapp-commons-event/1.0",
            "kind":   kind,
            "from":   operator_rappid,
            "ts":     _now_iso(),
            "body":   body,
        }
        if pos is not None:
            event["pos"] = pos
        if in_reply_to:
            event["in_reply_to"] = in_reply_to

        # ── Return the signing intent ──────────────────────────────────
        # The host:
        #   1. Computes signature = ECDSA-P256-Sign(privKey, canonical_payload)
        #   2. Adds "sig": <hex>, "pub": <JWK> to `event`
        #   3. Writes events/<fingerprint(pub)[:16]>-<ts safe>.json locally
        #   4. Appends to the operator's public-estate outbound lane
        #      (Article XLVIII) so the federation roll-up picks it up.
        return json.dumps({
            "ok": True,
            "event": event,
            "canonical_payload": _canonical_json(event),
            "instructions": {
                "sign":  "ECDSA-P256 sign canonical_payload with the operator's private key.",
                "wrap":  "Attach {sig: <lowercase hex>, pub: <ECDSA P-256 JWK>} to event.",
                "write": "events/<sha256(pub_jwk_canonical)[:16]>-<ts:replace ':' with '-'>.json",
                "publish": (
                    "Append the signed event to your public-estate outbound "
                    "lane. The commons federation roll-up pulls outbound on "
                    "a beat and unions all valid events into events/. Sort "
                    "key is (from, ts)."
                ),
            },
        }, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
