---
name: "rar-cowork-cookbook-configure-re-assign-case-to-another-team-individual"
description: "Applies a bulk configuration change to re-assign case to another team/individual from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_re_assign_case_to_another_team_individual", "rar_sha256": "8d78f1154673b252a76e021804211a53af9af95ca3c113ede8927357b8b1aee3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_re_assign_case_to_another_team_individual_agent.py` and embedded as the fenced Python below (sha256 8d78f1154673b252…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_re_assign_case_to_another_team_individual_agent.py` first:

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
    "version": '2.0.0',
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
