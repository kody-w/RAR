"""RETIRED: @borg/hacker_news_agent

This path is a promise, so it still resolves — but the agent that lived here has been retired.
Removed on 2026-07-23 as a duplicate of @rapp/hacker_news (one agent per concern).
The file as it was (version 1.0.0) is kept byte for byte at https://kody-w.github.io/RAR/versions/@borg/hacker_news_agent/e83a236ebf1f.py
Current version: https://kody-w.github.io/RAR/agents/@rapp/hacker_news_agent.py
"""

RAR_TOMBSTONE = {
    "name": "@borg/hacker_news_agent",
    "retired_version": "1.0.0",
    "upstream": "https://kody-w.github.io/RAR/agents/@rapp/hacker_news_agent.py",
}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@borg/hacker_news_agent",
    "version": "1.0.0",
    "display_name": "HackerNewsAgent (retired)",
    "description": "Retired tombstone: this path resolves, the agent does not run here anymore.",
    "author": "RAR",
    "tags": ["retired", "tombstone"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except Exception:  # standalone execution outside a brainstem
    class BasicAgent:  # type: ignore
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class HackerNewsAgentTombstoneAgent(BasicAgent):
    def __init__(self):
        super().__init__("hacker_news_agent", __manifest__)

    def perform(self, **kwargs) -> str:
        return "RETIRED: @borg/hacker_news_agent. " + ("Current version: https://kody-w.github.io/RAR/agents/@rapp/hacker_news_agent.py" if "https://kody-w.github.io/RAR/agents/@rapp/hacker_news_agent.py" else "No successor published.")


if __name__ == "__main__":
    print(HackerNewsAgentTombstoneAgent().perform())
