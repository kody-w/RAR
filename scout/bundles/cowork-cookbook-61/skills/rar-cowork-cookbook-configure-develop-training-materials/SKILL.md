---
name: "rar-cowork-cookbook-configure-develop-training-materials"
description: "Applies a bulk configuration change to develop training materials from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_training_materials", "rar_sha256": "aac41198f7e57d7156221aed961652ca22d344354942f28293e90c016424d039", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_training_materials`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_training_materials_agent.py` and in the RCI capsule.

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

Develop training materials Configuration Bulk Setup — Applies a bulk configuration change to develop training materials from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-training-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 aac41198f7e57d71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_training_materials_agent.py` first:

```bash
python3 configure_develop_training_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_training_materials_agent.py   # or on stdin
python3 configure_develop_training_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training materials Configuration Bulk Setup — Applies a bulk configuration change to develop training materials from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-training-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_training_materials',
    "version": '2.0.1',
    "display_name": 'Develop training materials Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop training materials from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-develop-training-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-training-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e2cfc48effa40a39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-materials'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-develop-training-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopTrainingMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopTrainingMaterials'
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
    print(ConfigureDevelopTrainingMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
