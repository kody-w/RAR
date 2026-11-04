---
name: "rar-kody-w-copilot-studio-probe"
description: "Send a message to a DEPLOYED Microsoft Copilot Studio agent over Direct Line and return its reply. Use to test whether a published agent routes and answers correctly (e.g. 'what are the top Hacker News stories?'). Requires COPILOT_DIRECTLINE_TOKEN_ENDPOINT or COPILOT_DIRECTLINE_SECRET."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_probe_agent", "rar_sha256": "6d84b5cefb5d1a032b208555020f96756bba3c6c0790b1d8544abafc868e1a99", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["copilot-studio", "direct-line", "probe", "testing", "integration", "m365"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_probe_agent.py` and embedded as the fenced Python below (sha256 6d84b5cefb5d1a03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_probe_agent.py` first:

```bash
python3 copilot_studio_probe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_probe_agent.py   # or on stdin
python3 copilot_studio_probe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/copilot_studio_probe_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_probe_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/copilot_studio_probe_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
