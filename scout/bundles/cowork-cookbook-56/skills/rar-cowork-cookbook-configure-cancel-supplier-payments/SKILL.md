---
name: "rar-cowork-cookbook-configure-cancel-supplier-payments"
description: "Applies a bulk configuration change to cancel supplier payments from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_cancel_supplier_payments", "rar_sha256": "3a3844d755cf906883e3ea09f5b725eab3f6a59995baa98b86757e8d0b291e69", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_cancel_supplier_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-cancel-supplier-payments:63c0e0fc05fd235865e8ab80e744995dfaa824108fa6ca6b0b98bd60218b9cd3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_cancel_supplier_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_cancel_supplier_payments_agent.py` is
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
