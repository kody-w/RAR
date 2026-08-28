---
name: "rar-cowork-cookbook-configure-subcontract-project-components"
description: "Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_subcontract_project_components", "rar_sha256": "d1af6cada471ef806bceef86e7bd87613a261bdcef7e6c0040e4b7e99497d89d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_subcontract_project_components`. The original RAPP
agent is preserved byte-for-byte in `configure_subcontract_project_components_agent.py` and in the RCI capsule.

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

Subcontract project components Configuration Bulk Setup — Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-subcontract-project-components
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 d1af6cada471ef80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_subcontract_project_components_agent.py` first:

```bash
python3 configure_subcontract_project_components_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_subcontract_project_components_agent.py   # or on stdin
python3 configure_subcontract_project_components_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract project components Configuration Bulk Setup — Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-subcontract-project-components
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_subcontract_project_components',
    "version": '2.0.1',
    "display_name": 'Subcontract project components Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-subcontract-project-components',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-subcontract-project-components',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b6fbd4b5f094a21',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/subcontract-project-components'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-subcontract-project-components', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureSubcontractProjectComponents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureSubcontractProjectComponents'
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
    print(ConfigureSubcontractProjectComponents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
