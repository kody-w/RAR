---
name: "rar-cowork-cookbook-configure-develop-training-materials"
description: "Applies a bulk configuration change to develop training materials from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_training_materials", "rar_sha256": "c1b650dfaacf7a54db7f2df736c6efca4c508e71331a5c8346a057ee19c7849e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_training_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-training-materials:607904d522d985449f12a93b41ba6dd1b7255bbce6a5909e6bccf5a5fe413d63", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_training_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_training_materials_agent.py` is
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
