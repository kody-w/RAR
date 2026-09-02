---
name: "rar-cowork-cookbook-report-manage-the-recurring-synchronization-of-data"
description: "Builds a structured summary report of manage the recurring synchronization of data activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_the_recurring_synchronization_of_data", "rar_sha256": "e018328e72d6f22a0bbd128e2fb718477e2738ad7ac2735dfe1a604daec64255", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_the_recurring_synchronization_of_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-the-recurring-synchronization-of-data:85112961670a6e973b7d46fe33151fbb509061d0049179dbd1a066defc118bf7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_the_recurring_synchronization_of_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_the_recurring_synchronization_of_data_agent.py` is
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

Manage the recurring synchronization of data Summary Report — Builds a structured summary report of manage the recurring synchronization of data activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 e018328e72d6f22a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_the_recurring_synchronization_of_data_agent.py` first:

```bash
python3 report_manage_the_recurring_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_the_recurring_synchronization_of_data_agent.py   # or on stdin
python3 report_manage_the_recurring_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the recurring synchronization of data Summary Report — Builds a structured summary report of manage the recurring synchronization of data activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_the_recurring_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the recurring synchronization of data Summary Report',
    "description": 'Builds a structured summary report of manage the recurring synchronization of data activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-the-recurring-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dd7a4bdffcf9d1be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-recurring-synchronization-of-data'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-the-recurring-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageTheRecurringSynchronizationOfData(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageTheRecurringSynchronizationOfData'
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
    print(ReportManageTheRecurringSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
