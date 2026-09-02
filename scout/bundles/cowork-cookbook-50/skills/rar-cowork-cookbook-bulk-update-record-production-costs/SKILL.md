---
name: "rar-cowork-cookbook-bulk-update-record-production-costs"
description: "Applies a bulk field update across record production costs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_production_costs", "rar_sha256": "368d6cfbc13c88dcd00a6d6b021aa830d15ba7fb4a936214b68382336f070bf7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_record_production_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-record-production-costs:ca9e830bd4f2ca5105202afbc4d2fbb60307370456096a85765aaf66e473f3d1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_record_production_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_record_production_costs_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 368d6cfbc13c88dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_production_costs_agent.py` first:

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
    "version": '2.0.0',
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
