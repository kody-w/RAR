---
name: "rar-cowork-cookbook-configure-model-service-capacity"
description: "Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_model_service_capacity", "rar_sha256": "ed257c1d4b006b61f7d8ab5b2c749da16cb970c9d0c0ca97b0471aa09b2511f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_model_service_capacity`. The original RAPP
agent is preserved byte-for-byte in `configure_model_service_capacity_agent.py` and in the RCI capsule.

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

Model service capacity Configuration Bulk Setup — Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-model-service-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 ed257c1d4b006b61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_model_service_capacity_agent.py` first:

```bash
python3 configure_model_service_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_model_service_capacity_agent.py   # or on stdin
python3 configure_model_service_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Model service capacity Configuration Bulk Setup — Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-model-service-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_model_service_capacity',
    "version": '2.0.0',
    "display_name": 'Model service capacity Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-model-service-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-model-service-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6342220e43654c34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/model-service-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-model-service-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureModelServiceCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureModelServiceCapacity'
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
    print(ConfigureModelServiceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
