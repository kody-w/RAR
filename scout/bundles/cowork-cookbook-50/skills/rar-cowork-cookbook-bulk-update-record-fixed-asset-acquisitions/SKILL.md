---
name: "rar-cowork-cookbook-bulk-update-record-fixed-asset-acquisitions"
description: "Applies a bulk field update across record fixed asset acquisitions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions", "rar_sha256": "46ac70b0469f7ad5d22008fb651da5d4af1faa44c57e4d3cc319c228e9b87b82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_record_fixed_asset_acquisitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-record-fixed-asset-acquisitions:e3fb72115783afb2300b6d71e723cc727e42081aafda239f9bde1b9ab4f9d182", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_record_fixed_asset_acquisitions_agent.py` is
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

Record fixed asset acquisitions Bulk Field Update — Applies a bulk field update across record fixed asset acquisitions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-fixed-asset-acquisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_fixed_asset_acquisitions_agent.py` and embedded as the fenced Python below (sha256 46ac70b0469f7ad5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_fixed_asset_acquisitions_agent.py` first:

```bash
python3 bulk_update_record_fixed_asset_acquisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_fixed_asset_acquisitions_agent.py   # or on stdin
python3 bulk_update_record_fixed_asset_acquisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record fixed asset acquisitions Bulk Field Update — Applies a bulk field update across record fixed asset acquisitions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-fixed-asset-acquisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions',
    "version": '2.0.0',
    "display_name": 'Record fixed asset acquisitions Bulk Field Update',
    "description": 'Applies a bulk field update across record fixed asset acquisitions records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-record-fixed-asset-acquisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-fixed-asset-acquisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0031d3a408b7124c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-fixed-asset-acquisitions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-record-fixed-asset-acquisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecordFixedAssetAcquisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordFixedAssetAcquisitions'
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
    print(BulkUpdateRecordFixedAssetAcquisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
