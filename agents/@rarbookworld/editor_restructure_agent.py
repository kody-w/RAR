"""editor_restructure_agent.py — single sacred agent.
Detects repetitive middle sections (the same point restated 2-3 times in
slightly different words) and consolidates them. Common in long-form
generated prose."""
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
    "name": "@rarbookworld/editor_restructure",
    "version": "0.1.0",
    "display_name": "Editor: Restructure",
    "description": "Editor specialist. Consolidates repetitive middle sections without rewriting the writer's voice.",
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

SOUL = """You are a structural editor. You read prose and consolidate
repetitive middle sections — passages where the same point is restated
2-3 times in slightly different words. This is a common failure mode in
long-form drafts: the writer makes a claim in paragraph 3, restates it in
paragraph 5, restates it again in paragraph 7. Each restatement feels like
emphasis but is actually drag.

Your job: identify those repetitions, KEEP the strongest single statement
of the idea, DELETE the others. You do not rewrite. You do not add. You
output the same draft minus the redundant restatements.

You preserve voice. You preserve code blocks (never cut a fenced code
block). You preserve real structural progression — when a later paragraph
sharpens or extends an earlier point, that is NOT repetition; keep both.
Cut only when a paragraph could be deleted with no loss of information,
because its information is already on the page elsewhere.

Output ONLY the restructured prose, nothing else."""


class EditorRestructureAgent(BasicAgent):
    def __init__(self):
        self.name = "EditorRestructure"
        self.metadata = {
            "name": self.name,
            "description": "Consolidates repetitive middle sections — keeps the strongest "
                           "statement of each idea, cuts the restatements.",
            "parameters": {"type": "object",
                "properties": {"input": {"type": "string", "description": "Draft prose"}},
                "required": ["input"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, input="", **kwargs):
        return _llm_call(SOUL,
            f"Draft to restructure:\n{input}\n\nReturn the same draft with redundant "
            "restatements consolidated. Keep the strongest single statement of each "
            "idea. Cut the rest. Output ONLY the restructured prose.")


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