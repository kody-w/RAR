# ── RAPP layer ticket ── @kody-w/own_ai
# What: Layer: own_ai — the unchanged grail thinks with the AI already on this device, with no sign-in.
# Add in chat: update my Brainstem with @kody-w/own_ai
# Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
# Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
#   confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
#   Label: own_ai. Health alone is not proof; test /chat and /chat/stream.
# Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
#   For a part added individually in chat, ask to remove its id or undo that shape change.
# Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1
# ── End RAPP layer ticket
"""Layer: own_ai — the unchanged grail thinks with the AI already on this device, with no sign-in.

The kernel knows one provider: the endpoint it is handed by its sign-in exchange, which speaks the OpenAI
chat-completions wire. When BRAINSTEM_AI names a command that runs the person's own AI for one message
(for example `claude -p`), this layer answers that exchange itself and sends every chat-completions call
to that command instead. The kernel file is untouched: soul, agents, memory, tool calls, /chat and the
web page all work as they do on any Brainstem. BRAINSTEM_AI unset: this layer does nothing.

Status: staging. Not seeded: the person turns it on. Proven on a Mac with one AI so far.

Env: BRAINSTEM_AI   the one-message command; the prompt is added as its last argument
     BRAINSTEM_AI_STDIN=1   send the prompt on standard input instead (for long conversations)
"""
import json
import os
import shlex
import subprocess
import tempfile
import time

import requests

WRAPS = {"requests.get", "requests.post"}

# Engines this was really run on: /chat and /chat/stream answered, a tool was called, a memory was stored
# and recalled in a new session, all through this layer with no sign-in (2026-11-10, Mac, `claude -p`).
PROVEN_GRAIL = {
    "84d86c3b29e111a2c1d1c68b67230e057261f7fc8a191dfefc0e3b26d6fcc99c",  # 0.6.17 (installed on the test Mac)
    "bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4",  # 0.6.16 (public rapp-installer main)
}

AI = os.environ.get("BRAINSTEM_AI", "").strip()
HOST = "http://own-ai.invalid"
MODEL = "own-ai"
_prev_get, _prev_post = requests.get, requests.post

RULES = """You are the language model inside a Brainstem, a local AI server. Another program sends you a conversation
and reads your reply. Answer as that model would.

Rules:
- Do not use any tools of your own. Do not read files, run commands or search. Everything you need is below.
- Reply with exactly one JSON object and nothing else, in one of these two shapes:
  {"content": "<your reply to the person>"}
  {"tool_calls": [{"name": "<a tool name from TOOLS>", "arguments": {<its arguments>}}]}
- Use a tool only when TOOLS lists one that fits. After a tool result appears in the conversation, answer
  the person with {"content": ...} using that result.
"""


def _fake(status, payload=None, text=None):
    r = requests.models.Response()
    r.status_code = status
    r._content = (text if text is not None else json.dumps(payload)).encode("utf-8")
    r._content_consumed = True
    r.headers["Content-Type"] = "text/event-stream" if text is not None else "application/json"
    r.encoding = "utf-8"
    return r


def _objects(text):
    """Every top-level JSON object found in text, in order."""
    out, dec, i = [], json.JSONDecoder(), 0
    while True:
        i = text.find("{", i)
        if i < 0:
            return out
        try:
            obj, end = dec.raw_decode(text, i)
            if isinstance(obj, dict):
                out.append(obj)
            i = end
        except ValueError:
            i += 1


def ask(body):
    """Hand one chat-completions request to the person's AI; return the assistant message."""
    tools = [t.get("function", t) for t in (body.get("tools") or [])]
    prompt = (RULES + "\nTOOLS:\n" + json.dumps(tools) + "\n\nCONVERSATION:\n" + json.dumps(body.get("messages") or []))
    cmd = shlex.split(AI, posix=os.name != "nt")
    on_stdin = os.environ.get("BRAINSTEM_AI_STDIN") == "1"
    done = subprocess.run(cmd if on_stdin else cmd + [prompt], input=prompt if on_stdin else None,
                          stdin=None if on_stdin else subprocess.DEVNULL, capture_output=True, text=True,
                          timeout=110, cwd=tempfile.gettempdir(),
                          env=dict(os.environ, BRAINSTEM_OWN_AI="1"))  # lets the AI's own hooks stay quiet for machine turns
    said = (done.stdout or "").strip()
    if done.returncode != 0 and not said:
        raise RuntimeError("the AI on this device did not answer: " + (done.stderr or "")[-300:])
    names = {t.get("name") for t in tools}
    picked = [o for o in _objects(said) if "content" in o or "tool_calls" in o]
    reply = picked[-1] if picked else {"content": said}
    calls = [c for c in (reply.get("tool_calls") or []) if isinstance(c, dict) and c.get("name") in names]
    if calls:
        return {"role": "assistant", "content": None, "tool_calls": [
            {"id": f"call_{int(time.time() * 1000)}_{n}", "type": "function",
             "function": {"name": c["name"], "arguments": json.dumps(c.get("arguments") or {})}}
            for n, c in enumerate(calls)]}
    return {"role": "assistant", "content": str(reply.get("content") or said)}


def _get(url, *a, **kw):
    u = str(url)
    if AI and u.endswith("/copilot_internal/v2/token"):
        return _fake(200, {"token": "own-ai", "expires_at": int(time.time()) + 365 * 86400, "endpoints": {"api": HOST}})
    if AI and u.startswith(HOST) and u.rstrip("/").endswith("/models"):
        return _fake(200, {"data": [{"id": MODEL, "name": f"{AI.split()[0]} (the AI on this device)",
                                     "capabilities": {"type": "chat"}, "supported_endpoints": ["/chat/completions"],
                                     "model_picker_enabled": True, "policy": {"state": "enabled"}}]})
    return _prev_get(url, *a, **kw)


def _post(url, *a, **kw):
    u = str(url)
    if not (AI and u.startswith(HOST) and u.rstrip("/").endswith("/chat/completions")):
        return _prev_post(url, *a, **kw)
    body = kw.get("json") or {}
    try:
        msg = ask(body)
    except Exception as e:
        return _fake(502, {"error": {"message": str(e)[:400]}})
    fr = "tool_calls" if msg.get("tool_calls") else "stop"
    if body.get("stream"):
        delta = dict(msg)
        if delta.get("tool_calls"):
            delta["tool_calls"] = [dict(c, index=n) for n, c in enumerate(delta["tool_calls"])]
        chunk = {"id": "own-ai", "model": MODEL, "choices": [{"index": 0, "delta": delta, "finish_reason": fr}]}
        return _fake(200, text="data: " + json.dumps(chunk) + "\n\ndata: [DONE]\n\n")
    return _fake(200, {"id": "own-ai", "object": "chat.completion", "model": MODEL,
                       "choices": [{"index": 0, "message": msg, "finish_reason": fr}]})


def apply():
    if not AI:
        return
    # The kernel only starts its exchange when it holds something to exchange. This placeholder is not a
    # credential and is never sent anywhere: the exchange is answered above, on this device.
    if not os.environ.get("GITHUB_TOKEN", "").strip():
        os.environ["GITHUB_TOKEN"] = "own-ai"
    os.environ["GITHUB_MODEL"] = MODEL
    requests.get, requests.post = _get, _post
