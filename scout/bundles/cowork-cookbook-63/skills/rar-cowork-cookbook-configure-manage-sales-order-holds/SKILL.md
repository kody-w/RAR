---
name: "rar-cowork-cookbook-configure-manage-sales-order-holds"
description: "Applies a bulk configuration change to manage sales order holds from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_sales_order_holds", "rar_sha256": "ef8f44ecc0f9d80a6a9c31d5938834c16ff0199fc4d0e4075c4dcd80912230c7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_sales_order_holds`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_sales_order_holds_agent.py` and in the RCI capsule.

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

Manage sales order holds Configuration Bulk Setup — Applies a bulk configuration change to manage sales order holds from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-sales-order-holds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 ef8f44ecc0f9d80a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_sales_order_holds_agent.py` first:

```bash
python3 configure_manage_sales_order_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_sales_order_holds_agent.py   # or on stdin
python3 configure_manage_sales_order_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order holds Configuration Bulk Setup — Applies a bulk configuration change to manage sales order holds from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-sales-order-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_sales_order_holds',
    "version": '2.0.1',
    "display_name": 'Manage sales order holds Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage sales order holds from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-sales-order-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-sales-order-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '611ac7cc212c0aee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-holds'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-manage-sales-order-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageSalesOrderHolds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSalesOrderHolds'
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
    print(ConfigureManageSalesOrderHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
