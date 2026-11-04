# ── RAPP layer ticket ── @kody-w/local_models
# What: Layer: local_models — the unchanged grail can talk to models running on this machine (Ollama).
# Add in chat: update my Brainstem with @kody-w/local_models
# Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
# Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
#   confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
#   Label: local_models. Health alone is not proof; test /chat and /chat/stream.
# Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
#   For a part added individually in chat, ask to remove its id or undo that shape change.
# Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1
# ── End RAPP layer ticket
"""Layer: local_models — the unchanged grail can talk to models running on this machine (Ollama).

The kernel only knows one provider: the GitHub Copilot endpoint it gets from its token exchange. Ollama serves
the same wire (OpenAI chat-completions, tool calls included) at http://127.0.0.1:11434/v1, so no adapter is
needed: this layer adds Ollama's models to the kernel's model list under the prefix `ollama/` and, when the
chosen model carries that prefix, sends the chat-completions call to Ollama instead of Copilot, with no
Authorization header. Everything else (Copilot models, the token exchange, streaming) passes straight through.

Composition: this layer WRAPS requests.get/post (it calls through to whatever an earlier layer, for example
responses_models, left there), so both can be live in one shape; the pack's order decides who is outermost.

Env: OLLAMA_URL (default http://127.0.0.1:11434). No Ollama running: the model list is unchanged and nothing
else happens. Probe before publishing (2026-11-03): Ollama 'llama3.2:latest' answered a chat-completions
request with a tool call in the kernel's exact shape, 1 of 1.
"""
import json

import requests

# Composable hook points: this layer chains to the functions already in place (see WRAPS in grail_layers.py).
WRAPS = {"requests.get", "requests.post"}

PROVEN_GRAIL = {
    "35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a",  # 0.6.17 (installed)
    "bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4",  # 0.6.16 (public rapp-installer main)
}

import os  # noqa: E402

OLLAMA = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
PREFIX = "ollama/"
_prev_get, _prev_post = requests.get, requests.post


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


def _get(url, *a, **kw):
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


def _post(url, *a, **kw):
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
    requests.get, requests.post = _get, _post
