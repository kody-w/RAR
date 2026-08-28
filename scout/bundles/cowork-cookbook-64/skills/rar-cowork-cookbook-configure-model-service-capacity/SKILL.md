---
name: "rar-cowork-cookbook-configure-model-service-capacity"
description: "Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_model_service_capacity", "rar_sha256": "a4e76b17bb032b181eb876c791d9edeeb68545e40e2017b87d4e1d9c2337afa8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 a4e76b17bb032b18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_model_service_capacity_agent.py` first:

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
    "version": '2.0.1',
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
