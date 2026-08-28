---
name: "rar-cowork-cookbook-report-manage-the-recurring-synchronization-of-data"
description: "Builds a structured summary report of manage the recurring synchronization of data activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_the_recurring_synchronization_of_data", "rar_sha256": "3dbde420ec6aa63f2bc675cc5c96f979355c0b09292a142464d00b6d5f8db0ec", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_the_recurring_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `report_manage_the_recurring_synchronization_of_data_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 3dbde420ec6aa63f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_the_recurring_synchronization_of_data_agent.py` first:

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
    "version": '2.0.1',
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
