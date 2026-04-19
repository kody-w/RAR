"""body_writer_agent.py — single sacred agent. Forges the 3-5 sentence Drop body."""
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
    "name": "@rarbookworld/body_writer",
    "version": "0.1.0",
    "display_name": "Body Writer",
    "description": "Writes the 3-5 sentence body of a Drop. Expands the hook, never restates. At least one concrete detail from key_facts.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "body"
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

SOUL = """You are the BodyWriter of the MomentFactory pipeline. You write the
3-to-5 sentence body that earns a Drop's place on the feed.

Rules:
- 3 to 5 sentences. Not 6. Not 2.
- The body must EXPAND on the hook, never restate it.
- Use at least one concrete detail from key_facts (a number, a name, a filename).
- Match the voice_signature.
- No prefatory throat-clearing ("So,", "Well,", "I think"). Start in the action.
- No closing summary line ("In conclusion,"). The last sentence is just the
  next sentence, not a wrap-up.
- If the source has fenced code blocks, you MAY include ONE — but only if it's
  load-bearing. The Drop is feed content, not a tutorial.

Output ONLY the body prose. No quotes, no commentary, no headers."""


class BodyWriterAgent(BasicAgent):
    def __init__(self):
        self.name = "BodyWriter"
        self.metadata = {
            "name": self.name,
            "description": "Returns 3-5 sentences expanding the hook into a feed-worthy Drop body.",
            "parameters": {"type": "object",
                "properties": {
                    "normalized_moment": {"type": "string", "description": "JSON from Sensorium"},
                    "hook":              {"type": "string", "description": "1-sentence hook"},
                },
                "required": ["normalized_moment", "hook"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, normalized_moment="", hook="", **kwargs):
        return _llm_call(SOUL,
            f"Normalized moment:\n{normalized_moment}\n\n"
            f"Hook:\n{hook}\n\n"
            "Return ONLY the 3-5 sentence body prose.")


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