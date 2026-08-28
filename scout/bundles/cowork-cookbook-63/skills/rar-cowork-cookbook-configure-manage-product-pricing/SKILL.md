---
name: "rar-cowork-cookbook-configure-manage-product-pricing"
description: "Applies a bulk configuration change to manage product pricing from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_product_pricing", "rar_sha256": "8cbfa112d21efd771b6ac72b3eb2c89510573bd7d8088de3455c26915b3a9332", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_product_pricing`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_product_pricing_agent.py` and in the RCI capsule.

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

Manage product pricing Configuration Bulk Setup — Applies a bulk configuration change to manage product pricing from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-product-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 8cbfa112d21efd77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_product_pricing_agent.py` first:

```bash
python3 configure_manage_product_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_product_pricing_agent.py   # or on stdin
python3 configure_manage_product_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product pricing Configuration Bulk Setup — Applies a bulk configuration change to manage product pricing from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-product-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_product_pricing',
    "version": '2.0.1',
    "display_name": 'Manage product pricing Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage product pricing from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-product-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-product-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9eab2af1d4146a0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-pricing'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-manage-product-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageProductPricing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProductPricing'
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
    print(ConfigureManageProductPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
