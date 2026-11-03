"""Layer: responses_models — lets the unchanged grail use models that only speak the Responses API
(for example gpt-6-astra and gpt-6.1-sol on GitHub Copilot).

The grail filters those models out of /models because it only calls /chat/completions. This layer
wraps the `requests` functions the grail calls, inside the Brainstem process only:
  GET  <endpoint>/models            -> keeps Responses-only models in the list (remembers which)
  POST <endpoint>/chat/completions  -> for those models: calls <endpoint>/responses and returns the
                                       answer in chat-completions shape; a streaming request gets a
                                       clean refusal so the grail falls back to its non-stream path.
Everything else passes straight through. Any error inside the layer -> the grail's original call.
"""
import json

import requests

# sha256 of every grail brainstem.py this layer was PROVEN against (a real /chat through it).
# The supervisor skips this layer on any other grail. Add a sha only after re-proving.
PROVEN_GRAIL = {
    "35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a",  # 0.6.17 (installed)
    "bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4",  # 0.6.16 (public rapp-installer main)
}

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


def _get(url, *a, **kw):
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


def _post(url, *a, **kw):
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


def apply():
    requests.get, requests.post = _get, _post
