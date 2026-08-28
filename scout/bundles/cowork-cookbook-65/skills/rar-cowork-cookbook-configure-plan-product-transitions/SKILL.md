---
name: "rar-cowork-cookbook-configure-plan-product-transitions"
description: "Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_product_transitions", "rar_sha256": "d7cfc9eba04dbafda2d31cf8956b945837be3d25b66b82d4179620577ed277dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 d7cfc9eba04dbafd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_product_transitions_agent.py` first:

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
    "version": '2.0.0',
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
