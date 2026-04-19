"""hook_writer_agent.py — single sacred agent. Forges the 1-sentence hook."""
try:
    from agents.basic_agent import BasicAgent  # RAPP layout
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent      # flat / @publisher layout
    except ModuleNotFoundError:
        class BasicAgent:                       # last-resort standalone
            def __init__(self, name, metadata): self.name, self.metadata = name, metadata
import json, os, urllib.request, urllib.error

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/hook_writer",
    "version": "0.1.0",
    "display_name": "Hook Writer",
    "description": "Writes the one sentence that earns a tap on the feed. Single sentence. Concrete over abstract. No clickbait.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "hook"
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT"
    ],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

SOUL = """You are the HookWriter of the MomentFactory pipeline. You write the
ONE sentence that earns a tap on the feed.

Rules:
- ONE sentence. Period. No two-sentence hooks, no "X. Y." cheats.
- Concrete > abstract. If the moment has a number, a name, or a filename,
  use one of them.
- The hook must be true to the source. If you exaggerate, the body will
  contradict you and the Reader will lose trust forever.
- No clickbait verbs ("you won't believe", "this changes everything").
- Match the voice_signature of the source — if the source is dry, the hook
  is dry. If the source is jokey, the hook is jokey.

Output ONLY the hook sentence. No quotes around it. No commentary."""


class HookWriterAgent(BasicAgent):
    def __init__(self):
        self.name = "HookWriter"
        self.metadata = {
            "name": self.name,
            "description": "Returns one sentence that earns a tap on the feed.",
            "parameters": {"type": "object",
                "properties": {"normalized_moment": {"type": "string", "description": "JSON from Sensorium"}},
                "required": ["normalized_moment"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, normalized_moment="", **kwargs):
        return _llm_call(SOUL,
            f"Normalized moment:\n{normalized_moment}\n\n"
            "Return ONLY the one-sentence hook.")


def _llm_call(soul, user_prompt):
    msgs = [{"role": "system", "content": soul}, {"role": "user", "content": user_prompt}]
    ep, key = os.environ.get("AZURE_OPENAI_ENDPOINT", ""), os.environ.get("AZURE_OPENAI_API_KEY", "")
    dep = os.environ.get("AZURE_OPENAI_DEPLOYMENT") or os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "")
    if ep and key:
        url = ep if "/chat/completions" in ep else ep.rstrip("/") + f"/openai/deployments/{dep}/chat/completions?api-version=2025-01-01-preview"
        if "/chat/completions" in ep and "/openai/v1/" not in ep and "?" not in url:
            url += "?api-version=2025-01-01-preview"
        return _post(url, {"messages": msgs, "model": dep},
                      {"Content-Type": "application/json", "api-key": key})
    if os.environ.get("OPENAI_API_KEY"):
        return _post("https://api.openai.com/v1/chat/completions",
                      {"model": os.environ.get("OPENAI_MODEL", "gpt-4o"), "messages": msgs},
                      {"Content-Type": "application/json",
                       "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    return "(no LLM configured)"


def _post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            j = json.loads(r.read().decode("utf-8"))
        c = j.get("choices") or []
        return (c[0]["message"].get("content") or "") if c else ""
    except urllib.error.HTTPError as e:
        return f"(LLM HTTP {e.code}: {e.read().decode('utf-8')[:200]})"
    except urllib.error.URLError as e:
        return f"(LLM network error: {e})"