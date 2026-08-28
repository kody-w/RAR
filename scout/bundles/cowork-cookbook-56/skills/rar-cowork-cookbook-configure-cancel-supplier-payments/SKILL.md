---
name: "rar-cowork-cookbook-configure-cancel-supplier-payments"
description: "Applies a bulk configuration change to cancel supplier payments from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_cancel_supplier_payments", "rar_sha256": "3a3844d755cf906883e3ea09f5b725eab3f6a59995baa98b86757e8d0b291e69", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 3a3844d755cf9068…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_cancel_supplier_payments_agent.py` first:

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
    "version": '2.0.0',
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
