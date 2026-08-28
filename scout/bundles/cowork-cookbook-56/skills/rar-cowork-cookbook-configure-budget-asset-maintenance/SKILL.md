---
name: "rar-cowork-cookbook-configure-budget-asset-maintenance"
description: "Applies a bulk configuration change to budget asset maintenance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_asset_maintenance", "rar_sha256": "67bac5258f189a7aa199ec57727ebb2970e3a5b35c6b80b70f7aeba63a1c81dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 67bac5258f189a7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_budget_asset_maintenance_agent.py` first:

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
    "version": '2.0.0',
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
