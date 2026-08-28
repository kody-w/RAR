---
name: "rar-cowork-cookbook-configure-manage-product-pricing"
description: "Applies a bulk configuration change to manage product pricing from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_product_pricing", "rar_sha256": "7e64d0955513787af2212a8f0d0f6e8676bb72760b99a1bbe67036df64fa6b30", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 7e64d0955513787a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_product_pricing_agent.py` first:

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
    "version": '2.0.0',
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
