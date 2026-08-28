---
name: "rar-cowork-cookbook-configure-budget-fixed-assets"
description: "Applies a bulk configuration change to budget fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_fixed_assets", "rar_sha256": "8a48f188816b099b24fc6c132dad96669871e355a79bb104a8b53f0e15730a6a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_budget_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_budget_fixed_assets_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_budget_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 8a48f188816b099b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_budget_fixed_assets_agent.py` first:

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
    "version": '2.0.1',
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
