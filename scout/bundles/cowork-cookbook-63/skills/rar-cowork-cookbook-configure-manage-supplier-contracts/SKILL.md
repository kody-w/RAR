---
name: "rar-cowork-cookbook-configure-manage-supplier-contracts"
description: "Applies a bulk configuration change to manage supplier contracts from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_supplier_contracts", "rar_sha256": "614dc8dfcf72a776c3804d7c402d090b16a86e8ed0e7cb0e661b1d65a7dc0fc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_supplier_contracts_agent.py` and embedded as the fenced Python below (sha256 614dc8dfcf72a776…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_supplier_contracts_agent.py` first:

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
    "version": '2.0.0',
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
