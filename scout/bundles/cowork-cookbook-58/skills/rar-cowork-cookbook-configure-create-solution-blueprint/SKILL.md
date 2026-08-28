---
name: "rar-cowork-cookbook-configure-create-solution-blueprint"
description: "Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_solution_blueprint", "rar_sha256": "970c84df0b198a3781ef6b78b1fe451303a82e005f7364a799d6cb4744ee50be", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_solution_blueprint`. The original RAPP
agent is preserved byte-for-byte in `configure_create_solution_blueprint_agent.py` and in the RCI capsule.

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

Create solution blueprint Configuration Bulk Setup — Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-solution-blueprint
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 970c84df0b198a37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_solution_blueprint_agent.py` first:

```bash
python3 configure_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_solution_blueprint_agent.py   # or on stdin
python3 configure_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Configuration Bulk Setup — Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_solution_blueprint',
    "version": '2.0.1',
    "display_name": 'Create solution blueprint Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b771f23f0be4b93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureCreateSolutionBlueprint(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateSolutionBlueprint'
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
    print(ConfigureCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
