---
name: "rar-cowork-cookbook-report-develop-campaign-themes-and-messages"
description: "Builds a structured summary report of develop campaign themes and messages activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_campaign_themes_and_messages", "rar_sha256": "ca07d2d3b96fbed62eeeff848f07a7fff25af65c9eccdec1a86cfc7ec9cfaa98", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_campaign_themes_and_messages`. The original RAPP
agent is preserved byte-for-byte in `report_develop_campaign_themes_and_messages_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Develop campaign themes and messages Summary Report — Builds a structured summary report of develop campaign themes and messages activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 ca07d2d3b96fbed6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_campaign_themes_and_messages_agent.py` first:

```bash
python3 report_develop_campaign_themes_and_messages_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_campaign_themes_and_messages_agent.py   # or on stdin
python3 report_develop_campaign_themes_and_messages_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop campaign themes and messages Summary Report — Builds a structured summary report of develop campaign themes and messages activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_campaign_themes_and_messages',
    "version": '2.0.1',
    "display_name": 'Develop campaign themes and messages Summary Report',
    "description": 'Builds a structured summary report of develop campaign themes and messages activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-develop-campaign-themes-and-messages',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-campaign-themes-and-messages',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36b7e62feaa02e5d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-develop-campaign-themes-and-messages', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDevelopCampaignThemesAndMessages(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopCampaignThemesAndMessages'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(ReportDevelopCampaignThemesAndMessages().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
