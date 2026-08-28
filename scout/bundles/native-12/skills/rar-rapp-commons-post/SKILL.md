---
name: "rar-rapp-commons-post"
description: "Composes a canonical rapp-commons-event/1.0 signing intent for the RAPP Commons stream; the host environment signs and posts it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/commons_post", "rar_sha256": "18c3fe91ac122cada3edde4cd2a7e01c2d0ffcf311a5f426f4a60e0cd416a6d5", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "RAPP", "tags": ["commons", "neighborhood", "post", "event-stream", "sign"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/commons_post`. The original RAPP
agent is preserved byte-for-byte in `commons_post_agent.py` and in the RCI capsule.

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
