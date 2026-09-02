---
name: "rar-cowork-cookbook-configure-budget-fixed-assets"
description: "Applies a bulk configuration change to budget fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_fixed_assets", "rar_sha256": "c5111d5d7583eb96827f37cfac86abb194fd17d841cab16fb6464b82cad5d6f9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_budget_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-budget-fixed-assets:e3bc4c1c9c3eee2562e56aacf9aa22f958f1950541d97d2669f08c8ae72143d6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_budget_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_budget_fixed_assets_agent.py` is
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

Budget fixed assets Configuration Bulk Setup — Applies a bulk configuration change to budget fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_budget_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 c5111d5d7583eb96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_budget_fixed_assets_agent.py` first:

```bash
python3 configure_budget_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_budget_fixed_assets_agent.py   # or on stdin
python3 configure_budget_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget fixed assets Configuration Bulk Setup — Applies a bulk configuration change to budget fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_budget_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Budget fixed assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to budget fixed assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-budget-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-budget-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bcdbeb4f3fbedc32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-budget-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureBudgetFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureBudgetFixedAssets'
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
    print(ConfigureBudgetFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
