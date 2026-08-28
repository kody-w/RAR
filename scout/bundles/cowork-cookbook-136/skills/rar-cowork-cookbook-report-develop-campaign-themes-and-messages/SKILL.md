---
name: "rar-cowork-cookbook-report-develop-campaign-themes-and-messages"
description: "Builds a structured summary report of develop campaign themes and messages activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_campaign_themes_and_messages", "rar_sha256": "ce9ea418e7cde80528a4c992b2f307518455c7129cc639f58722d16a850ae754", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 ce9ea418e7cde805…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_campaign_themes_and_messages_agent.py` first:

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
    "version": '2.0.0',
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
