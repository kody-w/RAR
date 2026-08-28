---
name: "rar-cowork-cookbook-configure-subcontract-project-components"
description: "Applies a bulk configuration change to subcontract project components from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_subcontract_project_components", "rar_sha256": "bc962d353717e50bad9485a5656b70bfd671135264065d1b709b0a879840c513", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_subcontract_project_components_agent.py` and embedded as the fenced Python below (sha256 bc962d353717e50b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_subcontract_project_components_agent.py` first:

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
    "version": '2.0.0',
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
