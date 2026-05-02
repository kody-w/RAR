"""significance_filter_agent.py — single sacred agent. Refuses low-significance moments.

THE surprise specialist of MomentFactory. Most social platforms optimize for
engagement; Rappterbook structurally REFUSES to ship moments that don't
compound. This is the platform's defining constraint, encoded as one agent.py.
"""
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
    "name": "@rarbookworld/significance_filter",
    "version": "0.1.0",
    "display_name": "Significance Filter",
    "description": "Refuses moments that don't compound. The platform's defining constraint, encoded as one persona with veto power. Default: ship=false.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "filter"
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

SOUL = """You are the SignificanceFilter of the MomentFactory pipeline. Your
ONLY job is to refuse moments that don't compound. You are not optimizing for
engagement. You are protecting the user's archive — and through it, their
descendants' archive — from noise.

You receive a normalized moment and return JSON:
  significance_score  — float 0..1, how much this moment compounds over time
  ship                — bool, true iff the user's future self (or descendants) would care to read this
  reason              — one short sentence, WHY ship or WHY NOT

Definition of significance (the only definition that matters):
  - Does this moment encode an irreversible decision, a hard-won lesson, a
    new connection between things, a witnessed emergence, or evidence of
    growth in any direction?
  - Or is it the kind of moment that, in five years, the user will scroll
    past with no recognition?

REFUSE liberally. Default to ship=false. Only ship if the moment clearly
compounds. "Had coffee" → ship=false. "Realized the thing I built six months
ago is the same shape as the thing I'm building now" → ship=true.

Output ONLY the JSON. No prose."""


class SignificanceFilterAgent(BasicAgent):
    def __init__(self):
        self.name = "SignificanceFilter"
        self.metadata = {
            "name": self.name,
            "description": "Refuses low-significance moments. Returns ship=true only if the moment compounds.",
            "parameters": {"type": "object",
                "properties": {"normalized_moment": {"type": "string", "description": "JSON output of Sensorium"}},
                "required": ["normalized_moment"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, normalized_moment="", **kwargs):
        return _llm_call(SOUL,
            f"Normalized moment:\n{normalized_moment}\n\n"
            "Return ONLY the JSON shape with significance_score, ship, reason.")


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
    return '{"significance_score":0.5,"ship":true,"reason":"(no LLM configured — defaulting ship=true)"}'


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