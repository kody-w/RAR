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
