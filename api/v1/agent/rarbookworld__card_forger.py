"""card_forger_agent.py — single sacred agent. Mints a RAR-compatible card from a Drop."""
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
    "name": "@rarbookworld/card_forger",
    "version": "0.1.0",
    "display_name": "Card Forger",
    "description": "Mints a RAR-compatible card (name + impact/novelty/compoundability stats + ability + lore + art_seed) from a Drop. Every Drop is a collectible.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "card"
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

SOUL = """You are the CardForger of the MomentFactory pipeline. You mint a
RAR-compatible card from a Drop — every Drop is also a collectible.

You output a JSON object with EXACTLY these keys:
  name        — short title for the card (2-6 words)
  stats       — object with three integers 0..10:
                  impact          — how much this moment moves the world
                  novelty         — how new the underlying pattern is
                  compoundability — how much it sets up future moments
  ability     — one sentence describing what this card "does" if drawn from
                an agents/ directory later (e.g. "Files itself in the framework's
                lessons-learned cache" or "Triggers a re-read of related Drops")
  lore        — one sentence of backstory connecting this Drop to its origin
  art_seed    — integer 0..9999999999, deterministic art reconstruction seed

Rules:
- Stats are honest, not flattering. A "had coffee" Drop is impact 0, novelty 0,
  compoundability 0. The CardForger does NOT inflate.
- The ability is a verb-led action, not a description.
- The lore is one sentence. Period.
- Output ONLY the JSON. No prose."""


class CardForgerAgent(BasicAgent):
    def __init__(self):
        self.name = "CardForger"
        self.metadata = {
            "name": self.name,
            "description": "Mints a RAR-compatible card (name + stats + ability + lore + art_seed) from a Drop.",
            "parameters": {"type": "object",
                "properties": {
                    "hook":    {"type": "string"},
                    "body":    {"type": "string"},
                    "channel": {"type": "string"},
                },
                "required": ["hook", "body"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, hook="", body="", channel="", **kwargs):
        return _llm_call(SOUL,
            f"Hook: {hook}\n\nBody: {body}\n\nChannel: {channel}\n\n"
            "Return ONLY the JSON card object.")


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
    return '{"name":"(no LLM)","stats":{"impact":0,"novelty":0,"compoundability":0},"ability":"unknown","lore":"unknown","art_seed":0}'


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