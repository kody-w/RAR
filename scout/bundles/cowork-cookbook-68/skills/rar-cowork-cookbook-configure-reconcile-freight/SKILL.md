---
name: "rar-cowork-cookbook-configure-reconcile-freight"
description: "Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_freight", "rar_sha256": "301946442d05e4c9c0ffc617bc5b1efc614ba9c6b0d5e47d84eae1d75a616e1f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `configure_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Configuration Bulk Setup — Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 301946442d05e4c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_freight_agent.py` first:

```bash
python3 configure_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_freight_agent.py   # or on stdin
python3 configure_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Configuration Bulk Setup — Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_freight',
    "version": '2.0.1',
    "display_name": 'Reconcile freight Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7117e3309270a7e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReconcileFreight(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileFreight'
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
    print(ConfigureReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
