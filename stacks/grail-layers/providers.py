# ── RAPP layer ticket ── @kody-w/providers
# What: Layer: providers — every model the unchanged grail can reach, in one provider part.
# Add in chat: update my Brainstem with @kody-w/providers
# Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
# Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
#   confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
#   Label: providers. Health alone is not proof; test /chat and /chat/stream.
# Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
#   For a part added individually in chat, ask to remove its id or undo that shape change.
# Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1
# ── End RAPP layer ticket
"""Layer: providers — every model the unchanged grail can reach, in one provider part.

Kody's ruling (2026-11-03): one occupant per shape point, so the two provider behaviours live in ONE part:
  1. responses_models: models that only speak the Responses API (gpt-6.1-sol, gpt-6-luna) on GitHub Copilot
     become usable; /chat/completions calls for them are translated to /responses and back.
  2. local_models: models running on this machine (Ollama, OLLAMA_URL default http://127.0.0.1:11434) join the
     model list as ollama/<name> and answer chat with tools, no Copilot needed for them.
`@kody-w/responses_models` and `@kody-w/local_models` are ALIASES of this part: their files stay published and
unchanged, new shapes use this one. Any error inside the layer -> the grail's original call.
"""
import json
import os

import requests

# Hook points this layer wraps. Two enabled layers touching the same point conflict; the pack's order wins.
TOUCHES = {"requests.get", "requests.post"}

PROVEN_GRAIL = {
    "35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a",  # 0.6.17 (installed)
    "bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4",  # 0.6.16 (public rapp-installer main)
}

# ---------------- 1. responses_models ----------------
RESPONSES_ONLY = set()
_orig_get, _orig_post = requests.get, requests.post
_orig_sget, _orig_spost = requests.Session.get, requests.Session.post


def _fake(status, payload):
    r = requests.models.Response()
    r.status_code = status
    r._content = json.dumps(payload).encode()
    r.headers["Content-Type"] = "application/json"
    r.encoding = "utf-8"
    return r


def _to_responses(body):
    instructions, items = [], []
    for m in body.get("messages", []):
        role, content = m.get("role"), m.get("content")
        if isinstance(content, list):
            content = "".join(p.get("text", "") for p in content if isinstance(p, dict))
        if role == "system":
            instructions.append(content or "")
        elif role == "tool":
            items.append({"type": "function_call_output", "call_id": m.get("tool_call_id"), "output": content or ""})
        elif role == "assistant":
            if content:
                items.append({"role": "assistant", "content": content})
            for tc in m.get("tool_calls") or []:
                f = tc.get("function", {})
                items.append({"type": "function_call", "call_id": tc.get("id"), "name": f.get("name"),
                              "arguments": f.get("arguments") or "{}"})
        else:
            items.append({"role": "user", "content": content or ""})
    out = {"model": body["model"], "input": items}
    if instructions:
        out["instructions"] = "\n\n".join(instructions)
    tools = [{"type": "function", "name": t["function"]["name"],
              "description": t["function"].get("description", ""),
              "parameters": t["function"].get("parameters") or {"type": "object", "properties": {}}}
             for t in body.get("tools") or [] if t.get("type") == "function"]
    if tools:
        out["tools"] = tools
        out["tool_choice"] = body.get("tool_choice", "auto")
    return out


def _to_chat(res, model):
    text, calls = [], []
    for item in res.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") in ("output_text", "text"):
                    text.append(c.get("text", ""))
        elif item.get("type") == "function_call":
            calls.append({"id": item.get("call_id") or item.get("id"), "type": "function",
                          "function": {"name": item.get("name"), "arguments": item.get("arguments") or "{}"}})
    msg = {"role": "assistant", "content": "".join(text) or None}
    if calls:
        msg["tool_calls"] = calls
    u = res.get("usage") or {}
    return {"id": res.get("id"), "object": "chat.completion", "model": model,
            "choices": [{"index": 0, "message": msg, "finish_reason": "tool_calls" if calls else "stop"}],
            "usage": {"prompt_tokens": u.get("input_tokens"), "completion_tokens": u.get("output_tokens"),
                      "total_tokens": u.get("total_tokens")}}


def _get_responses(url, *a, **kw):
    resp = _orig_get(url, *a, **kw)
    try:
        if str(url).rstrip("/").endswith("/models") and resp.status_code == 200:
            data = resp.json()
            lst = data if isinstance(data, list) else data.get("data", data.get("models", []))
            for m in lst:
                eps = m.get("supported_endpoints")
                if isinstance(eps, list) and "/responses" in eps and "/chat/completions" not in eps:
                    RESPONSES_ONLY.add(m.get("id"))
                    m["supported_endpoints"] = eps + ["/chat/completions"]  # served by this layer
            resp._content = json.dumps(data).encode()
    except Exception:
        pass
    return resp


def _post_responses(url, *a, **kw):
    try:
        body = kw.get("json")
        if str(url).endswith("/chat/completions") and isinstance(body, dict) and body.get("model") in RESPONSES_ONLY:
            if kw.get("stream"):
                return _fake(400, {"error": {"message": "layer: streaming not offered for Responses-only model"}})
            rurl = str(url)[: -len("/chat/completions")] + "/responses"
            kw2 = {k: v for k, v in kw.items() if k != "json"}
            r = _orig_post(rurl, *a, json=_to_responses(body), **kw2)
            if r.status_code != 200:
                return r
            return _fake(200, _to_chat(r.json(), body["model"]))
    except Exception:
        pass
    return _orig_post(url, *a, **kw)




# ---------------- 2. local_models (wraps the responses wrappers) ----------------


OLLAMA = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
PREFIX = "ollama/"
_prev_get, _prev_post = _get_responses, _post_responses


def _ollama_models():
    try:
        r = _prev_get(OLLAMA + "/v1/models", timeout=3)
        if r.status_code != 200:
            return []
        data = r.json()
        ids = [m.get("id") for m in (data.get("data") or []) if m.get("id")]
        return [{"id": PREFIX + i, "name": f"{i} (local, Ollama)", "capabilities": {"type": "chat"},
                 "supported_endpoints": ["/chat/completions"], "model_picker_enabled": True,
                 "policy": {"state": "enabled"}} for i in ids]
    except Exception:
        return []


def _get_local(url, *a, **kw):
    resp = _prev_get(url, *a, **kw)
    try:
        if str(url).rstrip("/").endswith("/models") and not str(url).startswith(OLLAMA) and resp.status_code == 200:
            data = resp.json()
            local = _ollama_models()
            if local:
                if isinstance(data, list):
                    data = data + local
                elif isinstance(data.get("data"), list):
                    data["data"] = data["data"] + local
                elif isinstance(data.get("models"), list):
                    data["models"] = data["models"] + local
                resp._content = json.dumps(data).encode()
    except Exception:
        pass
    return resp


def _post_local(url, *a, **kw):
    try:
        body = kw.get("json")
        if str(url).rstrip("/").endswith("/chat/completions") and isinstance(body, dict) \
                and str(body.get("model", "")).startswith(PREFIX):
            body = dict(body, model=body["model"][len(PREFIX):])
            headers = {k: v for k, v in (kw.get("headers") or {}).items() if k.lower() != "authorization"}
            kw2 = dict(kw, json=body, headers=headers)
            return _prev_post(OLLAMA + "/v1/chat/completions", *a, **kw2)
    except Exception:
        pass
    return _prev_post(url, *a, **kw)




def apply():
    requests.get, requests.post = _get_local, _post_local
