---
name: "rar-cowork-cookbook-bulk-update-record-production-costs"
description: "Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_production_costs", "rar_sha256": "4eb1b1bfb44160126e907d05d09105366856c41caca3efcea746c464f64e0f1a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_production_costs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_production_costs_agent.py` and in the RCI capsule.

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

Record production costs Bulk Field Update — Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 4eb1b1bfb4416012…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_production_costs_agent.py` first:

```bash
python3 bulk_update_record_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_production_costs_agent.py   # or on stdin
python3 bulk_update_record_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record production costs Bulk Field Update — Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_production_costs',
    "version": '2.0.1',
    "display_name": 'Record production costs Bulk Field Update',
    "description": 'Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-record-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ee2088fbec74f65',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/record-production-costs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-record-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecordProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordProductionCosts'
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
    print(BulkUpdateRecordProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
