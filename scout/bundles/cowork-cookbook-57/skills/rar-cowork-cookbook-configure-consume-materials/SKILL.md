---
name: "rar-cowork-cookbook-configure-consume-materials"
description: "Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_consume_materials", "rar_sha256": "70b2425548b52ac8f538ebd3d2555aa7fcd7978c9fc4ac0d944919ceb15dce8d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_consume_materials`. The original RAPP
agent is preserved byte-for-byte in `configure_consume_materials_agent.py` and in the RCI capsule.

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

Consume materials Configuration Bulk Setup — Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-consume-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_consume_materials_agent.py` and embedded as the fenced Python below (sha256 70b2425548b52ac8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_consume_materials_agent.py` first:

```bash
python3 configure_consume_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_consume_materials_agent.py   # or on stdin
python3 configure_consume_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume materials Configuration Bulk Setup — Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-consume-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_consume_materials',
    "version": '2.0.0',
    "display_name": 'Consume materials Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-consume-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-consume-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '970c7057531209b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-materials'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-consume-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConsumeMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConsumeMaterials'
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
    print(ConfigureConsumeMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
