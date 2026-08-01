"""
Power Automate Desktop Assessment — Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. perform() returns a description and a
link, so this is a catalog entry pointing home, not a copy.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment
  Upstream author: Ricardo Calejo
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_automate_desktop_assessment',
    "version": '1.1.0',
    "display_name": 'Power Automate Desktop Assessment',
    "description": 'Assess Power Automate Desktop and hybrid automation projects with evidence-based findings and prioritized remediation guidance.',
    "author": 'Ricardo Calejo',
    "tags": ['power_automate', 'desktop_flows', 'automation', 'assessment', 'governance'],
    "category": 'analysis',
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
        "upstream_slug": 'power-automate-desktop-assessment',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-automate-desktop-assessment',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd026e3d4a8378798',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class PowerAutomateDesktopAssessment(BasicAgent):
    """Catalog entry for an aggregated upstream skill."""

    def __init__(self):
        self.name = 'PowerAutomateDesktopAssessment'
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
        platforms = ['Cowork', 'Copilot Studio']
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
    print(PowerAutomateDesktopAssessment().perform())
