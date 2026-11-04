# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/hello_world_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hello_world_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/hello_world_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Hello World Agent — A friendly greeting agent that demonstrates the basics."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/hello_world_agent",
    "version": "1.0.3",
    "display_name": "Hello World",
    "description": "Greets the user by name with a canned hello message; a starter example touching no external systems.",
    "author": "kody-w",
    "tags": ["tutorial", "hello-world", "starter"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


class HelloWorldAgent(BasicAgent):
    def __init__(self):
        self.name = "HelloWorldAgent"
        self.metadata = {
            "name": self.name,
            "description": "Says hello to the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"}
                },
                "required": []
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        name = kwargs.get("name", "World")
        return f"Hello, {name}! Welcome to the RAPP Agent ecosystem."
