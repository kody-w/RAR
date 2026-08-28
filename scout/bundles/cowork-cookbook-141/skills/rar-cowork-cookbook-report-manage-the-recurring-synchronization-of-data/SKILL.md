---
name: "rar-cowork-cookbook-report-manage-the-recurring-synchronization-of-data"
description: "Builds a structured summary report of manage the recurring synchronization of data activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_the_recurring_synchronization_of_data", "rar_sha256": "e018328e72d6f22a0bbd128e2fb718477e2738ad7ac2735dfe1a604daec64255", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
