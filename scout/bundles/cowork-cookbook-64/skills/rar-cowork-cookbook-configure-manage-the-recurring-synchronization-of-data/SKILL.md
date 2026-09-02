---
name: "rar-cowork-cookbook-configure-manage-the-recurring-synchronization-of-data"
description: "Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data", "rar_sha256": "84faffbd9118032bf33f49b0dd2e6f919b736d1869012cc4beac4734870db4f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_the_recurring_synchronization_of_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-the-recurring-synchronization-of-data:314df02545d65ba35ab12bebcef2b685bf02e69496e02cc37fcd8e1fc533b09a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_the_recurring_synchronization_of_data_agent.py` is
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

Manage the recurring synchronization of data Configuration Bulk Setup — Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 84faffbd9118032b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_the_recurring_synchronization_of_data_agent.py` first:

```bash
python3 configure_manage_the_recurring_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_the_recurring_synchronization_of_data_agent.py   # or on stdin
python3 configure_manage_the_recurring_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the recurring synchronization of data Configuration Bulk Setup — Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the recurring synchronization of data Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-the-recurring-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33c8fceeffa06e25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-recurring-synchronization-of-data'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-the-recurring-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageTheRecurringSynchronizationOfData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageTheRecurringSynchronizationOfData'
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
    print(ConfigureManageTheRecurringSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
