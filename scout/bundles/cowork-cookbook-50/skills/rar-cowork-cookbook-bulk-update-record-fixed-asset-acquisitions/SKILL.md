---
name: "rar-cowork-cookbook-bulk-update-record-fixed-asset-acquisitions"
description: "Applies a bulk field update across record fixed asset acquisitions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions", "rar_sha256": "46ac70b0469f7ad5d22008fb651da5d4af1faa44c57e4d3cc319c228e9b87b82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
