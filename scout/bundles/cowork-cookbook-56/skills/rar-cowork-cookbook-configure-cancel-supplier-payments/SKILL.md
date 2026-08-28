---
name: "rar-cowork-cookbook-configure-cancel-supplier-payments"
description: "Applies a bulk configuration change to cancel supplier payments from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_cancel_supplier_payments", "rar_sha256": "56310aa1d4f75479906fe99d6effce330c0fa558ed3b2e1617edb0fcca48f782", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_cancel_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `configure_cancel_supplier_payments_agent.py` and in the RCI capsule.

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

Cancel supplier payments Configuration Bulk Setup — Applies a bulk configuration change to cancel supplier payments from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-cancel-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 56310aa1d4f75479…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_cancel_supplier_payments_agent.py` first:

```bash
python3 configure_cancel_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_cancel_supplier_payments_agent.py   # or on stdin
python3 configure_cancel_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel supplier payments Configuration Bulk Setup — Applies a bulk configuration change to cancel supplier payments from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-cancel-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_cancel_supplier_payments',
    "version": '2.0.1',
    "display_name": 'Cancel supplier payments Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to cancel supplier payments from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-cancel-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-cancel-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '69c0f6db75b623ab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/cancel-supplier-payments'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-cancel-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureCancelSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCancelSupplierPayments'
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
    print(ConfigureCancelSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
