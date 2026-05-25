"""channel_router_agent.py — single sacred agent. Picks the Subrappter for a Drop."""
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
    "name": "@rarbookworld/channel_router",
    "version": "0.1.0",
    "display_name": "Channel Router",
    "description": "Picks one Subrappter (r/builders, r/dreams, r/decisions, r/lessons, r/connections, etc.) for a Drop. Auto-classifies, no manual tagging.",
    "author": "rarbookworld",
    "tags": [
        "moment-pipeline",
        "router"
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

# Canonical Rappterbook channel set — lives in this file because the routing
# table is part of the agent's logic, not external config.
CHANNELS = [
    ("r/builders",   "engineering work, code, architectures, debugging stories"),
    ("r/commits",    "raw git activity, deploys, releases"),
    ("r/dreams",     "dreams, voice memos, half-formed thoughts captured before they vanish"),
    ("r/wins",       "shipped things, milestones reached, real outcomes"),
    ("r/decisions",  "irreversible choices, the moment a path was picked"),
    ("r/lessons",    "hard-won insights from being wrong, postmortems, retroactive realizations"),
    ("r/connections","seeing the same shape in two unrelated places, analogies that compound"),
    ("r/places",     "geo-tagged moments, location pings with context"),
    ("r/conversations","snippets from talks worth remembering"),
    ("r/reading",    "notes from things read, articles, books, papers"),
    ("r/agents",     "agent activity, runs, swarm events, framework moments"),
    ("r/heirloom",   "the rare moment a future descendant might want to read"),
]

SOUL = f"""You are the ChannelRouter of the MomentFactory pipeline. You pick the
ONE Subrappter (channel) where a Drop most belongs. You return only the channel
slug — nothing else.

Available channels:
{chr(10).join(f"  {slug:18s}  — {desc}" for slug, desc in CHANNELS)}

Rules:
- Pick exactly ONE channel.
- Return ONLY the slug (e.g. "r/builders"). No explanation, no quotes.
- If the moment touches multiple channels, pick the one that BEST fits the
  primary action of the moment, not the topic.
- "r/heirloom" is rare — only for moments with high descendant-readability.
- When in doubt between two adjacent channels, pick the more specific one.
"""


class ChannelRouterAgent(BasicAgent):
    def __init__(self):
        self.name = "ChannelRouter"
        self.metadata = {
            "name": self.name,
            "description": "Returns a single Rappterbook channel slug for a Drop.",
            "parameters": {"type": "object",
                "properties": {
                    "hook": {"type": "string", "description": "Drop hook"},
                    "body": {"type": "string", "description": "Drop body"},
                },
                "required": ["hook", "body"]},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, hook="", body="", **kwargs):
        out = _llm_call(SOUL,
            f"Hook: {hook}\n\nBody: {body}\n\n"
            "Return ONLY the channel slug (e.g. r/builders).")
        # Defensive: strip whitespace and any quotes the LLM might wrap
        return out.strip().strip('"').strip("'").splitlines()[0].strip() if out else "r/builders"


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
    return "r/builders"


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