---
name: "rar-cowork-cookbook-configure-manage-supplier-contracts"
description: "Applies a bulk configuration change to manage supplier contracts from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_supplier_contracts", "rar_sha256": "1dfd922fc45c8f6a41588269a6f95cc37f347f02e69531312b05099dabce0eb0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_supplier_contracts`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_supplier_contracts_agent.py` and in the RCI capsule.

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

Manage supplier contracts Configuration Bulk Setup — Applies a bulk configuration change to manage supplier contracts from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-supplier-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_supplier_contracts_agent.py` and embedded as the fenced Python below (sha256 1dfd922fc45c8f6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_supplier_contracts_agent.py` first:

```bash
python3 configure_manage_supplier_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_supplier_contracts_agent.py   # or on stdin
python3 configure_manage_supplier_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier contracts Configuration Bulk Setup — Applies a bulk configuration change to manage supplier contracts from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-supplier-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_supplier_contracts',
    "version": '2.0.1',
    "display_name": 'Manage supplier contracts Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage supplier contracts from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-manage-supplier-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-supplier-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac6968a052f3ab57',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-contracts'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-supplier-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageSupplierContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSupplierContracts'
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
    print(ConfigureManageSupplierContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
