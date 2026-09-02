---
name: "rar-cowork-cookbook-configure-manage-sales-order-holds"
description: "Applies a bulk configuration change to manage sales order holds from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_sales_order_holds", "rar_sha256": "e54b9f621be288c2b86930a3a3706fa6751522115b874405bcafa28f8a584ccc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_sales_order_holds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-sales-order-holds:69080967152cf7e4c02d26d415e618fcd30a605141172facda95df048db55de1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_sales_order_holds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_sales_order_holds_agent.py` is
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
