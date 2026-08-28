---
name: "rar-cowork-cookbook-configure-manage-the-recurring-synchronization-of-data"
description: "Applies a bulk configuration change to manage the recurring synchronization of data from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data", "rar_sha256": "599719c18d8b65f1f19e0a840151ddd38e5b6fd0368cfd1a7f8e8d648d5a0df7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_the_recurring_synchronization_of_data_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 599719c18d8b65f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_the_recurring_synchronization_of_data_agent.py` first:

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
    "version": '2.0.1',
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
