---
name: "rar-cowork-cookbook-configure-reconcile-asset-subledger"
description: "Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_asset_subledger", "rar_sha256": "0ea7ed0e6775053111d7accd402ad53562963e1c81437de419c44a30d864e3ab", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reconcile_asset_subledger`. The original RAPP
agent is preserved byte-for-byte in `configure_reconcile_asset_subledger_agent.py` and in the RCI capsule.

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

Reconcile asset subledger Configuration Bulk Setup — Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 0ea7ed0e67750531…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_asset_subledger_agent.py` first:

```bash
python3 configure_reconcile_asset_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_asset_subledger_agent.py   # or on stdin
python3 configure_reconcile_asset_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile asset subledger Configuration Bulk Setup — Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_asset_subledger',
    "version": '2.0.1',
    "display_name": 'Reconcile asset subledger Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-reconcile-asset-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f60d19f06198b18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/reconcile-asset-subledger'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-reconcile-asset-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReconcileAssetSubledger(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileAssetSubledger'
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
    print(ConfigureReconcileAssetSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
