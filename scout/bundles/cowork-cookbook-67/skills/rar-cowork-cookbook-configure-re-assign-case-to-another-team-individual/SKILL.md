---
name: "rar-cowork-cookbook-configure-re-assign-case-to-another-team-individual"
description: "Applies a bulk configuration change to re-assign case to another team/individual from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_re_assign_case_to_another_team_individual", "rar_sha256": "8d78f1154673b252a76e021804211a53af9af95ca3c113ede8927357b8b1aee3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_re_assign_case_to_another_team_individual_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-re-assign-case-to-another-team-individual:dad62fbb910072958811ee0482b3fce1c0fc5567129e95f1f81efe78dcf349eb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_re_assign_case_to_another_team_individual`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_re_assign_case_to_another_team_individual_agent.py` is
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
