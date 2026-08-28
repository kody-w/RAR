---
name: "rar-cowork-cookbook-configure-budget-asset-maintenance"
description: "Applies a bulk configuration change to budget asset maintenance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_asset_maintenance", "rar_sha256": "e4ce43d3bf4d2ed4757bc0e2d004861fbfcae37df94387422b8b7db2f6e2540c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_budget_asset_maintenance`. The original RAPP
agent is preserved byte-for-byte in `configure_budget_asset_maintenance_agent.py` and in the RCI capsule.

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

Budget asset maintenance Configuration Bulk Setup — Applies a bulk configuration change to budget asset maintenance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-asset-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 e4ce43d3bf4d2ed4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_budget_asset_maintenance_agent.py` first:

```bash
python3 configure_budget_asset_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_budget_asset_maintenance_agent.py   # or on stdin
python3 configure_budget_asset_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset maintenance Configuration Bulk Setup — Applies a bulk configuration change to budget asset maintenance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-asset-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_budget_asset_maintenance',
    "version": '2.0.1',
    "display_name": 'Budget asset maintenance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to budget asset maintenance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-budget-asset-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-budget-asset-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8df59be5f3b7efe1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/budget-asset-maintenance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-budget-asset-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureBudgetAssetMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureBudgetAssetMaintenance'
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
    print(ConfigureBudgetAssetMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
