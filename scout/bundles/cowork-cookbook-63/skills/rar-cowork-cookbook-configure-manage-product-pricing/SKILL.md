---
name: "rar-cowork-cookbook-configure-manage-product-pricing"
description: "Applies a bulk configuration change to manage product pricing from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_product_pricing", "rar_sha256": "7e64d0955513787af2212a8f0d0f6e8676bb72760b99a1bbe67036df64fa6b30", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_product_pricing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-product-pricing:1e976d4ba2f69258a88a2ae9ed25478c1aac278c301e21c6eb5e7fea26a361f2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_product_pricing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_product_pricing_agent.py` is
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
