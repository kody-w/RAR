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