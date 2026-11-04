---
name: "rar-kody-w-copilot-studio-probe"
description: "Send a message to a DEPLOYED Microsoft Copilot Studio agent over Direct Line and return its reply. Use to test whether a published agent routes and answers correctly (e.g. 'what are the top Hacker News stories?'). Requires COPILOT_DIRECTLINE_TOKEN_ENDPOINT or COPILOT_DIRECTLINE_SECRET."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/copilot_studio_probe_agent", "rar_sha256": "6d84b5cefb5d1a032b208555020f96756bba3c6c0790b1d8544abafc868e1a99", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["copilot-studio", "direct-line", "probe", "testing", "integration", "m365"]}
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
