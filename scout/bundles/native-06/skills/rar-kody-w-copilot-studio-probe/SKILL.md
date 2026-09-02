---
name: "rar-kody-w-copilot-studio-probe"
description: "Send a message to a DEPLOYED Microsoft Copilot Studio agent over Direct Line and return its reply. Use to test whether a published agent routes and answers correctly (e.g. 'what are the top Hacker News stories?'). Requires COPILOT_DIRECTLINE_TOKEN_ENDPOINT or COPILOT_DIRECTLINE_SECRET."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_probe_agent", "rar_sha256": "59b3c5cdb2228e333e20ea3ef89c41dac9bb8f12a940b68d591619726d2a0367", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_probe_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/copilot-studio-probe:2c9352fc32a3f9772652ada7236b2c98d512048a1d434bb7a46de226ebc53803", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["copilot-studio", "direct-line", "probe", "testing", "integration", "m365"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/copilot_studio_probe_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_probe_agent.py` is
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
