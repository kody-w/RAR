---
name: "rar-cowork-cookbook-configure-develop-training-materials"
description: "Applies a bulk configuration change to develop training materials from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_training_materials", "rar_sha256": "c1b650dfaacf7a54db7f2df736c6efca4c508e71331a5c8346a057ee19c7849e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 c1b650dfaacf7a54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_training_materials_agent.py` first:

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
    "version": '2.0.0',
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
