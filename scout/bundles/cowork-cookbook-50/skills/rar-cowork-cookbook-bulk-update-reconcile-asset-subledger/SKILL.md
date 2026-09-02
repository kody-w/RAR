---
name: "rar-cowork-cookbook-bulk-update-reconcile-asset-subledger"
description: "Applies a bulk field update across reconcile asset subledger records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_asset_subledger", "rar_sha256": "88353bf9e5195c849f1c547e4e0fd824c5998843c9a3c62142d073fd113f665d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_reconcile_asset_subledger_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-reconcile-asset-subledger:2ef83ffaf6e9284a77cadc0f0f92bc77b0ac0414fd22e58b6b17fb2b1a81c1c6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_reconcile_asset_subledger`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_reconcile_asset_subledger_agent.py` is
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
