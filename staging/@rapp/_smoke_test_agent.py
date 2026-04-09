"""
Pipeline Smoke Test Agent — DO NOT USE. Created by automated testing.
This agent is created and destroyed by the admin pipeline smoke test.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/_smoke_test_agent",
    "version": "1.0.0",
    "display_name": "SmokeTestAgent",
    "description": "Automated pipeline smoke test — created and destroyed by CI testing.",
    "author": "RAR Pipeline",
    "tags": ["test", "smoke", "pipeline"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name="", metadata=None): self.name = name; self.metadata = metadata or {}
        def perform(self, **kw): return ""

class SmokeTestAgent(BasicAgent):
    def __init__(self):
        self.name = "SmokeTestAgent"
        self.metadata = {"description": __manifest__["description"], "parameters": {"type": "object", "properties": {"operation": {"type": "string", "enum": ["ping"]}}}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        return "pong — smoke test passed"

if __name__ == "__main__":
    agent = SmokeTestAgent()
    print(agent.perform(operation="ping"))
