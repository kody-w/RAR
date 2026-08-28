---
name: "rar-cowork-cookbook-bulk-update-reconcile-asset-subledger"
description: "Applies a bulk field update across reconcile asset subledger records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_asset_subledger", "rar_sha256": "6a94d42e603efafae5997b0ebdc5baff974baef9143dc97af92dd085b812e0f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reconcile_asset_subledger`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reconcile_asset_subledger_agent.py` and in the RCI capsule.

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

Reconcile asset subledger Bulk Field Update — Applies a bulk field update across reconcile asset subledger records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-asset-subledger
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 6a94d42e603efafa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reconcile_asset_subledger_agent.py` first:

```bash
python3 bulk_update_reconcile_asset_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reconcile_asset_subledger_agent.py   # or on stdin
python3 bulk_update_reconcile_asset_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile asset subledger Bulk Field Update — Applies a bulk field update across reconcile asset subledger records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-asset-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reconcile_asset_subledger',
    "version": '2.0.1',
    "display_name": 'Reconcile asset subledger Bulk Field Update',
    "description": 'Applies a bulk field update across reconcile asset subledger records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-reconcile-asset-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reconcile-asset-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3dd6a441e94c72ac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/reconcile-asset-subledger'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-reconcile-asset-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReconcileAssetSubledger(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReconcileAssetSubledger'
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
    print(BulkUpdateReconcileAssetSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
