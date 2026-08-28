---
name: "rar-cowork-cookbook-bulk-update-record-fixed-asset-acquisitions"
description: "Applies a bulk field update across record fixed asset acquisitions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions", "rar_sha256": "116e010cb52fa6c890052d50168aa285eb067f95ade7e8b66d916bfd93002c07", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_fixed_asset_acquisitions_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_fixed_asset_acquisitions_agent.py` and embedded as the fenced Python below (sha256 116e010cb52fa6c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_fixed_asset_acquisitions_agent.py` first:

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
    "version": '2.0.1',
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
