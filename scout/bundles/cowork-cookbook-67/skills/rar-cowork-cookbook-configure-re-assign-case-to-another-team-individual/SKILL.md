---
name: "rar-cowork-cookbook-configure-re-assign-case-to-another-team-individual"
description: "Applies a bulk configuration change to re-assign case to another team/individual from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_re_assign_case_to_another_team_individual", "rar_sha256": "be4859217dc184d597344a4792c86186e008278876aa3cd1d643629538c6bab0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_re_assign_case_to_another_team_individual`. The original RAPP
agent is preserved byte-for-byte in `configure_re_assign_case_to_another_team_individual_agent.py` and in the RCI capsule.

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

Re-assign case to another team/individual Configuration Bulk Setup — Applies a bulk configuration change to re-assign case to another team/individual from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-re-assign-case-to-another-team-individual
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_re_assign_case_to_another_team_individual_agent.py` and embedded as the fenced Python below (sha256 be4859217dc184d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_re_assign_case_to_another_team_individual_agent.py` first:

```bash
python3 configure_re_assign_case_to_another_team_individual_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_re_assign_case_to_another_team_individual_agent.py   # or on stdin
python3 configure_re_assign_case_to_another_team_individual_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Re-assign case to another team/individual Configuration Bulk Setup — Applies a bulk configuration change to re-assign case to another team/individual from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-re-assign-case-to-another-team-individual
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_re_assign_case_to_another_team_individual',
    "version": '2.0.1',
    "display_name": 'Re-assign case to another team/individual Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to re-assign case to another team/individual from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-re-assign-case-to-another-team-individual',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-re-assign-case-to-another-team-individual',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74bfb73a51e445ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/re-assign-case-to-another-team-individual'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-re-assign-case-to-another-team-individual', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReAssignCaseToAnotherTeamIndividual(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReAssignCaseToAnotherTeamIndividual'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(ConfigureReAssignCaseToAnotherTeamIndividual().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
