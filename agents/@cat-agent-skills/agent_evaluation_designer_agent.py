"""
Agent Evaluation Designer — Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. perform() returns a description and a
link, so this is a catalog entry pointing home, not a copy.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer
  Upstream author: James Papadimitriou
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_evaluation_designer',
    "version": '1.0.0',
    "display_name": 'Agent Evaluation Designer',
    "description": 'Design a rigorous, platform-aware evaluation for an AI agent - define what good looks like, pick the right grading method, build a test set, and turn results into a defensible go/no-go decision.',
    "author": 'James Papadimitriou',
    "tags": ['evaluation', 'testing', 'quality_assurance', 'go_live', 'decision_making'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'agent-evaluation-designer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-evaluation-designer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '5932d5f6ea50fb35',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class AgentEvaluationDesigner(BasicAgent):
    """Catalog entry for an aggregated upstream skill."""

    def __init__(self):
        self.name = 'AgentEvaluationDesigner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {"type": "object", "properties": {}},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        """Describe the upstream capability and point to it. Returns a string."""
        src = __manifest__["source"]
        platforms = ['Copilot Studio']
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Aggregated from: {src['source_name']}",
            f"Upstream entry:  {src['upstream_url']}",
            f"Upstream author: {__manifest__['author']}",
        ]
        if platforms:
            lines.append("Runs on:         " + ", ".join(platforms))
        lines += [
            "",
            "This is a catalog entry. The upstream library holds the content; "
            "open the link above to get it from the source.",
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    print(AgentEvaluationDesigner().perform())
