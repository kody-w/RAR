"""editor_cutweak_agent.py — single sacred agent. Cuts the weakest 20%."""
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
    "name": "@rarbookworld/editor_cutweak",
    "version": "0.1.0",
    "display_name": "Editor: Cut Weakest 20%",
    "description": "Editor specialist. Returns the same prose with the weakest 20% cut. Preserves fenced code blocks as evidence.",
    "author": "rarbookworld",
    "tags": [
        "editor-specialist",
        "creative-pipeline"
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

SOUL = """You are a 'cut the weakest 20%' editor pass. You read prose and
return the same prose with the weakest paragraphs removed. You preserve the
writer's voice. You do not add new content. You output ONLY the cut prose,
nothing else.

CRITICAL: Fenced code blocks (```...```) are EVIDENCE, not prose. Never cut
a code block. Never abbreviate one. Never replace one with a description of
what it shows. If a paragraph is weak, cut the paragraph; if a code block
sits next to weak prose, keep the code block, cut the prose around it.
Code is the load-bearing material in technical writing — your job is to
remove the scaffolding around it, never the load itself."""


class EditorCutweakAgent(BasicAgent):
    def __init__(self):
        self.name = "EditorCutweak"
        self.metadata = {
            "name": self.name,
            "description": "Returns the same prose with the weakest 20% cut.",
            "parameters": {"type": "object",
                "properties": {"input": {"type": "string", "description": "Draft prose"}},
                "required": ["input"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, input="", **kwargs):
        return _llm_call(SOUL,
            f"Draft to cut:\n{input}\n\nReturn the same draft with the weakest "
            "20% removed. Output only the cut prose. No commentary.")


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