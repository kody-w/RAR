---
name: "rar-cowork-cookbook-configure-consume-materials"
description: "Applies a bulk configuration change to consume materials from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_consume_materials", "rar_sha256": "70b2425548b52ac8f538ebd3d2555aa7fcd7978c9fc4ac0d944919ceb15dce8d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_consume_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-consume-materials:229236ac2b65845405f139bf6b6d5d349b5eb19d3170a88d9a736508359f4d55", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_consume_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_consume_materials_agent.py` is
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
