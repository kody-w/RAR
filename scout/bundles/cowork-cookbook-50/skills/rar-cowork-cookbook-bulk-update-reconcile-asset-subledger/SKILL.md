---
name: "rar-cowork-cookbook-bulk-update-reconcile-asset-subledger"
description: "Applies a bulk field update across reconcile asset subledger records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_asset_subledger", "rar_sha256": "88353bf9e5195c849f1c547e4e0fd824c5998843c9a3c62142d073fd113f665d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 88353bf9e5195c84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reconcile_asset_subledger_agent.py` first:

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
    "version": '2.0.0',
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
