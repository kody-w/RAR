# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/ping_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ping_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/ping_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""ping_agent — Returns 'pong'. Smoke test for agent dispatch."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/ping_agent",
    "version": "1.0.1",
    "display_name": "Ping",
    "description": "Returns 'pong'. The smallest possible agent — useful as a smoke test that the brainstem can discover, load, and dispatch a tool call end-to-end.",
    "author": "RAPP",
    "tags": ["diagnostic", "smoke-test", "minimal"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent


class PingAgent(BasicAgent):
    def __init__(self):
        self.name = "Ping"
        self.metadata = {
            "name": self.name,
            "description": "Returns 'pong'. Smoke test for the agent dispatch path.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        return "pong"