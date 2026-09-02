---
name: "rar-cowork-cookbook-configure-manage-supplier-contracts"
description: "Applies a bulk configuration change to manage supplier contracts from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_supplier_contracts", "rar_sha256": "614dc8dfcf72a776c3804d7c402d090b16a86e8ed0e7cb0e661b1d65a7dc0fc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_supplier_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-supplier-contracts:2655a1583d9d23a82ea081d045c521d252e566e290e75722ef754ab516939b4f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_supplier_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_supplier_contracts_agent.py` is
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
