---
name: "rar-cowork-cookbook-bulk-update-plan-events"
description: "Applies a bulk field update across plan events records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_events", "rar_sha256": "a6b5be6fed856c1f8da50bbbdbdd7d409fa1e0a82fa79d3ab9336fa38d1f4ccf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_events_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-events:62c4c0670bc00b45700876dc9e2539224db1611105ca608223b671ad792abe06", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_events`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_events_agent.py` is
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

Plan events Bulk Field Update — Applies a bulk field update across plan events records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_events_agent.py` and embedded as the fenced Python below (sha256 a6b5be6fed856c1f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_events_agent.py` first:

```bash
python3 bulk_update_plan_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_events_agent.py   # or on stdin
python3 bulk_update_plan_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan events Bulk Field Update — Applies a bulk field update across plan events records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_events',
    "version": '2.0.0',
    "display_name": 'Plan events Bulk Field Update',
    "description": 'Applies a bulk field update across plan events records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68343183a7def23e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/plan-events'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-plan-events', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePlanEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanEvents'
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
    print(BulkUpdatePlanEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
