---
name: "rar-cowork-cookbook-configure-manage-sales-order-holds"
description: "Applies a bulk configuration change to manage sales order holds from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_sales_order_holds", "rar_sha256": "e54b9f621be288c2b86930a3a3706fa6751522115b874405bcafa28f8a584ccc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 e54b9f621be288c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_sales_order_holds_agent.py` first:

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
    "version": '2.0.0',
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
