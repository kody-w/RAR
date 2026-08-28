---
name: "rar-cowork-cookbook-configure-plan-product-transitions"
description: "Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_product_transitions", "rar_sha256": "39f3a90e80f3a7e4879079089f5e34fa4470664ba68748ce52682f0ad16c8dc4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_product_transitions`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_product_transitions_agent.py` and in the RCI capsule.

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

Plan product transitions Configuration Bulk Setup — Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-product-transitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 39f3a90e80f3a7e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_product_transitions_agent.py` first:

```bash
python3 configure_plan_product_transitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_product_transitions_agent.py   # or on stdin
python3 configure_plan_product_transitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product transitions Configuration Bulk Setup — Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-product-transitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_product_transitions',
    "version": '2.0.1',
    "display_name": 'Plan product transitions Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-product-transitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-product-transitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96a0c95a433b1bfb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-transitions'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-plan-product-transitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanProductTransitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProductTransitions'
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
    print(ConfigurePlanProductTransitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
