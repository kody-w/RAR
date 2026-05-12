"""
Sample private agent — replace with your own.

Same single-file convention as public RAR: a docstring, a __manifest__
dict, a class inheriting BasicAgent, and a perform() that returns str.

The only difference for private agents: this file lives in YOUR private
repo, not in public RAR. Public RAR may carry a matching `.py.stub`
listing pointing here, which is how other authorized users discover
and install it. If no stub exists, this agent is invisible to anyone
outside the private repo — also a valid mode.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/sample_private",
    "version": "1.0.0",
    "display_name": "SamplePrivate",
    "description": "Replace me. Demonstrates the private agent layout.",
    "author": "Your Name",
    "tags": ["sample", "private"],
    "category": "productivity",
    "quality_tier": "private",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


class SamplePrivateAgent(BasicAgent):
    def __init__(self):
        self.name = "SamplePrivate"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "A message to echo back.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        msg = kwargs.get("message", "hello from your private RAR")
        return f"SamplePrivate: {msg}"


if __name__ == "__main__":
    print(SamplePrivateAgent().perform(message="works"))
