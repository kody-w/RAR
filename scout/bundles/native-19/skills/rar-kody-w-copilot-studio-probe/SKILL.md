---
name: "rar-kody-w-copilot-studio-probe"
description: "Send a message to a DEPLOYED Microsoft Copilot Studio agent over Direct Line and return its reply. Use to test whether a published agent routes and answers correctly (e.g. 'what are the top Hacker News stories?'). Requires COPILOT_DIRECTLINE_TOKEN_ENDPOINT or COPILOT_DIRECTLINE_SECRET."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_probe_agent", "rar_sha256": "59b3c5cdb2228e333e20ea3ef89c41dac9bb8f12a940b68d591619726d2a0367", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["copilot-studio", "direct-line", "probe", "testing", "integration", "m365"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/copilot_studio_probe_agent`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_probe_agent.py` and in the RCI capsule.

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

Copilot Studio Probe — drive a DEPLOYED Microsoft Copilot Studio agent over
Direct Line, turning the brainstem into a test client for any published agent.

Given a question, it opens a Direct Line conversation with the deployed agent,
sends the message, waits for the bot to finish replying, and returns the text.
Use it to verify that a deployed agent routes and answers correctly — the runtime
"probe / verify" leg that complements the RAPP -> Copilot Studio forge and deploy
agents (forge -> deploy -> probe).

Connection (no server-side secret needed for a "No authentication" agent):
  set COPILOT_DIRECTLINE_TOKEN_ENDPOINT to the agent's
  Channels > Mobile app > Token Endpoint URL  (or pass token_endpoint=...).
  Alternatively set COPILOT_DIRECTLINE_SECRET (Azure Bot > Direct Line, or the
  Copilot Studio "Web channel security" secret) or pass secret=...
No credentials are stored in this file — everything is read from the environment
or passed at call time.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "query": {
      "description": "The message to send to the deployed Copilot Studio agent.",
      "type": "string"
    },
    "quiet_seconds": {
      "description": "Stop waiting after the bot is silent this long (default 5).",
      "type": "number"
    },
    "secret": {
      "description": "Direct Line secret (else env COPILOT_DIRECTLINE_SECRET).",
      "type": "string"
    },
    "token_endpoint": {
      "description": "Direct Line token endpoint URL (else env COPILOT_DIRECTLINE_TOKEN_ENDPOINT).",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_probe_agent.py` and embedded as the fenced Python below (sha256 59b3c5cdb2228e33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_probe_agent.py` first:

```bash
python3 copilot_studio_probe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_probe_agent.py   # or on stdin
python3 copilot_studio_probe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Copilot Studio Probe — drive a DEPLOYED Microsoft Copilot Studio agent over
Direct Line, turning the brainstem into a test client for any published agent.

Given a question, it opens a Direct Line conversation with the deployed agent,
sends the message, waits for the bot to finish replying, and returns the text.
Use it to verify that a deployed agent routes and answers correctly — the runtime
"probe / verify" leg that complements the RAPP -> Copilot Studio forge and deploy
agents (forge -> deploy -> probe).

Connection (no server-side secret needed for a "No authentication" agent):
  set COPILOT_DIRECTLINE_TOKEN_ENDPOINT to the agent's
  Channels > Mobile app > Token Endpoint URL  (or pass token_endpoint=...).
  Alternatively set COPILOT_DIRECTLINE_SECRET (Azure Bot > Direct Line, or the
  Copilot Studio "Web channel security" secret) or pass secret=...
No credentials are stored in this file — everything is read from the environment
or passed at call time.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/copilot_studio_probe_agent",
    "version": "1.0.1",
    "display_name": "CopilotStudioProbe",
    "description": "Sends a message to a deployed Copilot Studio agent over Direct Line and returns the bot's reply for runtime verification.",
    "author": "kody-w",
    "tags": ["copilot-studio", "direct-line", "probe", "testing", "integration", "m365"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": ["COPILOT_DIRECTLINE_TOKEN_ENDPOINT", "COPILOT_DIRECTLINE_SECRET"],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import os
import time
import urllib.error
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:  # pragma: no cover
        class BasicAgent:  # type: ignore
            def __init__(self, name, metadata):
                self.name = name
                self.metadata = metadata

DL_BASE = "https://directline.botframework.com/v3/directline"


def _http(method, url, token=None, body=None, timeout=40):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8", "replace")
            return r.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        return e.code, {"_error": e.read().decode("utf-8", "replace")[:300]}
    except Exception as e:  # noqa: BLE001
        return 0, {"_error": str(e)}


class CopilotStudioProbeAgent(BasicAgent):
    def __init__(self):
        self.name = "CopilotStudioProbe"
        self.metadata = {
            "name": self.name,
            "description": (
                "Send a message to a DEPLOYED Microsoft Copilot Studio agent over Direct "
                "Line and return its reply. Use to test whether a published agent routes "
                "and answers correctly (e.g. 'what are the top Hacker News stories?'). "
                "Requires COPILOT_DIRECTLINE_TOKEN_ENDPOINT or COPILOT_DIRECTLINE_SECRET."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The message to send to the deployed Copilot Studio agent."},
                    "token_endpoint": {"type": "string", "description": "Direct Line token endpoint URL (else env COPILOT_DIRECTLINE_TOKEN_ENDPOINT)."},
                    "secret": {"type": "string", "description": "Direct Line secret (else env COPILOT_DIRECTLINE_SECRET)."},
                    "quiet_seconds": {"type": "number", "description": "Stop waiting after the bot is silent this long (default 5)."},
                },
                "required": ["query"],
            },
        }
        super().__init__(self.name, self.metadata)

    def _get_token(self, token_endpoint, secret):
        if token_endpoint:
            code, r = _http("GET", token_endpoint)
            if code == 200 and r.get("token"):
                return r["token"], None
            return None, "token endpoint HTTP %s: %s" % (code, r.get("_error") or r)
        if secret:
            code, r = _http("POST", DL_BASE + "/tokens/generate", token=secret)
            if code == 200 and r.get("token"):
                return r["token"], None
            return None, "token generate HTTP %s: %s" % (code, r.get("_error") or r)
        return None, ("no connection: set COPILOT_DIRECTLINE_TOKEN_ENDPOINT (or pass "
                      "token_endpoint=), or COPILOT_DIRECTLINE_SECRET (or secret=).")

    def perform(self, **kwargs):
        query = (kwargs.get("query") or "").strip()
        if not query:
            return "CopilotStudioProbe: provide a `query` to send to the deployed agent."
        token_endpoint = kwargs.get("token_endpoint") or os.environ.get("COPILOT_DIRECTLINE_TOKEN_ENDPOINT")
        secret = kwargs.get("secret") or os.environ.get("COPILOT_DIRECTLINE_SECRET")
        quiet = float(kwargs.get("quiet_seconds", 5) or 5)

        token, err = self._get_token(token_endpoint, secret)
        if err:
            return "CopilotStudioProbe: " + err

        code, r = _http("POST", DL_BASE + "/conversations", token=token)
        if code not in (200, 201) or not r.get("conversationId"):
            return "CopilotStudioProbe: start conversation failed (HTTP %s): %s" % (code, r.get("_error") or r)
        conv = r["conversationId"]

        _http("POST", "%s/conversations/%s/activities" % (DL_BASE, conv), token=token,
              body={"type": "message", "from": {"id": "brainstem-probe"}, "text": query, "textFormat": "plain"})

        replies, watermark, deadline, last = [], None, time.time() + 45, time.time()
        while time.time() < deadline:
            url = "%s/conversations/%s/activities" % (DL_BASE, conv)
            if watermark is not None:
                url += "?watermark=%s" % watermark
            code, r = _http("GET", url, token=token)
            if code == 200:
                watermark = r.get("watermark", watermark)
                for a in r.get("activities", []):
                    if a.get("type") == "message" and (a.get("from") or {}).get("role") == "bot":
                        t = (a.get("text") or "").strip()
                        if t:
                            replies.append(t)
                            last = time.time()
            if replies and (time.time() - last) >= quiet:
                break
            time.sleep(1.5)

        if not replies:
            return "CopilotStudioProbe: sent '%s' but the agent returned no reply within the timeout." % query
        return "Deployed Copilot Studio agent replied:\n\n" + "\n\n".join(replies)


if __name__ == "__main__":
    import sys
    a = CopilotStudioProbeAgent()
    print(a.perform(query=(sys.argv[1] if len(sys.argv) > 1 else "what are the top Hacker News stories?")))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
