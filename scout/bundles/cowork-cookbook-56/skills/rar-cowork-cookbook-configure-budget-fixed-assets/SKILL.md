---
name: "rar-cowork-cookbook-configure-budget-fixed-assets"
description: "Applies a bulk configuration change to budget fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_fixed_assets", "rar_sha256": "c5111d5d7583eb96827f37cfac86abb194fd17d841cab16fb6464b82cad5d6f9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
