---
name: "rar-cowork-cookbook-configure-budget-asset-maintenance"
description: "Applies a bulk configuration change to budget asset maintenance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_asset_maintenance", "rar_sha256": "67bac5258f189a7aa199ec57727ebb2970e3a5b35c6b80b70f7aeba63a1c81dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_budget_asset_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-budget-asset-maintenance:49d6a8a2bc4c6fd4efaba33090bf9fcf0487601ba6f78e5fdecc01d84357f1b1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_budget_asset_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_budget_asset_maintenance_agent.py` is
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
