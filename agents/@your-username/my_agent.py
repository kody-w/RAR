"""
My Agent — An AI agent.
"""

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@your-username/my_agent",
    "version": "1.0.0",
    "display_name": "My Agent",
    "description": "An AI agent.",
    "author": "Anonymous",
    "tags": [],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}


class MyAgentAgent(BasicAgent):
    def __init__(self):
        self.name = "My Agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "What to do"
                    }
                },
                "required": ["task"]
            }
        }
        super().__init__(self.name, self.metadata)

    async def perform(self, **kwargs):
        task = kwargs.get("task", "")
        return f"My Agent received: task={task}"
