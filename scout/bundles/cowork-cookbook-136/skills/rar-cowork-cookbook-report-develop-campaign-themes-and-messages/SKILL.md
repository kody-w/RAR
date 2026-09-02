---
name: "rar-cowork-cookbook-report-develop-campaign-themes-and-messages"
description: "Builds a structured summary report of develop campaign themes and messages activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_campaign_themes_and_messages", "rar_sha256": "ce9ea418e7cde80528a4c992b2f307518455c7129cc639f58722d16a850ae754", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_campaign_themes_and_messages_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-campaign-themes-and-messages:6b5035070b3761a704302a8d1e984b335ee367834dc774c60094a1c76a785804", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_campaign_themes_and_messages`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_campaign_themes_and_messages_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
