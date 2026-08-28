---
name: "rar-cowork-cookbook-configure-reconcile-asset-subledger"
description: "Applies a bulk configuration change to reconcile asset subledger from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_asset_subledger", "rar_sha256": "9830cd1711efac4ffca4524cc9cd41aedd36bd9a9216bd9a76ec58593dfa5049", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 9830cd1711efac4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_asset_subledger_agent.py` first:

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
    "version": '2.0.0',
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
